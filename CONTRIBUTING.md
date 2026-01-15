# Contributing to Awesome Mnemonics

Thank you for contributing! This guide helps maintain consistency and quality.

## Submission Criteria

All mnemonics must meet these requirements:

- ✅ **Provable/actionable** - Not just motivational, must have concrete steps
- ✅ **Cross-references** - Should link to related mnemonics where applicable
- ✅ **Real-world context** - Include actual usage examples
- ✅ **Memorable** - The acronym/pattern should be easy to recall under pressure

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

**📋 Real-world example:** *Brief scenario showing the mnemonic in action*
```

### Complete Example

Here's a complete example following the template:

```markdown
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
```

## Submission Process

1. **Fork the repository**
2. **Add your mnemonic** to the appropriate section in `README.md`
3. **Update the Table of Contents** with your new entry
4. **Add cross-references** - Link your mnemonic in related "Combines well with" sections
5. **Test your links** - Ensure all anchor links work correctly
6. **Submit a pull request** with:
   - Clear description of the mnemonic
   - Why it fits the repository
   - Real-world context or use case

## Section Guidelines

### 🧩 Problem Solving
For frameworks that help identify root causes and develop solutions. Examples: PREPARE, ICEBERG, 8D Approach.

### 📊 Problem Analysis
For tools that help understand stakeholder roles, external pressures, and scope. Examples: RACI, SWOT, PESTEL.

### ⚠️ Problem Resolution Threats
For identifying blockers and resource constraints. Examples: DICE, FATE, PEST.

### 🧘 Stress & Resilience
For managing stress, building resilience, and maintaining well-being. Examples: STOP, PACE, CALM.

### 🗣️ Communication & Conflict
For staying calm and productive during difficult conversations. Examples: BREATHE, PAUSE, WAIT.

### 🔧 Infrastructure & Systems Engineering
For technical mnemonics specific to infrastructure and DevOps work. Examples: TRACE, SCALE, DEBUG.

## Pipeline Contributions

If you're proposing a new mnemonic pipeline (combination of multiple mnemonics), include:

- **When to use** - Specific scenario
- **The Flow** - Step-by-step breakdown
- **Why it works** - Explanation of the synergy
- **Time investment** - Realistic time estimate

## Quality Standards

- **Clarity** - Each step should be unambiguous
- **Actionability** - Must provide concrete actions, not just concepts
- **Completeness** - Include all required sections (When to use, Pitfalls, Combines well with, Example)
- **Consistency** - Follow existing formatting and style

## Mobile & Print Considerations

When adding mnemonics, keep in mind:

- **Mobile readability** - Keep descriptions concise; on-call engineers may be reading on phones
- **Print-friendly** - High-priority mnemonics may be added to `PRINT-QUICK-REFERENCE.md`
- **Link formatting** - Use proper anchor links (e.g., `[STOP](#stop)`) for cross-references
- **Code blocks** - Use triple backticks for mnemonic breakdowns to ensure proper formatting on all devices

## Who Uses This?

If your team or organization uses these mnemonics, we'd love to showcase you! Add yourself to the "Who Uses This?" section in `README.md`.

**How to add:**
1. Fork the repository
2. Add your entry to the "Who Uses This?" section in `README.md`:
   ```markdown
   - **[Your Organization/Team Name](https://your-website.com)** - Brief description (optional)
   ```
3. Submit a pull request

**Examples:**
- `- **[Acme Corp](https://acme.com)** - Our SRE team uses STOP → TRACE → DEBUG daily`
- `- **[Tech Startup](https://techstartup.io)** - On-call engineers reference this during incidents`
- `- **Engineering Team at BigCo** - We've integrated these into our incident response playbooks`

**Note:** Only add if you're actually using these mnemonics in production. This helps build credibility and shows real-world adoption.

## Questions?

Open an issue to discuss your mnemonic idea before submitting if you're unsure about:
- Which section it belongs in
- Whether it meets the criteria
- How to structure it

Thank you for helping make this field guide more comprehensive!
