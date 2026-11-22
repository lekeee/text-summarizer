<script setup lang="ts">
const ratio = defineModel<number>({ required: true })

defineProps<{
  targetSentences: number
  targetWords: number
}>()

const MIN = 10
const MAX = 60

const presets = [
  { label: 'Kratak', value: 15 },
  { label: 'Srednji', value: 30 },
  { label: 'Detaljan', value: 45 },
]
</script>

<template>
  <div class="flex flex-col gap-3.5">
    <div class="flex items-baseline justify-between gap-3">
      <label for="summary-length" class="text-sm font-semibold">Dužina sažetka</label>
      <span class="text-sm text-gray-600">≈ {{ targetSentences }} rečenica · {{ targetWords }} reči</span>
    </div>

    <div class="flex flex-wrap gap-2">
      <button
        v-for="preset in presets"
        :key="preset.value"
        type="button"
        :aria-pressed="ratio === preset.value"
        class="flex min-h-9 items-center gap-1.5 rounded-lg border px-3 py-1.5 text-sm font-medium transition-colors"
        :class="ratio === preset.value ? 'border-gray-900 bg-gray-900 text-surface' : 'border-gray-300 bg-surface text-gray-700 hover:bg-gray-50'"
        @click="ratio = preset.value"
      >
        {{ preset.label }}
        <span :class="ratio === preset.value ? 'text-gray-300' : 'text-gray-500'">{{ preset.value }}%</span>
      </button>
    </div>

    <div class="relative pt-[30px]">
      <span
        class="absolute top-0 -translate-x-1/2 rounded-md bg-gray-900 px-2 py-[3px] text-xs font-semibold whitespace-nowrap text-surface"
        :style="{ left: `${((ratio - MIN) / (MAX - MIN)) * 100}%` }"
      >
        {{ ratio }}%
      </span>
      <input
        id="summary-length"
        v-model.number="ratio"
        type="range"
        :min="MIN"
        :max="MAX"
        step="5"
        class="m-0 h-6 w-full accent-brand-600"
      />
      <div class="mt-1 flex justify-between text-xs text-gray-500">
        <span>{{ MIN }}%</span>
        <span>{{ MAX }}% originala</span>
      </div>
    </div>
  </div>
</template>
