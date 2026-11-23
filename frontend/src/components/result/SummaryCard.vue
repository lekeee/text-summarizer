<script setup lang="ts">
import { Check, ChevronDown, ChevronUp, Copy, Download } from '@lucide/vue'
import { computed, onBeforeUnmount, onMounted, ref, useTemplateRef } from 'vue'
import BaseButton from '../base/BaseButton.vue'
import BaseCard from '../base/BaseCard.vue'

const props = defineProps<{
  summary: string
  methodName: string
  methodTag: string
  ratio: number
}>()

const COLLAPSED_HEIGHT = 320
const COLLAPSE_THRESHOLD = COLLAPSED_HEIGHT + 80

const content = useTemplateRef<HTMLElement>('content')
const copied = ref(false)
const expanded = ref(false)
const tooLong = ref(false)

const collapsed = computed(() => tooLong.value && !expanded.value)

let observer: ResizeObserver | undefined

function measureContent() {
  if (content.value) {
    tooLong.value = content.value.offsetHeight > COLLAPSE_THRESHOLD
  }
}

onMounted(() => {
  observer = new ResizeObserver(measureContent)
  if (content.value) observer.observe(content.value)
})

onBeforeUnmount(() => observer?.disconnect())

function toggleExpanded() {
  expanded.value = !expanded.value
  if (!expanded.value) {
    content.value?.scrollIntoView({ behavior: 'smooth', block: 'nearest' })
  }
}

async function copySummary() {
  await navigator.clipboard.writeText(props.summary)
  copied.value = true
  setTimeout(() => (copied.value = false), 1600)
}

function downloadSummary() {
  const blob = new Blob([props.summary], { type: 'text/plain;charset=utf-8' })
  const url = URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.href = url
  link.download = 'sazetak.txt'
  link.click()
  URL.revokeObjectURL(url)
}
</script>

<template>
  <BaseCard raised class="flex flex-[999_1_560px] flex-col">
    <div class="flex flex-wrap items-center justify-between gap-3 border-b border-gray-200 px-6 py-[18px]">
      <div class="flex flex-wrap items-center gap-2 text-[13px]">
        <span class="inline-flex items-center gap-1.5 rounded-full bg-brand-100 px-2.5 py-1 font-semibold text-brand-700">
          <span class="size-2 rounded-full bg-brand-600" />
          {{ methodName }}
        </span>
        <span class="rounded-full border border-gray-200 px-2.5 py-1 font-medium text-gray-700">{{ methodTag }}</span>
        <span class="rounded-full border border-gray-200 px-2.5 py-1 font-medium text-gray-700">{{ ratio }}% dužine</span>
      </div>

      <div class="flex gap-2">
        <BaseButton size="sm" @click="copySummary">
          <Check v-if="copied" :size="16" />
          <Copy v-else :size="16" />
          {{ copied ? 'Kopirano' : 'Kopiraj' }}
        </BaseButton>
        <BaseButton size="sm" variant="primary" @click="downloadSummary">
          <Download :size="16" />
          Preuzmi .txt
        </BaseButton>
      </div>
    </div>

    <div class="relative overflow-hidden" :style="collapsed ? { maxHeight: `${COLLAPSED_HEIGHT}px` } : undefined">
      <p id="summary-text" ref="content" class="p-6 text-base leading-[1.8] text-gray-800">{{ summary }}</p>

      <div v-if="collapsed" aria-hidden="true" class="pointer-events-none absolute inset-x-0 bottom-0 h-32">
        <div class="absolute inset-0 backdrop-blur-[3px] [mask-image:linear-gradient(to_bottom,transparent,black_70%)]" />
        <div class="absolute inset-0 bg-linear-to-b from-transparent via-surface/70 to-surface" />
      </div>
    </div>

    <div v-if="tooLong" class="flex justify-center px-6 pt-1 pb-5">
      <BaseButton size="xs" aria-controls="summary-text" :aria-expanded="expanded" @click="toggleExpanded">
        <ChevronUp v-if="expanded" :size="16" />
        <ChevronDown v-else :size="16" />
        {{ expanded ? 'Prikaži manje' : 'Prikaži ceo sažetak' }}
      </BaseButton>
    </div>
  </BaseCard>
</template>
