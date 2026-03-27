# ArchXAI Deliverable 2.1.1 Pages Site

This folder contains a GitHub Pages compatible Jekyll site for **ArchXAI Deliverable D.2.1.1: Technology Comparison for Algorithms and Models**.

## What is included

- a landing page for the deliverable
- reusable project and methodology pages
- blog posts for the current NER and PII comparisons
- a GitHub Actions workflow for GitHub Pages deployment
- custom styling with no unsupported Jekyll plugins

## Suggested repository setup

This copy is configured for the organization root site:

`archxai.github.io`

That will publish to:

`https://archxai.github.io/`

If you later want to reuse the same site as a project site under the `archxai` organization, create a repository such as:

- `deliverable-2-1-1`
- `technology-comparison`
- `d211-technology-comparison`

## Before first push

The current `_config.yml` already matches the organization root site:

- `url: "https://archxai.github.io"`
- `baseurl: ""`

For a project site later, change `baseurl` to `"/<repo-name>"`.

## Local preview

If Ruby and Bundler are installed:

```bash
bundle install
bundle exec jekyll serve
```

## Source material used

- `D.2.1.1_Technology_Comparison.docx`
- `Project_Application.pdf`
- `NER_Section.md`
- `PII_Section.md`

## Publishing steps

1. Create a repository in the `archxai` organization.
2. Copy the contents of this folder into the repository root.
3. Push to `main`.
4. In GitHub, open `Settings -> Pages`.
5. Under `Source`, choose `GitHub Actions`.
6. Wait for the `pages` workflow to finish.

The included workflow file is `.github/workflows/pages.yml`.
