# Release Versions

This directory contains release-ready versions of the Awesome Mnemonics guide in multiple formats.

## Available Formats

### Complete Guide
The full guide with all mnemonics, pipelines, examples, and detailed explanations.

- **PDF** ([Awesome-Mnemonics-Complete-Guide.pdf](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-Complete-Guide.pdf)) - Print-ready PDF with working table of contents (129KB) - *Click to download*
- **DOCX** ([Awesome-Mnemonics-Complete-Guide.docx](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-Complete-Guide.docx)) - Microsoft Word format with working table of contents - *Click to download*
- **RTF** ([Awesome-Mnemonics-Complete-Guide.rtf](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-Complete-Guide.rtf)) - Rich Text Format for universal compatibility - *Click to download*
- **Markdown** ([Awesome-Mnemonics-Complete-Guide.md](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-Complete-Guide.md)) - Best for GitHub, GitLab, or any markdown viewer - *Click to download*

### Quick Reference
A condensed one-page reference card perfect for printing or keeping on your desk.

- **PDF** ([Awesome-Mnemonics-Quick-Reference.pdf](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-Quick-Reference.pdf)) - Print-ready PDF with working table of contents (39KB) - *Click to download*
- **DOCX** ([Awesome-Mnemonics-Quick-Reference.docx](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-Quick-Reference.docx)) - Print-ready Word format - *Click to download*
- **RTF** ([Awesome-Mnemonics-Quick-Reference.rtf](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-Quick-Reference.rtf)) - Universal RTF format - *Click to download*
- **Markdown** ([Awesome-Mnemonics-Quick-Reference.md](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-Quick-Reference.md)) - Quick reference in markdown format - *Click to download*

### ZIP bundles (v2.8)
One-click archives containing all formats for each guide:

- **Complete Guide** ([Awesome-Mnemonics-v2.8-Complete-Guide.zip](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-v2.8-Complete-Guide.zip)) — PDF, DOCX, RTF, Markdown - *Click to download*
- **Quick Reference** ([Awesome-Mnemonics-v2.8-Quick-Reference.zip](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-v2.8-Quick-Reference.zip)) — PDF, DOCX, RTF, Markdown - *Click to download*

## Features

✅ **Working Table of Contents** - All formats include clickable/navigable TOC  
✅ **Print-Optimized** - Clean formatting for printing and PDF conversion  
✅ **Offline-Ready** - No external dependencies, works offline  
✅ **Universal Compatibility** - RTF works with virtually any word processor  

## PDF Generation

PDF versions are already included! They were generated using `pdflatex` via pandoc. To regenerate:

```bash
# Use xelatex for Unicode/emoji support (pdflatex does not support emoji)
pandoc Awesome-Mnemonics-Complete-Guide.md -o Awesome-Mnemonics-Complete-Guide.pdf --standalone --toc --toc-depth=3 --pdf-engine=xelatex
pandoc Awesome-Mnemonics-Complete-Guide.md -o Awesome-Mnemonics-Complete-Guide.docx --standalone --toc --toc-depth=3
pandoc Awesome-Mnemonics-Complete-Guide.md -o Awesome-Mnemonics-Complete-Guide.rtf --standalone --toc --toc-depth=3
```

Alternatively, you can:
1. **From DOCX/RTF:** Open in Microsoft Word, LibreOffice, or Google Docs and export to PDF
2. **Online:** Use online converters like CloudConvert or Zamzar

## Usage

- **For Teams:** Share the DOCX files for easy editing and collaboration
- **For Printing:** Use RTF or DOCX formats, then print or convert to PDF
- **For Offline:** Download any format for offline reference during incidents
- **For Integration:** Use Markdown versions in documentation systems

## Updates

These release versions are generated from the main repository files. For the latest updates, check the main [README.md](../README.md) and [PRINT-QUICK-REFERENCE.md](../PRINT-QUICK-REFERENCE.md).

---

*Generated with pandoc — v2.8 (2026-01-26)*

---

## 📥 Quick Download Links

**All formats download directly when clicked (no GitHub file viewer):**

### Complete Guide
- [📄 PDF](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-Complete-Guide.pdf) · [📝 DOCX](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-Complete-Guide.docx) · [📄 RTF](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-Complete-Guide.rtf) · [📋 MD](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-Complete-Guide.md) · [📦 ZIP (all formats)](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-v2.8-Complete-Guide.zip)

### Quick Reference
- [📄 PDF](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-Quick-Reference.pdf) · [📝 DOCX](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-Quick-Reference.docx) · [📄 RTF](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-Quick-Reference.rtf) · [📋 MD](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-Quick-Reference.md) · [📦 ZIP (all formats)](https://github.com/StewAlexander-com/Awesome-Mnemonics/raw/main/releases/Awesome-Mnemonics-v2.8-Quick-Reference.zip)
