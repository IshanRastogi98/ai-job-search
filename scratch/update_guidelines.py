from pathlib import Path

# Update 05-cv-templates.md
cv_path = Path(".claude/skills/job-application-assistant/05-cv-templates.md")
cv_text = cv_path.read_text(encoding="utf-8")

old_cv_target = """### Compile command

```bash
cd cv && lualatex -interaction=nonstopmode main_<company>_<role>.tex
```

Expected output: `Output written on main_<company>_<role>.pdf (2 pages, ...)`. Any page count other than 2 is a failure that must be fixed before presenting to the user."""

new_cv_guardrails = """### Compile command

```bash
cd cv && lualatex -interaction=nonstopmode main_<company>_<role>.tex
```

Expected output: `Output written on main_<company>_<role>.pdf (1 page, ...)`. Any page count other than 1 is a failure that must be fixed before presenting to the user.

## Permanent Non-Negotiable CV Guardrails

### 1. Truthfulness & Zero Fabrication (Global Rule)
- **Source of Truth:** Every claim, metric, project title, and technical skill must come strictly from `01-candidate-profile.md`. You may reorder, trim, and emphasize existing bullets to match a job description, but NEVER invent new metrics, academic ranks (e.g. no "Rank 1"), or unverified claims.
- **No Unmeasured Numbers:** Only use exact metrics present in the master profile (e.g., 9.42/10 CGPA, 98.84 percentile, 0% job-collision rate, 60s JWT expiry, 1-2GB tmpfs cap, 4-hour session limit, 960-minute free-tier cap, 20 req/min rate limit, 5 msgs/min rate limit). Never invent percentage improvements or load reductions.
- **No Defenseless Practices or Buzzwords:** Never claim "open-source" without an explicit public repository link. Do not add CI/CD, GitHub Actions, TDD, unit testing, or buzzwords like "high-throughput" or "production-grade" unless explicitly documented in the master profile.
- **Role & Scope Fidelity:** Maintain exact project names and role scopes. Do not upgrade collaborative or 2-person team roles into solo management or director claims.

### 2. Candidate Stage & Skills Filtering
- **Fresher / Student Transparency:** Always state clearly that Ishan is an undergraduate B.Tech CSE student at IIIT Bhopal (2024–Present, Expected Graduation: August 2028) targeting internships, part-time, or student-eligible engineering roles.
- **20-Minute Quiz Rule for Skills:** Only list technical skills that are directly backed by a project or experience entry on the CV. Omit any "basics" or "familiar with" tools that have no project evidence.

### 3. Content Quality & Structure
- **Summary:** Keep the CV profile summary to a maximum of 1–2 concise lines without generic fluff.
- **Bullet Density:** Limit each project or experience entry to the 2–4 strongest, outcome-led bullets. Drop weaker bullets to save vertical space.
- **Zero Repetition:** Do not repeat the same sentences across summary, skills, project bullets, and cover letter.

### 4. Layout, LaTeX & Formatting Guardrails
- **Strict 1-Page Limit (Fresher/Intern Standard):** Every compiled CV MUST fit strictly on **1 single page** (A4 size). Automatically adjust spacing or trim secondary bullets if a CV ever spills onto page 2.
- **LaTeX Hygiene:** Never wrap numbers, fractions, or units (like `9.42/10` or `5 req/min`) in LaTeX math mode (`$...$`) or tildes (`~`). Render single-year projects as `2025` (never `2025-2025`). Use clean ASCII hyphens for date ranges.
- **Visual Consistency:** Single clean font, 10–10.5pt body text, plain standard bullets (no emojis or decorative icons), left-aligned text, single-line contact header (`Lucknow, Uttar Pradesh, India` with working clickable links for GitHub, LinkedIn, and live demos), and ensure headings never sit orphaned at the bottom of a page.
- **AI Tooling Attribution:** When mentioning agentic coding or AI tooling in CVs, explicitly reference **Claude Code** by name."""

