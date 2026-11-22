import { computed, type Ref } from 'vue'

export const WORDS_PER_PAGE = 300

const WORD = /\p{L}+/gu
const SENTENCE_BREAK = /(?<=[.!?…])\s+(?=[\p{Lu}\d"„«(])|\n\s*\n/u
const LETTER = /\p{L}/u

export function countWords(text: string): number {
  return text.match(WORD)?.length ?? 0
}

export function countSentences(text: string): number {
  return text.split(SENTENCE_BREAK).filter((part) => LETTER.test(part)).length
}

export function useTextStats(text: Ref<string>) {
  const words = computed(() => countWords(text.value))
  const sentences = computed(() => countSentences(text.value))
  const pages = computed(() => words.value / WORDS_PER_PAGE)

  return { words, sentences, pages }
}
