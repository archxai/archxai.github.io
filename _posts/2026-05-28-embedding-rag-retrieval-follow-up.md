---
title: "Embedding Search Meets Archive RAG"
summary: Follow-up RAG-style tests show that dense embeddings are useful for semantic paraphrase search, but archival retrieval needs lexical, structured, and hybrid search as well.
track: Embedding
track_icon: "🔎"
topics: [embedding]
chips:
  - icon: "🔎"
    label: Embedding
  - icon: "2️⃣"
    label: Secondary
date: 2026-05-30 00:00:00 +0300
---

The previous embedding note focused on multilingual benchmark datasets: semantic similarity, paraphrase retrieval, cross-lingual alignment, and retrieval benchmarks in Estonian, Finnish, Latvian, and Russian. That work was useful for choosing candidate embedding models, but it left one practical archive question partly unanswered:

**What happens when the retrieval task looks more like real RAG search over archive text?**

In this follow-up we tested the strongest embedding candidates on manually checked Estonian HTR/OCR text split into page-level chunks. The result is clearer than the model ranking alone: dense embeddings are valuable, but dense-only retrieval is not enough for archival search. The strongest practical direction is a hybrid architecture that combines semantic vectors with lexical, structured, and query-aware search.

## What changed since the last post

The earlier benchmark compared embedding models on general multilingual evaluation datasets. Since then, we built a more archive-like retrieval dataset from four manually checked Estonian text files. Each file represents a document, and page breaks were preserved so that retrieval could be evaluated at page level.

The corpus contains:

| Item | Count |
|---|---:|
| Documents | 4 |
| Page chunks | 2,451 |
| Synthetic RAG queries | 392 |

The synthetic query set deliberately mixes different retrieval behaviours:

| Query family | Count | Purpose |
|---|---:|---|
| `semantic_paraphrase` | 139 | Natural-language questions generated from page meaning using local Ollama. |
| `annif_topic` | 43 | Topic/keyphrase searches generated from Annif EMS subject suggestions. |
| `date_lookup` | 90 | Exact date searches generated with an Estonian date parser. |
| `number_lookup` | 120 | Exact numeric and archival-style value searches. |

This matters because archive users do not only ask broad semantic questions. They also search for people, places, dates, identifiers, page ranges, case numbers, and specific terms. A realistic retrieval test needs to include both semantic and exact lookup behaviour.

## Dense embedding results

We evaluated nine local Hugging Face embedding models selected from the benchmark tables. The best dense model on the new RAG-style dataset was `Octen/Octen-Embedding-8B`.

| Rank | Dense model | Hit@1 | Hit@5 | MRR@10 | nDCG@10 |
|---:|---|---:|---:|---:|---:|
| 1 | `Octen/Octen-Embedding-8B` | 0.1760 | 0.2449 | 0.2109 | 0.2277 |
| 2 | `Octen/Octen-Embedding-4B` | 0.1582 | 0.2551 | 0.2008 | 0.2194 |
| 3 | `Octen/Octen-Embedding-8B-INT8` | 0.1505 | 0.2296 | 0.1880 | 0.2066 |
| 4 | `bflhc/MoD-Embedding` | 0.1454 | 0.2321 | 0.1823 | 0.2028 |
| 5 | `Qwen/Qwen3-Embedding-4B` | 0.1429 | 0.2092 | 0.1728 | 0.1908 |
| 6 | `Qwen/Qwen3-Embedding-8B` | 0.1429 | 0.1990 | 0.1672 | 0.1781 |
| 7 | `microsoft/harrier-oss-v1-27b` | 0.0893 | 0.1480 | 0.1150 | 0.1291 |
| 8 | `nvidia/llama-embed-nemotron-8b` | 0.0638 | 0.1352 | 0.0945 | 0.1114 |
| 9 | `tencent/KaLM-Embedding-Gemma3-12B-2511` | 0.0357 | 0.0765 | 0.0540 | 0.0642 |

This does not overturn the earlier operational recommendation. `Octen/Octen-Embedding-4B` remains very attractive as a default because it is close to 8B in retrieval quality and materially faster. On this page-level RAG dataset:

