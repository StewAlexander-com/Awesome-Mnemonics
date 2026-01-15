# Release Versions

This directory contains release-ready versions of the Awesome Mnemonics guide in multiple formats.

## Available Formats

### Complete Guide
The full guide with all mnemonics, pipelines, examples, and detailed explanations.

- **PDF** (`Awesome-Mnemonics-Complete-Guide.pdf`) - Print-ready PDF with working table of contents (204KB)
- **DOCX** (`Awesome-Mnemonics-Complete-Guide.docx`) - Microsoft Word format with working table of contents
- **RTF** (`Awesome-Mnemonics-Complete-Guide.rtf`) - Rich Text Format for universal compatibility
- **Markdown** (`Awesome-Mnemonics-Complete-Guide.md`) - Best for GitHub, GitLab, or any markdown viewer

### Quick Reference
A condensed one-page reference card perfect for printing or keeping on your desk.

- **PDF** (`Awesome-Mnemonics-Quick-Reference.pdf`) - Print-ready PDF with working table of contents (128KB)
- **DOCX** (`Awesome-Mnemonics-Quick-Reference.docx`) - Print-ready Word format
- **RTF** (`Awesome-Mnemonics-Quick-Reference.rtf`) - Universal RTF format
- **Markdown** (`Awesome-Mnemonics-Quick-Reference.md`) - Quick reference in markdown format

## Features

✅ **Working Table of Contents** - All formats include clickable/navigable TOC  
✅ **Print-Optimized** - Clean formatting for printing and PDF conversion  
✅ **Offline-Ready** - No external dependencies, works offline  
✅ **Universal Compatibility** - RTF works with virtually any word processor  

## PDF Generation

PDF versions are already included! They were generated using `pdflatex` via pandoc. To regenerate:

```bash
# Note: Emojis are removed for PDF compatibility with pdflatex
pandoc Awesome-Mnemonics-Complete-Guide.md -o Awesome-Mnemonics-Complete-Guide.pdf --standalone --toc --pdf-engine=pdflatex
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

*Generated with pandoc - Last updated: $(date +%Y-%m-%d)*
