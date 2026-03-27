---
layout: default
title: Methodology
description: Evaluation methodology for the ArchXAI D.2.1.1 technology comparison.
permalink: /methodology/
---

<section class="panel">
  <p class="eyebrow">Evaluation logic</p>
  <h1>How the comparison is run</h1>
  <p class="lede">The methodology combines classic information retrieval metrics with operational deployment constraints. Accuracy matters, but this deliverable also treats runtime, hardware fit, and integration flexibility as first-class decision criteria.</p>
</section>

<section class="panel">
  <h2>Primary criteria</h2>
  <ul>
    <li><strong>Precision, recall, and F1.</strong> These are the main headline metrics, reported overall and, where relevant, per entity or label class.</li>
    <li><strong>Runtime.</strong> Total runtime and seconds per processed sentence are tracked to distinguish methods suitable for bulk indexing from methods better suited to targeted enrichment.</li>
    <li><strong>Ease of integration.</strong> The comparison favors solutions that can be inserted into a multilingual archival workflow without forcing every stakeholder into the same infrastructure or model stack.</li>
  </ul>
</section>

<section class="panel">
  <h2>Operational constraints</h2>
  <p>The current benchmarking environment is described as a system centered on an NVIDIA GB10 chip, which in practice limits routine evaluation to models that fit within approximately 128 GB RAM. That matters because some large language models may be interesting experimentally but remain impractical for widespread operational deployment.</p>
  <p>The comparison therefore treats transformer pipelines as the default high-throughput baseline and LLM-based methods as complementary: useful for fallback cases, targeted enrichment, or rapid experimentation where dedicated task models are weak or unavailable.</p>
</section>

<section class="panel">
  <h2>Testing framework</h2>
  <ul>
    <li>Benchmarking is cyclical rather than one-off.</li>
    <li>New models and datasets are added as the field changes and project needs become clearer.</li>
    <li>The website version is intended for continuous updates.</li>
    <li>Formal report versions can still be refreshed at larger project milestones.</li>
  </ul>
</section>

<section class="panel">
  <h2>Current evidence base</h2>
  <p>The strongest reusable material currently available in the workspace covers two technology tracks:</p>
  <ul>
    <li><strong>NER.</strong> Evaluation across modern, historical, and legal-domain datasets with mapped PER, ORG, and LOC labels.</li>
    <li><strong>PII detection and anonymization.</strong> Operational comparison between Presidio and MAPA on legal-domain multilingual data.</li>
  </ul>
  <p>Additional tracks can be added into the same site structure as benchmarking results stabilize.</p>
</section>
