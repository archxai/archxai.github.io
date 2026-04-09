---
title: "Secondary evaluation: NER with LLMs"
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

## Illustration placeholder

<div class="placeholder-figure">Illustration placeholder: add a simple prompt-and-answer example showing how an LLM extracts people, organisations, and places from the same archival text.</div>

## What we tested

This secondary note uses the LLM results from the current NER benchmark. The models were run locally with prompt-based extraction, and the outputs were mapped to the same **PER / ORG / LOC** evaluation scheme used for dedicated NER models.

The headline score is **F1**. The table below uses the same out-of-domain or stress-test datasets as the dedicated-model note where possible, so the two posts are easy to compare.

## Best current results on out-of-domain data

| Language | Out-of-domain dataset | Best current LLM | Accuracy score |
|---|---|---|---:|
| Estonian | `et_multileg` legal text | `gpt-oss:120b` | F1 56.0% |
| Finnish | `fi_multileg` legal text | `qwen3:32b` | F1 44.7% |
| Latvian | `lv_multileg` legal text | `gpt-oss:120b` | F1 54.5% |
| Russian | `ru_oldish` older-domain mix | `gpt-oss:120b` | F1 71.0% |

## Early interpretation

LLM extraction is not the main indexing recommendation at this stage. On most datasets, the best dedicated NER model is more accurate and much faster.

The value of LLMs is different: they are flexible. They can help with targeted enrichment, low-resource cases, rapid testing of new entity types, or cases where a dedicated model performs poorly and a slower fallback is acceptable.

## What to update next

The next useful update is to add a visual comparison between a dedicated NER pipeline and an LLM prompt workflow. The benchmark should also keep testing smaller and faster LLMs, because the operational question is not only whether LLMs can work, but whether they can work at a realistic cost.
