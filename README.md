# Awesome Mnemonics [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/StewAlexander-com/Awesome-Mnemonics/graphs/commit-activity)

> 🧠 A comprehensive field guide to memorable acronyms and mnemonics for problem-solving, stress management, and technical troubleshooting

**Note:** Unlike traditional Awesome lists, this guide includes full mnemonic definitions, cross-references, usage guidance, and real-world examples for immediate practical use. Each mnemonic is self-contained with embedded content rather than external links.

**Why this format?** Engineers facing production outages or high-pressure situations need immediate reference material, not another click to external resources. This guide prioritizes utility over format conformance, serving as a practical field guide you can reference during actual work.

Mnemonics are memory aids that encode complex workflows into easy-to-remember acronyms. This guide focuses on practical, field-tested mnemonics used by engineers, DevOps professionals, and technical managers to navigate high-pressure situations systematically.

## ⚡ Quick Reference

| **Situation** | **Use This** | **Time Needed** |
|---------------|--------------|-----------------|
| 🚨 Immediate crisis | [IDEA](#idea) → [STOP](#stop) | 2-5 min |
| 🔍 Root cause needed | [ICEBERG](#iceberg) + [5 Whys](#5-whys) | 30-60 min |
| 👥 Team conflict | [BREATHE](#breathe) → [PAUSE](#pause) → [WAIT](#wait) | 5-10 min |
| 📊 Strategic planning | [PREPARE](#prepare) + [SWOT](#swot) | 1-2 hours |
| 🏗️ System design | [SCALE](#scale-infrastructure-design) + [PESTEL](#pestel) | Planning phase |
| 🐛 Technical debugging | [TRACE](#trace-network-troubleshooting) → [DEBUG](#debug-code--system-analysis) | Variable |
| 😰 Stress overload | [PACE](#pace) → [ARIES](#aries) → [CALM](#calm) | 10-15 min |

## 🔄 Mnemonic Selection Flowchart

```
                    ┌─────────────┐
                    │  Problem?   │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
         ┌────▼───┐   ┌────▼───┐   ┌────▼────┐
         │ Quick? │   │Complex?│   │ Stress? │
         └────┬───┘   └────┬───┘   └────┬────┘
              │            │            │
         ┌────▼────┐  ┌────▼─────┐  ┌───▼────┐
         │  IDEA   │  │PREPARE/  │  │ STOP → │
         │    +    │  │ICEBERG+  │  │ PACE   │
         │  STOP   │  │ 5 Whys   │  └────────┘
         └─────────┘  └──────────┘
```

## Table of Contents
  
- [Awesome Mnemonics ](#awesome-mnemonics-)
  - [⚡ Quick Reference](#-quick-reference)
  - [🔄 Mnemonic Selection Flowchart](#-mnemonic-selection-flowchart)
  - [Table of Contents](#table-of-contents)
  - [🧩 Problem Solving Techniques](#-problem-solving-techniques)
    - [PREPARE](#prepare)
    - [PADDER](#padder)
    - [ICEBERG](#iceberg)
    - [IDEA](#idea)
    - [5 Whys](#5-whys)
    - [8D Approach](#8d-approach)
    - [5Ps](#5ps)
  - [📊 Problem Analysis](#-problem-analysis)
    - [RACI](#raci)
    - [PESTEL](#pestel)
    - [SWOT](#swot)
    - [SET (Systems Engineering Triangle)](#set-systems-engineering-triangle)
  - [⚠️ Problem Resolution Threats](#️-problem-resolution-threats)
    - [DICE](#dice)
    - [FATE](#fate)
    - [PEST](#pest)
  - [💪 Positivity \& Resilience](#-positivity--resilience)
    - [PUSH](#push)
    - [HOPE](#hope)
    - [SHINE](#shine)
  - [🗣️ Argumentation \& Communication](#️-argumentation--communication)
    - [BREATHE](#breathe)
    - [PAUSE](#pause)
    - [WAIT](#wait)
  - [🧘 Combating Stress](#-combating-stress)
    - [PACE](#pace)
    - [STOP](#stop)
    - [ARIES](#aries)
    - [HELP](#help)
    - [HANDLE](#handle)
    - [CALM](#calm)
  - [🔧 Infrastructure \& Systems Engineering](#-infrastructure--systems-engineering)
    - [TRACE (Network Troubleshooting)](#trace-network-troubleshooting)
    - [SCALE (Infrastructure Design)](#scale-infrastructure-design)
    - [DEBUG (Code \& System Analysis)](#debug-code--system-analysis)
  - [🔗 Proven Mnemonic Pipelines](#-proven-mnemonic-pipelines)
    - [**1. CRISIS RESPONSE CHAIN**](#1-crisis-response-chain)
    - [**2. CONFLICT RESOLUTION CHAIN**](#2-conflict-resolution-chain)
    - [**3. ROOT CAUSE INVESTIGATION CHAIN**](#3-root-cause-investigation-chain)
    - [**4. STRATEGIC DESIGN CHAIN**](#4-strategic-design-chain)
    - [**5. STRESS BURNOUT RECOVERY CHAIN**](#5-stress-burnout-recovery-chain)
    - [**6. RAPID TRIAGE CHAIN**](#6-rapid-triage-chain)
  - [📊 Pipeline Selection Matrix](#-pipeline-selection-matrix)
  - [💡 Pro Tips for Using Pipelines](#-pro-tips-for-using-pipelines)
  - [🎯 Common Mistakes to Avoid](#-common-mistakes-to-avoid)
  - [🤝 Contributing](#-contributing)

- - - - 

## 🧩 Problem Solving Techniques

*Start here for systematic approaches to complex problems*

- - - -
### PREPARE  
```
P - Prioritize the problem  
R - Research & brainstorm solutions  
E - Evaluate available options  
P - Plan steps to resolve issue  
A - Act on the plan  
R - Reflect on results  
E - Evaluate and revise plan as necessary  
```

**💡 When to use:**
- Strategic planning sessions (1-2 hours)
- Medium complexity problems with multiple stakeholders
- When you need structured documentation

**⚠️ Common pitfalls:**
- **Analysis paralysis** - Spending 2 hours planning a 10-minute problem. If you're past 30 minutes on "Research", switch to [IDEA](#idea).
- **Skipping reflection** - Acting without the final "Reflect/Evaluate" creates recurring issues. Always close the loop.
- **Wrong tool for crisis** - Don't PREPARE during a production outage. Use [STOP](#stop) → [TRACE](#trace-network-troubleshooting) → [DEBUG](#debug-code--system-analysis) first, [PREPARE](#prepare) during post-mortem.

**🔗 Combines well with:** [RACI](#raci) (assign responsibilities), [SWOT](#swot) (evaluate options), [ICEBERG](#iceberg) (if reflection reveals deeper issues)

**📋 Real-world example:** *Planning infrastructure migration - Use [PREPARE](#prepare) to structure approach, [RACI](#raci) during planning phase for role clarity, [SWOT](#swot) to evaluate cloud provider options*
### PADDER
```
P - Pinpoint problem  
A - Analyze data and look for patterns  
D - Develop solution & consider other ways to solve the issue - try to have more than one   
D - Design action plan  
E - Execute action plan & Monitor Results  
R - Reevaluate and refine plan as needed  
```

**💡 When to use:**
- Data-driven problem solving
- When patterns need to be identified
- Pairs with [8D Approach](#8d-approach)'s D3 (Interim Containment) for quick fixes

**🔗 Combines well with:** [IDEA](#idea) (simpler version), [8D Approach](#8d-approach) (formal resolution)

**📋 Real-world example:** *Recurring server crashes - Pinpoint timing, Analyze logs for patterns, Develop interim solutions (restart service) + permanent fix (increase memory), Monitor effectiveness*
### ICEBERG
```
I - Identify issue(s)  
C - Collect data and analyze situation  
E - Examine possible (root) causes  
B - Brainstorms solutions  
E - Execute solution(s)  
R - Review, evaluate, and adjust solutions  
G - Gather feedback  
```

**💡 When to use:**
- Complex problems requiring deep analysis (30-60 min)
- When surface symptoms hide deeper root causes
- Escalate from [IDEA](#idea) when complexity increases

**⚠️ Common pitfalls:**
- **Going too deep on simple problems** - Using ICEBERG for a 5-minute password reset. Start with [IDEA](#idea), escalate only if complexity emerges.
- **Skipping feedback (G)** - Gathering feedback seems optional but prevents recurrence. Always complete the full cycle.

**🔗 Combines well with:** [5 Whys](#5-whys) (deeper root cause), [8D Approach](#8d-approach) (formal prevention), [IDEA](#idea) (start simple, escalate if needed)

**📋 Real-world example:** *Network performance degradation - Identify slowness, Collect metrics (latency, packet loss), Examine causes (routing changes, bandwidth saturation), Brainstorm solutions, Execute, Review with team, Gather feedback from users*
### IDEA
``` 
I - Identify problem  
D - Develop Solution  
E - Execute Solution   
A - Assess Solution  
```

**💡 When to use:**
- Quick, simple problems (2-5 minutes)
- Crisis situations requiring immediate action
- Use [STOP](#stop) first if under stress

**⚠️ Common pitfalls:**
- **Escalation failure** - Not moving to [ICEBERG](#iceberg) or [PREPARE](#prepare) when problem reveals complexity. If you're past 10 minutes or hitting multiple blockers, escalate.
- **Skipping assessment** - Executing without validating the solution worked. The "A" step prevents recurring issues.

**🔗 Combines well with:** [STOP](#stop) (crisis stress management), [PREPARE](#prepare)/[ICEBERG](#iceberg) (escalation path for complex issues)

**📋 Real-world example:** *User can't access VPN - Identify (connection error), Develop (reset credentials), Execute (send new password), Assess (confirm access restored)*
### 5 Whys
* Keep asking why till root causes are identified

**💡 When to use:**
- Essential for root cause analysis
- During [8D Approach](#8d-approach)'s D4 (Root Cause Analysis)
- Combine with [ICEBERG](#iceberg) for systematic deep dives

**⚠️ Common pitfalls:**
- **Stopping at symptoms** - Stopping at "Why #3: Database slow" instead of drilling to root cause (missing migration). Keep asking until you reach a process/systemic failure.
- **Assuming single root cause** - Complex problems often have multiple root causes. Use 5 Whys for each branch.

**🔗 Combines well with:** [ICEBERG](#iceberg) (structured approach), [8D Approach](#8d-approach) (formal incident management)

**📋 Real-world example:** *Deployment failures - Why? Pipeline failed. Why? Tests timed out. Why? Database slow. Why? Index missing. Why? Schema change didn't include migration. Root cause: Missing migration validation step*

### 8D Approach
*Industry standard in automotive/manufacturing, adapted for IT incident management*
```
D1 - Form a team  
D2 - Describe the problem  
D3 - Interim Containment Action (the "band-aid")  
D4 - Root Cause Analysis & Escape Point(s)  
D5 - Permanent Corrective Actions  
D6 - Implement & Validate Corrective Actions  
D7 - Prevent reoccurrence(s)  
D8 - Closure & Celebration  
```

**💡 When to use:**
- Critical incidents requiring formal resolution
- Problems needing documentation and prevention
- When team coordination is essential (D1: use [RACI](#raci))

**⚠️ Common pitfalls:**
- **Stopping at D3** - Implementing the band-aid but never reaching D7 (Prevent Reoccurrence) means it will happen again.
- **Solo 8D** - Trying to do all 8 steps alone instead of D1 (Form a team). Use [RACI](#raci) during D1 to clarify roles.
- **Bureaucracy creep** - Over-formalizing 8D for simple problems. Use [IDEA](#idea) or [PREPARE](#prepare) for non-critical issues.

**🔗 Combines well with:** [PADDER](#padder) (D3 interim fixes), [5 Whys](#5-whys) + [ICEBERG](#iceberg) (D4 root cause), [RACI](#raci) (D1 team formation)

**📋 Real-world example:** *Data breach incident - Form security response team ([RACI](#raci) roles), Describe scope, Contain (disable compromised accounts), Analyze root cause ([5 Whys](#5-whys): phishing → no MFA → insufficient training), Implement MFA, Validate with penetration test, Prevent (mandatory security awareness), Celebrate team response*

### 5Ps
* Poor planning produces pitiful products  

- - - -

## 📊 Problem Analysis

*Frameworks for understanding scope and impact*

- - - - 
### RACI 
* Used to identify the roles and responsibilities of different stakeholders in a problem-solving process
```
R - Responsible (does the work)
A - Accountable (final approval)
C - Consulted (provides input)
I - Informed (kept updated)
```

**💡 When to use:**
- Resolving role confusion in teams
- [8D Approach](#8d-approach)'s D1 (Form a team) step
- End of [WAIT](#wait) → [BREATHE](#breathe) → [PAUSE](#pause) chain for conflict resolution

**⚠️ Common pitfalls:**
- **Multiple Accountables** - More than one "A" creates confusion. There should be exactly one Accountable person per task.
- **Too many Consulted** - Adding everyone as "C" slows decisions. Be selective - only include those with critical input.

**📋 Real-world example:** *Infrastructure upgrade project - Responsible: DevOps engineers, Accountable: Infrastructure Manager, Consulted: Security team, Informed: All developers*
### PESTEL 
* Used to identify and analyze the external factors that may impact a problem or decision

```
P - Political
E - Economic
S - Sociocultural
T - Technological
E - Environmental
L - Legal
```

**💡 When to use:**
- Strategic planning external factor analysis
- [SCALE](#scale-infrastructure-design) infrastructure design validation
- Architecture reviews considering compliance/regulations

**📋 Real-world example:** *Cloud migration planning - Political (vendor lock-in concerns), Economic (cost optimization), Technological (API compatibility), Legal (data sovereignty requirements)*

### SWOT
* Used to identify and analyze the internal and external factors that may impact a problem or decision

```
S - Strengths
W - Weaknesses
O - Opportunities
T - Threats
```

**💡 When to use:**
- [PREPARE](#prepare)'s "Evaluate options" step
- [SCALE](#scale-infrastructure-design) design validation
- Strategic decision making (1-2 hours)

**📋 Real-world example:** *Choosing deployment strategy - Strengths: automated rollback, Weaknesses: longer deployment time, Opportunities: canary testing, Threats: increased complexity*
### SET (Systems Engineering Triangle)
* Also called "Project Management Triangle" or "Iron Triangle"
```
1. Draw a triangle
2. Put one of these 3 words at each corner: "good", "fast", "cheap"
3. Pick 2 of them
4. The other word is what the solution will not likely be
   - A fast, cheap solution will not likely be good
   - A fast and good solution will not likely be cheap 
   - A good and cheap solution will not likely be fast
```

**💡 When to use:**
- Setting stakeholder expectations
- End of [SCALE](#scale-infrastructure-design) → [SWOT](#swot) → [PESTEL](#pestel) chain
- Architecture trade-off discussions

**📋 Real-world example:** *Urgent security patch needed - Choose: Good + Fast = Not Cheap (overtime, additional resources). Manage expectations with leadership accordingly*

*From the [SeBok - Systems Engineering Body of Knowledge](https://www.sebokwiki.org/wiki/Guide_to_the_Systems_Engineering_Body_of_Knowledge_(SEBoK))*




- - - -

## ⚠️ Problem Resolution Threats

*Identify blockers before they derail your solution*

- - - -

### DICE

```
D - Delay
I - Incompetence
C - Conflict
E - External factors
```

**💡 When to use:**
- Part of [IDEA](#idea) → [DICE](#dice) → [FATE](#fate) rapid triage chain
- Identifying blockers before execution
- Risk assessment in [PREPARE](#prepare) phase

### FATE
```
F - Funding
A - Allocation of resources 
T - Time
E - Expertise
```

**💡 When to use:**
- Resource validation in rapid triage
- Feasibility assessment (10-30 min)
- After [DICE](#dice) to validate resource availability
### PEST
```
P - Political
E - Economic
S - Social
T - Technological
```

**💡 When to use:**
- Identifying external threats to solutions
- Consider ways to combat/remove these threats

- - - -

## 💪 Positivity & Resilience

*Mental frameworks for maintaining momentum*

- - - -
### PUSH
```
P - Practice Gratitude   
U - Use positive affirmations  
S - Spend time with positive people  
H - Have a positive outlook  
```
### HOPE
```
H - Harness positive thoughts  
O - Open up to others   
P - Prioritize self-care  
E - Exercise regularly  
```
### SHINE
```
S - Stay present, in the moment  
H - Have a healthy positive perspective  
I - Identify and do positive activities   
N - Nourish positive relationships  
E - Express yourself  
```

**💡 When to use:**
- End of [PACE](#pace) → [ARIES](#aries) → [CALM](#calm) → [SHINE](#shine) burnout recovery chain
- Ongoing practice for sustainable positivity
- Connects to [CALM](#calm) for building positive self-image
- - - -

## 🗣️ Argumentation & Communication

*Stay calm and productive during difficult conversations*

- - - -
### BREATHE 
```
B - Breathe deeply and slowly   
R - Remain rational and listen  
E - Empathize with the other person's problem
A - Ask questions to understand  
T - Take a break if needed  
H - Hold back from reacting  
E - Express yourself calmly  
```

**💡 When to use:**
- First step when tensions rise (breathing regulates emotions)
- Part of [WAIT](#wait) → [BREATHE](#breathe) → [PAUSE](#pause) → [RACI](#raci) conflict resolution chain
- If break needed, escalate to PAUSE

**⚠️ Common pitfalls:**
- **Fake composure** - Going through motions without actually regulating emotions. The breathing must be intentional and deep.
- **Weaponizing calm** - Using "Let's BREATHE" dismissively to avoid addressing concerns. This damages trust - use it genuinely.

**🔗 Combines well with:** [WAIT](#wait) (listen first), [PAUSE](#pause) (step away if needed), [STOP](#stop) (stress management)

**📋 Real-world example:** *Stakeholder disagrees with technical approach in meeting - Breathe deeply (regulate emotions), Remain rational, Empathize with their concerns, Ask clarifying questions, Take 5-minute break if tension escalates, Hold back defensive reactions, Express technical rationale calmly*
### PAUSE
```
P - Put things in perspective   
A - Acknowledge your feelings and theirs
U - Understand that you don't have to act/react right away  
S - Step Away from the situation  
E - Evaluate options and plan before acting   
```

**💡 When to use:**
- When BREATHE isn't enough - need physical separation
- "Step Away" connects to WAIT philosophy
- Combine with STOP for immediate stress de-escalation (5-20 min)

**🔗 Combines well with:** [BREATHE](#breathe) (first step), [WAIT](#wait) (listen before speaking), [STOP](#stop) (stress response)

**📋 Real-world example:** *Heated debate about architecture decision - Put in perspective (not life-or-death), Acknowledge both viewpoints have merit, Don't decide now, Step away for lunch break, Evaluate pros/cons offline, Return with structured comparison*

### WAIT
* "Why am I troubled / talking?"  
* Not all things need an answer or response; don't seek trouble and don't answer negativity negatively

**💡 When to use:**
- Ask yourself before speaking - often listening is better
- First step in WAIT → BREATHE → PAUSE → RACI chain
- Use BREATHE first to regulate, then WAIT to choose response

**⚠️ Common pitfalls:**
- **Passive-aggressive silence** - Using WAIT to avoid necessary communication. This isn't "don't respond" - it's "choose the right response."
- **Escalation avoidance** - Not speaking up when issues need addressing. WAIT helps you respond effectively, not disappear.

**🔗 Combines well with:** [BREATHE](#breathe) (emotional regulation), [PAUSE](#pause) (step away technique)

**📋 Real-world example:** *Email with accusatory tone arrives - Ask "Why am I troubled?" (ego/defensiveness), "Why am I talking?" (to defend or to resolve?), Choose not to respond immediately, Use BREATHE + PAUSE, Respond later with facts, not emotion* 

- - - -

## 🧘 Combating Stress

*Immediate and long-term stress management tools*

- - - -

### PACE  
```
P - Physical activity
A - Avoiding unhealthy behaviors
C - Coping skills
E - Emotional awareness
```

**💡 When to use:**
- First step in PACE → ARIES → CALM → SHINE burnout recovery chain
- Immediate stress management actions

### STOP
```
S - Step back
T - Take a deep breath
O - Observe what is happening
P - Pull back and put things in perspective
```

**💡 When to use:**
- First response to ANY crisis - immediate stress management (2-5 min)
- Start of [STOP](#stop) → [TRACE](#trace-network-troubleshooting) → [DEBUG](#debug-code--system-analysis) → [8D](#8d-approach) crisis response chain
- Use with IDEA for quick problem resolution in crisis

**⚠️ Common pitfalls:**
- **Going through motions** - Rushing through STOP without actually calming. The "Take a deep breath" must be intentional - pause for 3-5 seconds.
- **Stopping at STOP** - Using STOP but not proceeding to next step (TRACE/IDEA). STOP is the foundation, not the solution.

**🔗 Combines well with:** [BREATHE](#breathe) + [PAUSE](#pause) (breathing techniques), [IDEA](#idea) (quick problem solving)

**📋 Real-world example:** *Production alert at 2 AM - Step back (don't panic), Take deep breath (reduce adrenaline), Observe (read alert details), Pull back perspective (assess severity before waking team), Then proceed to TRACE for diagnostics*

### ARIES
```
A - Avoid unnecessary stress
R - Relax and take breaks
I - Incorporate physical activity into your routine
E - Eat a healthy diet
S - Sleep well
```

**💡 When to use:**
- Lifestyle changes in PACE → ARIES → CALM chain
- Long-term stress reduction (2-4 weeks)

### HELP
* This mnemonic can help you remember four ways to manage stress: 
```
H - Handle problems one at a time
E - Exercise regularly
L - Learn to relax
P - Pace yourself and set limits.
```

### HANDLE
- This mnemonic can help you remember six stress-management strategies: 
```
H - Have a positive attitude
A - Avoid unnecessary stress
N - Nurture a strong support system
D - Deal with problems directly 
L - Learn to relax, 
E - Exercise regularly
```

### CALM
```
C - Confidence: Believe in your abilities and strengths
A - Awareness: Stay conscious of your thoughts and feelings
L - Logic: Use rational thinking to overcome doubts
M - Mindfulness: Practice being present and focused
```

**💡 When to use:**
- Builds long-term resilience and confidence
- Confidence connects to HOPE and SHINE (both build positive self-image)
- Use after PACE or ARIES for comprehensive stress management

**🔗 Combines well with:** Positivity ([HOPE](#hope), [SHINE](#shine)), Stress Management ([PACE](#pace), [ARIES](#aries))

- - - -

## 🔧 Infrastructure & Systems Engineering

*Technical mnemonics for infrastructure and DevOps work*

- - - -

### TRACE (Network Troubleshooting)
```
T - Test connectivity (ping, traceroute)
R - Review logs and metrics
A - Analyze packet captures
C - Check configurations
E - Escalate with documented evidence
```

**💡 When to use:**
- Use with [PREPARE](#prepare) and [8D Approach](#8d-approach) for systematic resolution
- Start with T (Test) for quick diagnostics, escalate to A (Analyze) for deep dives
- Document findings at each step for [8D Approach](#8d-approach)'s D2 (Describe the problem)

**🔗 Combines well with:** Problem Solving ([PREPARE](#prepare), [8D Approach](#8d-approach))

### SCALE (Infrastructure Design)
```
S - Security by design
C - Capacity planning
A - Automation-first
L - Load balancing
E - Error handling/resilience
```

**💡 When to use:**
- Use [SWOT](#swot) analysis alongside for design validation
- Apply [PESTEL](#pestel) to evaluate external factors affecting infrastructure
- Consider [SET](#set-systems-engineering-triangle) Triangle trade-offs (fast/cheap/good) for each component

**🔗 Combines well with:** Problem Analysis ([SWOT](#swot), [PESTEL](#pestel), [SET](#set-systems-engineering-triangle))

### DEBUG (Code & System Analysis)
```
D - Define the problem (what changed?)
E - Examine error messages/logs
B - Break down into components
U - Understand data flow
G - Generate hypothesis and test
```

**💡 When to use:**
- Combines [5 Whys](#5-whys) questioning with [ICEBERG](#iceberg)'s systematic approach
- Start with D (Define) - often the problem is unclear or misstated
- Use with [TRACE](#trace-network-troubleshooting) for network/system issues

**🔗 Combines well with:** Problem Solving ([5 Whys](#5-whys), [ICEBERG](#iceberg)), Infrastructure ([TRACE](#trace-network-troubleshooting))

- - - -

## 🔗 Proven Mnemonic Pipelines

*When certain mnemonics are combined in sequence, they create powerful workflows that amplify effectiveness. These chains are battle-tested for specific high-pressure scenarios.*

---

### **1. CRISIS RESPONSE CHAIN**
**STOP → TRACE → DEBUG → 8D**

**When to use:** Production outages, system failures, critical incidents

**The Flow:**
```
S - Step back (STOP)
T - Take a deep breath (STOP)
O - Observe what is happening (STOP)
P - Pull back and put things in perspective (STOP)
    ↓
T - Test connectivity (TRACE)
R - Review logs and metrics (TRACE)
A - Analyze packet captures (TRACE)
C - Check configurations (TRACE)
E - Escalate with documented evidence (TRACE)
    ↓
D - Define the problem (DEBUG)
E - Examine error messages/logs (DEBUG)
B - Break down into components (DEBUG)
U - Understand data flow (DEBUG)
G - Generate hypothesis and test (DEBUG)
    ↓
D1-D8 - Full 8D resolution cycle (8D Approach)
```

**Why it works:** STOP stabilizes you emotionally, TRACE gives you diagnostic data, DEBUG structures your analysis, 8D ensures you prevent recurrence.

**Time investment:** 1-4 hours (depending on complexity)

---

### **2. CONFLICT RESOLUTION CHAIN**
**WAIT → BREATHE → PAUSE → RACI**

**When to use:** Team disagreements, tense meetings, stakeholder conflicts

**The Flow:**
```
W - "Why am I talking?" (WAIT - listen first)
    ↓
B - Breathe deeply and slowly (BREATHE)
R - Remain rational and listen (BREATHE)
E - Empathize with the other person's problem (BREATHE)
A - Ask questions to understand (BREATHE)
    ↓
P - Put things in perspective (PAUSE)
A - Acknowledge your feelings and theirs (PAUSE)
U - Understand you don't have to react immediately (PAUSE)
S - Step Away from the situation (PAUSE)
E - Evaluate options and plan (PAUSE)
    ↓
R - Responsible (RACI - clarify roles)
A - Accountable (RACI)
C - Consulted (RACI)
I - Informed (RACI)
```

**Why it works:** WAIT prevents escalation, BREATHE regulates emotions, PAUSE creates space for rational thought, RACI resolves role confusion (often the root cause).

**Time investment:** 5-20 minutes

---

### **3. ROOT CAUSE INVESTIGATION CHAIN**
**ICEBERG → 5 Whys → PADDER → RACI**

**When to use:** Recurring issues, complex system problems, post-incident analysis

**The Flow:**
```
I - Identify issue(s) (ICEBERG)
C - Collect data and analyze situation (ICEBERG)
E - Examine possible root causes (ICEBERG)
    ↓
Why #1 → Why #2 → Why #3 → Why #4 → Why #5 (5 Whys)
    ↓
D - Develop solution (PADDER)
D - Design action plan (PADDER)
E - Execute action plan & Monitor (PADDER)
R - Reevaluate and refine (PADDER)
    ↓
R/A/C/I - Assign responsibilities (RACI)
```

**Why it works:** ICEBERG provides structure, 5 Whys drills to root cause, PADDER creates action plan, RACI ensures accountability.

**Time investment:** 1-2 hours

---

### **4. STRATEGIC DESIGN CHAIN**
**SCALE → SWOT → PESTEL → SET**

**When to use:** Infrastructure planning, architecture reviews, capacity planning

**The Flow:**
```
S - Security by design (SCALE)
C - Capacity planning (SCALE)
A - Automation-first (SCALE)
L - Load balancing (SCALE)
E - Error handling/resilience (SCALE)
    ↓
S - Strengths (SWOT - evaluate design)
W - Weaknesses (SWOT)
O - Opportunities (SWOT)
T - Threats (SWOT)
    ↓
P - Political (PESTEL - external factors)
E - Economic (PESTEL)
S - Sociocultural (PESTEL)
T - Technological (PESTEL)
E - Environmental (PESTEL)
L - Legal (PESTEL)
    ↓
Pick 2: Good / Fast / Cheap (SET Triangle - set expectations)
```

**Why it works:** SCALE sets technical requirements, SWOT evaluates approach, PESTEL identifies external risks, SET manages stakeholder expectations.

**Time investment:** 2-4 hours (planning phase)

---

### **5. STRESS BURNOUT RECOVERY CHAIN**
**PACE → ARIES → CALM → SHINE**

**When to use:** Long-term stress, approaching burnout, need for lifestyle reset

**The Flow:**
```
P - Physical activity (PACE - immediate actions)
A - Avoiding unhealthy behaviors (PACE)
C - Coping skills (PACE)
E - Emotional awareness (PACE)
    ↓
A - Avoid unnecessary stress (ARIES - lifestyle changes)
R - Relax and take breaks (ARIES)
I - Incorporate physical activity (ARIES)
E - Eat a healthy diet (ARIES)
S - Sleep well (ARIES)
    ↓
C - Confidence (CALM - mental framework)
A - Awareness (CALM)
L - Logic (CALM)
M - Mindfulness (CALM)
    ↓
S - Stay present (SHINE - ongoing practice)
H - Have healthy perspective (SHINE)
I - Identify positive activities (SHINE)
N - Nourish relationships (SHINE)
E - Express yourself (SHINE)
```

**Why it works:** PACE handles immediate stress, ARIES addresses root lifestyle causes, CALM builds mental resilience, SHINE creates sustainable positivity.

**Time investment:** Ongoing (2-4 weeks for habit formation)

---

### **6. RAPID TRIAGE CHAIN**
**IDEA → DICE → FATE**

**When to use:** Quick wins needed, time-critical decisions, assessing feasibility

**The Flow:**
```
I - Identify problem (IDEA)
D - Develop Solution (IDEA)
E - Execute Solution (IDEA)
A - Assess Solution (IDEA)
    ↓
D - Delay (DICE - check for blockers)
I - Incompetence (DICE)
C - Conflict (DICE)
E - External factors (DICE)
    ↓
F - Funding (FATE - resource check)
A - Allocation of resources (FATE)
T - Time (FATE)
E - Expertise (FATE)
```

**Why it works:** IDEA provides fast framework, DICE identifies blockers, FATE validates resource availability.

**Time investment:** 10-30 minutes

---

## 📊 Pipeline Selection Matrix

| **Your Situation** | **Pipeline** | **Key Benefit** |
|-------------------|-------------|-----------------|
| 🚨 System down NOW | [STOP](#stop) → [TRACE](#trace-network-troubleshooting) → [DEBUG](#debug-code--system-analysis) → [8D](#8d-approach) | Systematic crisis response |
| 😤 Team conflict escalating | [WAIT](#wait) → [BREATHE](#breathe) → [PAUSE](#pause) → [RACI](#raci) | De-escalation + role clarity |
| 🔁 Same issue keeps happening | [ICEBERG](#iceberg) → [5 Whys](#5-whys) → [PADDER](#padder) → [RACI](#raci) | Deep root cause + prevention |
| 🏗️ Designing new infrastructure | [SCALE](#scale-infrastructure-design) → [SWOT](#swot) → [PESTEL](#pestel) → [SET](#set-systems-engineering-triangle) | Complete planning framework |
| 😰 Feeling burned out | [PACE](#pace) → [ARIES](#aries) → [CALM](#calm) → [SHINE](#shine) | Comprehensive stress recovery |
| ⚡ Need quick decision | [IDEA](#idea) → [DICE](#dice) → [FATE](#fate) | Fast feasibility assessment |

---

## 💡 Pro Tips for Using Pipelines

1. **Don't skip steps** - Each mnemonic builds on the previous one
2. **Document at each stage** - Your [STOP](#stop) insights inform [TRACE](#trace-network-troubleshooting), [TRACE](#trace-network-troubleshooting) data feeds [DEBUG](#debug-code--system-analysis), etc.
3. **Know when to branch** - If [IDEA](#idea) reveals complexity, switch to [ICEBERG](#iceberg) → [5 Whys](#5-whys)
4. **Combine with stress tools** - Always start with [STOP](#stop) if you're emotionally activated
5. **Teach your team** - Shared vocabulary accelerates collaboration

---

## 🎯 Common Mistakes to Avoid

❌ **Jumping to solutions** - Skipping [STOP](#stop) or [WAIT](#wait) when stressed leads to poor decisions
❌ **Using wrong pipeline** - [IDEA](#idea) won't solve systemic issues needing [ICEBERG](#iceberg) → [5 Whys](#5-whys)
❌ **Incomplete execution** - Starting [8D Approach](#8d-approach) but not reaching D7 (Prevent Reoccurrence) means it will happen again
❌ **Solo hero mode** - Forgetting [RACI](#raci) means no accountability when you're not available
❌ **Analysis paralysis** - [PREPARE](#prepare) → [ICEBERG](#iceberg) → [5 Whys](#5-whys) → [8D](#8d-approach) is overkill for simple problems

- - - -

**[↑ Back to Quick Reference](#-quick-reference)** | **[↑ Back to Top](#awesome-mnemonics-)**

## 🤝 Contributing

Got a mnemonic that's saved you countless times? **Share it!**

**Submission criteria:**
- ✅ Must be provable/actionable (not just motivational)
- ✅ Should cross-reference existing mnemonics where applicable
- ✅ Include real-world usage context
- ✅ Keep it memorable (that's the point!)

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.
