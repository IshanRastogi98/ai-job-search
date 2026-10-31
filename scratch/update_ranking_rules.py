from pathlib import Path

# Update CLAUDE.md
claude_path = Path("CLAUDE.md")
claude_text = claude_path.read_text(encoding="utf-8")

ranking_rules = """### 6. Dynamic Project Ranking & Proportional Depth
- **Relevance-Based Ordering:** For every job application, evaluate all projects in `01-candidate-profile.md` against the target company's tech stack and domain. Order the projects from highest relevance to lowest relevance.
- **Fallback Order:** If relevance is equal or cannot be clearly ranked, default strictly to the canonical order in `01-candidate-profile.md` and `main_example.tex` (`GPUCloud`, `INSPIRE`, `MindsViewMsg`).
- **Proportional Bullet Allocation:** Allocate bullet depth dynamically based on the ranking to achieve optimal vertical density:
  - **Primary (Top-Ranked) Project:** Include 5–6 comprehensive bullets from the master profile, ordered by relevance to the role.
  - **Secondary Projects:** Include 3–4 strong bullets each from the master profile.
  - **Experience & Leadership:** Include all 3 bullets from the master profile.
  - **Tech Stack Lines:** Always include the explicit `Tech Stack:` summary line beneath each project entry as written in the master profile.

### 7. Page Density & Vertical Fill (75–85% Single-Page Target)
- **Target Coverage:** Every compiled CV must fill 75% to 85% of a single A4 page. Never leave more than 25% whitespace at the bottom (bottom space <= 25%), and never spill onto page 2.
- **Categorized Technical Skills:** Display the Technical Skills section broken out into its full category rows (Languages, Frontend, Backend, Auth & Security, Database & Cloud, Infra & DevOps, etc.) rather than collapsing them into a minimal block.
- **Complete Education & Achievements:** Include full education metadata (degree, institution, dates, CGPA, and relevant coursework) alongside verified honors from the master profile.
- **LaTeX Geometry & Spacing Calibration:**
  - Use balanced A4 margins (`top=0.5in, bottom=0.5in, left=0.55in, right=0.55in`), `10pt` or `10.5pt` body font, and `\\linespread{1.08}`.
  - Use consistent vertical spacing (`\\vspace{4pt}` to `\\vspace{6pt}` between sections and `\\itemsep 2pt` between list items). If a generated CV falls below 85% page fill, expand bullet inclusion from the master profile before adjusting spacing; if it exceeds 1 page, tighten `\\itemsep` or trim the lowest-priority bullet on the lowest-ranked project."""

target_marker = "### 5. Layout, LaTeX & Formatting Guardrails"
old_block_end = "- **AI Tooling Attribution:** When mentioning agentic coding or AI tooling in CVs or cover letters, explicitly reference **Claude Code** by name.\n"

if old_block_end in claude_text:
    claude_text = claude_text.replace(old_block_end, old_block_end + "\n" + ranking_rules + "\n")
    print("Added ranking rules to CLAUDE.md")
else:
    print("Warning: old_block_end not found in CLAUDE.md")

claude_path.write_text(claude_text, encoding="utf-8")

# Update 05-cv-templates.md
cv_path = Path(".claude/skills/job-application-assistant/05-cv-templates.md")
cv_text = cv_path.read_text(encoding="utf-8")

cv_guardrails_marker = "## Permanent Non-Negotiable CV Guardrails\n"

cv_ranking_rules = """### 5. Dynamic Project Ranking & Proportional Depth
- **Relevance-Based Ordering:** For every job application, evaluate all projects in `01-candidate-profile.md` against the target company's tech stack and domain. Order the projects from highest relevance to lowest relevance.
- **Fallback Order:** If relevance is equal or cannot be clearly ranked, default strictly to the canonical order in `01-candidate-profile.md` and `main_example.tex` (`GPUCloud`, `INSPIRE`, `MindsViewMsg`).
- **Proportional Bullet Allocation:** Allocate bullet depth dynamically based on the ranking to achieve optimal vertical density:
  - **Primary (Top-Ranked) Project:** Include 5–6 comprehensive bullets from the master profile, ordered by relevance to the role.
  - **Secondary Projects:** Include 3–4 strong bullets each from the master profile.
  - **Experience & Leadership:** Include all 3 bullets from the master profile.
  - **Tech Stack Lines:** Always include the explicit `Tech Stack:` summary line beneath each project entry as written in the master profile.

### 6. Page Density & Vertical Fill (75–85% Single-Page Target)
- **Target Coverage:** Every compiled CV must fill 75% to 85% of a single A4 page. Never leave more than 25% whitespace at the bottom (bottom space <= 25%), and never spill onto page 2.
- **Categorized Technical Skills:** Display the Technical Skills section broken out into its full category rows (Languages, Frontend, Backend, Auth & Security, Database & Cloud, Infra & DevOps, etc.) rather than collapsing them into a minimal block.
- **Complete Education & Achievements:** Include full education metadata (degree, institution, dates, CGPA, and relevant coursework) alongside verified honors from the master profile.
- **LaTeX Geometry & Spacing Calibration:**
  - Use balanced A4 margins (`top=0.5in, bottom=0.5in, left=0.55in, right=0.55in`), `10pt` or `10.5pt` body font, and `\\linespread{1.08}`.
  - Use consistent vertical spacing (`\\vspace{4pt}` to `\\vspace{6pt}` between sections and `\\itemsep 2pt` between list items). If a generated CV falls below 85% page fill, expand bullet inclusion from the master profile before adjusting spacing; if it exceeds 1 page, tighten `\\itemsep` or trim the lowest-priority bullet on the lowest-ranked project.\n\n"""

old_cv_marker = "- **AI Tooling Attribution:** When mentioning agentic coding or AI tooling in CVs, explicitly reference **Claude Code** by name.\n"

if old_cv_marker in cv_text:
    cv_text = cv_text.replace(old_cv_marker, old_cv_marker + "\n" + cv_ranking_rules)
    print("Added ranking rules to 05-cv-templates.md")
else:
    print("Warning: old_cv_marker not found in 05-cv-templates.md")

# Update geometry sample in 05-cv-templates.md
cv_text = cv_text.replace(
    r"\usepackage[scale=0.88,top=1.2cm,bottom=1.2cm,left=1.4cm,right=1.4cm]{geometry}",
    r"\usepackage[top=0.5in,bottom=0.5in,left=0.55in,right=0.55in]{geometry}" + "\n\\linespread{1.08}"
)

cv_path.write_text(cv_text, encoding="utf-8")
print("Updated 05-cv-templates.md")
