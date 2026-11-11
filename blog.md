---
layout: default
title: Benchmark Blog
description: ArchXAI benchmark notes and project updates in publication order.
permalink: /blog/
---

<section class="panel">
  <p class="eyebrow">🗓️ Development Blog</p>
  <h1>Publication stream</h1>
  <p class="lede">This page is the evidence archive behind the topic pages. Newest entries appear first, and each note keeps the same predictable structure: explanation, test scope, headline result, interpretation, and next update.</p>
  <div class="action-row">
    <a class="button button-primary" href="{{ '/tracks/' | relative_url }}">Browse by topic</a>
    <a class="button button-secondary" href="{{ '/methodology/' | relative_url }}">How we test tools</a>
    <a class="button button-secondary" href="{{ '/learning-corner/' | relative_url }}">Learn the metrics</a>
  </div>
</section>

<section class="panel">
  <div class="section-title">
    <div>
      <h2>Archive</h2>
      <p data-filter-label>Listed in reverse chronological order.</p>
    </div>
  </div>
  <div class="filter-row" data-blog-filters aria-label="Filter benchmark posts">
    <a class="filter-pill" href="{{ '/blog/' | relative_url }}" data-filter="all"><span class="topic-icon">🗂</span> All posts</a>
    {% for topic in site.data.topics %}
      <a class="filter-pill" href="{{ '/blog/' | relative_url }}?topic={{ topic.id | escape }}" data-filter="{{ topic.id | escape }}"><span class="topic-icon">{{ topic.icon }}</span> {{ topic.title | escape }}</a>
    {% endfor %}
  </div>
  <div class="blog-list">
    {% for post in site.posts %}
      <a class="blog-card" href="{{ post.url | relative_url }}" data-blog-post data-base-href="{{ post.url | relative_url }}" data-topics="{{ post.topics | join: ' ' | escape }}">
        <div class="blog-card-header">
          {% include topic-chips.html topics=post.topics %}
          <p class="blog-date">{{ post.date | date: "%d %B %Y" }}</p>
        </div>
        <h3>{{ post.title }}</h3>
        <p>{{ post.summary | default: post.excerpt | strip_html | truncate: 240 }}</p>
      </a>
    {% endfor %}
  </div>
  <p class="filter-empty" data-filter-empty hidden>No posts match this topic yet.</p>
</section>

<script>
  (() => {
    const labels = {
      all: "Listed in reverse chronological order."
      {% for topic in site.data.topics %}, {{ topic.id | jsonify }}: {{ topic.description | jsonify }}{% endfor %}
    };
    const params = new URLSearchParams(window.location.search);
    const topic = (params.get("topic") || "all").toLowerCase();
    const posts = Array.from(document.querySelectorAll("[data-blog-post]"));
    const filters = Array.from(document.querySelectorAll("[data-filter]"));
    const label = document.querySelector("[data-filter-label]");
    const empty = document.querySelector("[data-filter-empty]");

    function applyFilter(nextTopic) {
      const activeTopic = Object.hasOwn(labels, nextTopic) ? nextTopic : "all";
      let visibleCount = 0;

      posts.forEach((post) => {
        const postTopics = (post.dataset.topics || "").split(/\s+/);
        const visible = activeTopic === "all" || postTopics.includes(activeTopic);
        const baseHref = post.dataset.baseHref || post.getAttribute("href");
        post.hidden = !visible;
        post.href = activeTopic === "all" ? baseHref : baseHref + "?topic=" + encodeURIComponent(activeTopic);
        if (visible) visibleCount += 1;
      });

      filters.forEach((filter) => {
        const active = filter.dataset.filter === activeTopic;
        filter.setAttribute("aria-current", active ? "true" : "false");
      });

      if (label) label.textContent = labels[activeTopic];
      if (empty) empty.hidden = visibleCount > 0;
    }

    filters.forEach((filter) => {
      filter.addEventListener("click", (event) => {
        event.preventDefault();
        const nextTopic = filter.dataset.filter || "all";
        const url = nextTopic === "all" ? "{{ '/blog/' | relative_url }}" : "{{ '/blog/' | relative_url }}?topic=" + encodeURIComponent(nextTopic);
        window.history.pushState({}, "", url);
        applyFilter(nextTopic);
      });
    });

    window.addEventListener("popstate", () => {
      const nextParams = new URLSearchParams(window.location.search);
      applyFilter((nextParams.get("topic") || "all").toLowerCase());
    });

    applyFilter(topic);
  })();
</script>
