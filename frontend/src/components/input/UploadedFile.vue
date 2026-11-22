<script setup lang="ts">
import { Check, X } from '@lucide/vue'
import { computed } from 'vue'
import type { UploadState } from '../../composables/useSummarizer'
import { formatFileSize } from '../../utils/format'

const props = defineProps<{ upload: UploadState }>()

const extension = computed(() => props.upload.name.split('.').pop()?.toUpperCase() ?? '')

const badgeColor = computed(() => {
  if (extension.value === 'PDF') return 'bg-danger-600'
  if (extension.value === 'DOCX') return 'bg-brand-600'
  return 'bg-gray-600'
})
</script>

<template>
  <div class="flex animate-fade-up items-center gap-3.5 rounded-[14px] border border-gray-200 px-4 py-3.5">
    <span class="flex size-10 shrink-0 items-end justify-center rounded-lg bg-gray-100 pb-1.5">
      <span class="rounded-[3px] px-1 py-0.5 text-[9px] font-bold text-white" :class="badgeColor">{{ extension }}</span>
    </span>

    <div class="flex min-w-0 flex-1 flex-col gap-1.5">
      <div class="flex justify-between gap-3 text-sm">
        <span class="truncate font-semibold">{{ upload.name }}</span>
        <span class="shrink-0 text-gray-600">{{ formatFileSize(upload.size) }} · {{ upload.progress }}%</span>
      </div>
      <div class="h-1.5 overflow-hidden rounded-[3px] bg-gray-200">
        <div
          class="h-full rounded-[3px] transition-[width] duration-150"
          :class="upload.status === 'error' ? 'bg-danger-600' : 'bg-brand-600'"
          :style="{ width: `${upload.progress}%` }"
        />
      </div>
      <span v-if="upload.message" class="text-xs" :class="upload.status === 'error' ? 'text-danger-700' : 'text-gray-600'">
        {{ upload.message }}
      </span>
    </div>

    <span v-if="upload.status === 'done'" class="flex size-[22px] shrink-0 items-center justify-center rounded-full bg-brand-600">
      <Check :size="12" :stroke-width="3.5" class="text-white" />
    </span>
    <span v-else-if="upload.status === 'error'" class="flex size-[22px] shrink-0 items-center justify-center rounded-full bg-danger-600">
      <X :size="12" :stroke-width="3.5" class="text-white" />
    </span>
  </div>
</template>
