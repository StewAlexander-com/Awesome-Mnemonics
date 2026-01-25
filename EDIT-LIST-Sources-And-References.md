# Step-by-Step Edit List: Sources & References

Exact line ranges and patch-style edits for **README.md**, **CONTRIBUTING.md**, and **CITATION.cff**.

---

## 1. README.md

### 1.1 — Add disclaimer (after line 9)

**Location:** After the tagline (line 9), before the download line (line 11). If there is a blank at line 10, replace it with the disclaimer plus a blank; otherwise insert the disclaimer (and a blank) between lines 9 and 11.

**OLD (lines 9–11; line 11 is the full `**📥 Download Release Versions:**` line including all links — keep it unchanged):**
```
**Memory hacks that compress complex workflows into actionable acronyms. Use during incidents, RCAs, design decisions, or high-stress situations.**

**📥 Download Release Versions:** [Complete Guide (PDF)](releases/Awesome-Mnemonics-Complete-Guide.pdf) | [Quick Reference (PDF)](releases/Awesome-Mnemonics-Quick-Reference.pdf) | … (rest of links)
```

**NEW (insert the two middle lines; the `**📥**` line stays exactly as in your file):**
```
**Memory hacks that compress complex workflows into actionable acronyms. Use during incidents, RCAs, design decisions, or high-stress situations.**

**Disclaimer:** This collection includes both established, documented frameworks (e.g. 8D, SWOT, PESTEL, RACI, SET) and mnemonics compiled for learning and incident use. See [Sources & References](#sources--references) for attribution and classification.

**📥 Download Release Versions:** [Complete Guide (PDF)](releases/Awesome-Mnemonics-Complete-Guide.pdf) | … (unchanged)
```

**Patch (unified diff; the `**📥**` line is context, only the `+` lines are added):**
```diff
@@ -7,6 +7,10 @@
 **Memory hacks that compress complex workflows into actionable acronyms. Use during incidents, RCAs, design decisions, or high-stress situations.**
 
+**Disclaimer:** This collection includes both established, documented frameworks (e.g. 8D, SWOT, PESTEL, RACI, SET) and mnemonics compiled for learning and incident use. See [Sources & References](#sources--references) for attribution and classification.
+
 **📥 Download Release Versions:** [Complete Guide (PDF)](releases/Awesome-Mnemonics-Complete-Guide.pdf) | [Quick Reference (PDF)](releases/Awesome-Mnemonics-Quick-Reference.pdf) | ...
```

---

### 1.2 — Add TOC entry for Sources & References (after line 193)

**Location:** Table of Contents, after `[📥 Release Versions](#-release-versions)`.

**OLD (lines 192–195):**
```
  - [🤝 Contributing](#-contributing)
  - [📥 Release Versions](#-release-versions)

- - - -
```

**NEW:**
```
  - [🤝 Contributing](#-contributing)
  - [📥 Release Versions](#-release-versions)
  - [Sources & References](#sources--references)

- - - -
```

**Patch:**
```diff
@@ -191,6 +191,7 @@
   - [🤝 Contributing](#-contributing)
   - [📥 Release Versions](#-release-versions)
+  - [Sources & References](#sources--references)
 
 - - - -
```

---

### 1.3 — Add Sources & References section (after line 1011, at end of file)

**Location:** After the Release Versions section, at the end of README.md.

**OLD (lines 1009–1011):**
```
  - [Markdown](releases/Awesome-Mnemonics-Quick-Reference.md) - One-page quick reference card

*Perfect for printing, sharing with teams, or offline reference during incidents.*
```

