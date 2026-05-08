---
layout: default
title: PII Detection and Anonymization
description: Current ArchXAI view on PII detection and anonymization workflows.
permalink: /topics/pii/
---

<section class="panel">
  <p class="eyebrow">📑 Topics</p>
  <h1>PII Detection and Anonymization</h1>
  <p class="lede">PII work is less about a single benchmark winner and more about workflow fit. The practical choice depends on whether the archive needs flexible backend integration, visible anonymization review, or both.</p>
  <div class="action-row">
    <a class="button button-primary" href="{{ '/blog/' | relative_url }}?topic=pii">View evidence notes</a>
    <a class="button button-secondary" href="{{ '/methodology/' | relative_url }}">How we test tools</a>
    <a class="button button-secondary" href="{{ '/learning-corner/' | relative_url }}">Learn the metrics</a>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Current View</h2>
      <p>This summary emphasizes operational choices rather than raw score ranking alone.</p>
    </div>
  </div>
  <div class="callout-grid">
    <div class="callout-card">
      <h3>Default recommendation</h3>
      <p>Use Presidio as the default integration layer when the goal is to embed PII detection inside a multilingual archive workflow.</p>
    </div>
    <div class="callout-card">
      <h3>Where MAPA fits</h3>
      <p>Use MAPA when anonymization behavior, human review, and demonstrable interface-level workflows matter most.</p>
    </div>
    <div class="callout-card">
      <h3>Main caveat</h3>
      <p>Russian results are not yet part of the public PII note, so the cross-language picture is still incomplete.</p>
    </div>
    <div class="callout-card">
      <h3>Current signal</h3>
      <p>The current evidence supports a split conclusion: Presidio for extensibility, MAPA for anonymization-centered review support.</p>
    </div>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Evidence Notes</h2>
      <p>The published benchmark note focuses on Presidio, MAPA, and legal-domain release-review support.</p>
    </div>
  </div>
  <div class="post-grid">
    {% assign topic_name = "pii" %}
    {% for post in site.posts %}
      {% if post.topics contains topic_name %}
        <a class="post-card" href="{{ post.url | relative_url }}?topic=pii">
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
