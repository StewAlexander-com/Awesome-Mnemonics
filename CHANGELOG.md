# Changelog

All notable changes to Awesome Mnemonics are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [1.8.0] - 2026-01-25

### Added
- **CHANGELOG.md** — Version history (v1.0, v1.1, v1.5, v1.8) and maintenance notes
- **CI** (`.github/workflows/docs.yml`) — Markdown lint (markdownlint), link check (lychee), spellcheck (codespell)
- **mnemonics-index.yaml** — Tagged index for mnemonics and pipelines (enables search and CLI)
- **CLI** (`scripts/mnemonic`) — `pipeline` and `search` commands; requires PyYAML (`pip install -r scripts/requirements.txt`)
- **Runbook template** (`templates/incident-response-runbook.md`) — Pre-filled STOP → TRACE → DEBUG → 8D
- **docs/METRICS.md** — Map of pipelines and mnemonics to TTA, MTTI, MTTR, MTBF
- **docs/FIELD-REPORTS.md** — Template and CTA for incident write-ups
- **README** — Integrations line (CLI, runbook, Metrics, Field Reports), CHANGELOG link, flowchart text summary (accessibility)

### Changed
- **.markdownlint.yaml**, **.codespell-ignore-words** — Config so existing docs pass lint and spell
- **SNR refactor** — README, CONTRIBUTING, docs, runbook: clarity, readability, usability; reduced length and complexity without removing info
- **Downloadable docs (v1.8)** — Complete Guide and Quick Reference (PDF, DOCX, RTF, MD) rebuilt from latest README and PRINT-QUICK-REFERENCE; v1.8 ZIP bundles

---

## [1.5.0] - 2026-01-25

### Added
- Offline-ready release formats: PDF, DOCX, RTF, Markdown with working table of contents
- ZIP bundles for Complete Guide and Quick Reference (all formats in one file)
- Ishikawa (Fishbone) and A3 Problem Solving in Problem Solving, Categorized Index, and Quick Reference
- PADDER in Quick Reference and Print Quick Reference
- D8 wording fix in 8D Approach (Sources)
- Full Sources & References with attribution (✓ documented, ⚠ adapted, ℹ curated)
- CITATION.cff for citation metadata
- CHANGELOG.md (this file)

### Fixed
- Table of contents and anchor consistency across release formats
- CONTRIBUTING and Print Quick Reference links in PDF/DOCX/RTF for portability

---

## [1.1.0] - 2025-06-01

### Added
- Six Proven Mnemonic Pipelines: Crisis Response, Conflict Resolution, Root Cause Investigation, Strategic Design, Stress Burnout Recovery, Rapid Triage
- Categorized Index (Ops, RCA, Systems Design, Human Factors, Personal Life)
- Mnemonic Selection Flowchart (quick / complex / stress branches)
- Quick Reference & On-Call Guide with situation → pipeline mapping
- Problem Resolution Threats (DICE, FATE, PEST) and triage integration
- CONTRIBUTING.md with submission criteria and pipeline guidelines

---

## [1.0.0] - 2025-01-01

### Added
- Initial collection: Problem Solving (PREPARE, PADDER, ICEBERG, IDEA, 5 Whys, 8D), Problem Analysis (RACI, PESTEL, SWOT, SET), Stress (PACE, STOP, ARIES, HELP, HANDLE, CALM, PUSH, HOPE, SHINE), Communication (BREATHE, PAUSE, WAIT), Infrastructure (TRACE, SCALE, DEBUG)
- PRINT-QUICK-REFERENCE.md for one-page print use

---

## Maintaining this changelog

- **Added** for new mnemonics, pipelines, docs, or tooling
- **Changed** for updates to existing content or behavior
- **Fixed** for corrections and consistency
- **Removed** for deprecated or withdrawn content

When cutting a release, add a new `## [X.Y.Z] - YYYY-MM-DD` block at the top and link the version in the Release Versions section of README.
