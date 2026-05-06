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
      <p>ArchXAI explores how AI can help archives digitize, index, search, and safely review records across languages. This site now presents that work by topic first, so visitors can quickly see what is already usable, what still needs validation, and which benchmark notes support each conclusion.</p>
      <div class="action-row">
        <a class="button button-primary" href="{{ '/tracks/' | relative_url }}">Explore topics</a>
        <a class="button button-secondary" href="{{ '/blog/' | relative_url }}">Browse benchmark notes</a>
        <a class="button button-secondary" href="{{ '/methodology/' | relative_url }}">How we test tools</a>
      </div>
    </div>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Explore by Topic</h2>
      <p>Use the task areas below as the main way into the site. Each topic now aims to answer a practical question first, with the benchmark notes underneath.</p>
    </div>
    <a class="button button-secondary" href="{{ '/tracks/' | relative_url }}">Open all topics</a>
  </div>
  <div class="track-grid">
    <a class="track-card" href="{{ '/topics/ner/' | relative_url }}">
      <p class="chip">Published</p>
      <h3>📇 Named Entity Recognition</h3>
      <p>Current default: dedicated transformer NER models for indexing, with LLMs kept as a slower fallback or enrichment path.</p>
    </a>
    <a class="track-card" href="{{ '/topics/pii/' | relative_url }}">
      <p class="chip">Published</p>
      <h3>🔐 PII Detection and Anonymization</h3>
      <p>Current default: Presidio for integration workflows, with MAPA remaining valuable for review and anonymization-heavy use cases.</p>
    </a>
    <a class="track-card" href="{{ '/topics/tone/' | relative_url }}">
      <p class="chip">Preliminary</p>
      <h3>🗣 Tone and Sentiment Analysis</h3>
      <p>Current state: scored results exist, but the Finnish and Estonian outcomes still need validation before this becomes a strong operational recommendation.</p>
    </a>
    <a class="track-card" href="{{ '/topics/embedding/' | relative_url }}">
      <p class="chip">Published</p>
      <h3>🔎 Similarity and Semantic Search</h3>
      <p>Current default: multilingual embedding models are already usable for semantic search, with <code>Octen-Embedding-4B</code> leading the broadest recommendation.</p>
    </a>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Current Recommendations at a Glance</h2>
      <p>A fast read of what the current public evidence supports, before diving into the individual benchmark notes.</p>
    </div>
    <a class="button button-secondary" href="{{ '/methodology/' | relative_url }}">Read methodology</a>
  </div>
  <div class="callout-grid">
    <div class="callout-card">
      <h3>📇 NER</h3>
      <p>Use dedicated transformer NER models as the default indexing path. The strongest model should still be selected by language and collection type.</p>
    </div>
    <div class="callout-card">
      <h3>🔐 PII</h3>
      <p>Use Presidio when integration flexibility matters most, but keep MAPA in view when anonymization workflows and human review are central.</p>
    </div>
    <div class="callout-card">
      <h3>🗣 Tone</h3>
      <p>Treat tone and sentiment as exploratory. The current scores are informative, but not yet stable enough for a strong cross-language recommendation.</p>
    </div>
    <div class="callout-card">
      <h3>🔎 Similarity</h3>
      <p>Use multilingual embeddings for concept-level search. <code>Octen-Embedding-4B</code> is the broadest current default, with the best average score and lowest measured vector cost.</p>
    </div>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Recent benchmark notes</h2>
      <p>The newest evidence notes stay visible here, but the main browsing logic now sits under Topics rather than the publication timeline alone.</p>
    </div>
    <a class="button button-secondary" href="{{ '/blog/' | relative_url }}">Browse blog</a>
  </div>
  <div class="post-grid">
    {% for post in site.posts limit:4 %}
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
