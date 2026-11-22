<script setup lang="ts">
const text = defineModel<string>({ required: true })
</script>

<template>
  <div class="overflow-hidden rounded-[14px] border border-gray-300 shadow-xs focus-within:border-brand-600">
    <label for="document-text" class="sr-only">Tekst dokumenta</label>
    <textarea
      id="document-text"
      v-model="text"
      placeholder="Nalepite tekst na srpskom (latinica ili ćirilica)…"
      class="block min-h-[230px] w-full resize-y p-4 text-[15px] leading-[1.65] text-gray-900 outline-none placeholder:text-gray-400"
    />
  </div>
</template>
