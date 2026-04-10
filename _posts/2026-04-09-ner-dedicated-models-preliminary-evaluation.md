---
title: "Named Entity Recognition"
summary: Dedicated NER models remain the strongest default for high-throughput archive indexing, especially when they are routed by language and text domain.
track: NER
track_icon: "📇"
topics: [ner]
chips:
  - icon: "📇"
    label: NER
  - icon: "1️⃣"
    label: Preliminary
date: 2025-12-31 06:10:00 +0200
---

Named Entity Recognition (NER) is used to automatically identify key entities in text, especially **people**, **organisations**, and **locations**. In archival work, these are some of the most useful entry points for search, indexing, and access services.

The first dedicated-model benchmark in ArchXAI asked a practical question: which Hugging Face NER models are the strongest current candidates for multilingual archive indexing when labels are mapped to a shared **PER / ORG / LOC** scheme?

## What we tested

This note focuses on dedicated transformer-based NER models. The benchmark covered multilingual, Estonian, Finnish, Latvian, and Russian model candidates that could realistically be integrated into AI-based cataloguing and indexing workflows.

The headline score is **F1**, which balances two practical errors: marking things that are not entities, and missing entities that should have been found. Higher is better.

Because the source models and datasets do not all use the same label inventory, the benchmark maps results to a shared **PER / LOC / ORG** scheme before scoring.

## Headline results

| Language | Best dedicated model | Dataset | F1 (%) |
|---|---|---|---:|
| 🇪🇪 Estonian | [`51la5/roberta-large-NER`](https://huggingface.co/51la5/roberta-large-NER) | [`et_modern`](https://github.com/TartuNLP/EstNER) | 75.7% |
| 🇫🇮 Finnish | [`Kansallisarkisto/finbert-ner`](https://huggingface.co/Kansallisarkisto/finbert-ner) | [`fi_old`](https://zenodo.org/records/4573313) | 75.2% |
| 🇱🇻 Latvian | [`51la5/roberta-large-NER`](https://huggingface.co/51la5/roberta-large-NER) | [`lv_diverse`](https://github.com/LUMII-AILab/FullStack) | 84.1% |
| 🪆 Russian | [`pierre-tassel/rapido-ner-entity`](https://huggingface.co/pierre-tassel/rapido-ner-entity) | [`ru_modern`](https://bsnlp.cs.helsinki.fi/bsnlp-2019/shared_task.html) | 91.2% |

## What the output looks like

<div class="media-frame">
  <img class="content-illustration" src="{{ '/assets/images/posts/ner-model-example.png' | relative_url }}" alt="Example of named entity recognition output highlighting people, organisations, and locations across several languages">
</div>

## Evaluation setup

### Evaluation models

- 🌐 Multilingual
  - [`pierre-tassel/rapido-ner-entity`](https://huggingface.co/pierre-tassel/rapido-ner-entity)
  - [`51la5/roberta-large-NER`](https://huggingface.co/51la5/roberta-large-NER)
  - [`jplu/tf-xlm-r-ner-40-lang`](https://huggingface.co/jplu/tf-xlm-r-ner-40-lang)
  - [`Babelscape/wikineural-multilingual-ner`](https://huggingface.co/Babelscape/wikineural-multilingual-ner)
  - [`Davlan/distilbert-base-multilingual-cased-ner-hrl`](https://huggingface.co/Davlan/distilbert-base-multilingual-cased-ner-hrl)
  - [`nicolauduran45/affilgood-ner-multilingual-v2`](https://huggingface.co/nicolauduran45/affilgood-ner-multilingual-v2)
- 🇪🇪 Estonian
  - [`tartuNLP/EstBERT_NER_v2`](https://huggingface.co/tartuNLP/EstBERT_NER_v2)
  - [`tartuNLP/est-roberta-hist-ner`](https://huggingface.co/tartuNLP/est-roberta-hist-ner)
- 🇫🇮 Finnish
  - [`iguanodon-ai/bert-base-finnish-uncased-ner`](https://huggingface.co/iguanodon-ai/bert-base-finnish-uncased-ner)
  - [`Kansallisarkisto/finbert-ner`](https://huggingface.co/Kansallisarkisto/finbert-ner)
  - [`turku-combined-ext`](https://turkunlp.org/fin-ner.html)
- 🇱🇻 Latvian
  - [`51la5/roberta-large-NER`](https://huggingface.co/51la5/roberta-large-NER)
  - [`Davlan/distilbert-base-multilingual-cased-ner-hrl`](https://huggingface.co/Davlan/distilbert-base-multilingual-cased-ner-hrl)
  - [`Babelscape/wikineural-multilingual-ner`](https://huggingface.co/Babelscape/wikineural-multilingual-ner)
  - [`pierre-tassel/rapido-ner-entity`](https://huggingface.co/pierre-tassel/rapido-ner-entity)
- 🪆 Russian
  - [`Gherman/bert-base-NER-Russian`](https://huggingface.co/Gherman/bert-base-NER-Russian)
  - [`ivlcic/xlmr-ner-slavic`](https://huggingface.co/ivlcic/xlmr-ner-slavic)
  - [`creat89/NER_FEDA_Ru`](https://huggingface.co/creat89/NER_FEDA_Ru)
  - [`r1char9/ner-rubert-tiny-news`](https://huggingface.co/r1char9/ner-rubert-tiny-news)

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

The main engineering conclusion is still straightforward: dedicated NER models are the default choice for large-scale indexing. They are fast enough for bulk processing, and the best-performing model can be selected by language and collection type.

The language-level results also show that a single multilingual baseline is not always the only answer. In Estonian and Latvian, `51la5/roberta-large-NER` performed especially well, while Finnish favored `Kansallisarkisto/finbert-ner`, and Russian favored `pierre-tassel/rapido-ner-entity`.

Operationally, transformer NER still has the clearest advantage for routine archive processing: in local runs, these models process text in milliseconds per sentence, while LLM-based extraction takes seconds per sentence and is therefore better suited to targeted enrichment or fallback use.

## What to update next

The next useful update is to add more dataset-specific detail below the language summary, especially for legal and historical material where the archive use case is hardest. The strongest dedicated models should then be fine-tuned on project-specific archival data to test how much additional recall and robustness can be gained.
