---
title: "NER with dedicated models"
summary: Dedicated NER models remain the strongest default for high-throughput archive indexing, especially when they are routed by language and text domain.
track: NER
track_icon: "📇"
topics: [ner]
chips:
  - icon: "📇"
    label: NER
  - icon: "1️⃣"
    label: Preliminary
date: 2025-12-02 06:10:00 +0200
---

Named Entity Recognition (NER) is used to automatically identify key entities in text, especially **people**, **organisations**, and **locations**. In archival work, these are some of the most useful entry points for search, indexing, and access services.

The first dedicated-model benchmark in ArchXAI asked a practical question: which Hugging Face NER models are the strongest current candidates for multilingual archive indexing when labels are mapped to a shared **PER / ORG / LOC** scheme?

## Example output

<div class="media-frame">
  <img class="content-illustration" src="{{ '/assets/images/posts/ner-model-example.png' | relative_url }}" alt="Example of named entity recognition output highlighting people, organisations, and locations across several languages">
</div>

## What we tested

This note focuses on dedicated transformer-based NER models from the December 2, 2025 comparison. The benchmark covered multilingual, Estonian, Finnish, Latvian, and Russian model candidates that could realistically be integrated into AI-based cataloguing and indexing workflows.

The headline score is **F1**, which balances two practical errors: marking things that are not entities, and missing entities that should have been found. Higher is better.

Across the local run, the dedicated-model benchmark covered the following model set:

- Multilingual and cross-language baselines: [`pierre-tassel/rapido-ner-entity`](https://huggingface.co/pierre-tassel/rapido-ner-entity), [`51la5/roberta-large-NER`](https://huggingface.co/51la5/roberta-large-NER), [`jplu/tf-xlm-r-ner-40-lang`](https://huggingface.co/jplu/tf-xlm-r-ner-40-lang), [`Babelscape/wikineural-multilingual-ner`](https://huggingface.co/Babelscape/wikineural-multilingual-ner), [`Davlan/distilbert-base-multilingual-cased-ner-hrl`](https://huggingface.co/Davlan/distilbert-base-multilingual-cased-ner-hrl), and [`nicolauduran45/affilgood-ner-multilingual-v2`](https://huggingface.co/nicolauduran45/affilgood-ner-multilingual-v2).
- Finnish-oriented models: [`iguanodon-ai/bert-base-finnish-uncased-ner`](https://huggingface.co/iguanodon-ai/bert-base-finnish-uncased-ner), [`Kansallisarkisto/finbert-ner`](https://huggingface.co/Kansallisarkisto/finbert-ner), plus the locally referenced Turku benchmark entry `turku-combined-ext`.
- Estonian-oriented models: [`tartuNLP/EstBERT_NER_v2`](https://huggingface.co/tartuNLP/EstBERT_NER_v2) and [`tartuNLP/est-roberta-hist-ner`](https://huggingface.co/tartuNLP/est-roberta-hist-ner).
- Russian-oriented models: [`Gherman/bert-base-NER-Russian`](https://huggingface.co/Gherman/bert-base-NER-Russian), [`ivlcic/xlmr-ner-slavic`](https://huggingface.co/ivlcic/xlmr-ner-slavic), [`creat89/NER_FEDA_Ru`](https://huggingface.co/creat89/NER_FEDA_Ru), and [`r1char9/ner-rubert-tiny-news`](https://huggingface.co/r1char9/ner-rubert-tiny-news).

## Best dedicated-model results by language

| Language | Strongest result | Close second |
|---|---|---|
| Estonian | [`51la5/roberta-large-NER`](https://huggingface.co/51la5/roberta-large-NER) (`F1 = 0.757`) | [`pierre-tassel/rapido-ner-entity`](https://huggingface.co/pierre-tassel/rapido-ner-entity) (`F1 = 0.751`) |
| Finnish | [`Kansallisarkisto/finbert-ner`](https://huggingface.co/Kansallisarkisto/finbert-ner) (`F1 = 0.752`) | - |
| Latvian | [`51la5/roberta-large-NER`](https://huggingface.co/51la5/roberta-large-NER) (`F1 = 0.841`) | - |
| Russian | [`pierre-tassel/rapido-ner-entity`](https://huggingface.co/pierre-tassel/rapido-ner-entity) (`F1 = 0.912`) | - |

## Early interpretation

The main engineering conclusion is still straightforward: dedicated NER models are the default choice for large-scale indexing. They are fast enough for bulk processing, and the best-performing model can be selected by language and collection type.

The corrected language-level results also show that a single multilingual baseline is not always the only answer. In Estonian and Latvian, `51la5/roberta-large-NER` performed especially well, while Finnish favored `Kansallisarkisto/finbert-ner`, and Russian favored `pierre-tassel/rapido-ner-entity`.

Operationally, transformer NER still has the clearest advantage for routine archive processing: in local runs, these models process text in milliseconds per sentence, while LLM-based extraction takes seconds per sentence and is therefore better suited to targeted enrichment or fallback use.

## What to update next

The next useful update is to add more dataset-specific detail below the language summary, especially for legal and historical material where the archive use case is hardest. The strongest dedicated models should then be fine-tuned on project-specific archival data to test how much additional recall and robustness can be gained.
