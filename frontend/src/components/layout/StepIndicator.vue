<script setup lang="ts">
defineProps<{
  steps: string[]
  current: number
}>()
</script>

<template>
  <ol class="flex gap-2.5">
    <li v-for="(step, index) in steps" :key="step" class="flex flex-1 flex-col gap-2">
      <div class="h-1 rounded-sm" :class="index <= current ? 'bg-brand-600' : 'bg-gray-200'" />
      <span class="text-xs font-semibold" :class="index <= current ? 'text-gray-900' : 'text-gray-500'">
        {{ index + 1 }}. {{ step }}
      </span>
    </li>
  </ol>
</template>
