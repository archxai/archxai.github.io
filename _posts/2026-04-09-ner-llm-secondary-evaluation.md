---
title: "NER with LLMs"
summary: LLM-based NER is useful as a fallback and experimentation path, but current results make it slower and usually less accurate than dedicated NER models.
track: "NER + LLM"
track_icon: "🤖"
topics: [ner, llm]
chips:
  - icon: "📇"
    label: NER
  - icon: "🤖"
    label: LLM
  - icon: "2️⃣"
    label: Secondary
date: 2026-04-09 06:00:00 +0300
---

Large language models (LLMs) can also be asked to find named entities in text. Instead of using a dedicated NER model, the system gives the model instructions such as: list the people, organisations, and places in this passage.

This is useful when no good dedicated model exists, or when the project wants to test a new entity definition quickly. It is less useful when millions of sentences need to be processed, because LLM extraction is much slower.

## What we tested

This secondary note uses the LLM results from the current NER benchmark. The models were run locally through Ollama with prompt-based extraction, and the outputs were mapped to the same **PER / ORG / LOC** evaluation scheme used for dedicated NER models.

The headline score is **F1**, shown below as a percentage. The table highlights the strongest result reached by the local LLM set for each language.

## Headline results

| Language | Best local LLM | Dataset | F1 (%) |
|---|---|---|---:|
| 🇪🇪 Estonian | [`gpt-oss_120b`](https://ollama.com/library/gpt-oss) | `et_modern` | 64.6% |
| 🇫🇮 Finnish | [`gpt-oss_120b`](https://ollama.com/library/gpt-oss) | `fi_multileg` | 50.1% |
| 🇱🇻 Latvian | [`gpt-oss_120b`](https://ollama.com/library/gpt-oss) | `lv_diverse` | 76.9% |
| 🪆 Russian | [`gpt-oss_120b`](https://ollama.com/library/gpt-oss) | `ru_modern` | 88.8% |

## Evaluation setup

### Evaluation models

- [`gpt-oss_120b`](https://ollama.com/library/gpt-oss)
- [`deepseek-r1_70b`](https://ollama.com/library/deepseek-r1)
- [`qwen3_32b`](https://ollama.com/library/qwen3)
- [`llama4_latest`](https://ollama.com/library/llama4)
- [`gemma3_27b`](https://ollama.com/library/gemma3)
- [`mistral-large_latest`](https://ollama.com/library/mistral-large)

## Early interpretation

LLM extraction is not the main indexing recommendation at this stage. On most datasets, the best dedicated NER model is more accurate and much faster.

The value of LLMs is different: they are flexible. They can help with targeted enrichment, low-resource cases, rapid testing of new entity types, or cases where a dedicated model performs poorly and a slower fallback is acceptable.

## What to update next

The next useful update is to document the prompt format and add more dataset-level detail, especially for cases where LLM extraction still misses entities that a dedicated model can capture reliably. The benchmark should also keep testing smaller and faster local models, because the operational question is not only whether LLMs can work, but whether they can work at a realistic cost.
