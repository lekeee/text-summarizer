import { computed, ref, watchEffect } from 'vue'

export type Theme = 'light' | 'dark'

const STORAGE_KEY = 'theme'

function savedTheme(): Theme | null {
  const value = localStorage.getItem(STORAGE_KEY)
  return value === 'light' || value === 'dark' ? value : null
}

function systemTheme(): Theme {
  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
}

const theme = ref<Theme>(savedTheme() ?? systemTheme())

watchEffect(() => {
  document.documentElement.classList.toggle('dark', theme.value === 'dark')
})

function toggleTheme() {
  theme.value = theme.value === 'dark' ? 'light' : 'dark'
  localStorage.setItem(STORAGE_KEY, theme.value)
}

export function useTheme() {
  return {
    theme,
    isDark: computed(() => theme.value === 'dark'),
    toggleTheme,
  }
}
