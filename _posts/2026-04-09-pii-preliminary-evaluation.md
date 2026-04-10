---
title: "Personally Identifiable Information"
summary: Presidio is the most practical default integration layer for PII detection, while MAPA remains important for Latvian legal text and anonymization workflows.
track: PII
track_icon: "🔐"
topics: [pii]
chips:
  - icon: "🔐"
    label: PII
  - icon: "1️⃣"
    label: Preliminary
date: 2026-04-09 06:20:00 +0300
---

Personally identifiable information (PII) means information that can identify a person. In archives, this can include names, addresses, dates, identifiers, contact details, and other sensitive spans that may matter before records are released more widely.

PII detection is not the same as ordinary NER. NER often focuses on names, organisations, and places. PII detection is broader because release review may also need dates, personal codes, addresses, phone numbers, and other sensitive clues.

## Illustration placeholder

<div class="placeholder-figure">Illustration placeholder: add a MAPA or Presidio screenshot showing detected sensitive spans and anonymized replacements.</div>

## What we tested

This note compares **Presidio** and **MAPA** on legal-domain MultiLeg data. Presidio is useful as a modular integration layer, because it can host Hugging Face recognizers and can also wrap MAPA recognizers. MAPA is useful as an anonymization toolkit with its own detection and replacement logic.

The headline score is **F1**. The current local benchmark covers Estonian, Finnish, and Latvian legal-domain data; Russian PII results have not yet been added to the scored table.

## Best current results on out-of-domain data

| Language | Out-of-domain dataset | Best current PII pipeline | Accuracy score |
|---|---|---|---:|
| Estonian | `et_multileg` legal text | Presidio + Estonian Hugging Face recognizer | F1 43.03% |
| Finnish | `fi_multileg` legal text | Presidio + Finnish Hugging Face recognizer | F1 50.73% |
| Latvian | `lv_multileg` legal text | MAPA multilingual native pipeline | F1 47.77% |
| Russian | Not yet scored | TBD | TBD |

## Early interpretation

Presidio is the strongest default recommendation because it is flexible and easier to integrate into a multilingual archive workflow. It can use different recognizers by language and can absorb stronger models later.

MAPA should not be dismissed. It performs best in the current Latvian legal-domain result and has richer anonymization logic, which may matter if readable synthetic replacements are needed instead of simple masking or redaction.

## What to update next

The next useful update is to add screenshots from the anonymization interface and rerun Presidio with the strongest NER candidates where appropriate. The benchmark should also measure anonymized output quality, not only detection accuracy.
