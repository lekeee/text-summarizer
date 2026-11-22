<script setup lang="ts">
import { CloudUpload } from '@lucide/vue'
import { ref } from 'vue'

const emit = defineEmits<{ select: [file: File] }>()

const dragging = ref(false)

function onDrop(event: DragEvent) {
  dragging.value = false
  const file = event.dataTransfer?.files[0]
  if (file) emit('select', file)
}

function onChange(event: Event) {
  const input = event.target as HTMLInputElement
  const file = input.files?.[0]
  if (file) emit('select', file)
  input.value = ''
}
</script>

<template>
  <label
    for="document-file"
    class="relative flex min-h-[230px] cursor-pointer flex-col items-center justify-center gap-2.5 overflow-hidden rounded-2xl border-[1.5px] border-dashed px-6 py-8 text-center transition-colors focus-within:outline-2 focus-within:outline-offset-2 focus-within:outline-brand-600"
    :class="dragging ? 'border-brand-600 bg-brand-50' : 'border-gray-300 bg-gray-25'"
    @dragover.prevent="dragging = true"
    @dragleave="dragging = false"
    @drop.prevent="onDrop"
  >
    <span
      aria-hidden="true"
      class="absolute top-[22px] right-7 hidden h-[116px] w-[92px] animate-bob flex-col gap-1.5 rounded-[10px] bg-surface p-3 shadow-file sm:flex"
    >
      <span class="block h-3.5 w-[34px] rounded bg-brand-100" />
      <span class="block h-[5px] rounded-[3px] bg-gray-200" />
      <span class="block h-[5px] rounded-[3px] bg-gray-200" />
      <span class="block h-[5px] w-[70%] rounded-[3px] bg-gray-200" />
      <span class="block h-[5px] rounded-[3px] bg-gray-200" />
      <span class="block h-[5px] w-1/2 rounded-[3px] bg-gray-200" />
    </span>

    <span class="flex size-12 items-center justify-center rounded-xl bg-surface shadow-icon">
      <CloudUpload :size="22" class="text-gray-700" />
    </span>
    <span class="text-base font-semibold">{{ dragging ? 'Pustite fajl ovde' : 'Prevucite dokument ovde' }}</span>
    <span class="text-sm text-gray-600">ili kliknite za izbor · TXT, DOCX, PDF · do 5 strana</span>

    <input id="document-file" type="file" accept=".txt,.docx,.pdf" class="sr-only" @change="onChange" />
  </label>
</template>
