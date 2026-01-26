# Real-World Scenarios & Decision Tree

**Quick navigation:** [Role-Based Quick Start](#role-based-quick-start) | [Decision Tree](#which-framework-should-i-use) | [Scenarios](#scenarios) | [Framework Interdependencies](#framework-interdependencies)

---

## Role-Based Quick Start

Choose your role to jump to the most relevant scenario:

- **[IT/SRE Engineer](#scenario-1-it-incident-response-mttr-focus)** — Production incidents, MTTR focus, systematic troubleshooting
- **[Project Manager](#scenario-3-project-timeline-slippage)** — Timeline slippage, resource constraints, stakeholder management
- **[Security Professional](#scenario-2-cybersecurity-risk-assessment)** — Risk assessment, threat analysis, compliance
- **[Student/Learner](#scenario-5-learning-from-failures)** — Understanding frameworks, applying to case studies
- **[Personal/Stress Management](#scenario-4-conflict-resolution)** — Team conflicts, stress management, burnout recovery

---

## Which Framework Should I Use?

**Answer 6 questions to find your path:**

```
1. Is this a crisis/emergency? (System down, security breach, etc.)
   ├─ YES → Go to Question 2
   └─ NO → Go to Question 3

2. Is the problem simple or complex?
   ├─ Simple (2-5 min fix) → Use [IDEA](#idea) + [STOP](#stop)
   └─ Complex (needs investigation) → Use [STOP](#stop) → [TRACE](#trace-network-troubleshooting) → [DEBUG](#debug-code--system-analysis) → [8D](#8d-approach)

3. Is this a recurring problem?
   ├─ YES → Use [ICEBERG](#iceberg) → [5 Whys](#5-whys) → [PADDER](#padder) → [RACI](#raci)
   └─ NO → Go to Question 4

4. Is this about team conflict or stress?
   ├─ YES → Use [WAIT](#wait) → [BREATHE](#breathe) → [PAUSE](#pause) → [RACI](#raci)
   └─ NO → Go to Question 5

5. Is this strategic planning or design?
   ├─ YES → Use [SCALE](#scale-infrastructure-design) → [SWOT](#swot) → [PESTEL](#pestel) → [SET](#set-systems-engineering-triangle)
   └─ NO → Go to Question 6

6. Need quick feasibility check?
   └─ Use [IDEA](#idea) → [DICE](#dice) → [FATE](#fate)
```

**Still unsure?** Start with [IDEA](#idea) for simple problems, or [PREPARE](#prepare) for structured planning.

---

## Scenarios

### Scenario 1: IT Incident Response (MTTR Focus)

**Role:** IT/SRE Engineer  
**Situation:** Production database is experiencing intermittent timeouts. Users are reporting slow response times. Alert fired at 2:15 AM.

**Time:** 1-2 hours  
**Goal:** Restore service and prevent recurrence

#### Step-by-Step Walkthrough

**1. STOP (2-5 min) — Immediate Stress Management**
- **S**tep back: Don't panic. Read the alert details.
- **T**ake a deep breath: Pause for 3-5 seconds, reduce adrenaline.
- **O**bserve: Check alert severity, affected services, error patterns.
- **P**ull back perspective: Assess if this requires waking the team or can wait.

**2. TRACE (10-15 min) — Gather Evidence**
- **T**est connectivity: `ping`, `traceroute` to database server
- **R**eview logs: Check database logs, application logs, monitoring dashboards
- **A**nalyze packet captures: If network issue suspected, capture traffic
- **C**heck configurations: Recent changes? Deployment history?
- **E**scalate with documented evidence: Share findings with team

**3. DEBUG (15-30 min) — Structured Analysis**
- **D**efine the problem: "Database connection pool exhausted under load"
- **E**xamine error messages: Connection timeout errors, pool size limits
- **B**reak down into components: Application → Connection pool → Database
- **U**nderstand data flow: Request → Pool → Connection → Query → Response
- **G**enerate hypothesis: Pool size too small for peak load

**4. DICE (5 min) — Check Blockers**
- **D**elay: Can we wait for a fix? No — production issue.
- **I**ncompetence: Do we have the skills? Yes — DBA on call.
- **C**onflict: Team disagreement? No — clear path forward.
- **E**xternal factors: Vendor issue? No — our configuration.

**5. 8D Approach (1-2 hours) — Formal Resolution**

**D1 - Form a team:**
- RACI: R=On-call engineer, A=Engineering Manager, C=DBA, I=Product team

**D2 - Describe the problem:**
- "Database connection pool (size: 20) exhausted during peak traffic (2-3 PM). Users experience 5-10 second delays. Started 2 days ago after deployment v2.3.1."

**D3 - Interim Containment Action:**
- Increase connection pool from 20 → 50 (immediate fix)
- Add connection pool monitoring alerts
- Document rollback procedure

**D4 - Root Cause Analysis & Escape Point:**
- Use **5 Whys:**
  1. Why pool exhausted? → Peak traffic exceeded pool capacity
  2. Why now? → Deployment v2.3.1 introduced slower queries
  3. Why slower queries? → New feature added N+1 query pattern
  4. Why N+1? → Code review missed query optimization
  5. Why missed? → No performance testing in staging
- **Escape Point:** Deployment v2.3.1 without performance validation

**D5 - Permanent Corrective Actions:**
- Fix N+1 query (add eager loading)
- Add performance regression tests
- Set connection pool based on load testing

**D6 - Implement & Validate:**
- Deploy fix to staging, validate with load test
- Deploy to production, monitor for 24 hours
- Confirm pool utilization stays < 80%

**D7 - Prevent Reoccurrence:**
- Add performance testing to CI/CD pipeline
- Require load testing for features with database changes
- Document connection pool sizing guidelines

**D8 - Congratulate your team:**
- Post-mortem meeting: Recognize quick response (MTTR: 1.5 hours)
- Share learnings with engineering team
- Update runbook with this scenario

**Outcome:** Service restored in 1.5 hours. Root cause fixed. Prevention measures in place. MTTR improved from previous average of 3 hours.

**Key Learnings:**
- STOP prevented panic and wrong actions
- TRACE → DEBUG provided systematic evidence gathering
- 5 Whys revealed process gap (missing performance tests)
- 8D ensured permanent fix, not just band-aid

---

### Scenario 2: Cybersecurity Risk Assessment

**Role:** Security Professional  
**Situation:** New cloud migration project. Need to assess security risks before migration begins.

**Time:** 2-3 hours  
**Goal:** Identify security risks and mitigation strategies

#### Step-by-Step Walkthrough

**1. PREPARE (30 min) — Strategic Planning**
- **P**rioritize the problem: Security assessment is critical before migration
- **R**esearch & brainstorm: Review cloud provider security docs, compliance requirements
- **E**valuate available options: AWS vs Azure vs GCP security features
- **P**lan steps: PESTEL analysis → SWOT → Risk matrix
- **A**ct on the plan: Begin PESTEL analysis
- **R**eflect on results: Validate findings with security team
- **E**valuate and revise: Update risk matrix based on feedback

**2. PESTEL Analysis (45 min) — External Factors**

**P - Political:**
- Data sovereignty requirements (EU GDPR, country-specific regulations)
- Government access requests (cloud provider jurisdiction)

**E - Economic:**
- Cost of security tools (WAF, DDoS protection, encryption)
- Budget for security training and certifications

**S - Sociocultural:**
- User privacy expectations
- Organizational security culture

**T - Technological:**
- Cloud provider security features (encryption at rest, in transit)
- API security, identity management (IAM, SSO)
- Container security (if using Kubernetes)

**E - Environmental:**
- Data center locations (physical security, redundancy)
- Disaster recovery capabilities

**L - Legal:**
- Compliance requirements (SOC 2, ISO 27001, HIPAA)
- Data retention policies
- Breach notification requirements

**3. SWOT Analysis (30 min) — Internal & External Factors**

**Strengths:**
- Existing security team with cloud experience
- Current on-prem security controls (firewall, IDS)
- Compliance certifications already in place

**Weaknesses:**
- Limited cloud-native security expertise
- Legacy systems with known vulnerabilities
- Budget constraints for security tools

**Opportunities:**
- Cloud provider managed security services (reduce operational overhead)
- Automated security scanning in CI/CD
- Centralized logging and monitoring

**Threats:**
- Increased attack surface (public cloud)
- Misconfiguration risks (S3 bucket exposure, IAM over-privilege)
- Vendor lock-in for security tools

**4. SCALE (Infrastructure Design) — Security Requirements**

**S - Security by design:**
- Encryption at rest (AES-256) and in transit (TLS 1.3)
- Network segmentation (VPC, security groups)
- Least privilege IAM policies

**C - Capacity planning:**
- Security tool capacity (WAF throughput, log storage)
- Incident response team capacity

**A - Automation-first:**
- Automated security scanning (SAST, DAST)
- Infrastructure as Code (Terraform, CloudFormation) for consistent security configs
- Automated compliance checks

**L - Load balancing:**
- DDoS protection (CloudFlare, AWS Shield)
- WAF (Web Application Firewall) for application layer protection

**E - Error handling/resilience:**
- Security incident response plan
- Backup and disaster recovery (encrypted backups)
- Fail-secure defaults

**5. SET (Systems Engineering Triangle) — Trade-offs**

**Good + Fast ≠ Cheap:**
- Premium security tools (WAF, SIEM) + rapid deployment = higher cost
- Set expectation: Security budget needs approval

**Fast + Cheap ≠ Good:**
- Quick migration without security review = risk
- **Decision:** Prioritize Good (security) + Fast (timeline) → accept higher cost

**6. DICE (10 min) — Check Blockers**

- **D**elay: Can we delay migration? No — business deadline.
- **I**ncompetence: Do we have security expertise? Yes — team trained.
- **C**onflict: Disagreement on security controls? No — aligned.
- **E**xternal factors: Compliance audit deadline? Yes — must complete before audit.

**Outcome:** Comprehensive security risk assessment completed. Identified 12 risks (3 high, 5 medium, 4 low). Mitigation plan created. Budget approved for security tools. Migration approved with security controls in place.

**Key Learnings:**
- PESTEL revealed legal/compliance constraints early
- SWOT identified capability gaps (cloud expertise)
- SCALE ensured security built-in, not bolted-on
- SET helped set realistic expectations with leadership

---

### Scenario 3: Project Timeline Slippage

**Role:** Project Manager  
**Situation:** Software release is 3 weeks behind schedule. Stakeholders are concerned. Team is stressed.

**Time:** 1-2 hours  
**Goal:** Understand root cause, create recovery plan, set realistic expectations

#### Step-by-Step Walkthrough

**1. WAIT (2 min) — Choose Response**
- **W**hy am I troubled? → Pressure from stakeholders, fear of failure
- **W**hy am I talking? → Need to communicate status, but first need facts
- **Decision:** Gather data before responding to stakeholders

**2. BREATHE (3 min) — Regulate Emotions**
- **B**reathe deeply: 4-7-8 breathing (4 sec inhale, 7 hold, 8 exhale)
- **R**emain rational: This is a project issue, not a personal failure
- **E**mpathize: Team is also stressed; stakeholders need transparency
- **A**sk questions: What caused the delay? What can we recover?
- **T**ake a break: 5-minute walk to clear head
- **H**old back from reacting: Don't blame team or make promises yet
- **E**xpress yourself calmly: Schedule meeting with team to investigate

**3. ICEBERG (30-45 min) — Deep Analysis**

**I - Identify issue(s):**
- Release delayed by 3 weeks
- Multiple features incomplete
- Team reporting burnout

**C - Collect data and analyze:**
- Review sprint burndown charts
- Check JIRA/issue tracker for blocked items
- Interview team members (what's blocking them?)

**E - Examine possible (root) causes:**
- Scope creep? (Check original vs current requirements)
- Resource constraints? (Team size, availability)
- Technical debt? (Legacy code slowing development)
- External dependencies? (Third-party APIs, vendor delays)

**4. 5 Whys — Drill to Root Cause**

1. **Why is the release 3 weeks late?** → Features took longer than estimated
2. **Why did features take longer?** → Requirements changed mid-sprint
3. **Why did requirements change?** → Stakeholder feedback came late (after sprint started)
4. **Why did feedback come late?** → No defined review process for stakeholder sign-off
5. **Why no review process?** → Project started without proper planning phase

**Root Cause:** Missing stakeholder review process → late feedback → scope changes → delays

**5. FATE (15 min) — Validate Resources**

**F - Funding:**
- Budget available? Yes — no additional cost needed
- Can we extend timeline? Yes — but need stakeholder approval

**A - Allocation of resources:**
- Can we add team members? No — hiring freeze
- Can we reduce scope? Yes — defer non-critical features

**T - Time:**
- Can we extend deadline? Yes — but need to communicate impact
- Can we work overtime? Not sustainable — team already stressed

**E - Expertise:**
- Do we have the skills? Yes — team is capable
- Do we need training? No — skills are sufficient

**6. PREPARE (30 min) — Recovery Plan**

**P - Prioritize the problem:**
- Must-have features vs nice-to-have
- Defer 3 non-critical features to next release

**R - Research & brainstorm solutions:**
- Option 1: Extend deadline by 2 weeks (reduce scope)
- Option 2: Add contractors (not available)
- Option 3: Reduce scope, keep deadline (risky)

**E - Evaluate available options:**
- Best: Extend deadline + reduce scope (realistic, sustainable)

**P - Plan steps to resolve:**
1. Communicate delay to stakeholders (transparent)
2. Defer 3 features to v2.1
3. Adjust sprint plan (focus on must-haves)
4. Add stakeholder review checkpoint (prevent future delays)

**A - Act on the plan:**
- Schedule stakeholder meeting
- Update project timeline
- Adjust sprint backlog

**R - Reflect on results:**
- Monitor sprint velocity
- Check team morale (burnout risk)

**E - Evaluate and revise:**
- Weekly check-ins to catch delays early

**7. RACI (10 min) — Clarify Roles**

**R - Responsible:**
- Development team (deliver features)
- PM (coordinate, communicate)

**A - Accountable:**
- Engineering Manager (delivery)
- Product Manager (scope decisions)

**C - Consulted:**
- Stakeholders (feature priority)
- Tech Lead (technical feasibility)

**I - Informed:**
- All stakeholders (status updates)
- Executive team (timeline changes)

**Outcome:** Root cause identified (missing stakeholder review process). Recovery plan created: extend deadline by 2 weeks, defer 3 features. Stakeholders approved. Team morale improved (transparency reduced stress). Process improvement: added stakeholder review checkpoint to prevent future delays.

**Key Learnings:**
- WAIT → BREATHE prevented emotional reaction
- ICEBERG + 5 Whys revealed process gap (not team performance issue)
- FATE validated resources (can extend timeline, can't add people)
- PREPARE created actionable recovery plan
- RACI clarified accountability (reduced confusion)

---

### Scenario 4: Conflict Resolution

**Role:** Team Lead / Manager  
**Situation:** Two senior engineers disagree on architecture approach. Tension is rising. Meeting is unproductive.

**Time:** 10-20 minutes  
**Goal:** De-escalate, understand both perspectives, reach alignment

#### Step-by-Step Walkthrough

**1. WAIT (1 min) — Choose Response**
- **W**hy am I troubled? → Conflict is blocking progress, team morale affected
- **W**hy am I talking? → Need to facilitate, but first need to understand both sides
- **Decision:** Listen first, then facilitate discussion

**2. BREATHE (3-5 min) — Regulate Emotions (Team)**
- **B**reathe deeply: Guide team through 30-second breathing exercise
- **R**emain rational: "Both approaches have merit. Let's understand the trade-offs."
- **E**mpathize: "I understand this is important to both of you. Let's find common ground."
- **A**sk questions: "What are the key requirements? What are the constraints?"
- **T**ake a break: "Let's take a 5-minute break, then reconvene."
- **H**old back from reacting: Don't take sides yet
- **E**xpress yourself calmly: "I want to understand both perspectives before we decide."

**3. PAUSE (5-10 min) — Step Away**
- **P**ut things in perspective: "This is an architecture decision, not a personal attack."
- **A**cknowledge your feelings and theirs: "I see both of you are passionate about this. That's good."
- **U**nderstand that you don't have to act/react right away: "We don't need to decide today."
- **S**tep Away from the situation: Break for 10 minutes
- **E**valuate options and plan before acting: During break, think about:
  - What are the actual requirements?
  - What are the constraints (time, resources, team skills)?
  - Can we prototype both approaches?

**4. SWOT Analysis (10-15 min) — Evaluate Both Options**

**Option A: Microservices Architecture**

**Strengths:**
- Scalability (independent scaling)
- Technology diversity (right tool for each service)
- Team autonomy (smaller teams per service)

**Weaknesses:**
- Complexity (service mesh, distributed tracing)
- Operational overhead (more services to manage)
- Network latency (service-to-service calls)

**Opportunities:**
- Future growth (easier to scale)
- Team structure (aligns with Conway's Law)

**Threats:**
- Over-engineering (might be too complex for current scale)
- Team skills (need distributed systems expertise)

**Option B: Monolithic Architecture**

**Strengths:**
- Simplicity (easier to develop, deploy, debug)
- Performance (no network overhead)
- Team skills (current team comfortable with monolith)

**Weaknesses:**
- Scaling (must scale entire app)
- Technology lock-in (harder to adopt new tech)
- Team coordination (larger codebase, more conflicts)

**Opportunities:**
- Faster initial development
- Lower operational complexity

**Threats:**
- Future scaling challenges
- Technical debt (harder to refactor later)

**5. SET (Systems Engineering Triangle) — Trade-offs**

**Good + Fast ≠ Cheap:**
- Microservices (Good for scale) + Fast development = Higher operational cost

**Fast + Cheap ≠ Good:**
- Monolith (Fast + Cheap) = May not scale well long-term

**Good + Cheap ≠ Fast:**
- Microservices (Good) + Lower cost (if done right) = Slower initial development

**Decision Framework:**
- Current scale: Small (monolith sufficient)
- Future scale: Unknown (microservices more flexible)
- Team skills: Monolith (current), Microservices (need training)
- Timeline: Tight (monolith faster)

**6. RACI (5 min) — Clarify Decision Authority**

**R - Responsible:**
- Both engineers (provide technical input)

**A - Accountable:**
- Engineering Manager (final decision)

**C - Consulted:**
- Product Manager (requirements, timeline)
- DevOps (operational impact)

**I - Informed:**
- Entire engineering team

**Decision:** Start with monolith (faster, team skills match), but design for future microservices migration (modular structure, API boundaries). Revisit in 6 months based on scale.

**Outcome:** Conflict resolved. Both engineers feel heard. Decision made (monolith with migration path). Team alignment restored. Process improved: added architecture review process for future decisions.

**Key Learnings:**
- WAIT prevented taking sides prematurely
- BREATHE + PAUSE de-escalated emotions
- SWOT provided objective comparison (not personal)
- SET helped set realistic expectations
- RACI clarified who decides (reduced ambiguity)

---

### Scenario 5: Learning from Failures

**Role:** Student / Engineer Learning Frameworks  
**Situation:** Studying for systems design interview. Want to understand how frameworks chain together in real scenarios.

**Time:** 1-2 hours  
**Goal:** Learn framework interdependencies, practice applying frameworks

#### Step-by-Step Walkthrough

**Use Case:** Design a distributed cache system (like Redis)

**1. PREPARE (15 min) — Structure Learning**
- **P**rioritize: Understand cache design principles
- **R**esearch: Read about distributed caching, consistency models
- **E**valuate: Which frameworks apply? (SCALE, SWOT, PESTEL, SET)
- **P**lan: Apply frameworks step-by-step
- **A**ct: Start with SCALE
- **R**eflect: Does this make sense?
- **E**valuate: What did I learn?

**2. SCALE (Infrastructure Design) — Design Requirements**

**S - Security by design:**
- Authentication (API keys, TLS)
- Authorization (role-based access)
- Encryption (data at rest, in transit)

**C - Capacity planning:**
- Memory size (how much data to cache?)
- Throughput (requests per second)
- Network bandwidth

**A - Automation-first:**
- Auto-scaling (add/remove nodes based on load)
- Automated failover (primary → replica)
- Health checks

**L - Load balancing:**
- Distribute requests across cache nodes
- Consistent hashing (minimize cache misses on node addition/removal)

**E - Error handling/resilience:**
- Cache miss handling (fallback to database)
- Node failure (replication, failover)
- Network partitions (CAP theorem trade-offs)

**3. SWOT Analysis (20 min) — Evaluate Design Options**

**Option A: In-Memory Cache (Single Node)**

**Strengths:**
- Simple (easy to implement)
- Fast (in-memory access)
- Low latency

**Weaknesses:**
- Single point of failure
- Limited capacity (one machine's RAM)
- No persistence (data lost on restart)

**Opportunities:**
- Quick prototype
- Good for small scale

**Threats:**
- Doesn't scale
- Data loss risk

**Option B: Distributed Cache (Multiple Nodes)**

**Strengths:**
- Scalability (add nodes as needed)
- High availability (replication)
- Persistence (optional disk backup)

**Weaknesses:**
- Complexity (consistency, partitioning)
- Network latency (node-to-node communication)
- Operational overhead

**Opportunities:**
- Handles large scale
- Industry standard (Redis, Memcached)

**Threats:**
- CAP theorem trade-offs (Consistency vs Availability)
- More failure modes

**Decision:** Distributed cache (Option B) for scalability, but start simple (Option A) for learning.

**4. PESTEL Analysis (15 min) — External Factors**

**P - Political:**
- Data residency requirements (where can data be stored?)

**E - Economic:**
- Cost of infrastructure (cloud vs on-prem)
- Licensing (open source vs commercial)

**S - Sociocultural:**
- Developer preferences (Redis vs Memcached community)

**T - Technological:**
- Cloud provider offerings (AWS ElastiCache, Azure Cache)
- Network infrastructure (latency between regions)

**E - Environmental:**
- Data center locations (latency, compliance)

**L - Legal:**
- Data privacy regulations (GDPR, CCPA)

**5. SET (Systems Engineering Triangle) — Trade-offs**

**Good + Fast ≠ Cheap:**
- High-performance cache (Good) + Quick deployment (Fast) = Higher cloud costs

**Fast + Cheap ≠ Good:**
- Quick setup (Fast) + Free tier (Cheap) = Limited features, no support

**Good + Cheap ≠ Fast:**
- Self-hosted Redis (Good + Cheap) = Slower setup, operational overhead

**Decision:** Use managed cache service (Good + Fast) for production, self-hosted for learning.

**6. ICEBERG + 5 Whys — Deep Dive on Consistency**

**Problem:** How to handle cache consistency?

**ICEBERG:**
- **I**dentify: Cache consistency challenge
- **C**ollect: Research consistency models (strong, eventual, weak)
- **E**xamine: Why is consistency hard? (multiple nodes, network delays)
- **B**rainstorm: Solutions (write-through, write-back, TTL)
- **E**xecute: Choose eventual consistency (common for caches)
- **R**eview: Does this meet requirements?
- **G**ather feedback: Test with sample workload

**5 Whys:**
1. Why is consistency hard? → Multiple nodes have different data
2. Why different data? → Updates propagate with delay
3. Why delay? → Network latency between nodes
4. Why not wait for all nodes? → Would slow down writes (high latency)
5. Why accept eventual consistency? → Caches are for performance; slight staleness acceptable

**Outcome:** Learned how frameworks chain together:
- SCALE sets requirements
- SWOT evaluates options
- PESTEL considers external factors
- SET manages trade-offs
- ICEBERG + 5 Whys deep-dive on specific challenges

**Key Learnings:**
- Frameworks are tools, not rigid rules
- Chain frameworks based on problem complexity
- Start simple (SCALE), then add depth (ICEBERG + 5 Whys)
- SET helps communicate trade-offs to stakeholders

---

### Scenario 6: Stress & Burnout Recovery

**Role:** Individual Contributor / Manager  
**Situation:** Feeling overwhelmed. Working long hours. Sleep disrupted. Motivation declining. Approaching burnout.

**Time:** 2-4 weeks (habit formation)  
**Goal:** Recover from stress, build resilience, prevent burnout

#### Step-by-Step Walkthrough

**Week 1: Immediate Stress Management**

**1. STOP (Daily, 2-5 min) — Crisis Response**
- **S**tep back: Recognize you're in stress response
- **T**ake a deep breath: 4-7-8 breathing (4 sec inhale, 7 hold, 8 exhale)
- **O**bserve: What's causing stress? (Workload, deadlines, conflict?)
- **P**ull back perspective: This is temporary; you can recover

**2. PACE (Daily, 10-15 min) — Immediate Actions**

**P - Physical activity:**
- Morning walk (20 min) or exercise (30 min)
- Reduces cortisol, improves mood

**A - Avoiding unhealthy behaviors:**
- Limit caffeine (especially after 2 PM)
- Avoid alcohol as stress relief
- Don't skip meals

**C - Coping skills:**
- Meditation (10 min daily) — Headspace, Calm app
- Journaling (5 min) — Write down stressors
- Time blocking — Protect focus time

**E - Emotional awareness:**
- Check in with yourself 3x daily (morning, midday, evening)
- Rate stress level 1-10
- Identify triggers

**Week 2-3: Lifestyle Changes**

**3. ARIES (2-4 weeks) — Long-term Habits**

**A - Avoid unnecessary stress:**
- Say "no" to non-essential meetings
- Delegate tasks when possible
- Set boundaries (no work email after 6 PM)

**R - Relax and take breaks:**
- Pomodoro technique (25 min work, 5 min break)
- Lunch break away from desk
- Weekend activities (hiking, reading, hobbies)

**I - Incorporate physical activity:**
- Regular exercise (3-4x per week)
- Walking meetings instead of sitting
- Stand desk (if available)

**E - Eat a healthy diet:**
- Regular meals (don't skip breakfast)
- Hydration (water, not just coffee)
- Limit processed foods

**S - Sleep well:**
- Consistent sleep schedule (same bedtime, wake time)
- Sleep hygiene (dark room, no screens 1 hour before bed)
- 7-8 hours minimum

**Week 3-4: Build Resilience**

**4. CALM (Ongoing) — Mental Resilience**

**C - Confidence:**
- List your strengths and achievements
- Remind yourself: "I've handled challenges before"
- Celebrate small wins

**A - Awareness:**
- Mindfulness practice (present moment awareness)
- Notice negative self-talk, reframe it
- Body scan meditation (identify tension)

**L - Logic:**
- Challenge catastrophic thinking ("This will never get better" → "This is temporary")
- Problem-solve: What can I control? What can't I control?
- Break big problems into smaller steps

**M - Mindfulness:**
- Daily meditation (10-20 min)
- Mindful breathing (when stressed)
- Gratitude practice (3 things daily)

**5. SHINE (Ongoing) — Sustainable Positivity**

**S - Stay present:**
- Don't ruminate on past mistakes
- Don't worry about future problems
- Focus on what you can do now

**H - Have a healthy positive perspective:**
- Reframe challenges as opportunities
- Look for silver linings
- Practice optimism (realistic, not blind)

**I - Identify and do positive activities:**
- Hobbies (music, art, sports)
- Social activities (friends, family)
- Learning (new skills, reading)

**N - Nourish positive relationships:**
- Connect with supportive people
- Ask for help when needed
- Give back (help others, volunteer)

**E - Express yourself:**
- Talk to trusted friend/family/therapist
- Creative expression (writing, art)
- Don't bottle up emotions

**6. PREPARE (Week 4) — Prevention Plan**

**P - Prioritize:**
- What's truly important? (Health, family, meaningful work)
- What can wait? (Non-urgent tasks)

**R - Research:**
- Learn about burnout warning signs
- Identify your personal triggers

**E - Evaluate:**
- What worked? (PACE, ARIES, CALM)
- What didn't? (Adjust approach)

**P - Plan:**
- Weekly self-check (stress level, sleep, mood)
- Monthly review (am I maintaining balance?)
- Red flags to watch for (returning to old patterns)

**A - Act:**
- Continue healthy habits
- Adjust as needed

**R - Reflect:**
- Journal weekly: How am I feeling?
- What's improved? What still needs work?

**E - Evaluate:**
- Am I maintaining balance?
- Do I need additional support? (Therapist, coach)

**Outcome:** Stress reduced from 9/10 to 4/10. Sleep improved (7-8 hours consistently). Energy levels restored. Work performance improved (better focus, less mistakes). Prevention plan in place to maintain balance.

**Key Learnings:**
- STOP is the foundation (use daily when stressed)
- PACE provides immediate relief (physical activity is powerful)
- ARIES requires time (2-4 weeks for habit formation)
- CALM builds long-term resilience (mindset shift)
- SHINE sustains positivity (ongoing practice)
- PREPARE prevents recurrence (maintenance plan)

**Red Flags (Seek Professional Help):**
- Persistent depression or anxiety
- Suicidal thoughts
- Substance abuse
- Unable to function (work, relationships)

---

## Framework Interdependencies

**How frameworks chain together in real workflows:**

```
                    ┌────────────-─┐
                    │   Problem    │
                    └──────┬───────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
    ┌───▼───┐         ┌────▼────┐       ┌────▼────┐
    │ Crisis│         │Complex  │       │ Stress  │
    │       │         │Problem  │       │         │
    └───┬───┘         └────┬────┘       └────┬────┘
        │                  │                 │
    ┌───▼──────────┐  ┌──-─▼─────────┐  ┌──-─▼─────────┐
    │ STOP         │  │ ICEBERG      │  │ STOP         │
    │ (2-5 min)    │  │ (30-60 min)  │  │ (2-5 min)    │
    └───┬──────────┘  └───┬──────────┘  └───┬──────────┘
        │                 │                 │
    ┌───▼──────────┐  ┌───▼──────────┐  ┌───▼──────────┐
    │ TRACE        │  │ 5 Whys       │  │ PACE         │
    │ (10-15 min)  │  │ (15-30 min)  │  │ (10-15 min)  │
    └───┬──────────┘  └───┬──────────┘  └───┬──────────┘
        │                 │                 |
    ┌───▼──────────┐  ┌───▼──────────┐  ┌───▼──────────┐
    │ DEBUG        │  │ PADDER       │  │ ARIES        │
    │ (15-30 min)  │  │ (30-60 min)  │  │ (2-4 weeks)  │
    └───┬──────────┘  └───┬──────────┘  └───┬──────────┘
        │                 │                 │
    ┌───▼──────────┐  ┌───▼──────────┐  ┌───▼──────────┐
    │ 8D           │  │ RACI         │  │ CALM         │
    │ (1-4 hours)  │  │ (10 min)     │  │ (ongoing)    │
    └──────────────┘  └──────────────┘  └───┬──────────┘
                                            │
                                       ┌──-─▼─────────┐
                                       │ SHINE        │
                                       │ (ongoing)    │
                                       └──────────────┘

Strategic Planning Chain:
    PREPARE → SCALE → SWOT → PESTEL → SET

Conflict Resolution Chain:
    WAIT → BREATHE → PAUSE → RACI

Quick Triage Chain:
    IDEA → DICE → FATE
```

**Key Principles:**
1. **Start with the right entry point** — STOP for crisis, WAIT for conflict, PREPARE for planning
2. **Chain based on complexity** — Simple → IDEA, Complex → ICEBERG → 5 Whys
3. **Use DICE/FATE to validate** — Check blockers and resources before execution
4. **RACI clarifies roles** — Often resolves conflicts and ensures accountability
5. **SET manages expectations** — Communicate trade-offs to stakeholders

---

## Workflow Diagram

**From crisis to prevention:**

```
Crisis/Problem
    │
    ▼
[STOP/WAIT] ────► Immediate Response (2-5 min)
    │
    ▼
[TRACE/ICEBERG] ────► Diagnosis (10-60 min)
    │
    ▼
[DEBUG/5 Whys] ────► Root Cause Analysis (15-60 min)
    │
    ▼
[DICE/FATE] ────► Feasibility Check (5-15 min)
    │
    ▼
[PADDER/PREPARE] ────► Solution Planning (30-120 min)
    │
    ▼
[8D/RACI] ────► Formal Resolution (1-4 hours)
    │
    ▼
Prevention & Learning
    │
    ▼
[PREPARE] ────► Process Improvement
```

---

**Next Steps:**
- [Return to README](README.md) for full framework definitions
- [Check Sources](SOURCES.md) for citations and confidence ratings
- [Contribute a scenario](CONTRIBUTING.md) — share your real-world experience
