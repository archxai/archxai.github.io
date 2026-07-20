---
title: "What We Learned Training Summarisation Models in Four Languages"
summary: "Training useful summarisation models required more than adding data: factual support, domain balance, protected benchmarks, and qualitative review determined which updates were actually released."
track: Summarisation
track_icon: "📝"
topics: [summarisation, model-training, evaluation]
chips:
  - icon: "📝"
    label: Summarisation
  - icon: "🧪"
    label: Model training
  - icon: "2️⃣"
    label: Follow-up
date: 2026-07-20 06:40:00 +0300
---

Summarisation can help archive users and professionals understand long documents more quickly. It can support discovery, triage, catalogue enrichment, and review, but it also creates a particular risk: a fluent summary may contain information that is not supported by its source.

Over several training and evaluation rounds, ArchXAI developed dedicated Estonian, Finnish, Latvian, and Russian summarisation models. The work began as a comparison of existing Hugging Face models and local LLMs. It grew into a broader investigation of training-data quality, factual grounding, domain balance, benchmark leakage, output length, and the limits of automatic metrics.

The main learning is straightforward: **more training data is not automatically better training data**. The relationship between source and reference summary matters at least as much as corpus size.

## What we built

The four public models are language-specific fine-tunes of [`facebook/mbart-large-50-many-to-many-mmt`](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt):

