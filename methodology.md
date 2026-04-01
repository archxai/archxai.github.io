---
layout: default
title: How We Compare Tools
description: Plain-language explanation of how ArchXAI compares AI tools for archive work.
permalink: /methodology/
---

<section class="panel">
  <div class="intro-grid">
    <div>
      <p class="eyebrow">Evaluation logic</p>
      <h1>How we compare tools</h1>
      <p class="lede">We do not judge AI tools only by how impressive they sound. We compare them by how accurate they are, how fast they are, and whether they can realistically fit into archive workflows.</p>
    </div>
    <div class="media-frame">
      <img class="content-illustration" src="{{ '/assets/images/metrics-explainer.svg' | relative_url }}" alt="Illustration explaining precision, recall, and F1 in plain language">
    </div>
  </div>
</section>

<section class="panel">
  <h2>A plain-language guide to the main metrics</h2>
  <p>Simple example: if a tool highlights ten names and eight are real names, precision is eight out of ten. If there were twelve real names in the text and the tool found eight of them, recall is eight out of twelve.</p>
</section>

<section class="panel">
  <h2>Primary criteria</h2>
  <ul>
    <li><strong>Accuracy.</strong> Precision, recall, and F1 are the main headline measures, reported overall and, where relevant, per entity or label class.</li>
    <li><strong>Speed.</strong> Total runtime and seconds per processed sentence help separate tools suitable for bulk indexing from tools better suited to smaller, targeted tasks.</li>
    <li><strong>Integration fit.</strong> We favor solutions that can be inserted into a multilingual archival workflow without forcing every partner into the same infrastructure or model stack.</li>
  </ul>
</section>

<section class="panel">
  <h2>Operational constraints</h2>
  <p>The current benchmarking environment is described as a system centered on an NVIDIA GB10 chip, which in practice limits routine evaluation to models that fit within approximately 128 GB RAM. That matters because some large language models may be interesting experimentally but remain impractical for widespread operational deployment.</p>
  <p>The comparison therefore treats transformer pipelines as the default high-throughput baseline and LLM-based methods as complementary: useful for fallback cases, targeted enrichment, or rapid experimentation where dedicated task models are weak or unavailable.</p>
  <div class="media-frame">
    <img class="content-illustration" src="{{ '/assets/images/hardware-gb10.png' | relative_url }}" alt="Illustration of the GB10-based evaluation hardware used for local benchmarking">
  </div>
</section>

<section class="panel">
  <h2>Testing framework</h2>
  <ul>
    <li>Benchmarking is cyclical rather than one-off.</li>
    <li>New models and datasets are added as the field changes and project needs become clearer.</li>
    <li>This website is intended for continuous updates.</li>
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
