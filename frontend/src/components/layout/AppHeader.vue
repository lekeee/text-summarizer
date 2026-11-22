<script setup lang="ts">
import AppLogo from './AppLogo.vue'
import ThemeToggle from './ThemeToggle.vue'
</script>

<template>
  <header class="mx-auto flex w-full max-w-[1200px] items-center justify-between gap-3 px-4 py-5 sm:px-6">
    <div class="flex min-w-0 items-center gap-3">
      <AppLogo />
      <div class="flex min-w-0 flex-col">
        <span class="truncate text-[17px] leading-tight font-bold">Sistem za sažimanje teksta</span>
        <span class="truncate text-xs text-gray-600">Automatsko sažimanje dokumenata · srpski jezik</span>
      </div>
    </div>
    <ThemeToggle />
  </header>
</template>
