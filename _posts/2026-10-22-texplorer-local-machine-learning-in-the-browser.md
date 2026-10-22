---
title: "From a Hosting Constraint to a Local Web App: TeXplorer in the Browser"
summary: "Hugging Face's Spaces pricing changes led us from a Python demo to browser-side machine learning. Here is what we learned about Transformers.js, ONNX, quantisation, threading, storage, and keeping archival evidence inspectable."
track: Browser deployment
track_icon: "🌐"
topics: [ner, browser-ml, deployment, ocr]
chips:
  - icon: "🌐"
    label: Browser ML
  - icon: "📇"
    label: NER
  - icon: "🛠️"
    label: Development diary
date: 2026-10-22 09:00:00 +0300
---

We did not set out to build a browser-side machine-learning application. We wanted to put our existing archival text-exploration demo on Hugging Face Spaces.

The Python/Gradio version already recognised people, organisations, places, and dates. Around those predictions, we had built historical date parsing, fuzzy name linking, family relationships, maps, timelines, and comparisons with public sources. Publishing it initially looked like a hosting task.

Then the hosting assumptions changed. The no-subscription route available to us was a static HTML Space, rather than another server running Python. That constraint led us to [Transformers.js](https://huggingface.co/docs/transformers.js/index), and to a more interesting question:

**How much of the application could run on the archive user's own computer, inside an ordinary web page?**

The answer turned out to be considerably more than we expected. It also required understanding several things that a server application normally hides.

## What changed at Hugging Face

There is an important distinction behind the pricing story. At the time of writing, Hugging Face documents a subscription requirement for creating Gradio or Docker Spaces on **CPU Basic**: PRO for individual accounts, or Team/Enterprise for organisations. The hardware itself still has no hourly charge. Other routes, including paid hardware and limited personal-account ZeroGPU access, have their own conditions. [The current Space-management guide explains the distinction.](https://huggingface.co/docs/huggingface_hub/main/guides/manage-spaces)

[Static HTML Spaces remain free](https://huggingface.co/docs/hub/spaces-sdks-static). They serve files without running our own Python application server.

So this was not the end of Gradio, nor a rule that every Hugging Face application must become HTML. It was a constraint on **our chosen no-subscription deployment route**. We chose to investigate that route instead of treating a paid server as the only possible solution. These policy details were checked on 22 October 2026; readers should recheck them before making a new hosting decision.

## Static hosting does not mean a static application

Transformers.js uses ONNX Runtime to execute supported models locally. In TeXplorer, the browser downloads the application, runtime, and selected model, then performs inference on the user's device. Hugging Face hosts the files, but does not perform that inference for us.

We did not rewrite every Python algorithm in JavaScript. [Pyodide](https://pyodide.org/en/0.29.3/) let us bring selected existing Python modules into the browser through WebAssembly. That preserved the date parser, grouping rules, and relationship logic we had already spent time testing.

<figure>
  <div class="media-frame media-frame--center">
    <img class="content-illustration" src="{{ '/assets/images/texplorer-browser-architecture.svg' | relative_url }}" alt="Static hosting delivers the application and models to the browser. Separate local workers run NER, Python document logic, and OCR. Optional public lookups cross the browser boundary separately.">
  </div>
  <figcaption>Moving inference into the browser changes where computation happens. It does not eliminate downloads or optional network lookups. <a href="{{ '/assets/images/texplorer-browser-architecture.svg' | relative_url }}">View diagram at full size.</a></figcaption>
</figure>

The division of work is now:

| Component | What it does locally |
|---|---|
| JavaScript interface | Editing, highlighted tags, source review, maps, timelines, and family trees |
| Transformers.js worker | Named entity recognition (NER) with the selected language checkpoint |
| Pyodide worker | Language detection, dates, event categories, fuzzy grouping, and document relationships |
| ONNX Runtime Web OCR worker | Text-line detection and transcription when an image is imported |

Workers keep heavy computation away from the interface's main thread. They do not automatically make every algorithm parallel, but they help keep the page usable while work is in progress.

Free hosting does not make computation free: visitors supply the CPU time, memory, bandwidth, and energy. That makes modest-device testing part of the architecture, not an optional finishing touch.

This is still a development prototype, not a claim that the complete Gradio application has been reproduced. We deliberately left out summarisation, embedded semantic search, and the spaCy experiments from this browser version.

## ONNX was a compatibility requirement, not a hosting rule

One early misconception was that pointing JavaScript at any Hugging Face model repository would be enough. A PyTorch checkpoint or a `safetensors` file is not, by itself, an executable model for our browser runtime.

For this stack, the neural networks need compatible **ONNX graphs**, together with the correct tokenizer, configuration, labels, and preprocessing. This is a requirement of the Transformers.js/ONNX Runtime route we selected, not a rule that Hugging Face only hosts ONNX models.

Exporting the graph was only part of the work. Finnish tokenization differed from the shared Estonian/Latvian model. Russian Rapido used a custom encoder and a trained conditional random field (CRF) decoder. Replacing that decoder with a simple “pick the highest-scoring label” operation would have changed the model, not merely converted its format.

We also had to preserve character offsets. JavaScript strings use UTF-16 indexing; our Python processing uses Unicode code points. Without an explicit conversion, a prediction can look plausible while its highlight points at the wrong characters, especially around emoji or supplementary Unicode characters.

The practical lesson: validate the entire path from **input text to highlighted source span**, not just whether an ONNX session starts successfully.

## Quantisation and compression solve different problems

We use 8-bit quantised NER exports. [Quantisation](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html) represents selected model values at lower precision, reducing model size and potentially improving execution efficiency. It is not necessarily lossless, and a smaller model is not automatically a faster or equally accurate model on every backend.

Separately, we gzip the exported files for transport. Gzip reconstructs the same model bytes after decompression: it saves bandwidth and repository space without being another change to model precision.

Our current NER packaging illustrates the difference:

| Document language | Original checkpoint | Gzip weight download | Decoded ONNX weights |
|---|---|---:|---:|
| Finnish | [Kansallisarkisto/finbert-ner](https://huggingface.co/Kansallisarkisto/finbert-ner) | ~82 MB | ~125 MB |
| Estonian and Latvian | [51la5/roberta-large-NER](https://huggingface.co/51la5/roberta-large-NER) | ~393 MB | ~561 MB |
| Russian | [pierre-tassel/rapido-ner-entity](https://huggingface.co/pierre-tassel/rapido-ner-entity) | ~176 MB | ~310 MB |

These are approximate decimal megabytes for weights, not total browser memory requirements. Tokenizers, runtimes, tensors, and temporary buffers need space too. Only the selected checkpoint is loaded; Estonian and Latvian share one model, and switching to another checkpoint releases the previous worker.

Our small native/export checks retained the predicted labels in three Finnish and three Russian examples. One of six Estonian/Latvian examples had a changed token prediction. That is useful conversion evidence, **not an accuracy benchmark for historical documents**. The interface therefore warns users that the NER models are quantised and that recognised tags require review.

Browser-sized inputs also required overlapping chunks. That changes the available context compared with a model's original long-context configuration. “The same checkpoint” does not mean every surrounding processing choice is identical.

## The 1 GB limit was about the repository

Our first multilingual upload hit a 1 GB Space repository limit. This was not a limit on the user's RAM, and it was not the server's separately documented runtime disk allowance. Hugging Face staff have [recommended keeping large weights in model repositories rather than inside a Space repository](https://huggingface.co/spaces/flamehaze1115/Wonder3D-demo/discussions/23).

For a static application, moving a model elsewhere means the **browser** fetches it; there is no Python startup process to download it on the user's behalf.

We took several complementary steps:

- Quantise the NER graphs and compress weights and tokenizers losslessly for transport.
- Avoid duplicate runtime binaries and unnecessary build assets.
- Load only the requested model and cache downloads where the browser permits it.
- Check actual repository storage before deployment, including retained large-file history.

That last point was easy to miss. Removing a large file from the latest commit does not necessarily remove its historical storage. A small-looking current checkout can still have a large repository behind it. History cleanup needs a deliberate, recoverable procedure, not an automatic force-push on every update.

The current deployment artifact is about **764 MB**. That is our build size, not a new allowance or a guarantee of spare quota: retained revisions must be checked separately. The 1 GB repository constraint and the compute-plan change are separate issues; we are not claiming they were introduced together.

External model hosting can avoid bundling weights with the application. It cannot solve every access problem. A URL that downloads in a browser tab may still reject a JavaScript cross-origin fetch. That is why an ordinary Nextcloud share was not automatically a usable model host for us.

## Multi-threading: four was not the browser's ceiling

Getting the model off the main thread improved responsiveness. Making ONNX computation itself use several CPU threads was another step.

[ONNX Runtime Web's threading documentation](https://onnxruntime.ai/docs/tutorials/web/env-flags-and-session-options.html#envwasmnumthreads) describes an automatic default capped at four threads. That is a default policy, not a universal four-core browser limit. Threaded WebAssembly also requires the browser's shared-memory support and a cross-origin-isolated context.

Our Space supplies isolation headers, including:

```text
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
```

We check `crossOriginIsolated` and `SharedArrayBuffer` rather than assuming that the headers worked. Embedding the app in another page can affect the result. A meta tag or a browser's “enable GPU” setting does not substitute for the required HTTP configuration. [MDN explains the isolation requirements.](https://developer.mozilla.org/en-US/docs/Web/API/Window/crossOriginIsolated)

When isolation is available, our automatic policy uses half the browser-reported logical CPUs, capped at 32. The manual budget also avoids requesting all reported CPUs where possible. A device reporting 20 logical CPUs therefore selects 10 threads automatically. Users can override the choice within that budget. Without isolation, execution falls back to one thread.

The reported CPU count is only a hint: it does not reliably describe physical cores, performance cores, thermal limits, or competing work. More threads can add overhead rather than remove it.

Our recorded local checks showed useful improvements:

| Quantised NER checkpoint | Single-threaded WASM median | Isolated four-thread WASM median |
|---|---:|---:|
| Finnish | 1.683 s | 0.463 s |
| Shared Estonian/Latvian | 4.402 s | 1.216 s |

These were separate local runs on an **NVIDIA GB10 host in headless Chromium**, using fixed repeated snippets of roughly 2,000 and 1,500 characters and three warmed measurements per condition. Timings cover the NER worker's tokenisation, model execution, and decoding; model loading, internet downloads, and Python postprocessing are excluded. The single-thread runs were not isolated; the four-thread runs were. These are engineering checks, not randomized trials or predictions for an ordinary laptop.

A later Finnish comparison measured 0.467 s with four threads and 0.354 s with ten, again as three-run medians. The individual ten-thread times varied substantially. We publish the [small timing evidence snapshot]({{ '/assets/data/texplorer-browser-engineering-2026-10-22.json' | relative_url }}) so that the scope is visible, rather than presenting a universal speed-up factor.

The Python stage remains different. Our pinned [Pyodide 0.29.3 does not support ordinary Python threading or multiprocessing](https://pyodide.org/en/0.29.3/usage/wasm-constraints.html#threading-and-multiprocessing). Increasing the ONNX thread count does not parallelise fuzzy linking. We improved repeated neighbourhood scans with interval indexes instead of splitting documents arbitrarily and losing cross-document identity context.

## Why enabling the GPU did not automatically help

We tested WebGPU rather than assuming it would be faster. In the isolated four-thread checks above, warmed Finnish inference took 0.463 s on CPU/WASM versus 1.213 s through WebGPU; the shared Estonian/Latvian graph took 1.216 s versus 2.381 s.

Provider logs showed mixed CPU/GPU execution in the Finnish quantised graph. Some operations remained on CPU, with transfers between providers. A powerful GPU does not remove dispatch overhead, data movement, or operator-compatibility limits.

That does not establish that CPU is always better. Different exports, precision levels, inputs, and devices can change the result. It does explain why **CPU remains our default**, WebGPU is an experiment, and the app measures setup, first inference, and warmed inference separately.

## A local app still has network and privacy boundaries

Local inference has a real advantage for archival work: the document does not have to be uploaded to an inference service. But “runs locally” must not become a vague promise that nothing ever leaves the browser.

The first visit downloads application and model files. Public-source lookups send the selected name or lookup terms to the chosen service. Maps and remote images also make requests. Caching can reduce later downloads, but this is not a promise that the complete application works offline.

We learned to test **browser access**, not just whether a public website opens. CORS restrictions prevented several otherwise useful services from becoming direct lookup providers. A server-side `requests.get()` succeeding does not prove that a browser can read the same response. We should not silently introduce a third-party proxy and send archival names through it just to make the feature appear to work.

Private Spaces added another lesson: an authenticated HTML page does not guarantee that its JavaScript, workers, models, and images can all load when third-party cookies are blocked. We had to check those assets individually, keep access signatures on the Space's own origin, and verify that they never reached external services.

Equally, a public client-side app cannot hide a reusable private model token in its JavaScript. Files delivered to a visitor are accessible to that visitor. Hosting permissions, model licences, and data-publication decisions still need their own review.

## OCR made the architecture tangible

The same approach now supports imported images using the National Archives of Finland's [Estonian](https://huggingface.co/Kansallisarkisto/estonian-ppocrv6-medium) and [Finnish/Swedish](https://huggingface.co/Kansallisarkisto/multicentury-ppocrv6-medium) PP-OCRv6 models, with a [small text detector](https://huggingface.co/PaddlePaddle/PP-OCRv6_tiny_det_onnx).

These models were already available as ONNX, so we can fetch pinned revisions directly from their public model repositories, check their hashes, and run them with ONNX Runtime Web. They are **full-precision OCR models**: quantisation was a choice for our large NER exports, not a rule for every browser model.

The pipeline still needed the right character dictionary, channel order, crop geometry, and decoder. It is not enough to rename a Python package or copy its weights. We also unload the NER worker before OCR and release the OCR sessions afterwards, rather than retaining every model in memory at once.

Users can compare the original image with the editable transcription, hover over text-line outlines to find the corresponding text, and see a line preview while recognition runs. This makes uncertainty inspectable. Complex layouts and difficult historical handwriting still need evaluation; successful execution of synthetic samples is not proof of archival transcription quality. Finnish/Swedish OCR also does not imply that we have added Swedish NER.

## What we can claim, and what comes next

We have exercised the real NER models in all four document languages and the OCR models in Chromium and Firefox. Separate controlled UI tests cover source offsets, editing, merging, source acceptance, image overlays, and responsive layouts. These checks help catch implementation failures; they do not replace accuracy evaluation on representative archival documents.

The [TeXplorer development Space](https://huggingface.co/spaces/Rahvusarhiiv/ArchXAI_TeXplorer_Demo) is currently private. This article is an engineering report, not a public launch announcement. Redistribution and licensing review remains necessary before publishing the complete application and its bundled assets; in particular, availability of a checkpoint on the Hub is not itself a redistribution licence.

Our next priorities are representative laptop and mobile measurements, broader archive-domain accuracy checks after conversion and chunking, and continued review of model and source licences. A dedicated server remains useful when users need uniform performance, very large documents, private back-end credentials, or institutional batch processing.

The wider lesson is not that browser inference should replace every server. It is that a hosting constraint exposed a useful alternative. We started by trying to avoid running another Python service. We ended up learning how much archival exploration can happen on a user's own device—and how much care is still needed around performance, compatibility, evidence, and trust.
