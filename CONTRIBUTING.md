# Contributing to Awesome Mnemonics

## Submission Criteria

All mnemonics must meet:

- ✅ **Provable/actionable** - Not just motivational, must have concrete steps
- ✅ **Cross-references** - Should link to related mnemonics where applicable
- ✅ **Real-world context** - Include actual usage examples
- ✅ **Memorable** - The acronym/pattern should be easy to recall under pressure
- ✅ **Source/origin (if known)** - For established frameworks, note the origin (e.g. "Ford 8D", "Toyota 5 Whys"). For original or curated mnemonics, write "Curated for this collection." Maintainers may classify entries in the [Sources & References](README.md#sources--references) section.

## Mnemonic Submission Template

Use this template when submitting a new mnemonic:

```markdown
### MNEMONIC_NAME
```
M - Meaning of first letter
N - Meaning of second letter
E - Meaning of third letter
...
```

**💡 When to use:**
- Specific situation or phase it addresses
- Time estimate if applicable

**⚠️ Common pitfalls:**
- **Pitfall name** - Explanation of the mistake and how to avoid it

**🔗 Combines well with:** [Related Mnemonic](#link) (why it works together)

**Source (if applicable):** Published framework or "Curated for this collection."

**📋 Real-world example:** *Brief scenario.*
```

*See [IDEA](README.md#idea) in README for a full example.*

## Submission Process

1. **Fork the repository**
2. **Add your mnemonic** to the appropriate section in `README.md`
3. **Update the Table of Contents** with your new entry
4. **Add cross-references** - Link your mnemonic in related "Combines well with" sections
5. **Provide source/origin** — Include origin for established frameworks so we can cite in [Sources & References](README.md#sources--references).
6. **Test your links** — Ensure anchor links work.
7. **Submit a PR** with: description, why it fits, real-world context.

## Section Guidelines

### 🧩 Problem Solving
Root causes, solutions. PREPARE, ICEBERG, 8D.

### 📊 Problem Analysis
Stakeholder roles, external pressures, scope. RACI, SWOT, PESTEL.

### ⚠️ Problem Resolution Threats
Blockers, resource constraints. DICE, FATE, PEST.

### 🧘 Stress & Resilience
Stress, resilience. STOP, PACE, CALM.

### 🗣️ Communication & Conflict
Calm in difficult conversations. BREATHE, PAUSE, WAIT.

### 🔧 Infrastructure & Systems Engineering
Infra, DevOps. TRACE, SCALE, DEBUG.

## Pipeline Contributions

For a new pipeline, include:

- **When to use** — scenario
- **Flow** — step-by-step
- **Why it works** — synergy
- **Time** — estimate

## Quality Standards

- **Clarity** — Unambiguous steps
- **Actionability** — Concrete actions, not just concepts
- **Completeness** — When to use, Pitfalls, Combines well with, Example
- **Consistency** — Match existing formatting
- **Attribution** — Sources for established frameworks (✓/⚠/ℹ in [Sources & References](README.md#sources--references))

## Mobile & Print

Keep descriptions concise (on-call = phones). Use `[STOP](#stop)`-style anchors. Mnemonic letters in triple-backtick blocks. High-priority items may go in `PRINT-QUICK-REFERENCE.md`.

## High-Value Contributions

- **Domain addenda** — [network-engineering](docs/network-engineering.md), [cloud-native](docs/cloud-native.md), [database-performance](docs/database-performance.md): BGP, K8s, service mesh, query/connection-pool content. Stubs in place; add via PR.
- **Field Reports** — [FIELD-REPORTS.md](docs/FIELD-REPORTS.md): incident write-ups with MTTR, what worked, improvements.

## Who Uses This?

Social proof helps adoption. Adding your org helps others.

Add your team to the "Who Uses This?" section in `README.md` via PR:

```markdown
- **[Org/Team](https://url)** — Brief description
```

*Only if you use these in production. Example: `**[Acme](https://acme.com)** — SRE uses STOP→TRACE→DEBUG daily`.*

## Questions?

Open an issue to discuss your mnemonic idea before submitting if you're unsure about:
- Which section it belongs in
- Whether it meets the criteria
- How to structure it

**Maintainers:** If you change `mnemonics-index.yaml`, update `mnemonic_cli/data/mnemonics_index.yaml` so the installed `mnemonic` command stays in sync.

Thank you for helping make this field guide more comprehensive!
