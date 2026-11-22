<script setup lang="ts">
import { Check } from '@lucide/vue'
import { computed } from 'vue'
import type { SummaryMethod, SummaryResult } from '../../types/summary'
import { capitalize, formatDecimal, formatReadingTime } from '../../utils/format'
import BaseButton from '../base/BaseButton.vue'
import CompressionDonut from './CompressionDonut.vue'
import SentenceMap from './SentenceMap.vue'
import StatTile from './StatTile.vue'
import SummaryCard from './SummaryCard.vue'

const props = defineProps<{
  result: SummaryResult
  method?: SummaryMethod
}>()

defineEmits<{
  editSettings: []
  restart: []
}>()

const WORDS_PER_MINUTE = 200

const stats = computed(() => {
  const { original_words, summary_words, original_sentences, summary_sentences } = props.result.stats
  const savedSeconds = Math.max(0, Math.round(((original_words - summary_words) / WORDS_PER_MINUTE) * 60))
  const averageLength = summary_sentences ? summary_words / summary_sentences : 0

  return [
    { label: 'Rečenice', value: `${summary_sentences} / ${original_sentences}`, hint: 'u sažetku / u originalu' },
    { label: 'Ušteda čitanja', value: formatReadingTime(savedSeconds), hint: `pri ${WORDS_PER_MINUTE} reči u minuti` },
    { label: 'Vreme obrade', value: `${formatDecimal(props.result.elapsed_ms / 1000, 2)} s`, hint: 'izmereno na serveru' },
    { label: 'Dužina rečenice', value: formatDecimal(averageLength), hint: 'prosečno reči u sažetku' },
  ]
})
</script>

<template>
  <div class="flex animate-fade-up flex-col gap-6">
    <div class="flex flex-wrap items-end justify-between gap-4 pt-2">
      <div class="flex flex-col gap-1.5">
        <span class="inline-flex items-center gap-2 text-[13px] font-semibold text-brand-600">
          <span class="flex size-[18px] items-center justify-center rounded-full bg-brand-600">
            <Check :size="10" :stroke-width="4" class="text-white" />
          </span>
          Gotovo
        </span>
        <h1 class="text-[clamp(26px,3.5vw,34px)] font-bold tracking-tight">Vaš sažetak je spreman</h1>
      </div>
      <div class="flex flex-wrap gap-2.5">
        <BaseButton size="sm" @click="$emit('editSettings')">Promeni podešavanja</BaseButton>
        <BaseButton size="sm" variant="dark" @click="$emit('restart')">Novi dokument</BaseButton>
      </div>
    </div>

    <div class="flex flex-wrap items-stretch gap-6">
      <SummaryCard
        :summary="result.summary"
        :method-name="method?.name ?? result.method"
        :method-tag="method?.kind ? capitalize(method.kind) : ''"
        :ratio="result.ratio"
      />

      <aside aria-label="Statistika sažetka" class="flex min-w-0 flex-[1_1_340px] flex-col gap-4">
        <CompressionDonut :summary-words="result.stats.summary_words" :original-words="result.stats.original_words" />
        <div class="flex flex-wrap gap-4">
          <StatTile v-for="stat in stats" :key="stat.label" v-bind="stat" />
        </div>
      </aside>
    </div>

    <SentenceMap :sentences="result.sentences" />
  </div>
</template>
