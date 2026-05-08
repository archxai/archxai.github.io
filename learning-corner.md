---
layout: default
title: Learning Corner
description: Plain-language explanations of evaluation metrics used in ArchXAI benchmark notes.
permalink: /learning-corner/
---

<section class="panel">
  <p class="eyebrow">Learning corner</p>
  <h1>Evaluation metrics without a statistics background</h1>
  <p class="lede">A metric is a score that answers one specific question about how well a system is doing. Start with the kind of system you are evaluating, then choose the metric family that matches it.</p>
  <div class="action-row">
    <a class="button button-primary" href="{{ '/learning-corner/classification/' | relative_url }}">Classification metrics</a>
    <a class="button button-secondary" href="{{ '/learning-corner/ranking/' | relative_url }}">Ranking metrics</a>
    <a class="button button-secondary" href="{{ '/methodology/' | relative_url }}">How we run tests</a>
  </div>
</section>

<section class="panel">
  <h2>Choose the right starting point</h2>
  <div class="track-grid">
    <a class="track-card" href="{{ '/learning-corner/classification/' | relative_url }}">
      <p class="chip">Classification</p>
      <h3>Precision, Recall, and F1</h3>
      <p>Use this path when a system decides whether something belongs to a class: cat or not cat, name or not name, sensitive or not sensitive.</p>
    </a>
    <a class="track-card" href="{{ '/learning-corner/ranking/' | relative_url }}">
      <p class="chip">Search and ranking</p>
      <h3>Recall@1, Spearman, and MRR@10</h3>
      <p>Use this path when a system returns an ordered list: search results, similar documents, recommendations, or ranked answers.</p>
    </a>
  </div>
</section>

<section class="panel">
  <h2>One-page cheat sheet</h2>
  <table>
    <thead>
      <tr>
        <th>Metric</th>
        <th>Plain-English question</th>
        <th>Best for</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>🎯<strong>Precision</strong></td>
        <td>When the system says yes, how often is it right?</td>
        <td>Avoiding false alarms.</td>
      </tr>
      <tr>
        <td>🔍<strong>Recall</strong></td>
        <td>Of everything we wanted to find, how much did we find?</td>
        <td>Avoiding missed items.</td>
      </tr>
      <tr>
        <td>⚖️<strong>F1</strong></td>
        <td>Is the system both careful and complete?</td>
        <td>Balancing precision and recall.</td>
      </tr>
      <tr>
        <td>🔍<strong>Recall@1</strong></td>
        <td>Was the correct item first?</td>
        <td>Strict top-result evaluation.</td>
      </tr>
      <tr>
        <td>⚔️<strong>Spearman</strong></td>
        <td>Do two rankings mostly agree?</td>
        <td>Comparing ordered lists.</td>
      </tr>
      <tr>
        <td>🥇<strong>MRR@10</strong></td>
        <td>How high was the first correct item within the top 10?</td>
        <td>Search, recommendation, and retrieval systems.</td>
      </tr>
    </tbody>
  </table>
</section>
