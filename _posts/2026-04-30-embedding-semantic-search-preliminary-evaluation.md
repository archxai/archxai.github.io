---
title: "Similarity and Semantic Search"
summary: Similarity and semantic search use embedding models to turn words, sentences, or passages into vectors so that related texts land close together in search. In archives, this matters when exact keyword matching is too brittle and users need concept-level retrieval across languages, spellings, and phrasing styles.
track: Embedding
track_icon: "🔎"
topics: [embedding]
chips:
  - icon: "🔎"
    label: Embedding
  - icon: "1️⃣"
    label: Preliminary
date: 2026-04-30 06:40:00 +0300
---

## What we tested

We evaluated seven local embedding models across Estonian, Finnish, Latvian, and Russian:

- [`Octen/Octen-Embedding-4B`](https://huggingface.co/Octen/Octen-Embedding-4B)
- [`Octen/Octen-Embedding-8B`](https://huggingface.co/Octen/Octen-Embedding-8B)
- [`Octen/Octen-Embedding-8B-INT8`](https://huggingface.co/Octen/Octen-Embedding-8B-INT8)
- [`Qwen/Qwen3-Embedding-8B`](https://huggingface.co/Qwen/Qwen3-Embedding-8B)
- [`tencent/KaLM-Embedding-Gemma3-12B-2511`](https://huggingface.co/tencent/KaLM-Embedding-Gemma3-12B-2511)
- [`microsoft/harrier-oss-v1-27b`](https://huggingface.co/microsoft/harrier-oss-v1-27b)
- [`nvidia/llama-embed-nemotron-8b`](https://huggingface.co/nvidia/llama-embed-nemotron-8b)

API-only baselines such as `voyage-4-large` and `gemini-embedding-001` were listed in the wider benchmark selection, but were not part of this local scored run.

The headline score is a composite `0-100` ranking. Each task is first min-max normalized across the evaluated models, then averaged within each task family, then averaged across task families for the language. This keeps one dataset family from dominating the result just because it contributes more task rows.

## Headline recommendations

| Scope | Recommended model | Composite (0-100) | Note |
|---|---|---:|---|
| 🌐 Overall default | [`Octen/Octen-Embedding-4B`](https://huggingface.co/Octen/Octen-Embedding-4B) | 77.51 | Best four-language average, fastest measured embedding time, and smallest vectors. |
| 🇪🇪 Estonian | [`Octen/Octen-Embedding-4B`](https://huggingface.co/Octen/Octen-Embedding-4B) | 76.02 | Best Estonian composite score. |
| 🇫🇮 Finnish | [`Octen/Octen-Embedding-8B`](https://huggingface.co/Octen/Octen-Embedding-8B) | 73.01 | Best Finnish composite score. |
| 🇱🇻 Latvian | [`Octen/Octen-Embedding-8B-INT8`](https://huggingface.co/Octen/Octen-Embedding-8B-INT8) | 86.27 | Best Latvian composite after adding synthetic MultiSimLex and TAPACO. |
| 🪆 Russian | [`Octen/Octen-Embedding-4B`](https://huggingface.co/Octen/Octen-Embedding-4B) | 88.35 | Best Russian composite score. |

## Language rankings

| Language | Rank 1 | Rank 2 | Rank 3 |
|---|---|---|---|
| Estonian | `Octen-Embedding-4B` (76.02) | `KaLM-Embedding-Gemma3-12B-2511` (74.54) | `Octen-Embedding-8B` (72.61) |
| Finnish | `Octen-Embedding-8B` (73.01) | `Octen-Embedding-8B-INT8` (69.29) | `Octen-Embedding-4B` (65.23) |
| Latvian | `Octen-Embedding-8B-INT8` (86.27) | `Octen-Embedding-4B` (80.44) | `Octen-Embedding-8B` (79.51) |
| Russian | `Octen-Embedding-4B` (88.35) | `Octen-Embedding-8B` (78.28) | `Octen-Embedding-8B-INT8` (75.32) |

The overall average across the four target languages now ranks the models as follows:

| Rank | Model | Average composite |
|---:|---|---:|
| 1 | `Octen-Embedding-4B` | 77.51 |
| 2 | `Octen-Embedding-8B-INT8` | 75.87 |
| 3 | `Octen-Embedding-8B` | 75.85 |
| 4 | `Qwen3-Embedding-8B` | 63.73 |
| 5 | `KaLM-Embedding-Gemma3-12B-2511` | 62.20 |
| 6 | `harrier-oss-v1-27b` | 52.90 |
| 7 | `llama-embed-nemotron-8b` | 22.20 |

## Evaluation datasets and metrics

- MultiSimLex tests word-level semantic similarity. Model similarity scores are compared with human similarity judgments using Spearman correlation. Higher is better.
- TAPACO tests same-language paraphrase retrieval. Each sentence is used as a query, and the score is MRR@10: models are rewarded for ranking another sentence from the same paraphrase cluster near the top.
- FLORES tests cross-lingual sentence alignment. The metric is symmetric Recall@1: each sentence should retrieve its translation in the paired language, and the score averages both retrieval directions.
- MR-TyDi tests retrieval over Finnish and Russian query-passage examples. The metric is MRR@10 over candidate passages.

Dataset sizes in this run were:

| Dataset family | Coverage |
|---|---|
| MultiSimLex | 1,888 word pairs per language, including synthetic Latvian translated from English. |
| TAPACO | 239 Estonian, 3,000 Finnish, 2,337 synthetic Latvian, and 3,000 Russian texts. |
| FLORES | 900 aligned sentence pairs for each language pair. |
| MR-TyDi | 6,560 Finnish and 5,366 Russian queries. |

The Latvian MultiSimLex and TAPACO results should be read as a practical approximation, not as a native Latvian gold standard. The machine translated datasets reduce the bias of the earlier FLORES-only Latvian ranking, but a future native Latvian evaluation set would still be better.

## Latency and vector cost

We also measured operational performance on a multilingual TAPACO-derived sample with 3,000 corpus texts and 512 query texts. The search benchmark used an exact flat NumPy dot-product index, so the numbers are useful as a local baseline rather than as vector-database or approximate-nearest-neighbour production latency.

| Model | Dim | Embed ms/query | Index build ms | Query p50 ms | Query p95 ms | Memory/vector |
|---|---:|---:|---:|---:|---:|---:|
| `Octen-Embedding-4B` | 2,560 | 13.27 | 8.02 | 0.61 | 0.72 | 10,240 B |
| `Octen-Embedding-8B-INT8` | 4,096 | 25.01 | 18.76 | 1.09 | 1.27 | 16,384 B |
| `Octen-Embedding-8B` | 4,096 | 23.19 | 20.14 | 1.28 | 1.53 | 16,384 B |
| `Qwen3-Embedding-8B` | 4,096 | 23.19 | 18.80 | 1.43 | 2.08 | 16,384 B |
| `llama-embed-nemotron-8b` | 4,096 | 22.86 | 19.75 | 1.21 | 1.50 | 16,384 B |
| `KaLM-Embedding-Gemma3-12B-2511` | 3,840 | 36.29 | 10.37 | 1.12 | 3.13 | 15,360 B |
| `harrier-oss-v1-27b` | 5,376 | 86.26 | 13.78 | 1.57 | 3.52 | 21,504 B |

This performance view strengthens the case for `Octen-Embedding-4B` as the default operational choice. It is not only the best average scorer; it is also materially faster and cheaper to store because it emits 2,560-dimensional vectors rather than 4,096-dimensional or larger vectors.

## Interpretation

The main engineering conclusion is that multilingual semantic search is ready for archive-style experimentation. The safest default is now `Octen/Octen-Embedding-4B`, especially when speed and index size matter. `Octen/Octen-Embedding-8B` remains the best Finnish-specific model, while `Octen/Octen-Embedding-8B-INT8` is the strongest Latvian result in the updated evaluation.

The key caveat has shifted. The problem is no longer that Latvian is FLORES-only; it is that the added Latvian similarity and paraphrase datasets are machine-translated. That is still a weaker evidence base than native Latvian benchmark data, but it is a more balanced comparison than the previous version.

## What to update next

The next useful update is to validate the top models on archive-style retrieval tasks: real collection descriptions, OCR or HTR text, query logs where available, and multilingual search examples from project partners. That would test whether the benchmark ranking transfers to the retrieval behaviour users actually experience.
