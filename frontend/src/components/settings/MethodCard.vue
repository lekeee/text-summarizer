<script setup lang="ts">
import { Hourglass, Waypoints } from '@lucide/vue'
import { computed } from 'vue'
import type { SummaryMethod } from '../../types/summary'
import { capitalize } from '../../utils/format'

const props = defineProps<{
  method: SummaryMethod
  selected: boolean
}>()

defineEmits<{ select: [] }>()

const tag = computed(() => (props.method.kind ? capitalize(props.method.kind) : 'Uskoro'))
</script>

<template>
  <button
    type="button"
    :aria-pressed="selected"
    :disabled="!method.available"
    class="flex flex-[1_1_200px] flex-col gap-3 rounded-2xl border-[1.5px] p-4 text-left transition-[border-color,box-shadow] disabled:cursor-not-allowed disabled:opacity-55"
    :class="selected ? 'border-brand-600 bg-brand-25 shadow-selected' : 'border-gray-200 bg-surface shadow-xs enabled:hover:border-gray-300'"
    @click="$emit('select')"
  >
    <span class="flex w-full items-start justify-between">
      <span
        class="flex size-11 items-center justify-center rounded-xl"
        :class="method.available ? 'bg-brand-100 text-brand-600' : 'bg-gray-100 text-gray-500'"
      >
        <Waypoints v-if="method.available" :size="24" />
        <Hourglass v-else :size="22" />
      </span>
      <span
        class="flex size-5 items-center justify-center rounded-full border-[1.5px]"
        :class="selected ? 'border-brand-600 bg-brand-600' : 'border-gray-300 bg-surface'"
      >
        <span v-if="selected" class="size-2 rounded-full bg-white" />
      </span>
    </span>

    <span class="flex flex-col gap-1">
      <span class="text-[15px] font-semibold">{{ method.name }}</span>
      <span class="text-[13px] leading-normal text-gray-600">{{ method.description }}</span>
    </span>

    <span class="self-start rounded-md border border-gray-200 px-2 py-0.5 text-xs font-medium text-gray-700">{{ tag }}</span>
  </button>
</template>
