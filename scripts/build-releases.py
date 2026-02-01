#!/usr/bin/env python3
"""
Build releases/Awesome-Mnemonics-Complete-Guide.md from README.md.
Run from repo root. Version and date are injected.
Also generates DOCX, PDF, and RTF files using pandoc.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
QUICK_REF = ROOT / "PRINT-QUICK-REFERENCE.md"
RELEASES_DIR = ROOT / "releases"
OUT_MD = RELEASES_DIR / "Awesome-Mnemonics-Complete-Guide.md"
OUT_QUICK_MD = RELEASES_DIR / "Awesome-Mnemonics-Quick-Reference.md"
VERSION = "2.9"
DATE = "2026-01-31"

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

    # 5) After Note, insert release stamp and PDF note (Disclaimer was removed in v2.8)
    # Look for the Note line and insert release info after it
    note_pattern = r'(\*\*Note:\*\* This is a \*\*field guide/playbook\*\*[^\n]+\n\n)'
    release_note = f'*Release v{VERSION} — {DATE}*\n\n*In PDF and DOCX, the table of contents and in-text links are clickable; use the TOC to jump to sections.*\n\n**Note:** This downloadable guide contains the core framework definitions. For real-world scenarios showing how frameworks chain together, see [SCENARIOS.md](../SCENARIOS.md) in the repository. For detailed citations and Framework Confidence Ratings, see [SOURCES.md](../SOURCES.md) in the repository.\n\n'
    text = re.sub(note_pattern, r'\1' + release_note, text)

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
        f'**v{VERSION}** ({DATE}) — Streamlined README: reduced content before TOC from ~160 to 31 lines, condensed Categorized Index, moved detailed sections after TOC for better navigation. [CHANGELOG](../CHANGELOG.md)',
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

    OUT_MD.write_text(text, encoding="utf-8")
    print("Wrote", OUT_MD)
    
    # Generate Quick Reference markdown if source exists
    if QUICK_REF.exists():
        quick_text = QUICK_REF.read_text(encoding="utf-8")
        # Update paths for release version
        quick_text = quick_text.replace('](README.md)', '](../README.md)')
        quick_text = quick_text.replace('](SCENARIOS.md)', '](../SCENARIOS.md) *(available in repository)*')
        quick_text = quick_text.replace('](SOURCES.md)', '](../SOURCES.md) *(available in repository)*')
        OUT_QUICK_MD.write_text(quick_text, encoding="utf-8")
        print("Wrote", OUT_QUICK_MD)
    
    # Generate DOCX, PDF, RTF files using pandoc
    print("\nGenerating DOCX, PDF, and RTF files...")
    generate_formats(OUT_MD, "Awesome-Mnemonics-Complete-Guide")
    if OUT_QUICK_MD.exists():
        generate_formats(OUT_QUICK_MD, "Awesome-Mnemonics-Quick-Reference")
    
    # Create ZIP bundles
    print("\nCreating ZIP bundles...")
    create_zip_bundle("Awesome-Mnemonics-Complete-Guide", VERSION)
    if OUT_QUICK_MD.exists():
        create_zip_bundle("Awesome-Mnemonics-Quick-Reference", VERSION)

def generate_formats(md_file: Path, base_name: str):
    """Generate DOCX, PDF, and RTF files from markdown using pandoc."""
    if not md_file.exists():
        print(f"Warning: {md_file} does not exist, skipping format generation")
        return
    
    # Check if pandoc is available
    try:
        subprocess.run(["pandoc", "--version"], 
                      capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Warning: pandoc not found. Install with: brew install pandoc")
        print("Skipping DOCX/PDF/RTF generation.")
        return
    
    output_dir = md_file.parent
    base_path = output_dir / base_name
    
    # Generate DOCX
    try:
        subprocess.run([
            "pandoc", str(md_file),
            "-o", str(base_path.with_suffix(".docx")),
            "--standalone", "--toc", "--toc-depth=3"
        ], capture_output=True, check=True)
        print(f"  ✓ Generated {base_name}.docx")
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Failed to generate {base_name}.docx: {e.stderr.decode()}")
    
    # Generate RTF
    try:
        subprocess.run([
            "pandoc", str(md_file),
            "-o", str(base_path.with_suffix(".rtf")),
            "--standalone", "--toc", "--toc-depth=3"
        ], capture_output=True, check=True)
        print(f"  ✓ Generated {base_name}.rtf")
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Failed to generate {base_name}.rtf: {e.stderr.decode()}")
    
    # Generate PDF (requires xelatex for emoji support)
    try:
        # Check for xelatex
        subprocess.run(["xelatex", "--version"], 
                      capture_output=True, check=True)
        subprocess.run([
            "pandoc", str(md_file),
            "-o", str(base_path.with_suffix(".pdf")),
            "--standalone", "--toc", "--toc-depth=3",
            "--pdf-engine=xelatex"
        ], capture_output=True, check=True)
        print(f"  ✓ Generated {base_name}.pdf")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f"  ⊘ Skipped {base_name}.pdf (xelatex not found)")

def create_zip_bundle(base_name: str, version: str):
    """Create a ZIP bundle containing all formats for a guide."""
    output_dir = RELEASES_DIR
    # Format: Awesome-Mnemonics-v2.8-Complete-Guide.zip
    # Extract the suffix (Complete-Guide or Quick-Reference) from base_name
    suffix = base_name.replace("Awesome-Mnemonics-", "")
    zip_name = f"Awesome-Mnemonics-v{version}-{suffix}.zip"
    zip_path = output_dir / zip_name
    
    # Files to include in ZIP
    formats = [".pdf", ".docx", ".rtf", ".md"]
    files_to_zip = []
    
    for fmt in formats:
        file_path = output_dir / f"{base_name}{fmt}"
        if file_path.exists():
            files_to_zip.append(file_path)
    
    if not files_to_zip:
        print(f"  ⊘ No files found for {base_name}, skipping ZIP")
        return
    
    # Create ZIP file
    try:
        import zipfile
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in files_to_zip:
                zipf.write(file_path, file_path.name)
                print(f"    Added {file_path.name}")
        zip_size = zip_path.stat().st_size / 1024  # KB
        print(f"  ✓ Created {zip_name} ({zip_size:.1f} KB)")
    except Exception as e:
        print(f"  ✗ Failed to create {zip_name}: {e}")

if __name__ == "__main__":
    main()
