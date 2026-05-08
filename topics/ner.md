---
layout: default
title: Named Entity Recognition
description: Current ArchXAI view on named entity recognition for multilingual archive indexing.
permalink: /topics/ner/
---

<section class="panel">
  <p class="eyebrow">📑 Topics</p>
  <h1>Named Entity Recognition</h1>
  <p class="lede">Named Entity Recognition is currently one of the strongest task areas on the site. The main question is no longer whether NER can work for archive indexing, but which model family is the most defensible default and where LLMs still help.</p>
  <div class="action-row">
    <a class="button button-primary" href="{{ '/blog/' | relative_url }}?topic=ner">View evidence notes</a>
    <a class="button button-secondary" href="{{ '/methodology/' | relative_url }}">How we test tools</a>
    <a class="button button-secondary" href="{{ '/learning-corner/' | relative_url }}">Learn the metrics</a>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Current View</h2>
      <p>The topic summary below is meant for fast comprehension before reading the underlying benchmark posts.</p>
    </div>
  </div>
  <div class="callout-grid">
    <div class="callout-card">
      <h3>Default recommendation</h3>
      <p>Use dedicated transformer NER models as the primary indexing path, selecting the strongest model by language and collection type.</p>
    </div>
    <div class="callout-card">
      <h3>Where LLMs fit</h3>
      <p>Use LLM extraction as a slower fallback or targeted enrichment path when dedicated models are weak or unavailable.</p>
    </div>
    <div class="callout-card">
      <h3>Main caveat</h3>
      <p>Label inventories vary heavily across datasets, so mapped evaluation is necessary and direct score comparisons need care.</p>
    </div>
    <div class="callout-card">
      <h3>Current signal</h3>
      <p>The strongest current evidence still favors dedicated NER over prompt-based LLM extraction for routine multilingual archive indexing.</p>
    </div>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Evidence Notes</h2>
      <p>These posts contain the detailed benchmark tables, setup notes, and interpretation behind the current recommendation.</p>
    </div>
  </div>
  <div class="post-grid">
    {% assign topic_name = "ner" %}
    {% for post in site.posts %}
      {% if post.topics contains topic_name %}
        <a class="post-card" href="{{ post.url | relative_url }}?topic=ner">
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
