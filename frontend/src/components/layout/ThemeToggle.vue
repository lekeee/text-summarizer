<script setup lang="ts">
import { Moon, Sun } from '@lucide/vue'
import { computed } from 'vue'
import { useTheme } from '../../composables/useTheme'

const { isDark, toggleTheme } = useTheme()

const label = computed(() => (isDark.value ? 'Uključi svetlu temu' : 'Uključi tamnu temu'))
</script>

<template>
  <button
    type="button"
    :aria-label="label"
    :title="label"
    :aria-pressed="isDark"
    class="flex size-10 items-center justify-center rounded-[10px] border border-gray-300 bg-surface text-gray-700 shadow-xs transition-colors hover:bg-gray-50 hover:text-gray-900"
    @click="toggleTheme"
  >
    <Sun v-if="isDark" :size="18" />
    <Moon v-else :size="18" />
  </button>
</template>
