---
title: "Similarity and Semantic Search"
summary: Embedding benchmarks already show a usable multilingual default for semantic search, but Latvian remains a narrower case because its current evaluation is FLORES-only.
track: Embedding
track_icon: "🔎"
topics: [embedding]
chips:
  - icon: "🔎"
    label: Embedding
  - icon: "1️⃣"
    label: Preliminary
date: 2026-04-20 06:40:00 +0300
---

Similarity and semantic search use embedding models to turn words, sentences, or passages into vectors so that related texts land close together in search. In archives, this matters when exact keyword matching is too brittle and users need concept-level retrieval across languages, spellings, and phrasing styles.

This is not the same as named entity extraction or sentiment analysis. The question here is whether the vector space itself preserves enough meaning to support paraphrase search, cross-lingual retrieval, and broader semantic lookup.

## What we tested

This note evaluates seven local embedding models across Estonian, Finnish, Latvian, and Russian. The scored local set included [`Octen/Octen-Embedding-4B`](https://huggingface.co/Octen/Octen-Embedding-4B), [`Octen/Octen-Embedding-8B`](https://huggingface.co/Octen/Octen-Embedding-8B), [`Octen/Octen-Embedding-8B-INT8`](https://huggingface.co/Octen/Octen-Embedding-8B-INT8), [`Qwen/Qwen3-Embedding-8B`](https://huggingface.co/Qwen/Qwen3-Embedding-8B), [`tencent/KaLM-Embedding-Gemma3-12B-2511`](https://huggingface.co/tencent/KaLM-Embedding-Gemma3-12B-2511), [`microsoft/harrier-oss-v1-27b`](https://huggingface.co/microsoft/harrier-oss-v1-27b), and [`nvidia/llama-embed-nemotron-8b`](https://huggingface.co/nvidia/llama-embed-nemotron-8b).

The headline score below is a composite `0-100` ranking built from min-max normalized results across four task families: MultiSimLex semantic similarity, TAPACO paraphrase retrieval, FLORES cross-lingual sentence retrieval, and MR-TyDi retrieval. API-only baselines such as `voyage-4-large` and `gemini-embedding-001` were listed in the wider experiment but were not part of the scored local run.

## Headline results

| Scope | Recommended model | Composite (0-100) | Note |
|---|---|---:|---|
| 🌍 Overall default | [`Octen/Octen-Embedding-8B`](https://huggingface.co/Octen/Octen-Embedding-8B) | 78.28 | Best average across all four target languages. |
| 🇪🇪 Estonian | [`Octen/Octen-Embedding-4B`](https://huggingface.co/Octen/Octen-Embedding-4B) | 76.02 | Best Estonian composite score. |
| 🇫🇮 Finnish | [`Octen/Octen-Embedding-8B`](https://huggingface.co/Octen/Octen-Embedding-8B) | 73.01 | Best Finnish composite score. |
| 🇱🇻 Latvian | [`tencent/KaLM-Embedding-Gemma3-12B-2511`](https://huggingface.co/tencent/KaLM-Embedding-Gemma3-12B-2511) | 100.00 | Strongest Latvian result, but Latvian is FLORES-only in this run. |
| 🪆 Russian | [`Octen/Octen-Embedding-4B`](https://huggingface.co/Octen/Octen-Embedding-4B) | 88.35 | Best Russian composite score. |

## Evaluation setup

### Evaluation datasets

- Semantic similarity: MultiSimLex with 1,888 scored word pairs per available language.
- Same-language paraphrase retrieval: TAPACO with 239 Estonian, 3,000 Finnish, and 3,000 Russian texts.
- Cross-lingual sentence retrieval: FLORES with 900 aligned sentence pairs for each evaluated language pair.
- Retrieval: MR-TyDi with 6,560 Finnish and 5,366 Russian queries.

### Evaluation models

- [`Octen/Octen-Embedding-8B`](https://huggingface.co/Octen/Octen-Embedding-8B)
- [`Octen/Octen-Embedding-8B-INT8`](https://huggingface.co/Octen/Octen-Embedding-8B-INT8)
- [`Octen/Octen-Embedding-4B`](https://huggingface.co/Octen/Octen-Embedding-4B)
- [`Qwen/Qwen3-Embedding-8B`](https://huggingface.co/Qwen/Qwen3-Embedding-8B)
- [`tencent/KaLM-Embedding-Gemma3-12B-2511`](https://huggingface.co/tencent/KaLM-Embedding-Gemma3-12B-2511)
- [`microsoft/harrier-oss-v1-27b`](https://huggingface.co/microsoft/harrier-oss-v1-27b)
- [`nvidia/llama-embed-nemotron-8b`](https://huggingface.co/nvidia/llama-embed-nemotron-8b)

## Early interpretation

The main engineering conclusion is that semantic search is already usable with current multilingual embedding models. `Octen/Octen-Embedding-8B` is the safest overall default because it stays near the top across all four target languages, while `Octen/Octen-Embedding-4B` is especially strong for Estonian and Russian and also leads the average once Latvian's narrower setup is excluded.

The biggest caveat is Latvian coverage. Because Latvian currently relies on FLORES only, the Latvian ranking says more about cross-lingual retrieval than about the broader mix of similarity and retrieval tasks used for Estonian, Finnish, and Russian.

## What to update next

The next useful update is to add Latvian benchmarks beyond FLORES so that all four languages are compared on a more balanced footing. After that, the strongest local models should be tested inside archive-style vector search workflows to measure retrieval quality, latency, and storage cost in a more operational setting.
