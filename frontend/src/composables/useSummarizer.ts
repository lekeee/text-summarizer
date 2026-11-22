import { computed, ref } from 'vue'
import { ApiError, extractDocument, getMethods, summarize } from '../api/client'
import type { SummaryMethod, SummaryResult } from '../types/summary'
import { SAMPLE_TEXT } from '../utils/sampleText'

export type Screen = 'input' | 'settings' | 'loading' | 'result'
export type InputMode = 'file' | 'text'

export interface UploadState {
  name: string
  size: number
  progress: number
  status: 'uploading' | 'done' | 'error'
  message: string
}

export const LOADING_PHASES = [
  'Delim tekst na rečenice',
  'Svodim reči na koren',
  'Gradim graf sličnosti',
  'Rangiram rečenice (PageRank)',
]

const PHASE_DURATION_MS = 350
const SLOW_SERVER_MS = 3000

const screen = ref<Screen>('input')
const inputMode = ref<InputMode>('file')
const text = ref('')
const upload = ref<UploadState | null>(null)
const methods = ref<SummaryMethod[]>([])
const methodsError = ref('')
const methodId = ref('textrank')
const ratio = ref(30)
const loadingPhase = ref(0)
const result = ref<SummaryResult | null>(null)
const summarizeError = ref('')
const serverWaking = ref(false)

const selectedMethod = computed(() => methods.value.find((method) => method.id === methodId.value))
const hasText = computed(() => text.value.trim().length > 0)
const isUploading = computed(() => upload.value?.status === 'uploading')

function messageOf(error: unknown): string {
  return error instanceof ApiError ? error.message : 'Došlo je do greške. Pokušajte ponovo.'
}

function wait(milliseconds: number) {
  return new Promise((resolve) => setTimeout(resolve, milliseconds))
}

async function whileServerWakes<T>(request: Promise<T>): Promise<T> {
  const timer = setTimeout(() => (serverWaking.value = true), SLOW_SERVER_MS)
  try {
    return await request
  } finally {
    clearTimeout(timer)
    serverWaking.value = false
  }
}

async function loadMethods() {
  methodsError.value = ''
  try {
    methods.value = await whileServerWakes(getMethods())
  } catch (error) {
    methodsError.value = messageOf(error)
  }
}

async function uploadFile(file: File) {
  upload.value = { name: file.name, size: file.size, progress: 0, status: 'uploading', message: '' }
  const current = upload.value
  text.value = ''

  try {
    const document = await whileServerWakes(
      extractDocument(file, (progress) => {
        current.progress = progress
      }),
    )
    if (upload.value !== current) return

    text.value = document.text
    current.progress = 100
    current.status = 'done'
    current.message = 'Tekst je izdvojen iz fajla.'
  } catch (error) {
    if (upload.value !== current) return

    current.status = 'error'
    current.message = messageOf(error)
  }
}

function loadSample() {
  upload.value = null
  text.value = SAMPLE_TEXT
  inputMode.value = 'text'
}

function clearInput() {
  upload.value = null
  text.value = ''
}

function goToInput() {
  screen.value = 'input'
}

function goToSettings() {
  if (hasText.value && !isUploading.value) {
    summarizeError.value = ''
    screen.value = 'settings'
  }
}

async function playLoadingPhases() {
  for (let phase = 1; phase <= LOADING_PHASES.length; phase++) {
    await wait(PHASE_DURATION_MS)
    loadingPhase.value = phase
  }
}

async function generate() {
  summarizeError.value = ''
  loadingPhase.value = 0
  screen.value = 'loading'

  try {
    const [summary] = await Promise.all([
      whileServerWakes(summarize(text.value, methodId.value, ratio.value)),
      playLoadingPhases(),
    ])
    result.value = summary
    screen.value = 'result'
  } catch (error) {
    summarizeError.value = messageOf(error)
    screen.value = 'settings'
  }
}

function restart() {
  clearInput()
  result.value = null
  inputMode.value = 'file'
  screen.value = 'input'
}

export function useSummarizer() {
  return {
    screen,
    inputMode,
    text,
    upload,
    methods,
    methodsError,
    methodId,
    ratio,
    loadingPhase,
    result,
    summarizeError,
    serverWaking,
    selectedMethod,
    hasText,
    isUploading,
    loadMethods,
    uploadFile,
    loadSample,
    clearInput,
    goToInput,
    goToSettings,
    generate,
    restart,
  }
}
