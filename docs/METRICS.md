# Metrics & Mnemonics

Map mnemonics and pipelines to incident and reliability metrics. Use this to justify adoption, set targets, and measure improvement.

---

## Pipeline → metric focus

| Pipeline | Primary metric | Secondary | Notes |
|----------|----------------|-----------|-------|
| **Crisis Response** (STOP → TRACE → DEBUG → 8D) | MTTR, TTA | MTTI | STOP reduces time-to-acknowledge; TRACE+DEBUG improve mean time to identify |
| **Rapid Triage** (IDEA → DICE → FATE) | TTA, decision latency | — | Fast triage and go/no-go |
| **Root Cause** (ICEBERG → 5 Whys → PADDER → RACI) | MTTI, recurrence | MTBF | Better root cause → fewer repeats; 8D D7 drives MTBF |
| **Conflict Resolution** (WAIT → BREATHE → PAUSE → RACI) | Escalation rate, resolution time | — | Less escalation, faster alignment |
| **Stress / Burnout** (PACE → ARIES → CALM → SHINE) | Burnout, sick leave, retention | — | Softer outcomes; track over quarters |

---

## Mnemonic → metric

| Mnemonic | Metric | How |
|----------|--------|-----|
| **STOP** | TTA (time-to-acknowledge) | Pause before acting; reduces panic-restarts and wrong service restarts |
| **TRACE** | MTTI (mean time to identify) | Structured diagnostics (ping, logs, config) speed up identification |
| **DEBUG** | MTTI | Define → Examine → Break down → Understand → Test reduces thrashing |
| **8D (D7)** | MTBF, recurrence | “Prevent recurrence” directly targets root cause and repeat incidents |
| **ICEBERG + 5 Whys** | Recurrence, MTTI | Deeper root cause → better fixes and fewer repeats |
| **IDEA** | TTA, MTTR (simple issues) | Quick path for simple problems avoids over-investment |
| **DICE / FATE** | Decision quality, rework | Fewer “no-go” projects that get started anyway |

---

## Definitions (brief)

- **TTA** – Time to acknowledge: from first alert/signal to first committed action (e.g. assignee, comm in channel).
- **MTTI** – Mean time to identify: from “we know something is wrong” to “we have root cause (or strong hypothesis).”
- **MTTR** – Mean time to resolve: from start of incident to restoration of service.
- **MTBF** – Mean time between failures: time between resolved incident and next related failure; improved by D7 and recurrence reduction.

---

## Using this in practice

1. **Baseline** – Measure TTA, MTTI, MTTR (and recurrence if possible) before standardizing on a pipeline.
2. **Target** – e.g. “STOP embedded in onboarding → TTA under 5 min for P1” or “8D D7 completed for P1 → recurrence under 5%.”
3. **Retros** – In post-mortems, note which mnemonics/pipelines were used and whether they helped (e.g. “TRACE cut MTTI; DEBUG’s U step was slow without a service map”).
4. **Field Reports** – Document real incidents in [Field Reports](FIELD-REPORTS.md) with metrics (anonymized) to refine this mapping.

---

*See also: [Proven Mnemonic Pipelines](https://github.com/StewAlexander-com/Awesome-Mnemonics#-proven-mnemonic-pipelines) and [Crisis Response Chain](https://github.com/StewAlexander-com/Awesome-Mnemonics#1-crisis-response-chain) in the main guide.*
