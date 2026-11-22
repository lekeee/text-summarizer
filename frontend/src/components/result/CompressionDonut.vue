<script setup lang="ts">
import { computed } from 'vue'
import BaseCard from '../base/BaseCard.vue'

const props = defineProps<{
  summaryWords: number
  originalWords: number
}>()

const keptPercent = computed(() =>
  props.originalWords ? Math.min(100, Math.round((props.summaryWords / props.originalWords) * 100)) : 0,
)
const droppedWords = computed(() => Math.max(0, props.originalWords - props.summaryWords))
</script>

<template>
  <BaseCard class="flex flex-wrap items-center gap-[22px] p-[22px]">
    <div
      role="img"
      :aria-label="`Sažetak zadržava ${keptPercent}% reči originala`"
      class="relative size-[132px] shrink-0 rounded-full"
      :style="{ background: `conic-gradient(var(--color-brand-600) 0 ${keptPercent * 3.6}deg, var(--color-gray-200) 0)` }"
    >
      <div class="absolute inset-3.5 flex flex-col items-center justify-center rounded-full bg-surface">
        <span class="text-[26px] font-bold tracking-tight">{{ 100 - keptPercent }}%</span>
        <span class="text-xs text-gray-600">kraće</span>
      </div>
    </div>

    <div class="flex flex-[1_1_140px] flex-col gap-3">
      <span class="text-sm font-semibold">Kompresija</span>
      <div class="flex items-center gap-2 text-[13px] text-gray-600">
        <span class="size-2.5 rounded-[3px] bg-brand-600" />
        Sažetak
        <strong class="ml-auto text-gray-900 tabular-nums">{{ summaryWords }} reči</strong>
      </div>
      <div class="flex items-center gap-2 text-[13px] text-gray-600">
        <span class="size-2.5 rounded-[3px] bg-gray-200" />
        Izostavljeno
        <strong class="ml-auto text-gray-900 tabular-nums">{{ droppedWords }} reči</strong>
      </div>
    </div>
  </BaseCard>
</template>
