---
layout: default
title: Technology Comparison Blog
description: Continuous web publication for ArchXAI Deliverable D.2.1.1.
permalink: /
---

<section class="hero">
  <p class="eyebrow">ArchXAI · Deliverable D.2.1.1</p>
  <h1>Technology comparison for algorithms and models</h1>
  <p>This site is the continuously updated web version of the ArchXAI technology comparison work. It translates the deliverable into a publishable GitHub Pages format and keeps the current evidence visible as benchmarking evolves during the project.</p>
  <div class="action-row">
    <a class="button button-primary" href="{{ '/overview/' | relative_url }}">Read the overview</a>
    <a class="button button-secondary" href="{{ '/methodology/' | relative_url }}">See the evaluation method</a>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>At a glance</h2>
      <p>Project context drawn from the approved application and current WP2 benchmarking material.</p>
    </div>
  </div>
  <div class="stats-grid">
    <div class="stat-card">
      <h3>Project</h3>
      <p>AI enhanced cross-border archives (CB0600307), focused on improving archival access with shared AI-based public services.</p>
    </div>
    <div class="stat-card">
      <h3>Partners</h3>
      <p>South-Eastern Finland University of Applied Sciences, the National Archives of Finland, the National Archives of Estonia, and the National Archives of Latvia.</p>
    </div>
    <div class="stat-card">
      <h3>Work package link</h3>
      <p>Deliverable D.2.1.1 supports WP2 by documenting model and algorithm choices for cataloguing, indexing, and adjacent archival AI tasks.</p>
    </div>
    <div class="stat-card">
      <h3>Publication model</h3>
      <p>GitHub Pages blog structure, intended for continuous updates instead of a single static report snapshot.</p>
    </div>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Current coverage</h2>
      <p>The site already includes the strongest material available in the workspace and leaves room for later additions.</p>
    </div>
  </div>
  <div class="callout-grid">
    <div class="callout-card">
      <h3>Named Entity Recognition</h3>
      <p>Transformer and LLM benchmarking across Estonian, Finnish, Latvian, and Russian datasets, with accuracy and runtime tradeoffs.</p>
    </div>
    <div class="callout-card">
      <h3>PII Detection and Anonymization</h3>
      <p>Operational comparison of Presidio and MAPA for legal-domain multilingual screening workflows.</p>
    </div>
    <div class="callout-card">
      <h3>Methodology and update cycle</h3>
      <p>Precision, recall, F1, runtime, integration fit, hardware limits, and a commitment to recurring updates as models change.</p>
    </div>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Latest updates</h2>
      <p>Blog-style entries for the current deliverable content.</p>
    </div>
  </div>
  <div class="post-grid">
    {% for post in site.posts %}
      <a class="post-card" href="{{ post.url | relative_url }}">
        {% if post.track %}
          <span class="chip">{{ post.track }}</span>
        {% endif %}
        <h3>{{ post.title }}</h3>
        <p>{{ post.summary | default: post.excerpt | strip_html | truncate: 180 }}</p>
        <p class="post-meta">Open update</p>
      </a>
    {% endfor %}
  </div>
</section>
