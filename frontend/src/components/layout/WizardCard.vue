<script setup lang="ts">
import StepIndicator from './StepIndicator.vue'

defineProps<{ step: number }>()

const steps = ['Tekst', 'Metod', 'Rezultat']
</script>

<template>
  <div class="w-full max-w-[760px] animate-fade-up overflow-hidden rounded-3xl bg-surface shadow-wizard">
    <div class="px-5 pt-6 sm:px-7">
      <StepIndicator :steps="steps" :current="step" />
    </div>
    <slot />
  </div>
</template>
