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
date: 2026-01-30 06:00:00 +0200
---

Large language models (LLMs) can also be asked to find named entities in text. Instead of using a dedicated NER model, the system gives the model instructions such as: list the people, organisations, and places in this passage.

This is useful when no good dedicated model exists, or when the project wants to test a new entity definition quickly. It is less useful when millions of sentences need to be processed, because LLM extraction is much slower.

## What we tested

This secondary note uses the LLM results from the current NER benchmark. The models were run locally through Ollama with prompt-based extraction, and the outputs were mapped to the same **PER / ORG / LOC** evaluation scheme used for dedicated NER models.

The headline score is **F1**, shown below as a percentage. The table highlights the strongest result reached by the local LLM set for each language.

## Headline results

| Language | Best local LLM | Dataset | F1 (%) |
|---|---|---|---:|
| 🇪🇪 Estonian | [`gpt-oss_120b`](https://ollama.com/library/gpt-oss) | [`et_modern`](https://github.com/TartuNLP/EstNER) | 64.6% |
| 🇫🇮 Finnish | [`gpt-oss_120b`](https://ollama.com/library/gpt-oss) | [`fi_multileg`](https://github.com/tilde-nlp/MultiLeg-dataset/) | 50.1% |
| 🇱🇻 Latvian | [`gpt-oss_120b`](https://ollama.com/library/gpt-oss) | [`lv_diverse`](https://github.com/LUMII-AILab/FullStack) | 76.9% |
| 🪆 Russian | [`gpt-oss_120b`](https://ollama.com/library/gpt-oss) | [`ru_modern`](https://bsnlp.cs.helsinki.fi/bsnlp-2019/shared_task.html) | 88.8% |

## Evaluation setup

### Evaluation models

- [`gpt-oss_120b`](https://ollama.com/library/gpt-oss)
- [`deepseek-r1_70b`](https://ollama.com/library/deepseek-r1)
- [`qwen3_32b`](https://ollama.com/library/qwen3)
- [`llama4_latest`](https://ollama.com/library/llama4)
- [`gemma3_27b`](https://ollama.com/library/gemma3)
- [`mistral-large_latest`](https://ollama.com/library/mistral-large)

### Evaluation datasets

- 🌐 Multilingual
  - [`et_multileg.conll`](https://github.com/tilde-nlp/MultiLeg-dataset/) (100 804)
  - [`fi_multileg.conll`](https://github.com/tilde-nlp/MultiLeg-dataset/) (96 488)
  - [`lv_multileg.conll`](https://github.com/tilde-nlp/MultiLeg-dataset/) (110 860)
- 🇪🇪 Estonian
  - [`et_modern.conll`](https://github.com/TartuNLP/EstNER) (165 947)
  - [`et_old.conll`](https://github.com/soras/vk_ner_lrec_2022) (54 069)
- 🇫🇮 Finnish
  - [`fi_old.conll`](https://zenodo.org/records/4573313) (51 839)
- 🇱🇻 Latvian
  - [`lv_modern.conll`](https://github.com/RinaldsViksna/Latvian-food-NER-corpus) (21 951)
  - [`lv_diverse.conll`](https://github.com/LUMII-AILab/FullStack) (199 155)
- 🪆 Russian
  - [`ru_modern.conll`](https://bsnlp.cs.helsinki.fi/bsnlp-2019/shared_task.html) (47 187)
  - [`ru_oldish.conll`](https://github.com/razmecheno/main) (18 838)

## Early interpretation

LLM extraction is not the main indexing recommendation at this stage. On most datasets, the best dedicated NER model is more accurate and much faster.

The value of LLMs is different: they are flexible. They can help with targeted enrichment, low-resource cases, rapid testing of new entity types, or cases where a dedicated model performs poorly and a slower fallback is acceptable.

## What to update next

The next useful update is to document the prompt format and add more dataset-level detail, especially for cases where LLM extraction still misses entities that a dedicated model can capture reliably. The benchmark should also keep testing smaller and faster local models, because the operational question is not only whether LLMs can work, but whether they can work at a realistic cost.
