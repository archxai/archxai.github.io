---
layout: default
title: How We Test Tools
description: How ArchXAI runs AI tool evaluations, including benchmark scope, hardware resources, and reporting rules.
permalink: /methodology/
---

<section class="panel">
  <p class="eyebrow">💻 Methodology</p>
  <h1>Evaluation methods</h1>
  <p class="lede">This page explains how ArchXAI runs tool comparisons: what we measure, what hardware constraints shape the tests, and how results move from experiments into public benchmark notes.</p>
</section>

<section class="panel">
  <h2>What we report:/h2>
  <div class="callout-grid">
    <div class="callout-card">
      <h3>⭐ Quality</h3>
      <p>Each task uses metrics suited to its output type: precision, recall, F1, ranking metrics, correlation metrics, or task-specific retrieval scores.</p>
    </div>
    <div class="callout-card">
      <h3>⚡ Performance</h3>
      <p>Where relevant, we add runtime, latency, memory, or vector-size measurements so that a high-scoring model is not mistaken for an automatically deployable model.</p>
    </div>
    <div class="callout-card">
      <h3>🌐 Coverage</h3>
      <p>We report results by language whenever possible, because a model that performs well in one project language may be much weaker in another.</p>
    </div>
    <div class="callout-card">
      <h3>⚠️ Caveats</h3>
      <p>We call out weak datasets, synthetic data, suspiciously strong results, or incomplete model coverage instead of hiding those limits in a single average.</p>
    </div>
  </div>
</section>

<section class="panel">
  <h2>Hardware and runtime limitations</h2>
  <p>The current local benchmarking environment is centered on an NVIDIA GB10 system with CUDA support and approximately 128 GB of shared memory. This is large enough to test many modern transformer and embedding models locally, including several multi-billion-parameter models.</p>
  <p>Those resources still matter. Some models can be tested experimentally but remain expensive for routine deployment because of memory use, vector size, latency, or operational complexity. For that reason, the site treats quality scores and operational costs as separate but connected evidence.</p>
  <div class="media-frame">
    <img class="content-illustration" src="{{ '/assets/images/hardware-gb10.png' | relative_url }}" alt="Illustration of the GB10-based evaluation hardware used for local benchmarking">
  </div>
</section>

<section class="panel">
  <h2>Testing framework</h2>
  <ul>
    <li>Benchmarking is cyclical rather than one-off.</li>
    <li>New models and datasets are added as the field changes and project needs become clearer.</li>
    <li>Public pages are updated continuously, while formal report versions can still be refreshed at larger project milestones.</li>
    <li>Local experiments are preferred when model weights are available, while API-only tools are listed separately unless credentials and usage terms allow a fair comparison.</li>
  </ul>
</section>
