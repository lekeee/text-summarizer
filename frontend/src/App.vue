<script setup lang="ts">
import { onMounted, watch } from 'vue'
import AlertMessage from './components/base/AlertMessage.vue'
import InputStep from './components/input/InputStep.vue'
import AppHeader from './components/layout/AppHeader.vue'
import WizardCard from './components/layout/WizardCard.vue'
import LoadingView from './components/loading/LoadingView.vue'
import ResultView from './components/result/ResultView.vue'
import SettingsStep from './components/settings/SettingsStep.vue'
import { useSummarizer } from './composables/useSummarizer'

const { screen, result, selectedMethod, methodsError, serverWaking, loadMethods, goToSettings, restart } =
  useSummarizer()

onMounted(loadMethods)
watch(screen, () => window.scrollTo({ top: 0 }))
</script>

<template>
  <div class="flex min-h-screen flex-col">
    <AppHeader />

    <main class="mx-auto flex w-full max-w-[1200px] flex-1 flex-col gap-6 px-4 pt-4 pb-16 sm:px-6">
      <AlertMessage
        v-if="serverWaking"
        tone="info"
        message="Server se pokreće posle neaktivnosti. Prvi zahtev može da potraje do jednog minuta."
      />
      <AlertMessage v-if="methodsError" :message="methodsError" action-label="Pokušaj ponovo" @action="loadMethods" />

      <div v-if="screen === 'input' || screen === 'settings'" class="flex flex-col items-center gap-7 pt-6">
        <div class="flex max-w-[640px] flex-col gap-2.5 text-center">
          <h1 class="text-[clamp(28px,4vw,40px)] leading-tight font-bold tracking-tight">Dug dokument, kratak sažetak</h1>
          <p class="text-base leading-relaxed text-gray-600">U dva koraka: dodajte tekst, izaberite metod. Ostalo radi sistem.</p>
        </div>

        <WizardCard :step="screen === 'input' ? 0 : 1">
          <InputStep v-if="screen === 'input'" />
          <SettingsStep v-else />
        </WizardCard>
      </div>

      <LoadingView v-else-if="screen === 'loading'" />

      <ResultView
        v-else-if="screen === 'result' && result"
        :result="result"
        :method="selectedMethod"
        @edit-settings="goToSettings"
        @restart="restart"
      />
    </main>
  </div>
</template>
