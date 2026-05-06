---
layout: default
title: Current Topics
description: Current and planned ArchXAI topics covered on this site.
permalink: /tracks/
---

<section class="panel">
  <p class="eyebrow">Technology landscape</p>
  <h1>Current and planned topics</h1>
  <p class="lede">This page is now the main entry point for the published benchmark topics. Each topic leads to a short landing page with the current recommendation, the main caveat, and the evidence notes behind it.</p>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Published Topics</h2>
      <p>Use these when you want the current state of a task first, not just the publication timeline.</p>
    </div>
  </div>
  <div class="track-grid">
    <a class="track-card" href="{{ '/topics/ner/' | relative_url }}">
      <p class="chip">Published</p>
      <h3>📇 Named Entity Recognition</h3>
      <p>Default recommendation: dedicated transformer NER models for indexing, with LLMs kept as a secondary fallback and enrichment path.</p>
    </a>
    <a class="track-card" href="{{ '/topics/pii/' | relative_url }}">
      <p class="chip">Published</p>
      <h3>🔐 PII Detection and Anonymization</h3>
      <p>Default recommendation: Presidio for integration-heavy workflows, while MAPA stays relevant for anonymization and visual review.</p>
    </a>
    <a class="track-card" href="{{ '/topics/tone/' | relative_url }}">
      <p class="chip">Preliminary</p>
      <h3>🗣 Tone and Sentiment Analysis</h3>
      <p>Current state: scored results exist, but Estonian underperforms and Finnish still needs an explicit overlap check before stronger conclusions.</p>
    </a>
    <a class="track-card" href="{{ '/topics/embedding/' | relative_url }}">
      <p class="chip">Published</p>
      <h3>🔎 Similarity and Semantic Search</h3>
      <p>Default recommendation: multilingual embeddings are ready for semantic search, with <code>Octen-Embedding-4B</code> currently the broadest safe default.</p>
    </a>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Cross-cutting and Planned</h2>
      <p>These are still useful to track, but they do not yet function as standalone topic hubs in the same way.</p>
    </div>
  </div>
  <div class="track-grid">
    <a class="track-card" href="{{ '/blog/' | relative_url }}?topic=llm">
      <p class="chip">Preliminary</p>
      <h3>🤖 Large Language and Multimodal Models</h3>
      <p>Current LLM evidence appears mainly inside the secondary NER evaluation; a broader multimodal archive workflow view is still planned.</p>
    </a>
    <div class="track-card">
      <p class="chip">Planned</p>
      <h3>Image Classification</h3>
      <p>Reserved for visual archival classification tasks once the benchmark material is curated.</p>
    </div>
  </div>
</section>

<section class="panel">
  <h2>Publication principle</h2>
  <p>Each topic should only move from planned to published when it has enough evidence to support a defensible engineering recommendation. This keeps the site credible and avoids turning the deliverable into a placeholder-heavy document with weak conclusions.</p>
</section>