**NEW:**
```
  - [Markdown](releases/Awesome-Mnemonics-Quick-Reference.md) - One-page quick reference card

*Perfect for printing, sharing with teams, or offline reference during incidents.*

---

## Sources & References

### Problem-Solving Methodologies
- **8D (Eight Disciplines)** ✓ — Ford Motor Company (1987). *Team Oriented Problem Solving Manual*. Evolved from TQM; in wide use in automotive and aerospace. [Wikipedia](https://en.wikipedia.org/wiki/Eight_disciplines_problem_solving)
- **5 Whys** ⚠ — Toyota Production System root cause technique; widely adapted across industries.
- **PADDER, ICEBERG, IDEA, PREPARE** ℹ — Curated/educational problem-solving mnemonics for this collection.

### Strategic & Analysis Frameworks
- **PESTEL** ✓ — Aguilar, F. (1967). *Scanning the Business Environment*. Harvard; later extended to PESTLE/PESTEL (Legal, Environmental). [Background](https://www.linkedin.com/pulse/background-development-pestel-analysis-biplab-paul-8hj0c)
- **PEST** ℹ — Four-factor variant (Political, Economic, Social, Technological); conceptually from the PESTEL lineage.
- **SWOT** ✓ — Humphrey, A. (1960s–70s). Stanford Research Institute (SRI International); developed with Fortune 500 planning research. [e.g. Ninety](https://www.ninety.io/hubfs/Founders%20Framework%20-%20The%20SWOT%20Analysis%20and%20Strategic%20Planning%20Framework.pdf)
- **RACI** ✓ — Responsibility Assignment Matrix; emerged ~1950s–70s, no single inventor. [Wikipedia RAM](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)
- **SET (Systems Engineering Triangle)** ✓ — SEBoK, *Guide to the Systems Engineering Body of Knowledge*. [SEBoK](https://www.sebokwiki.org/wiki/Guide_to_the_Systems_Engineering_Body_of_Knowledge_(SEBoK))

### Problem Resolution Threats & Triage
- **DICE, FATE** ℹ — Educational mnemonics for blockers and resource checks in this collection.

### Communication, Stress & Resilience, Infrastructure
- **BREATHE, PAUSE, WAIT, PACE, STOP, ARIES, HELP, HANDLE, CALM, PUSH, HOPE, SHINE** ℹ — Curated for stress management and conflict de-escalation.
- **TRACE, SCALE, DEBUG** ℹ — Curated for infrastructure and troubleshooting.

### Related Root Cause / Quality Tools (not in this repo)
- **Ishikawa (Fishbone) Diagram** — Cause–effect analysis; pairs with 5 Whys.
- **A3 Problem Solving** — Toyota's single-page, structured problem-solving format.

**Note:** ✓ = documented origin; ⚠ = widely used, adapted from a known source; ℹ = compiled/curated for learning in this guide. Some entries are established frameworks; others are educational compilations.
```

**Patch (conceptual; add after the last line):**
```diff
@@ -1008,3 +1008,38 @@
 *Perfect for printing, sharing with teams, or offline reference during incidents.*
+
+---
+
+## Sources & References
+
+### Problem-Solving Methodologies
+- **8D (Eight Disciplines)** ✓ — Ford Motor Company (1987). *Team Oriented Problem Solving Manual*. Evolved from TQM; in wide use in automotive and aerospace. [Wikipedia](https://en.wikipedia.org/wiki/Eight_disciplines_problem_solving)
+- **5 Whys** ⚠ — Toyota Production System root cause technique; widely adapted across industries.
+- **PADDER, ICEBERG, IDEA, PREPARE** ℹ — Curated/educational problem-solving mnemonics for this collection.
+
+### Strategic & Analysis Frameworks
+- **PESTEL** ✓ — Aguilar, F. (1967). *Scanning the Business Environment*. Harvard; later extended to PESTLE/PESTEL (Legal, Environmental). [Background](https://www.linkedin.com/pulse/background-development-pestel-analysis-biplab-paul-8hj0c)
+- **PEST** ℹ — Four-factor variant (Political, Economic, Social, Technological); conceptually from the PESTEL lineage.
+- **SWOT** ✓ — Humphrey, A. (1960s–70s). Stanford Research Institute (SRI International); developed with Fortune 500 planning research. [e.g. Ninety](https://www.ninety.io/hubfs/Founders%20Framework%20-%20The%20SWOT%20Analysis%20and%20Strategic%20Planning%20Framework.pdf)
+- **RACI** ✓ — Responsibility Assignment Matrix; emerged ~1950s–70s, no single inventor. [Wikipedia RAM](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)
+- **SET (Systems Engineering Triangle)** ✓ — SEBoK, *Guide to the Systems Engineering Body of Knowledge*. [SEBoK](https://www.sebokwiki.org/wiki/Guide_to_the_Systems_Engineering_Body_of_Knowledge_(SEBoK))
+
+### Problem Resolution Threats & Triage
+- **DICE, FATE** ℹ — Educational mnemonics for blockers and resource checks in this collection.
+
+### Communication, Stress & Resilience, Infrastructure
+- **BREATHE, PAUSE, WAIT, PACE, STOP, ARIES, HELP, HANDLE, CALM, PUSH, HOPE, SHINE** ℹ — Curated for stress management and conflict de-escalation.
+- **TRACE, SCALE, DEBUG** ℹ — Curated for infrastructure and troubleshooting.
+
+### Related Root Cause / Quality Tools (not in this repo)
+- **Ishikawa (Fishbone) Diagram** — Cause–effect analysis; pairs with 5 Whys.
+- **A3 Problem Solving** — Toyota's single-page, structured problem-solving format.
+
+**Note:** ✓ = documented origin; ⚠ = widely used, adapted from a known source; ℹ = compiled/curated for learning in this guide. Some entries are established frameworks; others are educational compilations.
```

