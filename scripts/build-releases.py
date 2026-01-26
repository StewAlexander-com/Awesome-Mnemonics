#!/usr/bin/env python3
"""
Build releases/Awesome-Mnemonics-Complete-Guide.md from README.md.
Run from repo root. Version and date are injected.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
OUT = ROOT / "releases" / "Awesome-Mnemonics-Complete-Guide.md"
VERSION = "2.7"
DATE = "2026-01-26"

def main():
    text = README.read_text(encoding="utf-8")

    # 1) Title: strip badge, use release title
    text = re.sub(r'^# Awesome Mnemonics \[!\[Awesome\][^\]]*\][^\n]*\n', '# Awesome Mnemonics - Complete Guide\n', text, count=1)

    # 2) Image path
    text = text.replace('src="images/awesome-mnemonics-header.png"', 'src="../images/awesome-mnemonics-header.png"')

    # 3) Remove **📥 Download (v...):** line
    text = re.sub(r'\n\*\*📥 Download \(v[^)]+\):\*\* [^\n]*\n', '\n', text)

    # 4) Remove **Tools & docs:** line, but keep note about scenarios/sources
    text = re.sub(r'\n\*\*Tools & docs:\*\* [^\n]*\n', '\n', text)
    
    # 4a) Handle SCENARIOS.md and SOURCES.md references - add note that they're in the repo
    # Also handle badge links that point to SOURCES.md
    text = text.replace('](SOURCES.md)', '](../SOURCES.md) *(available in repository)*')
    text = text.replace('](SCENARIOS.md)', '](../SCENARIOS.md) *(available in repository)*')

    # 5) After Disclaimer, insert release stamp and PDF note
    old = '**Disclaimer:** Includes established frameworks (8D, SWOT, PESTEL, RACI, SET) and curated mnemonics. [Sources & References](#sources--references) for attribution.\n\n'
    new = f'**Disclaimer:** Includes established frameworks (8D, SWOT, PESTEL, RACI, SET) and curated mnemonics. [Sources & References](#sources--references) for attribution.\n\n*Release v{VERSION} — {DATE}*\n\n*In PDF and DOCX, the table of contents and in-text links are clickable; use the TOC to jump to sections.*\n\n**Note:** This downloadable guide contains the core framework definitions. For real-world scenarios showing how frameworks chain together, see [SCENARIOS.md](../SCENARIOS.md) in the repository. For detailed citations and Framework Confidence Ratings, see [SOURCES.md](../SOURCES.md) in the repository.\n\n'
    text = text.replace(old, new)

    # 6) Paths: templates/, docs/ (for same-repo links only), CONTRIBUTING.md, SCENARIOS.md, SOURCES.md
    text = text.replace('](templates/', '](../templates/')
    text = text.replace('](docs/METRICS.md)', '](../docs/METRICS.md)')
    text = text.replace('](docs/FIELD-REPORTS.md)', '](../docs/FIELD-REPORTS.md)')
    text = text.replace('](docs/network-engineering.md)', '](../docs/network-engineering.md)')
    text = text.replace('](docs/cloud-native.md)', '](../docs/cloud-native.md)')
    text = text.replace('](docs/database-performance.md)', '](../docs/database-performance.md)')
    text = text.replace('](CONTRIBUTING.md)', '](../CONTRIBUTING.md)')
    text = text.replace('](PRINT-QUICK-REFERENCE.md)', '](../PRINT-QUICK-REFERENCE.md)')
    text = text.replace('](CHANGELOG.md)', '](../CHANGELOG.md)')
    # SCENARIOS.md and SOURCES.md already handled in step 4a

    # 7) Release Versions section: update to current version, description, and release-relative asset paths
    # Match any v2.x version and replace with current
    text = re.sub(
        r'\*\*v2\.\d+\*\* \(\d{4}-\d{2}-\d{2}\) — [^\[]+\[CHANGELOG\]\(CHANGELOG\.md\)',
        f'**v{VERSION}** ({DATE}) — Added SCENARIOS.md (6 real-world scenarios, decision tree), SOURCES.md (citations, confidence ratings), updated downloadable docs with repository references. [CHANGELOG](../CHANGELOG.md)',
        text
    )
    # Update ZIP file references to current version
    text = re.sub(r'releases/Awesome-Mnemonics-v\d+\.\d+-Complete-Guide\.zip', f'Awesome-Mnemonics-v{VERSION}-Complete-Guide.zip', text)
    text = re.sub(r'releases/Awesome-Mnemonics-v\d+\.\d+-Quick-Reference\.zip', f'Awesome-Mnemonics-v{VERSION}-Quick-Reference.zip', text)
    text = text.replace('releases/Awesome-Mnemonics-Complete-Guide.pdf', 'Awesome-Mnemonics-Complete-Guide.pdf')
    text = text.replace('releases/Awesome-Mnemonics-Complete-Guide.docx', 'Awesome-Mnemonics-Complete-Guide.docx')
    text = text.replace('releases/Awesome-Mnemonics-Complete-Guide.rtf', 'Awesome-Mnemonics-Complete-Guide.rtf')
    text = text.replace('releases/Awesome-Mnemonics-Complete-Guide.md', 'Awesome-Mnemonics-Complete-Guide.md')
    text = text.replace('releases/Awesome-Mnemonics-Quick-Reference.pdf', 'Awesome-Mnemonics-Quick-Reference.pdf')
    text = text.replace('releases/Awesome-Mnemonics-Quick-Reference.docx', 'Awesome-Mnemonics-Quick-Reference.docx')
    text = text.replace('releases/Awesome-Mnemonics-Quick-Reference.rtf', 'Awesome-Mnemonics-Quick-Reference.rtf')
    text = text.replace('releases/Awesome-Mnemonics-Quick-Reference.md', 'Awesome-Mnemonics-Quick-Reference.md')
    text = text.replace('[releases/README](releases/README.md)', '[README](README.md)')

    # 8) Top link
    text = text.replace('[↑ Top](#awesome-mnemonics)', '[↑ Top](#awesome-mnemonics---complete-guide)')

    # 9) TOC first item
    text = text.replace('- [Awesome Mnemonics](#awesome-mnemonics)', '- [Awesome Mnemonics - Complete Guide](#awesome-mnemonics---complete-guide)')

    OUT.write_text(text, encoding="utf-8")
    print("Wrote", OUT)

if __name__ == "__main__":
    main()
