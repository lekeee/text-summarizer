<script setup lang="ts">
import { Check, Copy, Download } from '@lucide/vue'
import { ref } from 'vue'
import BaseButton from '../base/BaseButton.vue'
import BaseCard from '../base/BaseCard.vue'

const props = defineProps<{
  summary: string
  methodName: string
  methodTag: string
  ratio: number
}>()

const copied = ref(false)

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

    <p class="p-6 text-base leading-[1.8] text-gray-800">{{ summary }}</p>
  </BaseCard>
</template>