cv_text = cv_text.replace(r"\address{Bhopal, Madhya Pradesh, India}{}{}", r"\address{Lucknow, Uttar Pradesh, India}{}{}")
cv_text = cv_text.replace("Check the output page count: must be exactly 2", "Check the output page count: must be exactly 1")
cv_text = cv_text.replace(r"\documentclass[11pt,a4paper,sans]{moderncv}", r"\documentclass[10pt,a4paper,sans]{moderncv}")

if old_cv_target in cv_text:
    cv_text = cv_text.replace(old_cv_target, new_cv_guardrails)
    print("Replaced old_cv_target")
else:
    print("Warning: old_cv_target not found in cv_text")

cv_path.write_text(cv_text, encoding="utf-8")
print("Updated 05-cv-templates.md")

# Update 06-cover-letter-templates.md
cl_path = Path(".claude/skills/job-application-assistant/06-cover-letter-templates.md")
cl_text = cl_path.read_text(encoding="utf-8")

old_cl_target = """## Compile-and-Inspect Loop (MANDATORY)

After writing the cover letter and before presenting to the user, always compile and visually inspect the PDF. Iterate until the layout is clean:

1. Run `xelatex -interaction=nonstopmode cover_<company>_<role>.tex`
2. Confirm page count is exactly 1 and compile succeeded
3. Read the PDF via the Read tool and visually check: signature fits at the bottom, no text cut off, bullet font matches body"""

new_cl_guardrails = """## Permanent Non-Negotiable Cover Letter Guardrails

### 1. Truthfulness & Zero Fabrication (Global Rule)
- **Source of Truth:** Every claim, metric, and project reference must come strictly from `01-candidate-profile.md`. Never invent metrics or unverified assertions.
- **Role & Scope Fidelity:** Maintain exact project names and scopes. Accurately describe collaborative team projects (e.g. 2-person core engineering team at INSPIRE).
- **Fresher / Student Transparency:** Clearly state undergraduate status (B.Tech CSE student at IIIT Bhopal, Class of 2028), targeting student-eligible, internship, or part-time roles, along with exact availability windows.

### 2. Format & Prose Standards
- **Format:** Strictly **1 page**, written in **3–4 short, natural prose paragraphs**.
- **NEVER use bullet points in a cover letter.** Bullet lists belong on the CV; the cover letter is a cohesive narrative.
- **Tone & Content:** Eliminate generic filler ("strong enthusiasm", "passionate about", "gold standard", "esteemed team"). Reference 1–2 specific projects in narrative form (told differently from the CV bullets), connect them to the company's specific product or engineering mission, and plainly state availability and student timeline.

### 3. Layout, LaTeX & Typography
- **Strict 1-Page Limit:** The cover letter must fit completely on 1 single page including salutation and signature block.
- **Visual Consistency:** Clean font, 10–11pt text, single-line contact header (`Lucknow, Uttar Pradesh, India` with working clickable links for GitHub and LinkedIn).
- **AI Tooling Attribution:** Explicitly reference **Claude Code** by name when citing AI-assisted development tools.

## Compile-and-Inspect Loop (MANDATORY)

After writing the cover letter and before presenting to the user, always compile and visually inspect the PDF. Iterate until the layout is clean:

1. Run `xelatex -interaction=nonstopmode cover_<company>_<role>.tex`
2. Confirm page count is exactly 1 and compile succeeded
3. Read the PDF via the Read tool and visually check: signature fits at the bottom, no text cut off, 3-4 natural prose paragraphs with zero bullet points"""

if old_cl_target in cl_text:
    cl_text = cl_text.replace(old_cl_target, new_cl_guardrails)
    print("Replaced old_cl_target")
else:
    print("Warning: old_cl_target not found in cl_text")

# Update address/contact line if present in sample
cl_text = cl_text.replace("Bhopal, Madhya Pradesh, India", "Lucknow, Uttar Pradesh, India")

cl_path.write_text(cl_text, encoding="utf-8")
print("Updated 06-cover-letter-templates.md")
