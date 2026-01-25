# Field Reports

Real incidents where these mnemonics helped (or didn’t). Use this format to share anonymized lessons and improve the guide.

---

## Why contribute

- **Validate** which pipelines work and where they fall short  
- **Improve** the guide and runbook with concrete feedback  
- **Speed up** adoption by showing realistic MTTR, MTTI, and “what I’d do differently”  
- **Evidence base:** Three field reports with MTTR would strengthen the guide for teams evaluating adoption.

---

## Template

Copy this block into a new section (or PR) and fill it in.

```markdown
## Incident: [Short title] (YYYY-MM-DD)

**Pipeline used:** e.g. STOP → TRACE → DEBUG → 8D

**MTTR:** e.g. 45 minutes (baseline for similar: ~2 hours)

**What worked:**
- [Mnemonic/step] — [concrete effect]

**What didn’t:**
- [Mnemonic/step] — [what was slow, unclear, or missing]

**Improvement:**
- [Change to runbook, tooling, or guide]

**Context (optional):** e.g. “Database connection pool exhaustion; team of 4; first time using the pipeline.”
```

---

## Examples (placeholder)

*Add your own via PR. These are illustrative only.*

### Incident: Database connection pool exhaustion (example) (2025-01-18)

**Pipeline used:** STOP → DEBUG → ICEBERG → 8D

**MTTR:** 45 minutes (baseline: ~2 hours)

**What worked:** STOP prevented a panic-restart of the wrong service. DEBUG’s “Define the problem” forced us to agree on symptoms before touching config.

**What didn’t:** DEBUG’s “Understand data flow” took too long without a pre-made service topology.

**Improvement:** Added a generated service map to the runbook and linked it from the DEBUG step.

---

### Incident: [Your incident title] (YYYY-MM-DD)

*Your report here. See [CONTRIBUTING](../CONTRIBUTING.md) for how to submit.*

---

## How to submit

1. PR adding a `### Incident: ...` section (or template edit).
2. No customer/PII; “Database,” “API,” “Cache” are fine.
3. Optional: team size, on-call setup, first vs. repeated use.

---

*[METRICS](METRICS.md) · [Crisis Response Chain](https://github.com/StewAlexander-com/Awesome-Mnemonics#1-crisis-response-chain) · [CONTRIBUTING](../CONTRIBUTING.md)*