| Metric | `Octen-Embedding-8B` | `Octen-Embedding-4B` | Difference |
|---|---:|---:|---:|
| Hit@1 | 0.1760 | 0.1582 | 8B +0.0179 |
| Hit@5 | 0.2449 | 0.2551 | 4B +0.0102 |
| MRR@10 | 0.2109 | 0.2008 | 8B +0.0100 |
| nDCG@10 | 0.2277 | 0.2194 | 8B +0.0083 |
| Total local evaluation time | 530.3 s | 320.0 s | 4B faster |
| Embedding dimension | 4,096 | 2,560 | 4B smaller |

The practical reading is: use `Octen-Embedding-8B` when pure dense quality matters most, but use `Octen-Embedding-4B` when speed, index size, and operating cost matter.

## Where dense retrieval works

Dense embeddings performed best on semantic paraphrase queries. These are the queries closest to what embedding search is designed for.

For `Octen/Octen-Embedding-8B`, the semantic-only slice scored:

| Query type | Hit@1 | Hit@5 | MRR@10 | nDCG@10 |
|---|---:|---:|---:|---:|
| `semantic_paraphrase` | 0.4748 | 0.6259 | 0.5486 | 0.5906 |

One successful example was:

> miks kadusid eestlaste sidemed Eestiga pärast piiri tekkimist

The correct page was ranked first. The top neighbouring results were also sensible: pages about the Eesti-Läti border, Alolinna eestlased, and disrupted contact with Estonia.

This is the strong case for dense retrieval. It can connect user phrasing to meaning even when the exact wording differs.

## Where dense retrieval fails

The weak cases were equally important. Dense-only retrieval performed poorly on exact dates, numbers, and some topic labels.

For `Octen/Octen-Embedding-8B`:

| Query type | Hit@1 | Hit@5 | MRR@10 | nDCG@10 |
|---|---:|---:|---:|---:|
| `annif_topic` | 0.0000 | 0.0698 | 0.0411 | 0.0368 |
| `date_lookup` | 0.0222 | 0.0444 | 0.0333 | 0.0404 |
| `number_lookup` | 0.0083 | 0.0167 | 0.0137 | 0.0164 |

One failure was:

> Leia lehekülg, kus esineb number 75-100.

The correct page was ranked 2,432nd out of 2,451 pages. Dense embeddings treated the query as a vague semantic request about a number, not as an exact value that should be matched literally.

This is not a surprising failure. Embedding models are not reliable exact-match engines. Archive search, however, often depends on exact values: dates, names, identifiers, reference numbers, page ranges, and institutional terms.

## Lexical and hybrid retrieval

We then compared dense retrieval with lexical and hybrid retrieval.

The lexical baselines used TF-IDF word n-grams and TF-IDF character n-grams. The hybrid retriever combined dense scores from `Octen/Octen-Embedding-8B` with lexical scores after per-query normalization:

```text
hybrid_score = alpha * dense_score + (1 - alpha) * lexical_score
```

The best overall result came from character n-gram TF-IDF with a small dense component:

| Retriever | Hit@1 | Hit@5 | MRR@10 | nDCG@10 | Median first rank |
|---|---:|---:|---:|---:|---:|
| `hybrid_tfidf_char_wb_3_5_dense0.25` | 0.4770 | 0.6607 | 0.5588 | 0.5819 | 2.0 |
| `tfidf_char_wb_3_5` | 0.4643 | 0.6786 | 0.5573 | 0.5854 | 2.0 |
| `hybrid_tfidf_word_1_2_dense0.25` | 0.4005 | 0.6071 | 0.4917 | 0.5465 | 3.0 |
| `tfidf_word_1_2` | 0.3827 | 0.6122 | 0.4817 | 0.5399 | 3.0 |
| Dense `Octen/Octen-Embedding-8B` | 0.1760 | 0.2449 | 0.2109 | 0.2277 | 117.5 |

The improvement is too large to ignore. The best hybrid setup more than doubled Hit@1 and MRR@10 compared with dense-only retrieval.

