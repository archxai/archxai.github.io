---
layout: default
title: Similarity and Semantic Search
description: Current ArchXAI view on embeddings for similarity and semantic search.
permalink: /topics/embedding/
---

<section class="panel">
  <p class="eyebrow">Topic brief</p>
  <h1>Similarity and Semantic Search</h1>
  <p class="lede">This topic is already moving from exploration toward deployment-oriented questions. The main issue is less whether embeddings work at all, and more which multilingual model is the safest default for archive search and where current dataset coverage is still uneven.</p>
  <div class="action-row">
    <a class="button button-primary" href="{{ '/blog/' | relative_url }}?topic=embedding">View evidence notes</a>
    <a class="button button-secondary" href="{{ '/methodology/' | relative_url }}">How we test tools</a>
    <a class="button button-secondary" href="{{ '/learning-corner/' | relative_url }}">Learn the metrics</a>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Current View</h2>
      <p>This topic already supports a practical recommendation, with the main caution now focused on synthetic Latvian benchmark coverage.</p>
    </div>
  </div>
  <div class="callout-grid">
    <div class="callout-card">
      <h3>Default recommendation</h3>
      <p>Use <code>Octen-Embedding-4B</code> as the broadest current default for multilingual semantic search across the four target languages.</p>
    </div>
    <div class="callout-card">
      <h3>Language-specific signal</h3>
      <p><code>Octen-Embedding-8B</code> leads Finnish, while <code>Octen-Embedding-8B-INT8</code> leads Latvian after adding synthetic similarity and paraphrase data.</p>
    </div>
    <div class="callout-card">
      <h3>Main caveat</h3>
      <p>The Latvian ranking is no longer FLORES-only, but the added MultiSimLex and TAPACO data are machine-translated and should be validated against native Latvian archive material.</p>
    </div>
    <div class="callout-card">
      <h3>Operational signal</h3>
      <p><code>Octen-Embedding-4B</code> is also the fastest measured model and has the smallest vectors, making it the strongest practical default for indexing experiments.</p>
    </div>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Evidence Notes</h2>
      <p>The published note summarizes the current multilingual embedding benchmark and its language-level recommendations.</p>
    </div>
  </div>
  <div class="post-grid">
    {% assign topic_name = "embedding" %}
    {% for post in site.posts %}
      {% if post.topics contains topic_name %}
        <a class="post-card" href="{{ post.url | relative_url }}?topic=embedding">
          {% if post.chips %}
            <div class="chip-row">
              {% for chip in post.chips %}
                <span class="chip">{% if chip.icon %}<span class="topic-icon">{{ chip.icon }}</span> {% endif %}{{ chip.label }}</span>
              {% endfor %}
            </div>
          {% endif %}
          <h3>{{ post.title }}</h3>
          <p>{{ post.summary | strip_html | truncate: 180 }}</p>
          <p class="post-meta">{{ post.date | date: "%d %B %Y" }}</p>
        </a>
      {% endif %}
    {% endfor %}
  </div>
</section>
