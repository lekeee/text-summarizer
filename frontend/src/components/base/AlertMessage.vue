<script setup lang="ts">
import { CircleAlert } from '@lucide/vue'

defineProps<{
  message: string
  actionLabel?: string
}>()

defineEmits<{ action: [] }>()
</script>

<template>
  <div
    role="alert"
    class="flex flex-wrap items-center gap-3 rounded-xl border border-danger-600/20 bg-danger-50 px-4 py-3 text-sm text-danger-700"
  >
    <CircleAlert :size="18" class="shrink-0" />
    <span class="flex-1">{{ message }}</span>
    <button v-if="actionLabel" type="button" class="font-semibold underline underline-offset-2" @click="$emit('action')">
      {{ actionLabel }}
    </button>
  </div>
</template>
