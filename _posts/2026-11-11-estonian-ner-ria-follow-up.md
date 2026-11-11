---
title: "Estonian NER Follow-up: Testing Two RIA Models"
summary: "Two RIA/Bürokratt models showed useful category-specific strengths, but neither displaced our previously tested multilingual model as the general Estonian default."
topics: [ner]
date: 2026-11-11 00:00:00 +0200
---

Following our [earlier NER comparison]({% post_url 2026-04-09-ner-dedicated-models-preliminary-evaluation %}), we tested two additional Estonian models published under RIA's `buerokrattRIA` account: **XLM-RoBERTa-NER-syntheticGov** and **EstBert_NER_SyntheticGov**. Their model cards describe adaptation to government-service and chat-style text using synthetic data.

**Neither displaced the previously tested multilingual RoBERTa as our overall Estonian default.** That is a finding about our evaluation, not a claim that the models cannot perform better on their intended government-service tasks.

## Contemporary Estonian text

In the 28 October evaluation, we used the published [EstNER](https://github.com/TartuNLP/EstNER) test split: 39 documents, scored separately for people (PER), organisations (ORG), and locations (LOC, including geopolitical entities). The table compares **full-precision models after our shared postprocessing**, not a full-precision newcomer against a quantised baseline.

| Model | PER F1 | ORG F1 | LOC F1 | Macro F1 |
|---|---:|---:|---:|---:|
| [Multilingual RoBERTa](https://huggingface.co/51la5/roberta-large-NER) | 89.74% | 69.07% | 76.91% | **78.57%** |
| [RIA Gov XLM-RoBERTa](https://huggingface.co/buerokrattRIA/xlm-roberta-NER-syntheticGov) | 89.55% | 65.05% | 76.60% | 77.07% |
| [RIA Gov EstBERT](https://huggingface.co/buerokrattRIA/EstBert_NER_SyntheticGov) | 79.38% | 65.34% | 76.31% | 73.68% |

Macro F1 gives the three categories equal weight. Exact boundaries and category must match. This follow-up uses a different evaluation setup from the earlier post, so its headline percentages should not be compared directly with that older table.

## Archives still need domain-specific testing

We also tested historical [parish court records](https://github.com/soras/vk_ner_lrec_2022) and human-annotated archival pages. The RIA models did not lead the court-record comparison overall; the historical Tartu specialist was substantially stronger in its original domain. On the archival pages, however, Gov XLM-RoBERTa recovered more exact location boundaries, while Gov EstBERT improved organisation-boundary recall. Those annotations are incomplete, so we report recall there, not F1.

For [TeXplorer](https://huggingface.co/spaces/Rahvusarhiiv/ArchXAI_TeXplorer_Demo), deployment matters too: at the evaluated revisions, the new checkpoints contained approximately **2.24 GB** and **495 MB** of full-precision Safetensors weights, respectively, with no supplied ONNX graph. Their quantised browser performance remains untested. We therefore kept the existing browser default unchanged.

[Download the aggregate results, pinned model revisions and evaluation caveats]({{ '/assets/data/estonian-ner-ria-followup-2026-10-28.json' | relative_url }}). No source-document text is included.
