---
layout: default
title: ArchXAI Technology Updates
description: Public-facing updates on ArchXAI benchmarking and AI workflow development for archive access.
permalink: /
---

<section class="hero">
  <div class="hero-grid">
    <div class="logo-frame">
      <img class="hero-logo" src="{{ '/assets/images/archxai-logo.png' | relative_url }}" alt="Interreg Central Baltic Programme and ArchXAI project logo">
    </div>
    <div class="hero-copy">
      <p class="eyebrow">Cross-border archive innovation</p>
      <h1>AI tools for better archive access</h1>
      <p>ArchXAI explores how AI can help archives digitize, index, search, and safely review records across languages. This site shares what we are testing, what works well, and where human review still matters.</p>
      <div class="action-row">
        <a class="button button-primary" href="{{ '/overview/' | relative_url }}">About the project</a>
        <a class="button button-secondary" href="{{ '/methodology/' | relative_url }}">How we test tools</a>
        <a class="button button-secondary" href="{{ '/blog/' | relative_url }}">Benchmark blog</a>
      </div>
    </div>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>At a glance</h2>
      <p>The current public-facing view of ArchXAI's benchmarking and tool evaluation work.</p>
    </div>
  </div>
  <div class="stats-grid">
    <div class="stat-card">
      <h3>What ArchXAI does</h3>
      <p>The project develops and tests AI-assisted tools that can help archives improve access to records and respond to information requests faster.</p>
    </div>
    <div class="stat-card">
      <h3>Who it is for</h3>
      <p>Archivists, archive users, researchers, and the wider public who benefit from better indexing, search, and multilingual access.</p>
    </div>
    <div class="stat-card">
      <h3>What is published here</h3>
      <p>Short benchmark notes, explanations of how we compare tools, and practical conclusions about what is ready for real workflows.</p>
    </div>
    <div class="stat-card">
      <h3>Why it stays current</h3>
      <p>AI tools move fast, so this site is updated continuously instead of waiting for a single static report at the end of the process.</p>
    </div>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Current topics</h2>
      <p>The strongest material currently available focuses on two practical archive-facing use cases.</p>
    </div>
  </div>
  <div class="callout-grid">
    <div class="callout-card">
      <h3>Named Entity Recognition</h3>
      <p>Can AI reliably spot names of people, places, and organisations in multilingual archival text, and can it do so quickly enough for large-scale indexing?</p>
    </div>
    <div class="callout-card">
      <h3>PII Detection and Anonymization</h3>
      <p>Can AI help identify sensitive information before material is released or opened more widely for research and public use?</p>
    </div>
    <div class="callout-card">
      <h3>How we judge the tools</h3>
      <p>We look at accuracy, speed, and how realistic each method is to integrate into archive workflows. The plain-language explanation is on the methodology page.</p>
    </div>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Project resources</h2>
      <p>Follow the wider project, open models, and code outside this site.</p>
    </div>
  </div>
  <div class="resource-logo-grid">
    <a class="resource-logo-link" href="https://centralbaltic.eu/project/archxai/" target="_blank" rel="noopener" aria-label="Central Baltic project page">
      <img src="{{ '/assets/images/resources/central-baltic.png' | relative_url }}" alt="Interreg Central Baltic Programme logo">
    </a>
    <a class="resource-logo-link" href="https://huggingface.co/archxai-project" target="_blank" rel="noopener" aria-label="Hugging Face">
      <img src="{{ '/assets/images/resources/huggingface.png' | relative_url }}" alt="Hugging Face logo">
    </a>
    <a class="resource-logo-link" href="https://github.com/archxai" target="_blank" rel="noopener" aria-label="GitHub organization">
      <img src="{{ '/assets/images/resources/github.png' | relative_url }}" alt="GitHub logo">
    </a>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Project partners</h2>
      <p>The ArchXAI consortium brings together applied research and national archival institutions from Finland, Estonia, and Latvia.</p>
    </div>
  </div>
  <div class="partner-logo-grid">
    <a class="partner-logo-link" href="https://www.xamk.fi/en/" target="_blank" rel="noopener" aria-label="Xamk">
      <img src="{{ '/assets/images/partners/xamk.png' | relative_url }}" alt="Xamk logo">
    </a>
    <a class="partner-logo-link" href="https://kansallisarkisto.fi/en/frontpage" target="_blank" rel="noopener" aria-label="National Archives of Finland">
      <img src="{{ '/assets/images/partners/naf.png' | relative_url }}" alt="National Archives of Finland logo">
    </a>
    <a class="partner-logo-link" href="https://www.ra.ee/en/" target="_blank" rel="noopener" aria-label="National Archives of Estonia">
      <img src="{{ '/assets/images/partners/nae.png' | relative_url }}" alt="National Archives of Estonia logo">
    </a>
    <a class="partner-logo-link" href="https://www.arhivi.gov.lv/en" target="_blank" rel="noopener" aria-label="National Archives of Latvia">
      <img src="{{ '/assets/images/partners/nal.png' | relative_url }}" alt="National Archives of Latvia logo">
    </a>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Recent benchmark notes</h2>
      <p>Short updates about what has been tested and what the current results suggest.</p>
    </div>
    <a class="button button-secondary" href="{{ '/blog/' | relative_url }}">Browse blog</a>
  </div>
  <div class="post-grid">
    {% for post in site.posts limit:3 %}
      <a class="post-card" href="{{ post.url | relative_url }}">
        {% if post.track %}
          <span class="chip">{{ post.track }}</span>
        {% endif %}
        <h3>{{ post.title }}</h3>
        <p>{{ post.summary | default: post.excerpt | strip_html | truncate: 180 }}</p>
        <p class="post-meta">{{ post.date | date: "%d %B %Y" }}</p>
      </a>
    {% endfor %}
  </div>
</section>
