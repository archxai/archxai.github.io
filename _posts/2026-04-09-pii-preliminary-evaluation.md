---
title: "Personally Identifiable Information"
summary: Presidio is the most practical default integration layer for PII detection, while MAPA remains valuable when anonymization and visual review matter most.
track: PII
track_icon: "🔐"
topics: [pii]
chips:
  - icon: "🔐"
    label: PII
  - icon: "1️⃣"
    label: Preliminary
date: 2026-02-27 06:20:00 +0200
---

Personally identifiable information (PII) means information that can identify a person. In archives, this can include names, addresses, dates, identifiers, contact details, and other sensitive spans that may matter before records are released more widely.

PII detection is not the same as ordinary NER. NER often focuses on names, organisations, and places. PII detection is broader because release review may also need dates, personal codes, addresses, phone numbers, and other sensitive clues.

## What we tested

This note compares [Presidio](https://github.com/microsoft/presidio) and [MAPA](https://gitlab.com/MAPA-EU-Project/mapa_project) on legal-domain PII handling. Presidio is useful as a modular integration layer, because it can host Hugging Face recognizers and can also wrap MAPA recognizers. MAPA is useful as an anonymization toolkit with its own detection and replacement logic.

The current local comparison uses the [MultiLeg dataset](https://github.com/tilde-nlp/MultiLeg-dataset/) for Estonian (`et_multileg.conll`), Finnish (`fi_multileg.conll`), and Latvian (`lv_multileg.conll`). Russian PII results have not yet been added to this note.

## Headline comparison

| Feature | Presidio | MAPA | Why it matters |
|---|---|---|---|
| Local or self-hosted deployment | ✓ | ✓ | Both fit archive workflows where sensitive material cannot be sent to external services. |
| Built-in anonymization or replacement workflow | ✓ | ✓ | Both can support masking, obfuscation, or replacement rather than simple detection only. |
| Ready-made visual interface for review and demos | - | ✓ | MAPA is easier to show to non-technical users and project stakeholders. |
| Pluggable recognizers and model routing | ✓ | △ | Presidio is stronger as a framework for swapping in language-specific components. |
| Easy integration into larger processing pipelines | ✓ | △ | Presidio is easier to embed as a backend service inside broader archive tooling. |
| Strong fit for anonymization-focused workflows | △ | ✓ | MAPA is more directly centered on end-user anonymization tasks. |

## What the tool output looks like

<div class="media-frame">
  <img class="content-illustration" src="{{ '/assets/images/posts/mapa-gui-example.png' | relative_url }}" alt="MAPA interface showing multilingual sensitive spans and anonymized replacements">
</div>

## Early interpretation

Presidio is the strongest default recommendation when the goal is to integrate PII detection into a multilingual archive workflow. It is flexible, easier to extend, and better suited to pipeline-style processing where recognizers may change over time.

MAPA should not be dismissed. It is especially useful when the workflow needs a demonstrable anonymization interface, clear replacement behavior, and a tool that non-technical reviewers can inspect directly.

## What to update next

The next useful update is to compare anonymized output quality more directly, not only detection coverage. The benchmark should also test how well each approach supports archive-specific review tasks such as masking, replacement consistency, and human validation.
