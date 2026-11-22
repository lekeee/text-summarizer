<script setup lang="ts">
type Variant = 'primary' | 'secondary' | 'dark'
type Size = 'xs' | 'sm' | 'md'

const { variant = 'secondary', size = 'md' } = defineProps<{
  variant?: Variant
  size?: Size
}>()

const variants: Record<Variant, string> = {
  primary: 'border-brand-600 bg-brand-600 text-white enabled:hover:border-brand-700 enabled:hover:bg-brand-700',
  secondary: 'border-gray-300 bg-surface text-gray-700 shadow-xs enabled:hover:bg-gray-50',
  dark: 'border-gray-900 bg-gray-900 text-surface enabled:hover:bg-gray-800',
}

const sizes: Record<Size, string> = {
  xs: 'min-h-[34px] rounded-lg px-2.5 py-1 text-sm font-medium',
  sm: 'min-h-10 rounded-[10px] px-3.5 py-2 text-sm font-semibold',
  md: 'min-h-11 rounded-[10px] px-5 py-2.5 text-[15px] font-semibold',
}
</script>

<template>
  <button
    type="button"
    class="inline-flex items-center justify-center gap-2 border transition-colors disabled:cursor-not-allowed disabled:opacity-45"
    :class="[variants[variant], sizes[size]]"
  >
    <slot />
  </button>
</template>