| Language | Public model | Current release | Training rows in current release |
|---|---|---|---:|
| 🇪🇪 Estonian | [`Rahvusarhiiv/et_summariser`](https://huggingface.co/Rahvusarhiiv/et_summariser) | Initial grounded release | 23,996 |
| 🇫🇮 Finnish | [`Rahvusarhiiv/fi_summariser`](https://huggingface.co/Rahvusarhiiv/fi_summariser) | Archive-balanced release | 2,741 |
| 🇱🇻 Latvian | [`Rahvusarhiiv/lv_summariser`](https://huggingface.co/Rahvusarhiiv/lv_summariser) | Revision 2 | 30,000 |
| 🪆 Russian | [`Rahvusarhiiv/ru_summariser`](https://huggingface.co/Rahvusarhiiv/ru_summariser) | Expanded-news release | 100,000 |

The row counts are not directly comparable measures of quality. The languages have different source availability, document lengths, domains, and duplication patterns. They are included to describe the releases, not to rank them.

We kept one general model per language rather than creating separate news, legal, academic, and encyclopedic models. This makes deployment simpler and better matches the archive use case, where document type may not be known in advance. It also makes data balance more important: one large domain can shape the behaviour of the whole model.

## How the training process changed

The first training rounds used available news, legal, academic, and long-document summarisation datasets. Automatic results looked promising, but qualitative review exposed problems that aggregate scores did not show clearly.

Some generated summaries introduced people, events, or conclusions not found in the input. Some copied a title or opening sentence instead of summarising the document. Others reproduced EU legal language in unrelated contexts, repeated phrases, included media filenames, or ended abruptly.

These failures changed the development process in four ways.

### 1. We audited source-summary support

A reference summary is not necessarily supported by the text paired with it. News descriptions may depend on a title, date, location, or other metadata that is absent from the article body. Academic abstracts may contain claims or framing that do not appear in the retrieved full text. Legal summaries may combine information from several acts even when a dataset provides only one source document.

Training on such pairs teaches a model that adding plausible information is acceptable.

We therefore added support checks between sources and summaries, including content-token overlap, named-entity and number checks, and sentence-level evidence selection. Unsupported examples could be rejected, repaired with available metadata, or paired with source spans that better supported the target.

Metadata was not added as one rigid template to every example. It was included only where needed, with variation and dropout, so the model would not simply learn that a fixed metadata block always precedes the text. When the required metadata was unavailable, the target still had to be supported by the source that remained.

### 2. We expanded non-legal data

The early Finnish and Latvian mixes contained too much EU legal material relative to other domains. This produced summaries that sometimes sounded like legislation even when the input was news or encyclopedic text.

We collected and cleaned additional data:

- 🇪🇪 Estonian: ERR-style news, long-form Estonian summaries, and filtered legal material.
- 🇫🇮 Finnish: Yle RSS and archive news, Theseus thesis records, filtered academic summaries, and a capped synthetic Finnish PDF-summary collection.
- 🇱🇻 Latvian: LSM and Delfi news, the larger LSM archive, Latvian academic OAI records, and repaired EUR-Lex pairs.
- 🪆 Russian: Gazeta, MLSUM, XLSum, LR-Sum, Lenta, SumNews, and Taiga-derived news material after filtering.

For Latvian legal examples, [`FMISummarization/FMI_Summarization`](https://huggingface.co/datasets/FMISummarization/FMI_Summarization) was used to recover additional source acts for existing [`dennlinger/eur-lex-sum`](https://huggingface.co/datasets/dennlinger/eur-lex-sum) summaries. It was used to improve source evidence rather than to duplicate the same summaries as extra training mass.

### 3. We cleaned recurring artifacts

The later preprocessing pipeline removes or flags:

- duplicated first summary lines
- repeated title or title-prefix text
- EU legal headings and boilerplate outside the useful summary section
- media filenames and HTML remnants
- targets truncated in the middle of a sentence
- very long legal targets that would dominate training
- exact and near-duplicate source-summary pairs

Targets are truncated at sentence boundaries instead of raw token boundaries. Very long legal summaries can be capped or downweighted. These changes do not guarantee complete output, but they remove several ways in which the training data itself encouraged abrupt or formulaic generations.

### 4. We rebalanced rather than splitting models

We retained universal models, but sampled less legal material per epoch and more news and academic material. The exact achievable balance differed by language because the available corpora differed.

The Latvian revision-2 training mix, for example, contained 27,180 news rows, 2,412 legal rows, and 408 academic rows. This was not the originally proposed ideal balance, but it substantially reduced the relative legal weight while making use of the much larger accepted LSM archive collection.

## Preventing evaluation leakage

Evaluation leakage became a first-class requirement. A model should not be evaluated on the same article, summary, translated counterpart, or close duplicate that it saw during training.

Protected benchmark rows were excluded before training splits and balancing. The checks included:

- stable record identifiers
- normalized URLs
- exact normalized source, summary, and source-summary hashes
- shared token shingles for near-duplicate detection
- grouped legal identifiers where one summary referred to several acts

This was especially important after adding large public datasets, because the same news or legal document can appear in several repositories under different formatting.

## Building a broader benchmark

No single existing dataset gave a fair cross-language view. We therefore built three complementary protected evaluations:

1. **Strict Wiki4** uses topics available in Estonian, Finnish, Latvian, and Russian Wikipedia. The collected articles were filtered so the reference introduction was well supported by the remaining article text.
2. **Recent GDELT news** tests newer material from varied publishers, reducing the chance that evaluation simply rewards an older training distribution.
3. **Held-out supported news** uses accepted news pairs from the collected language-specific corpora, with support and overlap checks.

The revision-2 comparison used 100 identically selected examples from each benchmark and language. All models received the same decoding settings: 768 input tokens, up to 512 generated tokens, four beams, length penalty 1.0, and a repeated 3-gram block.

Wiki4 makes the topic set more comparable across languages, but it does not make the gold summaries identical. Language editions differ in content and editorial style, so cross-language score differences still need caution.

## Why ROUGE was not enough

ROUGE remains useful because it measures overlap with a reference summary. It is not a factuality metric, and it may reward a copied lead or penalise a valid paraphrase.

The evaluation therefore grew to include:

- reference content-token coverage
- prediction-to-source content-token precision
- named-entity and numeric overlap
- compression ratio and generated-token count
- repeated 4-gram rate and distinct-1 / distinct-2
- duplicate title-prefix detection
- terminal-punctuation and maximum-token flags
- media filename, HTML, and EU-legalese artifact flags

A local `gemma4:31b` Ollama judge also scored sampled summaries for factuality, coverage, focus, language quality, and overall usefulness. LLM judging was treated as a comparative signal, not ground truth. Small samples are useful for finding directional differences, but they do not replace human review.

## What revision 2 told us

The final comparison tested the released Hugging Face model for each language against its revision-2 candidate. The automatic figures below are macro averages across Strict Wiki4, recent GDELT, and held-out supported news, with 100 examples per benchmark. The judge score is the macro average from five paired examples per benchmark.

| Language | ROUGE-L released → r2 | Ref. coverage released → r2 | Source precision released → r2 | Judge overall released → r2 | Decision |
|---|---:|---:|---:|---:|---|
| 🇪🇪 Estonian | 0.269 → 0.251 | 0.317 → 0.265 | 0.827 → 0.838 | 2.27 → 2.93 | Keep released model; investigate factuality gain with a larger review |
| 🇫🇮 Finnish | 0.245 → 0.215 | 0.257 → 0.233 | 0.861 → 0.858 | 2.80 → 2.80 | Keep released model |
| 🇱🇻 Latvian | 0.234 → 0.266 | 0.244 → 0.264 | 0.788 → 0.831 | 2.07 → 2.53 | Release revision 2 |
| 🪆 Russian | 0.224 → 0.221 | 0.224 → 0.243 | 0.909 → 0.887 | 3.00 → 2.60 | Keep released model |

Only Latvian improved consistently enough across the protected domains to replace its public checkpoint. It gained strongly on both news benchmarks, improved source precision across all three benchmarks, and eliminated the detected EU-legalese artifact rate in this evaluation.

The Latvian tradeoff is also documented: revision 2 produced shorter Wiki4 summaries, lowering Wiki4 ROUGE and reference coverage while increasing source precision. This is better grounding, but also more omission. It should not be described as an unconditional improvement on every kind of text.

The Estonian result shows why multiple signals matter. Its revision-2 candidate received better sampled judge scores for factuality and overall quality, but automatic coverage and ROUGE declined. That is a reason for a larger qualitative review, not an automatic release.

Finnish revision 2 lost too much coverage, while Russian revision 2 reduced source precision and received a lower judge score. In both cases, keeping the existing public model was the more defensible decision.

## What did not work

Several ideas looked reasonable but did not reliably improve the models:

- Adding a large dataset without controlling its domain weight could make the model worse outside that domain.
- High-quality gold summaries could still be harmful when they depended on information absent from the paired source.
- Stronger factual support could be achieved by generating very short summaries, but that reduced usefulness through omission.
- Synthetic summaries increased Finnish variety, but required strict filtering and capping rather than unrestricted sampling.
- A high aggregate score could hide title copying, legal boilerplate, filenames, abrupt endings, or individual hallucinations.
- A larger or later checkpoint was not automatically a better release candidate.

The release decision therefore became conservative: a candidate had to improve across domains or present a deliberate, documented tradeoff that was worthwhile for archive use.

## Current release status

All four models are available through the [Rahvusarhiiv Hugging Face organisation](https://huggingface.co/Rahvusarhiiv):

- [`Rahvusarhiiv/et_summariser`](https://huggingface.co/Rahvusarhiiv/et_summariser)
- [`Rahvusarhiiv/fi_summariser`](https://huggingface.co/Rahvusarhiiv/fi_summariser)
- [`Rahvusarhiiv/lv_summariser`](https://huggingface.co/Rahvusarhiiv/lv_summariser)
- [`Rahvusarhiiv/ru_summariser`](https://huggingface.co/Rahvusarhiiv/ru_summariser)

The model cards describe intended use, training sources, evaluation results, failure modes, generation settings, and the absence of measured CO2 data. The older Latvian checkpoint is preserved under the `v1` tag and revision 2 under `v2`.

These are experimental research releases, not state-of-the-art claims. They can still hallucinate, omit important information, or mishandle names, dates, numbers, and specialised terminology. Human verification remains necessary for public-facing summaries, legal material, and archival description.

## What to improve next

The next training round should be driven by observed failure modes rather than data volume alone:

1. Expand human qualitative review, especially for the Estonian revision-2 factuality signal.
2. Add more supported non-legal Finnish data before retraining.
3. Improve controllable short, medium, and long summary generation without teaching a rigid prompt structure.
4. Continue extending recent-news and archive-style protected benchmarks.
5. Use factuality-aware training only after the cleaned-data gains have been separated from judge-model effects.
6. Keep preserving older releases and publish a replacement only when its cross-domain evidence is convincing.

The broader conclusion is that summarisation quality is a system property. It depends on the source-summary relationship, corpus balance, preprocessing, decoding, benchmark construction, metrics, and human judgement. Model architecture matters, but it is only one part of the work.
