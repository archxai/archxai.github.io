---
title: PII detection and anonymization comparison
summary: Presidio is the strongest default integration layer for ArchXAI, while MAPA remains valuable for Latvian legal text and richer anonymization logic.
track: PII
---

Personally identifiable information detection matters in ArchXAI because archives need practical ways to screen material before release, sharing, or broader public access. In the project context, this is especially relevant for GDPR-oriented review workflows.

The current local comparison evaluates two solution families:

- **Presidio**, used as a modular detection and anonymization framework
- **MAPA**, used as an end-to-end anonymization toolkit with its own detection and replacement logic

## Why this comparison is different from plain NER

The target is not only person-name recognition. Archival release screening also needs support for dates, identifiers, addresses, contact details, and adjacent sensitive spans. That shifts the decision from "which model is most accurate" to "which operational stack is most realistic for multilingual archive workflows."

## Main findings from the logged local benchmark

- Presidio is the more flexible integration layer because it can host both Hugging Face recognizers and MAPA models.
- MAPA has richer built-in substitution logic, which matters if readable synthetic replacement becomes a requirement.
- Presidio performed best on the Estonian and Finnish legal-domain benchmarks.
- MAPA multilingual performed best on the Latvian legal-domain benchmark.
- Wrapping MAPA inside Presidio caused only minimal loss, so a common Presidio-based operational layer remains feasible.

## Best results by dataset

| Dataset | Best Presidio pipeline | Best MAPA pipeline | Higher-performing family |
|---|---:|---:|---|
| `et_multileg` | Presidio + Estonian HF (`F1 = 43.03`) | MAPA multilingual native (`F1 = 31.97`) | Presidio |
| `fi_multileg` | Presidio + Finnish HF (`F1 = 50.73`) | MAPA multilingual native (`F1 = 47.76`) | Presidio |
| `lv_multileg` | Presidio + Latvian HF (`F1 = 36.76`) | MAPA multilingual native (`F1 = 47.77`) | MAPA |

## Operational recommendation

The strongest default recommendation is:

- use **Presidio** as the common integration framework
- route by language and model family where needed
- keep **MAPA multilingual** in the Latvian path until a stronger Latvian legal-domain baseline is identified
- use current outputs for triage, prioritization, and reviewer assistance rather than for autonomous GDPR release decisions

This is not a claim that Presidio wins every benchmark. It is an engineering recommendation based on the combination of benchmark scores, architecture, configurability, and how well the framework can absorb future model changes.

## Important limitation

The current results are useful for workflow prioritization, but they are not strong enough to justify fully automatic release decisions. Human review remains necessary.

## Recommended next steps

- benchmark the strongest Hugging Face candidates from the NER work inside the PII pipeline
- separate more GDPR-relevant entity categories instead of relying only on coarse shared mappings
- evaluate anonymized output quality in addition to detection quality
- test the workflows on noisier, more realistic archival material
