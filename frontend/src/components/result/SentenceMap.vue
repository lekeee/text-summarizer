<script setup lang="ts">
import { computed, ref } from 'vue'
import { countWords } from '../../composables/useTextStats'
import type { SentenceScore } from '../../types/summary'
import { formatDecimal } from '../../utils/format'
import BaseButton from '../base/BaseButton.vue'
import BaseCard from '../base/BaseCard.vue'

const props = defineProps<{ sentences: SentenceScore[] }>()

const focusedIndex = ref(props.sentences.find((sentence) => sentence.selected)?.index ?? 0)
const showAll = ref(false)

const focused = computed(() => props.sentences[focusedIndex.value])

const scoreRange = computed(() => {
  const scores = props.sentences.map((sentence) => sentence.score)
  const lowest = Math.min(...scores)
  return { lowest, span: Math.max(...scores) - lowest || 1 }
})

function relativeScore(score: number): number {
  return (score - scoreRange.value.lowest) / scoreRange.value.span
}

function segmentColor(sentence: SentenceScore): string {
  const strength = relativeScore(sentence.score)
  if (sentence.selected) {
    return `color-mix(in srgb, var(--color-brand-600) ${Math.round(55 + 45 * strength)}%, transparent)`
  }
  return `color-mix(in srgb, var(--color-gray-500) ${Math.round(10 + 35 * strength)}%, transparent)`
}
</script>

<template>
  <BaseCard class="flex flex-col gap-[18px] p-5 sm:p-6">
    <div class="flex flex-wrap items-start justify-between gap-3">
      <div class="flex flex-col gap-1">
        <h2 id="sentence-map" class="text-[17px] font-semibold">Mapa važnosti rečenica</h2>
        <span class="text-sm text-gray-600">
          Svaki segment je jedna rečenica originala, širina prati njenu dužinu. Izaberite segment da vidite rečenicu.
        </span>
      </div>
      <div class="flex items-center gap-3.5 text-xs text-gray-600">
        <span class="flex items-center gap-1.5">
          <span class="h-2.5 w-6 rounded-[3px] bg-linear-to-r from-gray-500/10 to-gray-500/45" />
          Ocena
        </span>
        <span class="flex items-center gap-1.5">
          <span class="h-2.5 w-3 rounded-[3px] bg-brand-600" />
          U sažetku
        </span>
      </div>
    </div>

    <div class="flex h-12 gap-[3px]" role="list" aria-labelledby="sentence-map">
      <button
        v-for="sentence in sentences"
        :key="sentence.index"
        type="button"
        role="listitem"
        :aria-label="`Rečenica ${sentence.index + 1}`"
        class="min-w-1 rounded-md transition-transform duration-100"
        :class="sentence.index === focusedIndex ? '-translate-y-[3px] shadow-focus' : ''"
        :style="{ flex: `${Math.max(1, countWords(sentence.text))} 1 0`, background: segmentColor(sentence) }"
        @mouseenter="focusedIndex = sentence.index"
        @focus="focusedIndex = sentence.index"
        @click="focusedIndex = sentence.index"
      />
    </div>

    <div v-if="focused" class="flex items-start gap-3.5 rounded-xl border border-gray-200 bg-gray-50 px-4 py-3.5">
      <span
        class="shrink-0 rounded-md border border-gray-200 bg-surface px-2 py-[3px] text-xs font-bold"
        :class="focused.selected ? 'text-brand-600' : 'text-gray-600'"
      >
        #{{ focused.index + 1 }}
      </span>
      <div class="flex min-w-0 flex-col gap-1.5">
        <span class="text-xs text-gray-600">
          Ocena {{ formatDecimal(focused.score, 2) }} · {{ focused.selected ? 'u sažetku' : 'nije u sažetku' }}
        </span>
        <span class="text-sm leading-relaxed">{{ focused.text }}</span>
      </div>
    </div>

    <BaseButton size="xs" class="self-start" :aria-expanded="showAll" @click="showAll = !showAll">
      {{ showAll ? 'Sakrij listu rečenica' : 'Prikaži sve rečenice sa ocenama' }}
    </BaseButton>

    <ol v-if="showAll" class="flex flex-col gap-1">
      <li
        v-for="sentence in sentences"
        :key="sentence.index"
        class="flex flex-wrap items-center gap-x-4 gap-y-2 rounded-[10px] px-3 py-2.5"
        :class="sentence.selected ? 'bg-brand-100' : ''"
      >
        <span class="w-7 shrink-0 text-xs font-semibold text-gray-500">#{{ sentence.index + 1 }}</span>
        <span
          class="min-w-0 flex-[999_1_420px] text-sm leading-normal"
          :class="sentence.selected ? 'text-gray-900' : 'text-gray-600'"
        >
          {{ sentence.text }}
        </span>
        <span class="flex flex-[1_1_140px] items-center gap-2.5">
          <span class="h-1.5 flex-1 overflow-hidden rounded-[3px] bg-gray-200">
            <span
              class="block h-full rounded-[3px]"
              :class="sentence.selected ? 'bg-brand-600' : 'bg-gray-400'"
              :style="{ width: `${Math.round(sentence.score * 100)}%` }"
            />
          </span>
          <span class="w-[34px] text-right text-xs text-gray-700 tabular-nums">{{ formatDecimal(sentence.score, 2) }}</span>
        </span>
      </li>
    </ol>
  </BaseCard>
</template>
