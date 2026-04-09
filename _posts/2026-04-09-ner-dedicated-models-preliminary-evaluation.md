---
title: "Preliminary evaluation: NER with dedicated models"
summary: Dedicated NER models remain the strongest default for high-throughput archive indexing, especially when they are routed by language and text domain.
track: NER
track_icon: "📇"
topics: [ner]
date: 2026-04-09 06:10:00 +0300
---

Named Entity Recognition (NER) is the task of finding named things in text. In the ArchXAI benchmarks, the first focus is on **people**, **organisations**, and **places**, because these are common entry points for archive search and indexing.

For archive work, NER can help turn long text collections into searchable metadata. A good NER model can point users toward records that mention a person, institution, or location without requiring every document to be described by hand.

## Illustration placeholder

<div class="placeholder-figure">Illustration placeholder: add a simple before/after example showing a short archival text with names, organisations, and places highlighted.</div>

## What we tested

This note focuses on dedicated transformer-based NER models from the current local benchmark. The evaluated datasets cover Estonian, Finnish, Latvian, and Russian material, including legal-domain and older-domain text that is harder than clean modern examples.

The headline score is **F1**, which balances two practical problems: marking things that are not entities, and missing entities that should have been found. Higher is better.

## Best current results on out-of-domain data

| Language | Out-of-domain dataset | Best current dedicated model | Accuracy score |
|---|---|---|---:|
| Estonian | `et_multileg` legal text | `pierre-tassel/rapido-ner-entity` | F1 58.8% |
| Finnish | `fi_multileg` legal text | `pierre-tassel/rapido-ner-entity` | F1 56.8% |
| Latvian | `lv_multileg` legal text | `51la5/roberta-large-NER` | F1 57.9% |
| Russian | `ru_oldish` older-domain mix | `pierre-tassel/rapido-ner-entity` | F1 83.4% |

## Early interpretation

The main result is practical: dedicated NER models are still the default choice for large-scale indexing. They are fast enough for bulk processing, and the best model can be selected by language and domain.

The harder legal-domain datasets show that archival-adjacent material is not solved yet. Scores around 57-59% are useful for assisted indexing, but they are not enough for unsupervised metadata creation without review or further tuning.

## What to update next

The next useful update is to add clearer illustrations and expand the table when new out-of-domain datasets are tested. The strongest candidates should also be fine-tuned on project-specific archival material, especially for legal and historical text.
