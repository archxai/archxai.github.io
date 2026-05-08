---
layout: default
title: Ranking Metrics
description: Plain-language explanations of Recall@1, Spearman, MRR, and MRR@10.
permalink: /learning-corner/ranking/
---

<section class="panel">
  <p class="eyebrow">🎓 Learning corner</p>
  <h1>Ranking and retrieval metrics</h1>
  <p class="lede">Use these metrics when a system returns an ordered list: search results, similar documents, recommendations, or ranked answers.</p>
  <div class="action-row">
    <a class="button button-primary" href="{{ '/learning-corner/' | relative_url }}">Back to Learning Corner</a>
    <a class="button button-secondary" href="{{ '/learning-corner/classification/' | relative_url }}">Classification metrics</a>
  </div>
</section>

<section class="panel">
  <h2>Ranked results: when position matters</h2>
  <p>Search, recommendations, semantic retrieval, and question answering often return a ranked list. For those tasks, we care not only whether the right item appears, but how far down the list users must look.</p>
  <table>
    <thead>
      <tr>
        <th>Question</th>
        <th>Correct result appears at...</th>
        <th>Recall@1 credit</th>
        <th>MRR@10 credit</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Q1</td>
        <td>Rank 1</td>
        <td>1</td>
        <td>1.00</td>
      </tr>
      <tr>
        <td>Q2</td>
        <td>Rank 2</td>
        <td>0</td>
        <td>0.50</td>
      </tr>
      <tr>
        <td>Q3</td>
        <td>Rank 12</td>
        <td>0</td>
        <td>0.00</td>
      </tr>
      <tr>
        <td>Q4</td>
        <td>Rank 1</td>
        <td>1</td>
        <td>1.00</td>
      </tr>
      <tr>
        <td>Q5</td>
        <td>Rank 5</td>
        <td>0</td>
        <td>0.20</td>
      </tr>
    </tbody>
  </table>
  <div class="metric-summary">
    <div>
      <h3>Recall@1</h3>
      <p>Only checks the first result. Here, 2 out of 5 top results are correct, so Recall@1 is 40%.</p>
    </div>
    <div>
      <h3>MRR@10</h3>
      <p>Gives partial credit when the first correct result appears within the top 10. Here, the average is 0.54.</p>
    </div>
  </div>
</section>

<section class="panel">
  <h2>Spearman: do two rankings mostly agree?</h2>
  <p>Spearman is used when the exact score matters less than the order. It asks whether two ranked lists place the same items in a similar order.</p>
  <figure class="metric-figure">
    <img class="metric-image" src="{{ '/assets/images/learning/spearman-ranking.png' | relative_url }}" alt="Spearman example comparing two movie rankings with lines connecting corresponding movies.">
  </figure>
  <table>
    <thead>
      <tr>
        <th>Spearman value</th>
        <th>Plain meaning</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>+1</td>
        <td>The two rankings perfectly agree.</td>
      </tr>
      <tr>
        <td>Around 0</td>
        <td>There is no clear relationship between the rankings.</td>
      </tr>
      <tr>
        <td>-1</td>
        <td>The two rankings are exactly reversed.</td>
      </tr>
    </tbody>
  </table>
</section>

<section class="panel">
  <h2>Mean Reciprocal Rank: how far down did the user have to look?</h2>
  <p>Mean Reciprocal Rank, or MRR, gives more credit when the first correct result appears higher in the list. Rank 1 gets full credit. Rank 2 gets half credit. Rank 3 gets one-third credit.</p>
  <figure class="metric-figure">
    <img class="metric-image" src="{{ '/assets/images/learning/mean-reciprocal-rank.png' | relative_url }}" alt="Mean reciprocal rank chart showing that lower ranked correct answers receive less credit.">
  </figure>
  <p>MRR@10 uses the same idea but only checks the top 10 results. If the first correct result appears below rank 10, it receives no credit for that query.</p>
</section>
