<script setup lang="ts">
defineProps<{
  label: string
  value: string
  hint: string
}>()
</script>

<template>
  <div class="flex flex-[1_1_140px] flex-col gap-1.5 rounded-2xl bg-surface px-[18px] py-4 shadow-panel">
    <span class="text-[13px] text-gray-600">{{ label }}</span>
    <span class="text-2xl font-bold tracking-tight">{{ value }}</span>
    <span class="text-xs text-gray-500">{{ hint }}</span>
  </div>
</template>
