---
layout: default
title: Current Topics
description: Current and planned ArchXAI topics covered on this site.
permalink: /tracks/
---

<section class="panel">
  <p class="eyebrow">Technology landscape</p>
  <h1>Current and planned topics</h1>
  <p class="lede">This site publishes the parts of the ArchXAI comparison work that already have useful evidence behind them, while keeping the next planned topics visible.</p>
</section>

<section class="panel">
  <div class="track-grid">
    <a class="track-card" href="{{ '/blog/' | relative_url }}?topic=ner">
      <p class="chip">Published</p>
      <h3>Named Entity Recognition</h3>
      <p>Best current evidence for dedicated transformer and LLM entity extraction in Estonian, Finnish, Latvian, and Russian archival-adjacent text.</p>
    </a>
    <a class="track-card" href="{{ '/blog/' | relative_url }}?topic=pii">
      <p class="chip">Published</p>
      <h3>PII Detection and Anonymization</h3>
      <p>Presidio and MAPA comparison with emphasis on legal-domain release-review support workflows.</p>
    </a>
    <a class="track-card" href="{{ '/blog/' | relative_url }}?topic=tone">
      <p class="chip">Preliminary</p>
      <h3>Text Classification and Tone Analysis</h3>
      <p>Initial explanation and benchmark table structure are published; scored results will be added once the out-of-domain evaluation is run.</p>
    </a>
    <div class="track-card">
      <p class="chip">Planned</p>
      <h3>Similarity and Semantic Search</h3>
      <p>Reserved for embedding-based retrieval, vector search, and retrieval-augmented archive access experiments.</p>
    </div>
    <div class="track-card">
      <p class="chip">Planned</p>
      <h3>Image Classification</h3>
      <p>Reserved for visual archival classification tasks once the benchmark material is curated.</p>
    </div>
    <div class="track-card">
      <p class="chip">Planned</p>
      <h3>Large Language and Multimodal Models</h3>
      <p>Reserved for cross-task prompt-based workflows and multimodal archival assistance use cases.</p>
    </div>
  </div>
</section>

<section class="panel">
  <h2>Publication principle</h2>
  <p>Each track should only move from planned to published when it has enough evidence to support a defensible engineering recommendation. This keeps the site credible and avoids turning the deliverable into a placeholder-heavy document with weak conclusions.</p>
</section>
