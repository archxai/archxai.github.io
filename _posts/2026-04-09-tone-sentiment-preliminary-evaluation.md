---
title: "Tone and sentiment analysis"
summary: Tone and sentiment analysis may help classify document style or attitude, but the current cross-language results need careful interpretation.
track: Tone
track_icon: "🗣"
topics: [tone]
chips:
  - icon: "🗣"
    label: Tone
  - icon: "1️⃣"
    label: Preliminary
date: 2026-03-31 06:30:00 +0300
---

Tone and sentiment analysis tries to estimate the attitude or emotional direction of a text. A simple sentiment task might label a passage as positive, negative, or neutral. A tone task can be broader, for example identifying whether a text sounds formal, urgent, hostile, administrative, or uncertain.

For archives, this is not mainly about judging whether a document is "happy" or "sad". The more useful question is whether tone or sentiment labels can help sort large collections, identify sensitive material, or support thematic exploration.

## What we tested

This benchmark track compares language-specific Hugging Face sentiment models across Estonian, Finnish, Latvian, and Russian. The headline score is **F1**, shown below as a percentage.

The current results already show that this track needs careful validation. Estonian performed poorly, while the Finnish result looks unusually strong and should be checked for possible overlap between evaluation data and training data.

## Headline results

| Language | Best model | F1 |
|---|---|---:|
| 🇪🇪 Estonian | [`tartuNLP/EstBERT128_sentiment`](https://huggingface.co/tartuNLP/EstBERT128_sentiment) | 33.6% |
| 🇫🇮 Finnish | [`nisancoskun/bert-finnish-sentiment-analysis-v2`](https://huggingface.co/nisancoskun/bert-finnish-sentiment-analysis-v2) | 99.7% 🚩 |
| 🇱🇻 Latvian | [`matiss/Latvian-Twitter-Sentiment-Analysis`](https://huggingface.co/matiss/Latvian-Twitter-Sentiment-Analysis) | 60.0% |
| 🪆 Russian | [`blanchefort/rubert-base-cased-sentiment-rusentiment`](https://huggingface.co/blanchefort/rubert-base-cased-sentiment-rusentiment) | 68.7% |

## Early interpretation

The main risk is that tone and sentiment can be misleading in archival material. A document may describe conflict, legal action, illness, or financial distress without expressing an emotional attitude in the modern social-media sense.

The current results reinforce that caution. The Estonian score is low enough that the task may need different data, labels, or models, while the Finnish score is high enough to justify an explicit data-overlap check before it is treated as a reliable benchmark result.

## What to update next

The next useful update is to validate the Finnish benchmark setup, investigate why Estonian underperforms, and add an illustration once there is a clear example worth showing. This track may also benefit from reframing toward archive-relevant document style or review-priority categories rather than generic sentiment alone.
