<script setup lang="ts">
const { raised = false } = defineProps<{ raised?: boolean }>()
</script>

<template>
  <div class="min-w-0 rounded-[20px] bg-surface" :class="raised ? 'shadow-panel-lg' : 'shadow-panel'">
    <slot />
  </div>
</template>
