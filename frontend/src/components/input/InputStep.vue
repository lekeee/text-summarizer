<script setup lang="ts">
import { ArrowRight, Plus, X } from '@lucide/vue'
import { useSummarizer, type InputMode } from '../../composables/useSummarizer'
import { useTextStats } from '../../composables/useTextStats'
import { formatDecimal } from '../../utils/format'
import BaseButton from '../base/BaseButton.vue'
import WizardFooter from '../layout/WizardFooter.vue'
import FileDrop from './FileDrop.vue'
import TextInput from './TextInput.vue'
import UploadedFile from './UploadedFile.vue'

const { inputMode, text, upload, hasText, isUploading, uploadFile, loadSample, clearInput, goToSettings } = useSummarizer()
const { words, sentences, pages } = useTextStats(text)

const modes: { id: InputMode; label: string }[] = [
  { id: 'file', label: 'Fajl' },
  { id: 'text', label: 'Tekst' },
]
</script>

<template>
  <div class="flex animate-fade-up flex-col gap-5 px-5 pt-6 pb-7 sm:px-7">
    <div class="flex flex-wrap items-start justify-between gap-4">
      <div class="flex flex-col gap-1">
        <h2 class="text-[22px] font-semibold">Šta želite da sažmete?</h2>
        <span class="text-[15px] text-gray-600">Nalepite tekst ili učitajte dokument do 5 strana.</span>
      </div>

      <div role="tablist" aria-label="Način unosa" class="flex gap-1 rounded-[10px] border border-gray-200 bg-gray-100 p-1">
        <button
          v-for="mode in modes"
          :key="mode.id"
          type="button"
          role="tab"
          :aria-selected="inputMode === mode.id"
          class="min-h-9 rounded-[7px] px-3.5 py-1.5 text-sm font-semibold transition-colors"
          :class="inputMode === mode.id ? 'bg-surface text-gray-900 shadow-tab' : 'text-gray-600 hover:text-gray-900'"
          @click="inputMode = mode.id"
        >
          {{ mode.label }}
        </button>
      </div>
    </div>

    <template v-if="inputMode === 'file'">
      <FileDrop @select="uploadFile" />
      <UploadedFile v-if="upload" :upload="upload" />
    </template>
    <TextInput v-else v-model="text" />

    <div class="flex flex-wrap items-center justify-between gap-2.5">
      <div class="flex flex-wrap gap-2">
        <BaseButton size="xs" @click="loadSample">
          <Plus :size="14" :stroke-width="2.4" class="text-gray-500" />
          Primer teksta
        </BaseButton>
        <BaseButton v-if="hasText || upload" size="xs" @click="clearInput">
          <X :size="14" :stroke-width="2.4" class="text-gray-500" />
          Obriši
        </BaseButton>
      </div>
      <span class="text-sm text-gray-600">
        {{ words }} reči · {{ sentences }} rečenica · ≈ {{ formatDecimal(pages) }} str.
      </span>
    </div>
  </div>

  <WizardFooter>
    <span class="text-[13px] text-gray-500">Korak 1 od 2</span>
    <BaseButton variant="primary" :disabled="!hasText || isUploading" @click="goToSettings">
      Dalje
      <ArrowRight :size="16" :stroke-width="2.4" />
    </BaseButton>
  </WizardFooter>
</template>
