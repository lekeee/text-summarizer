<script setup lang="ts">
import { Check } from '@lucide/vue'
import { computed } from 'vue'
import { LOADING_PHASES, useSummarizer } from '../../composables/useSummarizer'
import ResultSkeleton from './ResultSkeleton.vue'

const { selectedMethod, ratio, loadingPhase } = useSummarizer()

const progress = computed(() => Math.round((loadingPhase.value / LOADING_PHASES.length) * 100))
</script>

<template>
  <div class="flex flex-col gap-6">
    <div class="flex w-full max-w-[560px] animate-fade-up flex-col gap-[18px] self-center rounded-3xl bg-surface px-5 py-6 shadow-wizard sm:px-7">
      <div class="flex items-center gap-3.5">
        <span class="size-9 shrink-0 animate-spin rounded-full border-[3px] border-brand-100 border-t-brand-600" />
        <div class="flex flex-col gap-0.5">
          <span role="status" class="text-[17px] font-semibold">Sažimam dokument…</span>
          <span class="text-sm text-gray-600">{{ selectedMethod?.name }} · {{ ratio }}% dužine</span>
        </div>
        <span class="ml-auto text-sm font-semibold text-brand-600 tabular-nums">{{ progress }}%</span>
      </div>

      <div class="h-1.5 overflow-hidden rounded-[3px] bg-gray-200">
        <div class="h-full rounded-[3px] bg-brand-600 transition-[width] duration-500 ease-out" :style="{ width: `${progress}%` }" />
      </div>

      <ul class="flex flex-col gap-2.5">
        <li
          v-for="(phase, index) in LOADING_PHASES"
          :key="phase"
          class="flex items-center gap-2.5 text-sm"
          :class="index <= loadingPhase ? 'text-gray-900' : 'text-gray-500'"
        >
          <span v-if="index < loadingPhase" class="flex size-[18px] items-center justify-center rounded-full bg-brand-600">
            <Check :size="10" :stroke-width="4" class="text-white" />
          </span>
          <span v-else-if="index === loadingPhase" class="size-[18px] animate-spin rounded-full border-2 border-brand-100 border-t-brand-600" />
          <span v-else class="size-[18px] rounded-full border-2 border-gray-300" />
          {{ phase }}
        </li>
      </ul>
    </div>

    <ResultSkeleton />
  </div>
</template>
