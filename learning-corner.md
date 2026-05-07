---
layout: default
title: Learning Corner
description: Plain-language explanations of evaluation metrics used in ArchXAI benchmark notes.
permalink: /learning-corner/
---

<section class="panel">
  <p class="eyebrow">Learning corner</p>
  <h1>Evaluation metrics without a statistics background</h1>
  <p class="lede">A metric is a score that answers one specific question about how well a system is doing. This page explains the main metrics used in the ArchXAI benchmark notes with simple examples.</p>
  <div class="action-row">
    <a class="button button-primary" href="#classification">Classification metrics</a>
    <a class="button button-secondary" href="#ranking">Ranking metrics</a>
    <a class="button button-secondary" href="{{ '/methodology/' | relative_url }}">How we run tests</a>
  </div>
</section>

<section class="panel" id="classification">
  <h2>Start with a cat-photo detector</h2>
  <p>Imagine a system that looks at 100 photos and predicts either <strong>Cat</strong> or <strong>Not Cat</strong>. The four boxes below are the starting point for precision, recall, and F1.</p>
  <figure class="metric-figure">
    <img class="metric-image" src="{{ '/assets/images/learning/confusion-matrix-cat-detector.png' | relative_url }}" alt="Cat detector confusion matrix showing 20 detected cats, 10 missed cats, 5 false alarms, and 65 correct non-cats.">
  </figure>
  <div class="metric-summary">
    <div>
      <h3>Correct decisions</h3>
      <p>20 real cats were detected, and 65 real non-cats were correctly rejected.</p>
    </div>
    <div>
      <h3>Mistakes</h3>
      <p>5 non-cats were false alarms, and 10 real cats were missed.</p>
    </div>
  </div>
</section>

<section class="panel">
  <h2>Precision: when the system says yes, how often is it right?</h2>
  <p>Precision looks only at the items the system selected. In the cat example, the system predicted 25 photos as cats. 20 really were cats and 5 were false alarms.</p>
  <figure class="metric-figure">
    <img class="metric-image" src="{{ '/assets/images/learning/precision-cat-detector.png' | relative_url }}" alt="Precision example showing 20 correct cat predictions and 5 false alarms among 25 predicted cats.">
  </figure>
  <div class="formula-card">
    <code>Precision = 20 / (20 + 5) = 80%</code>
  </div>
  <p>High precision means: when the system makes a claim, users can usually trust it. This matters when false alarms are costly.</p>
</section>

<section class="panel">
  <h2>Recall: of everything we wanted to find, how much did we find?</h2>
  <p>Recall looks at all the truly relevant items. In the cat example, there were 30 real cats. The system found 20 and missed 10.</p>
  <figure class="metric-figure">
    <img class="metric-image" src="{{ '/assets/images/learning/recall-cat-detector.png' | relative_url }}" alt="Recall example showing 20 detected cats and 10 missed cats among 30 real cat photos.">
  </figure>
  <div class="formula-card">
    <code>Recall = 20 / (20 + 10) = 66.7%</code>
  </div>
  <p>High recall means: the system does not miss many of the things we care about. This matters when missing an item is more harmful than reviewing an extra false alarm.</p>
</section>

<section class="panel">
  <h2>F1: a single score that balances precision and recall</h2>
  <p>F1 combines precision and recall into one stricter balance score. It is high only when the system is both careful and complete.</p>
  <figure class="metric-figure">
    <img class="metric-image" src="{{ '/assets/images/learning/f1-score-balance.png' | relative_url }}" alt="F1 score illustration balancing 80 percent precision and 66.7 percent recall to produce F1 of 72.7 percent.">
  </figure>
  <div class="formula-card">
    <code>F1 = 72.7%</code>
  </div>
  <p>F1 is useful when both kinds of mistakes matter: false alarms waste time, but missed items are also risky.</p>
</section>

<section class="panel" id="ranking">
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

<section class="panel">
  <h2>Quick comparison</h2>
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
        <td><strong>Precision</strong></td>
        <td>When the system says yes, how often is it right?</td>
        <td>Avoiding false alarms.</td>
      </tr>
      <tr>
        <td><strong>Recall</strong></td>
        <td>Of everything we wanted to find, how much did we find?</td>
        <td>Avoiding missed items.</td>
      </tr>
      <tr>
        <td><strong>Recall@1</strong></td>
        <td>Was the correct item first?</td>
        <td>Strict top-result evaluation.</td>
      </tr>
      <tr>
        <td><strong>F1</strong></td>
        <td>Is the system both careful and complete?</td>
        <td>Balancing precision and recall.</td>
      </tr>
      <tr>
        <td><strong>Spearman</strong></td>
        <td>Do two rankings mostly agree?</td>
        <td>Comparing ordered lists.</td>
      </tr>
      <tr>
        <td><strong>MRR@10</strong></td>
        <td>How high was the first correct item within the top 10?</td>
        <td>Search, recommendation, and retrieval systems.</td>
      </tr>
    </tbody>
  </table>
</section>
