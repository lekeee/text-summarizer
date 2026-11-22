<script setup lang="ts">
import { CircleAlert, Hourglass } from '@lucide/vue'

const { tone = 'error' } = defineProps<{
  message: string
  actionLabel?: string
  tone?: 'error' | 'info'
}>()

defineEmits<{ action: [] }>()
</script>

<template>
  <div
    :role="tone === 'error' ? 'alert' : 'status'"
    class="flex flex-wrap items-center gap-3 rounded-xl border px-4 py-3 text-sm"
    :class="
      tone === 'error'
        ? 'border-danger-600/20 bg-danger-50 text-danger-700'
        : 'border-brand-600/20 bg-brand-50 text-brand-700'
    "
  >
    <CircleAlert v-if="tone === 'error'" :size="18" class="shrink-0" />
    <Hourglass v-else :size="18" class="shrink-0" />
    <span class="flex-1">{{ message }}</span>
    <button v-if="actionLabel" type="button" class="font-semibold underline underline-offset-2" @click="$emit('action')">
      {{ actionLabel }}
    </button>
  </div>
</template>
