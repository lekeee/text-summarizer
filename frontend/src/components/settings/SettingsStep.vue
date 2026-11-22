<script setup lang="ts">
import { ArrowLeft } from '@lucide/vue'
import { computed } from 'vue'
import { useSummarizer } from '../../composables/useSummarizer'
import { useTextStats } from '../../composables/useTextStats'
import AlertMessage from '../base/AlertMessage.vue'
import BaseButton from '../base/BaseButton.vue'
import WizardFooter from '../layout/WizardFooter.vue'
import LengthPicker from './LengthPicker.vue'
import MethodCard from './MethodCard.vue'

const { text, methods, methodId, ratio, selectedMethod, summarizeError, goToInput, generate } = useSummarizer()
const { words, sentences } = useTextStats(text)

const targetSentences = computed(() => Math.max(1, Math.round((sentences.value * ratio.value) / 100)))
const targetWords = computed(() => Math.round((words.value * ratio.value) / 100))
const canGenerate = computed(() => selectedMethod.value?.available ?? false)
</script>

<template>
  <div class="flex animate-fade-up flex-col gap-6 px-5 pt-6 pb-7 sm:px-7">
    <div class="flex flex-col gap-1">
      <h2 class="text-[22px] font-semibold">Kako želite da sažmete?</h2>
      <span class="text-[15px] text-gray-600">{{ words }} reči spremno za obradu. Izaberite metod i dužinu sažetka.</span>
    </div>

    <fieldset>
      <legend class="mb-3 text-sm font-semibold">Metod</legend>
      <div v-if="methods.length" class="flex flex-wrap gap-3">
        <MethodCard
          v-for="method in methods"
          :key="method.id"
          :method="method"
          :selected="method.id === methodId"
          @select="methodId = method.id"
        />
      </div>
      <p v-else class="text-sm text-gray-600">Lista metoda nije učitana.</p>
    </fieldset>

    <LengthPicker v-model="ratio" :target-sentences="targetSentences" :target-words="targetWords" />

    <AlertMessage v-if="summarizeError" :message="summarizeError" />
  </div>

  <WizardFooter>
    <BaseButton @click="goToInput">
      <ArrowLeft :size="16" :stroke-width="2.4" />
      Nazad
    </BaseButton>
    <BaseButton variant="primary" :disabled="!canGenerate" @click="generate">Generiši sažetak</BaseButton>
  </WizardFooter>
</template>
