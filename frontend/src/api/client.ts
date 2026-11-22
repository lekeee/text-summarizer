import type { ExtractedDocument, SummaryMethod, SummaryResult } from '../types/summary'

const API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api'
const SERVER_DOWN = 'Server nije dostupan. Proverite da li je backend pokrenut.'
const UNKNOWN_ERROR = 'Došlo je do greške. Pokušajte ponovo.'

export class ApiError extends Error {}

function errorMessage(body: unknown): string {
  if (body && typeof body === 'object' && 'detail' in body && typeof body.detail === 'string') {
    return body.detail
  }
  return UNKNOWN_ERROR
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  let response: Response
  try {
    response = await fetch(`${API_URL}${path}`, init)
  } catch {
    throw new ApiError(SERVER_DOWN)
  }

  const body = await response.json().catch(() => null)
  if (!response.ok) {
    throw new ApiError(errorMessage(body))
  }
  return body as T
}

export function getMethods(): Promise<SummaryMethod[]> {
  return request('/methods')
}

export function summarize(text: string, method: string, ratio: number): Promise<SummaryResult> {
  return request('/summarize', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, method, ratio }),
  })
}

export function extractDocument(file: File, onProgress: (percent: number) => void): Promise<ExtractedDocument> {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest()
    const form = new FormData()
    form.append('file', file)

    xhr.upload.onprogress = (event) => {
      if (event.lengthComputable) {
        onProgress(Math.round((event.loaded / event.total) * 100))
      }
    }
    xhr.onload = () => {
      const body = JSON.parse(xhr.responseText || 'null')
      if (xhr.status >= 200 && xhr.status < 300) {
        resolve(body)
      } else {
        reject(new ApiError(errorMessage(body)))
      }
    }
    xhr.onerror = () => reject(new ApiError(SERVER_DOWN))

    xhr.open('POST', `${API_URL}/documents/extract`)
    xhr.send(form)
  })
}
