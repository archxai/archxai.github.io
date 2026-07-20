---
title: "Deliverable D.2.1.1 Is Live"
summary: ArchXAI has completed its public technology-comparison site for algorithms and models, turning the project application promise into a continuously updated evidence base.
track: Project update
topics: [project]
chips:
  - label: Project update
  - label: D.2.1.1
date: 2026-06-22 00:00:00 +0300
---

ArchXAI has completed Deliverable D.2.1.1, **Technology comparison for algorithm and model**. The result is now available as a public, continuously updated technology-comparison site at [archxai.github.io](https://archxai.github.io/).

In the project application, Deliverable D.2.1.1 was promised as a provided website subpage describing state-of-the-art models and methods, updated during the project so the work keeps pace with rapid AI development. It belonged to Activity 2.1, Algorithm and Model Selection, where the project committed to testing and experimenting with AI and NLP tools for archive cataloguing and indexing: named entity recognition, image classification, sensitivity and personally identifiable information detection, tone classification, similarity analysis, and related model-selection work.

The delivered site meets that promise in a practical and transparent form. Instead of a static list of tools, it provides a public evidence base that explains what has been tested, why it matters for archival workflows, how results were measured, and where the current limits remain. The site includes a landing page for the deliverable, a methodology page, topic pages, and a development blog where benchmark notes are published in order.

The strongest completed evidence currently covers four areas. Named Entity Recognition is treated as a core indexing task, with results showing that dedicated transformer NER models remain the most defensible default for routine multilingual entity extraction, while LLM extraction is better positioned as a slower fallback or enrichment path. PII detection and anonymization are evaluated from both model-quality and workflow perspectives, comparing Presidio-style integration with MAPA-style review support. Tone and sentiment analysis are included, but with a deliberately cautious recommendation because the current datasets and task framing still need validation for archival use. Embedding and semantic-search work has moved beyond general model ranking into archive-style retrieval experiments, where the main conclusion is architectural: dense embeddings are useful, but archival RAG needs hybrid retrieval with lexical, structured, entity, date, and number-aware signals.

The comparison between promise and delivery is clear. The application asked for a public, continuously updated description of state-of-the-art models and methods. The delivered site does that, while also adding methodological transparency, language-specific caveats, operational recommendations, and a running publication stream. It also remains honest about what is not yet settled: image classification and broader large-language or multimodal model workflows are marked as planned rather than presented as finished.

This matters because technology comparison in archival AI cannot be a one-time procurement table. Models change, datasets improve, and archive requirements vary by language, collection type, and institutional workflow. D.2.1.1 now gives the project and its stakeholders a public place to track those choices as the evidence develops.