---

### 1.4 — [OPTIONAL] Refine D8 wording in 8D Approach (lines 318–319)

**Location:** 8D block, D8 line only.

**OLD:**
```
D8 - Closure & Celebration  
```

**NEW (align with formal 8D; keep your phrase in parentheses):**
```
D8 - Congratulate your team and close the loop (closure & celebration)
```

**Patch:**
```diff
@@ -315,7 +315,7 @@
 D6 - Implement & Validate Corrective Actions  
 D7 - Prevent reoccurrence(s)  
-D8 - Closure & Celebration  
+D8 - Congratulate your team and close the loop (closure & celebration)
 ```

---

## 2. CONTRIBUTING.md

### 2.1 — Add source/origin to Submission Criteria (after line 12)

**Location:** In the “Submission Criteria” bullet list, after the “Memorable” item.

**OLD (lines 9–14):**
```
- ✅ **Provable/actionable** - Not just motivational, must have concrete steps
- ✅ **Cross-references** - Should link to related mnemonics where applicable
- ✅ **Real-world context** - Include actual usage examples
- ✅ **Memorable** - The acronym/pattern should be easy to recall under pressure

## Mnemonic Submission Template
```

**NEW:**
```
- ✅ **Provable/actionable** - Not just motivational, must have concrete steps
- ✅ **Cross-references** - Should link to related mnemonics where applicable
- ✅ **Real-world context** - Include actual usage examples
- ✅ **Memorable** - The acronym/pattern should be easy to recall under pressure
- ✅ **Source/origin (if known)** - For established frameworks, note the origin (e.g. "Ford 8D", "Toyota 5 Whys"). For original or curated mnemonics, write "Curated for this collection." Maintainers may classify entries in the [Sources & References](README.md#sources--references) section.

## Mnemonic Submission Template
```

**Patch:**
```diff
@@ -9,6 +9,7 @@
 - ✅ **Cross-references** - Should link to related mnemonics where applicable
 - ✅ **Real-world context** - Include actual usage examples
 - ✅ **Memorable** - The acronym/pattern should be easy to recall under pressure
+- ✅ **Source/origin (if known)** - For established frameworks, note the origin (e.g. "Ford 8D", "Toyota 5 Whys"). For original or curated mnemonics, write "Curated for this collection." Maintainers may classify entries in the [Sources & References](README.md#sources--references) section.
 
 ## Mnemonic Submission Template
 ```

---

### 2.2 — Add “Source (if applicable)” to Mnemonic Submission Template (lines 35–38)

**Location:** Inside the template code block, between `**🔗 Combines well with:**` and `**📋 Real-world example:**`.

**OLD:**
```
**🔗 Combines well with:** [Related Mnemonic](#link) (why it works together)

**📋 Real-world example:** *Brief scenario showing the mnemonic in action*
```

**NEW:**
```
**🔗 Combines well with:** [Related Mnemonic](#link) (why it works together)

**Source (if applicable):** Published framework, standard, or "Curated for this collection."

**📋 Real-world example:** *Brief scenario showing the mnemonic in action*
```

**Patch:**
```diff
@@ -34,6 +34,8 @@
 **🔗 Combines well with:** [Related Mnemonic](#link) (why it works together)
 
+**Source (if applicable):** Published framework, standard, or "Curated for this collection."
+
 **📋 Real-world example:** *Brief scenario showing the mnemonic in action*
 ```

---

### 2.3 — Add “Provide source/origin” to Submission Process (after step 4; renumber 5→6, 6→7)

**Location:** In “Submission Process”, after “Add cross-references” and before “Test your links”.

**OLD (lines 69–77):**
```
4. **Add cross-references** - Link your mnemonic in related "Combines well with" sections
5. **Test your links** - Ensure all anchor links work correctly
6. **Submit a pull request** with:
```

