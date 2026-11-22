export function formatDecimal(value: number, digits = 1): string {
  return value.toFixed(digits).replace('.', ',')
}

export function formatFileSize(bytes: number): string {
  const kilobytes = bytes / 1024
  if (kilobytes >= 1024) {
    return `${formatDecimal(kilobytes / 1024)} MB`
  }
  return `${Math.max(1, Math.round(kilobytes))} KB`
}

export function formatReadingTime(seconds: number): string {
  if (seconds < 60) {
    return `${seconds} s`
  }
  return `${Math.floor(seconds / 60)} min ${seconds % 60} s`
}

export function capitalize(text: string): string {
  return text.charAt(0).toUpperCase() + text.slice(1)
}