The character n-gram result is especially relevant for archive material. It is more tolerant of OCR/HTR noise, spelling variation, and inflectional endings than strict word matching.

## What this means architecturally

The main conclusion is not simply "use TF-IDF instead of embeddings". The conclusion is that archive RAG should not be dense-only.

A practical retrieval architecture should use several complementary signals:

```text
user query
  -> query analysis
     -> semantic embedding
     -> lexical terms
     -> entities
     -> dates
     -> numbers and identifiers
     -> topics / keyphrases

document pages
  -> dense vectors
  -> raw text index
  -> lemmatized text index
  -> character n-gram index
  -> entity/date/number fields

retrieval
  -> dense candidates
  -> lexical candidates
  -> structured exact-match candidates
  -> fused or reranked result list
```

This matters because different query types need different treatment.

| Query need | Best signal |
|---|---|
| Broad meaning or paraphrase | Dense vectors |
| Names, places, organisations | NER plus lexical/entity index |
| Dates | Date parser plus exact normalized date field |
| Numbers and archive references | Structured number/reference extraction |
| OCR/HTR noise | Character n-grams |
| Morphological variation | Lemmatized lexical field |
| Mixed user questions | Hybrid fusion and reranking |

In other words, the embedding model should be one part of the retrieval system, not the whole retrieval system.

## Query-side analysis is the next step

The current hybrid experiment used simple score fusion. The next version should also analyze the query itself.

For example:

```text
Leia lehekülg, kus esineb number 75-100.
```

A query-aware system should extract `75-100` as a number/range and strongly boost or require pages containing that value. It should not leave that decision to dense embeddings.

Similarly:

```text
Mis toimus 10. detsembril 1934?
```

The system should normalize the date, search a parsed-date field, and still use dense retrieval for the semantic context around "what happened".

The same applies to names and organisations. NER should run on both documents and queries. This would allow the retriever to combine "find pages about this concept" with "and this person or institution must be present".

## Lemmatisation should be added

Estonian morphology makes lemmatisation important for the lexical side of retrieval. Dense models often handle inflectional variation reasonably well, but lexical retrieval needs help.

For example, these forms should be connectable:

```text
valitsus
valitsuse
valitsusele
valitsuses
valitsuselt
```

The safer architecture is not to replace raw text with lemmatised text, but to index both:

| Field | Purpose |
|---|---|
| Raw text | Exact phrases, names, IDs, archival codes, original spelling |
| Lowercased text | Basic lexical retrieval |
| Lemmatized text | Morphology-tolerant topic and content retrieval |
| Character n-grams | OCR/HTR noise tolerance |
| Structured fields | Entities, dates, numbers, references |
| Dense vectors | Semantic retrieval |

Annif already uses `simplemma(et)` in the EMS setup, so a lightweight first prototype can use the same lemmatisation route for Estonian lexical retrieval.

## Updated recommendation

The earlier embedding benchmark remains useful for selecting dense vector models. The new RAG-style test changes the deployment recommendation:

1. Use `Octen/Octen-Embedding-4B` as the default dense model when speed, storage, and operating cost matter.
2. Use `Octen/Octen-Embedding-8B` when dense-only ranking quality is the priority and the higher cost is acceptable.
3. Do not use dense retrieval alone for archive RAG.
4. Build the production retriever as a hybrid system with lexical, character n-gram, lemmatised, entity, date, and number-aware retrieval.
5. Run NER and date/number parsing on the query as well as on the documents.

The most important learning is that embedding models are good at meaning, not at every form of retrieval. Archival access needs meaning, but it also needs exact evidence. A useful system has to support both.

## What to test next

The next evaluation step should compare:

- dense-only retrieval
- lexical BM25 or TF-IDF retrieval
- character n-gram retrieval
- lemmatised lexical retrieval
- query-aware entity/date/number retrieval
- hybrid fusion
- reranking over the top candidates

The current synthetic dataset is useful for development, but the next validation step should include real user-style search questions or partner-provided retrieval examples. That will show how much of the hybrid gain transfers from synthetic queries to actual archive access workflows.
