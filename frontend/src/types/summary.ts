export type MethodKind = 'ekstraktivni' | 'apstraktivni'

export interface SummaryMethod {
  id: string
  name: string
  description: string
  kind: MethodKind | null
  available: boolean
}

export interface SentenceScore {
  index: number
  text: string
  score: number
  selected: boolean
}

export interface SummaryStats {
  original_words: number
  summary_words: number
  original_sentences: number
  summary_sentences: number
}

export interface SummaryResult {
  method: string
  ratio: number
  summary: string
  sentences: SentenceScore[]
  stats: SummaryStats
  elapsed_ms: number
}

export interface ExtractedDocument {
  file_name: string
  text: string
  words: number
  sentences: number
  pages: number
}