**NEW:**
```
4. **Add cross-references** - Link your mnemonic in related "Combines well with" sections
5. **Provide source/origin** - If it's an established framework, include its origin so we can cite it in [Sources & References](README.md#sources--references).
6. **Test your links** - Ensure all anchor links work correctly
7. **Submit a pull request** with:
```

**Patch:**
```diff
@@ -68,8 +68,10 @@
 4. **Add cross-references** - Link your mnemonic in related "Combines well with" sections
+5. **Provide source/origin** - If it's an established framework, include its origin so we can cite it in [Sources & References](README.md#sources--references).
-5. **Test your links** - Ensure all anchor links work correctly
-6. **Submit a pull request** with:
+6. **Test your links** - Ensure all anchor links work correctly
+7. **Submit a pull request** with:
```

---

### 2.4 — Add Attribution to Quality Standards (after line 111)

**Location:** In the “Quality Standards” list, after “Consistency”.

**OLD (lines 108–113):**
```
- **Completeness** - Include all required sections (When to use, Pitfalls, Combines well with, Example)
- **Consistency** - Follow existing formatting and style

## Mobile & Print Considerations
```

**NEW:**
```
- **Completeness** - Include all required sections (When to use, Pitfalls, Combines well with, Example)
- **Consistency** - Follow existing formatting and style
- **Attribution** - For established frameworks, provide sources so maintainers can classify them (✓ verified / ⚠ common usage / ℹ curated) in the [Sources & References](README.md#sources--references) section.

## Mobile & Print Considerations
```

**Patch:**
```diff
@@ -108,6 +108,7 @@
 - **Completeness** - Include all required sections (When to use, Pitfalls, Combines well with, Example)
 - **Consistency** - Follow existing formatting and style
+- **Attribution** - For established frameworks, provide sources so maintainers can classify them (✓ verified / ⚠ common usage / ℹ curated) in the [Sources & References](README.md#sources--references) section.
 
 ## Mobile & Print Considerations
 ```

---

## 3. CITATION.cff (new file)

**Location:** Repo root: `CITATION.cff`

**Action:** Create the file with the following content. Adjust `date-released` and `url` / `repository-code` if your canonical repo or release date differ.

**Contents:**
```yaml
cff-version: 1.2.0
title: "Awesome Mnemonics"
message: "If you use this collection in writing or training, please cite it."
authors:
  - family-names: "Alexander"
    given-names: "Stew"
date-released: "2022-01-01"
url: "https://github.com/StewAlexander-com/Awesome-Mnemonics"
repository-code: "https://github.com/StewAlexander-com/Awesome-Mnemonics"
```

**Note:** There is no “old” content; this is a new file. If your repo lives at a different URL, replace both `url` and `repository-code`.

---

## Summary Checklist

| #   | File          | Lines / action                          | Description                                      |
|-----|---------------|-----------------------------------------|--------------------------------------------------|
| 1.1 | README.md     | After 9                                 | Add disclaimer                                   |
| 1.2 | README.md     | After 193                               | Add TOC entry for Sources & References           |
| 1.3 | README.md     | After 1011                              | Add full Sources & References section            |
| 1.4 | README.md     | 318–319 (optional)                       | Refine D8 wording in 8D Approach                 |
| 2.1 | CONTRIBUTING  | After 12                                 | Add source/origin to Submission Criteria         |
| 2.2 | CONTRIBUTING  | 35–38 (inside template)                  | Add “Source (if applicable)” to template         |
| 2.3 | CONTRIBUTING  | 69–77                                   | Add step 5 “Provide source/origin”, renumber 5–7 |
| 2.4 | CONTRIBUTING  | After 111                                | Add Attribution to Quality Standards             |
| 3   | CITATION.cff  | (new file)                               | Create CITATION.cff in repo root                 |

---

## Applying the edits

- **By hand:** Work through the OLD → NEW blocks in order. For README, do 1.1 → 1.2 → 1.3 (and 1.4 if desired). For CONTRIBUTING, do 2.1 → 2.2 → 2.3 → 2.4. Then create `CITATION.cff`.
- **With `patch`:** The unified-diff blocks are illustrative; line numbers can shift after earlier edits. Save each patch to a `.patch` file, apply one at a time, and fix offsets if needed.
- **Downstream:** If `releases/Awesome-Mnemonics-Complete-Guide.md`, `PRINT-QUICK-REFERENCE.md`, or release DOCX/PDF/RTF are generated from README or other sources, re-run the build and, if you change D8 (1.4), update any 8D mention there too.
