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
      <p>ArchXAI is a cross-border project exploring how AI can improve archive access, indexing, search, and related public services. This site is the public web version of the project's benchmarking and technology-comparison work.</p>
      <div class="action-row">
        <a class="button button-primary" href="{{ '/blog/' | relative_url }}">Read the blog</a>
        <a class="button button-secondary" href="{{ '/tracks/' | relative_url }}">Explore topics</a>
        <a class="button button-secondary" href="{{ '/learning-corner/' | relative_url }}">Learn more</a>
      </div>
    </div>
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
  <h2>Project summary</h2>
  <p>The common challenge addressed by ArchXAI is improving timely access to archive collections while both archival volumes and public information requests continue to grow. The project objective is to improve public services and archival access through jointly developed AI-based solutions that make cataloguing, indexing, and information request handling faster and more usable across borders.</p>
  <p>The project outputs described in the application are an open source AI HTR tool, an open source AI OCR tool, a tool for enhanced cataloguing and indexing, and an AI-assisted toolset for information requests. The beneficiaries are archivists, archive users, researchers, and the broader public.</p>
  <p>Internally, the underlying material comes from the project's technology-comparison deliverable. For external readers, the purpose is simpler: we test tools, explain what they are good at, and publish useful conclusions as the evidence becomes solid enough to share.</p>
  <p>The current publication emphasizes practical questions:</p>
  <ul>
    <li>Which model families are accurate enough for multilingual archival tasks?</li>
    <li>Which approaches are fast enough for large-scale indexing?</li>
    <li>Which tools are realistic to operate inside institutional archive environments?</li>
    <li>Which solutions are still strong enough only for triage and review support, not for autonomous decisions?</li>
  </ul>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Latest news</h2>
    </div>
    <a class="button button-secondary" href="{{ '/blog/' | relative_url }}">More...</a>
  </div>
  <div class="post-grid">
    {% for post in site.posts limit:3 %}
      <a class="post-card" href="{{ post.url | relative_url }}">
        {% if post.chips %}
          <div class="chip-row">
            {% for chip in post.chips %}
              <span class="chip">{% if chip.icon %}<span class="topic-icon">{{ chip.icon }}</span> {% endif %}{{ chip.label }}</span>
            {% endfor %}
          </div>
        {% elsif post.track %}
          <div class="chip-row">
            <span class="chip">{% if post.track_icon %}<span class="topic-icon">{{ post.track_icon }}</span> {% endif %}{{ post.track }}</span>
          </div>
        {% endif %}
        <h3>{{ post.title }}</h3>
        <p>{{ post.summary | default: post.excerpt | strip_html | truncate: 180 }}</p>
        <p class="post-meta">{{ post.date | date: "%d %B %Y" }}</p>
      </a>
    {% endfor %}
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>More information</h2>
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
