#!/bin/bash
# Generate DOCX, PDF, and RTF files from markdown
# Requires: pandoc, xelatex (for PDF)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
RELEASES_DIR="$REPO_ROOT/releases"

cd "$RELEASES_DIR"

echo "Generating DOCX, PDF, and RTF files from markdown..."
echo ""

# Check for pandoc
if ! command -v pandoc &> /dev/null; then
    echo "Error: pandoc is not installed. Install it with: brew install pandoc"
    exit 1
fi

# Generate Complete Guide formats
echo "Generating Complete Guide formats..."
pandoc Awesome-Mnemonics-Complete-Guide.md \
    -o Awesome-Mnemonics-Complete-Guide.docx \
    --standalone --toc --toc-depth=3 \
    2>&1 | grep -v "WARNING.*rsvg-convert" || true

if command -v xelatex &> /dev/null; then
    pandoc Awesome-Mnemonics-Complete-Guide.md \
        -o Awesome-Mnemonics-Complete-Guide.pdf \
        --standalone --toc --toc-depth=3 \
        --pdf-engine=xelatex \
        2>&1 | grep -v "WARNING.*rsvg-convert" || true
else
    echo "Warning: xelatex not found. Skipping PDF generation. Install with: brew install --cask mactex"
fi

pandoc Awesome-Mnemonics-Complete-Guide.md \
    -o Awesome-Mnemonics-Complete-Guide.rtf \
    --standalone --toc --toc-depth=3 \
    2>&1 | grep -v "WARNING.*rsvg-convert" || true

# Generate Quick Reference formats
echo "Generating Quick Reference formats..."
pandoc Awesome-Mnemonics-Quick-Reference.md \
    -o Awesome-Mnemonics-Quick-Reference.docx \
    --standalone --toc --toc-depth=3 \
    2>&1 | grep -v "WARNING.*rsvg-convert" || true

if command -v xelatex &> /dev/null; then
    pandoc Awesome-Mnemonics-Quick-Reference.md \
        -o Awesome-Mnemonics-Quick-Reference.pdf \
        --standalone --toc --toc-depth=3 \
        --pdf-engine=xelatex \
        2>&1 | grep -v "WARNING.*rsvg-convert" || true
else
    echo "Warning: xelatex not found. Skipping PDF generation."
fi

pandoc Awesome-Mnemonics-Quick-Reference.md \
    -o Awesome-Mnemonics-Quick-Reference.rtf \
    --standalone --toc --toc-depth=3 \
    2>&1 | grep -v "WARNING.*rsvg-convert" || true

echo ""
echo "✓ All formats generated successfully!"
echo ""
echo "Generated files:"
ls -lh Awesome-Mnemonics-*.{docx,pdf,rtf} 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'
