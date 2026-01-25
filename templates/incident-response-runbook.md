# Incident Response Runbook — STOP → TRACE → DEBUG → 8D

*Pre-filled from [Awesome Mnemonics](https://github.com/StewAlexander-com/Awesome-Mnemonics) Crisis Response Chain.  
Use for production outages, system failures, and critical incidents. Time: 1–4 hours depending on complexity.*

---

## 1. STOP (2–5 min)

*Step back before acting. Reduces panic and wrong moves.*

| Step | Done | Notes |
|------|------|-------|
| **S**tep back | ☐ | Pause before restarting or changing anything |
| **T**ake a deep breath | ☐ | Regulate reaction |
| **O**bserve what is happening | ☐ | Symptoms, scope, who is affected |
| **P**ull back and put things in perspective | ☐ | Severity, blast radius |

---

## 2. TRACE (network / system diagnostics)

*Gather evidence before debugging.*

| Step | Done | Notes |
|------|------|-------|
| **T**est connectivity | ☐ | ping, traceroute, health checks |
| **R**eview logs and metrics | ☐ | Errors, latency, saturation |
| **A**nalyze packet captures | ☐ | If needed |
| **C**heck configurations | ☐ | Recent changes, drift |
| **E**scalate with documented evidence | ☐ | Handoff notes |

---

## 3. DEBUG (define and analyze)

*Structure the analysis before fixing.*

| Step | Done | Notes |
|------|------|-------|
| **D**efine the problem | ☐ | What changed? What is actually broken? |
| **E**xamine error messages/logs | ☐ | Stack traces, messages |
| **B**reak down into components | ☐ | Service / host / network |
| **U**nderstand data flow | ☐ | Where it fails |
| **G**enerate hypothesis and test | ☐ | One change at a time |

---

## 4. 8D (formal resolution and prevention)

*After the immediate fix: document and prevent recurrence.*

| D | Step | Done | Notes |
|---|------|------|-------|
| D1 | Team / form | ☐ | Who is on the response and follow-up |
| D2 | Describe the problem | ☐ | Use TRACE/DEBUG output |
| D3 | Containment | ☐ | Interim mitigations |
| D4 | Root cause | ☐ | 5 Whys or ICEBERG if needed |
| D5 | Choose corrections | ☐ | Permanent fix options |
| D6 | Implement | ☐ | Deploy and verify |
| D7 | Prevent recurrence | ☐ | Config, monitoring, training |
| D8 | Congratulate the team | ☐ | Close the loop |

---

## Incident metadata

| Field | Value |
|-------|-------|
| **Started** |  |
| **Acknowledged** |  |
| **Resolved** |  |
| **Pipeline used** | STOP → TRACE → DEBUG → 8D |
| **Root cause (D4)** |  |
| **Prevention (D7)** |  |

---

*For more pipelines (conflict, root cause, stress, triage), see the [Proven Mnemonic Pipelines](https://github.com/StewAlexander-com/Awesome-Mnemonics#-proven-mnemonic-pipelines) section of Awesome Mnemonics.*
