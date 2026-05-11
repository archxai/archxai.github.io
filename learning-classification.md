---
layout: default
title: Classification Metrics
description: Plain-language explanations of precision, recall, and F1.
permalink: /learning-corner/classification/
---

<section class="panel">
  <p class="eyebrow">🎓 Learning corner</p>
  <h1>Classification metrics</h1>
  <p class="lede">Use these metrics when a system decides whether something belongs to a class: cat or not cat, name or not name, sensitive or not sensitive.</p>
  <div class="action-row">
    <a class="button button-primary" href="{{ '/learning-corner/' | relative_url }}">Back to Learning Corner</a>
    <a class="button button-secondary" href="{{ '/learning-corner/ranking/' | relative_url }}">Ranking metrics</a>
  </div>
</section>

<section class="panel">
  <h2>Example Background</h2>
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
  <h2><a href="https://en.wikipedia.org/wiki/Precision_and_recall">🎯 Precision</a></h2>
  <p>Precision looks only at the items the system selected. In the cat example, the system predicted 25 photos as cats. 20 really were cats and 5 were false alarms.</p>
  <figure class="metric-figure">
    <img class="metric-image" src="{{ '/assets/images/learning/precision-cat-detector.png' | relative_url }}" alt="Precision example showing 20 correct cat predictions and 5 false alarms among 25 predicted cats.">
  </figure>
  <div class="formula-card">
    <code>Precision = TP / (TP + FP)</code><br>
    <code>Precision = 20 / (20 + 5) = 80%</code>
  </div>
  <p>High precision means: when the system makes a claim, users can usually trust it. This matters when false alarms are costly.</p>
</section>

<section class="panel">
  <h2><a href="https://en.wikipedia.org/wiki/Precision_and_recall">🔍 Recall</a></h2>
  <p>Recall looks at all the truly relevant items. In the cat example, there were 30 real cats. The system found 20 and missed 10.</p>
  <figure class="metric-figure">
    <img class="metric-image" src="{{ '/assets/images/learning/recall-cat-detector.png' | relative_url }}" alt="Recall example showing 20 detected cats and 10 missed cats among 30 real cat photos.">
  </figure>
  <div class="formula-card">
    <code>Recall = TP / (TP + FN)</code><br>
    <code>Recall = 20 / (20 + 10) = 66.7%</code>
  </div>
  <p>High recall means: the system does not miss many of the things we care about. This matters when missing an item is more harmful than reviewing an extra false alarm.</p>
</section>

<section class="panel">
  <h2><a href="https://en.wikipedia.org/wiki/F-score">⚖️ F1 Score</a></h2>
  <p>F1 combines precision and recall into one stricter balance score. It is high only when the system is both careful and complete.</p>
  <figure class="metric-figure">
    <img class="metric-image" src="{{ '/assets/images/learning/f1-score-balance.png' | relative_url }}" alt="F1 score illustration balancing 80 percent precision and 66.7 percent recall to produce F1 of 72.7 percent.">
  </figure>
  <div class="formula-card">
    <code>F1 = 2 × (Precision × Recall) / (Precision + Recall)</code><br>
    <code>F1 = 2 × (0.80 × 0.667) / (0.80 + 0.667) = 0.727 = 72.7%</code>
  </div>
  <p>F1 is useful when both kinds of mistakes matter: false alarms waste time, but missed items are also risky.</p>
</section>
