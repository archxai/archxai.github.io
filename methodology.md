---
layout: default
title: How We Test Tools
description: How ArchXAI runs AI tool evaluations, including benchmark scope, hardware resources, and reporting rules.
permalink: /methodology/
---

<section class="panel">
  <p class="eyebrow">Evaluation method</p>
  <h1>How we test tools</h1>
  <p class="lede">This page explains how ArchXAI runs tool comparisons: what we measure, what hardware constraints shape the tests, and how results move from experiments into public benchmark notes.</p>
  <div class="action-row">
    <a class="button button-primary" href="{{ '/learning-corner/' | relative_url }}">Learn the metrics</a>
    <a class="button button-secondary" href="{{ '/blog/' | relative_url }}">Read benchmark notes</a>
  </div>
</section>

<section class="panel">
  <h2>Evaluation logic</h2>
  <p>We do not judge AI tools only by how impressive they sound. We compare them by how accurate they are, how fast they are, and whether they can realistically fit into archive workflows.</p>
  <ul>
    <li><strong>Accuracy and quality.</strong> Each task uses metrics suited to its output type: precision, recall, F1, ranking metrics, correlation metrics, or task-specific retrieval scores.</li>
    <li><strong>Speed and throughput.</strong> We report runtime, sentence or query processing speed, and where relevant index build or search latency.</li>
    <li><strong>Integration fit.</strong> We prefer tools that can be inserted into multilingual archival workflows without forcing every partner into the same infrastructure or model stack.</li>
    <li><strong>Evidence strength.</strong> Results are labeled as preliminary when dataset coverage, language coverage, or task realism is still weak.</li>
  </ul>
</section>

<section class="panel">
  <h2>Hardware and runtime resources</h2>
  <p>The current local benchmarking environment is centered on an NVIDIA GB10 system with CUDA support and approximately 128 GB of shared memory. This is large enough to test many modern transformer and embedding models locally, including several multi-billion-parameter models.</p>
  <p>Those resources still matter. Some models can be tested experimentally but remain expensive for routine deployment because of memory use, vector size, latency, or operational complexity. For that reason, the site treats quality scores and operational costs as separate but connected evidence.</p>
  <div class="media-frame">
    <img class="content-illustration" src="{{ '/assets/images/hardware-gb10.png' | relative_url }}" alt="Illustration of the GB10-based evaluation hardware used for local benchmarking">
  </div>
</section>

<section class="panel">
  <h2>What we report</h2>
  <div class="callout-grid">
    <div class="callout-card">
      <h3>Task scores</h3>
      <p>Each benchmark note reports the metric that matches the task: for example F1 for extraction, MRR@10 for retrieval, or Spearman for ranking agreement.</p>
    </div>
    <div class="callout-card">
      <h3>Operational cost</h3>
      <p>Where relevant, we add runtime, latency, memory, or vector-size measurements so that a high-scoring model is not mistaken for an automatically deployable model.</p>
    </div>
    <div class="callout-card">
      <h3>Language coverage</h3>
      <p>We report results by language whenever possible, because a model that performs well in one project language may be much weaker in another.</p>
    </div>
    <div class="callout-card">
      <h3>Caveats</h3>
      <p>We call out weak datasets, synthetic data, suspiciously strong results, or incomplete model coverage instead of hiding those limits in a single average.</p>
    </div>
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

<section class="panel">
  <h2>Current evidence base</h2>
  <p>The strongest reusable material currently available covers four published technology tracks:</p>
  <ul>
    <li><strong>NER.</strong> Evaluation across modern, historical, and legal-domain datasets with mapped PER, ORG, and LOC labels, including dedicated transformer models and a secondary LLM comparison.</li>
    <li><strong>PII detection and anonymization.</strong> Operational comparison between Presidio and MAPA on legal-domain multilingual data.</li>
    <li><strong>Tone and sentiment analysis.</strong> Preliminary scored results are published, with explicit caveats around Estonian underperformance and a suspiciously strong Finnish result.</li>
    <li><strong>Similarity and semantic search.</strong> Multilingual embedding benchmarks now cover semantic similarity, paraphrase retrieval, cross-lingual sentence retrieval, retrieval-style search tasks, and basic latency/vector-cost measurements.</li>
  </ul>
</section>
