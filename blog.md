---
layout: default
title: Benchmark Blog
description: ArchXAI benchmark notes and project updates in publication order.
permalink: /blog/
---

<section class="panel">
  <p class="eyebrow">Publication stream</p>
  <h1>Benchmark blog</h1>
  <p class="lede">This page collects the current ArchXAI benchmark notes in a predictable format. Newest entries appear first, and each note starts with a short explanation before moving to the test scope, result table, interpretation, and next update.</p>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>All posts</h2>
      <p>Listed in reverse chronological order.</p>
    </div>
  </div>
  <div class="blog-list">
    {% for post in site.posts %}
      <a class="blog-card" href="{{ post.url | relative_url }}">
        <div class="blog-card-header">
          {% if post.track %}
            <span class="chip">{{ post.track }}</span>
          {% endif %}
          <p class="blog-date">{{ post.date | date: "%d %B %Y" }}</p>
        </div>
        <h3>{{ post.title }}</h3>
        <p>{{ post.summary | default: post.excerpt | strip_html | truncate: 240 }}</p>
      </a>
    {% endfor %}
  </div>
</section>
