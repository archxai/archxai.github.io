---
title: Named Entity Recognition technology comparison
summary: Current NER benchmarking shows that language- and domain-specific transformer models are the strongest default for large-scale indexing, while LLM extraction remains a slower fallback or enrichment path.
track: NER
---

Named Entity Recognition is used in ArchXAI to automatically identify key entities in text, especially **persons (PER)**, **organisations (ORG)**, and **locations (LOC)**. These entities are central to improving archival catalogues and indexes, and therefore to improving access for archival professionals and archive users across the Central Baltic region.

The current comparison evaluates two broad model families:

- publicly available transformer-based NER models
- locally executed LLMs used for prompt-based entity extraction

Because the evaluated datasets use different label inventories, labels were mapped into a shared **PER / ORG / LOC** scheme so that cross-language comparison remained meaningful.

## Data and update scope

Results in this iteration are computed on a deterministic sample of **744 sentences per dataset**. The current reusable benchmark material reflects runs dated **28 January 2026 to 14 February 2026**.

## Headline findings

- Dedicated transformer models are the strongest default choice for large-scale indexing.
- LLM extraction is substantially slower and is better treated as targeted enrichment or fallback.
- Historical and legal-domain corpora remain harder than modern in-domain datasets.
- Latvian modern is the clearest exception, where the best tested LLM outperformed the tested transformer baselines.

## Best-performing models by dataset

| Dataset | Best transformer | Best LLM |
|---|---|---|
| `et_modern` | `tartuNLP/EstBERT_NER_v2` (`F1 = 0.999`, `0.02s/sentence`) | `gpt-oss:120b` (`F1 = 0.646`, `8.57s/sentence`) |
| `et_old` | `tartuNLP/est-roberta-hist-ner` (`F1 = 0.930`, `0.02s/sentence`) | `gpt-oss:120b` (`F1 = 0.514`, `4.95s/sentence`) |
| `et_multileg` | `pierre-tassel/rapido-ner-entity` (`F1 = 0.588`, `0.03s/sentence`) | `gpt-oss:120b` (`F1 = 0.560`, `7.19s/sentence`) |
| `fi_old` | `Kansallisarkisto/finbert-ner` (`F1 = 0.752`, `0.01s/sentence`) | `qwen3:32b` (`F1 = 0.468`, `18.22s/sentence`) |
| `fi_multileg` | `pierre-tassel/rapido-ner-entity` (`F1 = 0.568`, `0.03s/sentence`) | `qwen3:32b` (`F1 = 0.447`, `59.60s/sentence`) |
| `lv_diverse` | `Davlan/distilbert-base-multilingual-cased-ner-hrl` (`F1 = 0.945`, `0.01s/sentence`) | `gpt-oss:120b` (`F1 = 0.769`, `12.56s/sentence`) |
| `lv_modern` | `Davlan/distilbert-base-multilingual-cased-ner-hrl` (`F1 = 0.460`, `0.01s/sentence`) | `gpt-oss:120b` (`F1 = 0.604`, `3.37s/sentence`) |
| `lv_multileg` | `51la5/roberta-large-NER` (`F1 = 0.579`, `0.03s/sentence`) | `gpt-oss:120b` (`F1 = 0.545`, `5.87s/sentence`) |
| `ru_modern` | `ivlcic/xlmr-ner-slavic` (`F1 = 0.969`, `0.02s/sentence`) | `gpt-oss:120b` (`F1 = 0.888`, `5.06s/sentence`) |
| `ru_oldish` | `pierre-tassel/rapido-ner-entity` (`F1 = 0.834`, `0.03s/sentence`) | `gpt-oss:120b` (`F1 = 0.710`, `2.80s/sentence`) |

## Interpretation

The main engineering conclusion is straightforward: use **transformer NER models as the default indexing layer**, routed by language and domain, and keep LLM extraction as a supplementary option where dedicated models are weak, unavailable, or too rigid for a new task.

The strongest modern language-specific models are already close to operational readiness for indexing. The weaker legal-domain and historical results show where further fine-tuning or project-specific training data will matter most.

## Recommended next steps

- extend evaluation beyond `PER`, `ORG`, and `LOC` when archival metadata needs require it
- fine-tune promising models on project-specific data
- validate robustness under OCR noise, mixed-language material, and heterogeneous archival formatting
