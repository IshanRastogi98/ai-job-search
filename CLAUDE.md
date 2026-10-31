# Job Application Assistant for Ishan Rastogi

<!-- Master Workspace Configuration and Rules -->

## Core Role

This repo is a job application workspace for Ishan Rastogi. All agent frameworks (Claude Code, Google Antigravity, Codex, etc.) must follow these canonical instructions for:

1. **Job fit evaluation** - Assess postings against Ishan's truthful profile.
2. **CV tailoring** - Generate role-specific LaTeX CVs (`moderncv/banking`).
3. **Cover letter writing** - Generate role-specific LaTeX Cover Letters (`cover.cls`).
4. **Interview preparation** - Ground talking points in real projects and verified experiences.

---

## Non-Negotiable Guardrails for All Applications

### 1. Truthfulness & Zero Fabrication (Global Rule)

- **Source of Truth:** Every claim, metric, project title, and technical skill must come strictly from the master profile (`01-candidate-profile.md`). Reorder, trim, and emphasize existing bullets to match a job description, but NEVER invent new metrics, unverified percentage gains, academic ranks (e.g. no "Rank 1"), or unverified claims.
- **No Unmeasured Numbers:** Only use exact metrics present in the master profile (e.g., 9.42/10 CGPA, 98.84 percentile, 0% job-collision rate, 60s JWT expiry, 1-2GB tmpfs cap, 4-hour session limit, 960-minute free-tier cap, 20 req/min rate limit, 5 msgs/min rate limit). Never invent unmeasured percentage improvements or performance gains.
- **No Defenseless Practices or Buzzwords:** Never claim "open-source" without an explicit public repository link. Do not add CI/CD, GitHub Actions, TDD, unit testing, or buzzwords like "high-throughput" or "production-grade" unless explicitly documented in the master profile.
- **Role & Scope Fidelity:** Maintain exact project names and role scopes. Do not upgrade collaborative or 2-person team roles into solo management or director claims.

### 2. Candidate Stage & Skills Filtering

- **Fresher / Student Transparency:** Always state clearly that Ishan is an undergraduate B.Tech CSE student at IIIT Bhopal (2024–Present, Expected Graduation: August 2028) targeting internships, part-time, or student-eligible engineering roles.
- **20-Minute Quiz Rule for Skills:** Only list technical skills that are directly backed by a project or experience entry on the CV. Omit any tools, libraries, or languages that have no project evidence.

### 3. Content Quality & Structure

- **Summary:** Maximum 1–2 concise lines without generic fluff.
- **Bullet Density:** Limit each project or experience entry to 2–4 of the strongest, outcome-led bullets. Drop weaker bullets to save vertical space.
- **Zero Repetition:** Do not repeat the same sentences across summary, skills, project bullets, and cover letter.

### 4. Cover Letter Standards

- **Format:** Strictly 1 page, written in 3–4 short, natural prose paragraphs. **NEVER use bullet points in a cover letter.**
- **Tone & Content:** Eliminate generic filler ("strong enthusiasm", "passionate about", "gold standard"). Reference 1–2 specific projects in narrative form (told differently from the CV bullets), connect them to the company's specific product/mission, and plainly state student timeline and availability.

### 5. Layout, LaTeX & Formatting Guardrails

- **Strict 1-Page Limit (Fresher/Intern Standard):** Every compiled CV and every Cover Letter MUST fit strictly on **1 single page** (A4 size). Automatically adjust spacing or trim secondary bullets if a CV ever spills onto page 2.
- **LaTeX Hygiene:** Never wrap numbers, fractions, or units (like `9.42/10` or `5 req/min`) in LaTeX math mode (`$...$`) or tildes (`~`). Render single-year projects as `2025` (never `2025-2025`). Use clean ASCII hyphens for date ranges.
- **Visual Consistency:** Single clean font, 10–10.5pt body text, plain standard bullets (no emojis or decorative icons), left-aligned text, single-line contact header (`Lucknow, Uttar Pradesh, India` with working clickable links for GitHub, LinkedIn, and live demos), and ensure headings never sit orphaned at the bottom of a page.
- **AI Tooling Attribution:** When mentioning agentic coding or AI tooling in CVs or cover letters, explicitly reference **Claude Code** by name.

### 6. Dynamic Project Ranking & Proportional Depth

- **Relevance-Based Ordering:** For every job application, evaluate all projects in `01-candidate-profile.md` against the target company's tech stack and domain. Order the projects from highest relevance to lowest relevance.
- **Fallback Order:** If relevance is equal or cannot be clearly ranked, default strictly to the canonical order in `01-candidate-profile.md` and `main_example.tex` (`GPUCloud`, `INSPIRE`, `MindsViewMsg`).
- **Proportional Bullet Allocation:** Allocate bullet depth dynamically based on the ranking to achieve optimal vertical density:
  - **Primary (Top-Ranked) Project:** Include 5–6 comprehensive bullets from the master profile, ordered by relevance to the role.
  - **Secondary Projects:** Include 3–4 strong bullets each from the master profile.
  - **Experience & Leadership:** Include all 3 bullets from the master profile.
  - **Tech Stack Lines:** Always include the explicit `Tech Stack:` summary line beneath each project entry as written in the master profile.

### 7. Page Density & Vertical Fill (85–95% Single-Page Target)

- **Target Coverage:** Every compiled CV must fill 85% to 95% of a single A4 page. Never leave more than 15% whitespace at the bottom (bottom space <= 15%), and never spill onto page 2.
- **Categorized Technical Skills:** Display the Technical Skills section broken out into its full category rows (Languages, Frontend, Backend, Auth & Security, Database & Cloud, Infra & DevOps, etc.) rather than collapsing them into a minimal block.
- **Complete Education & Achievements:** Include full education metadata (degree, institution, dates, CGPA, and relevant coursework) alongside verified honors from the master profile.
- **LaTeX Geometry & Spacing Calibration:**
  - Use balanced A4 margins (`top=0.5in, bottom=0.5in, left=0.55in, right=0.55in`), `10pt` or `10.5pt` body font, and `\linespread{1.08}`.
  - Use consistent vertical spacing (`\vspace{4pt}` to `\vspace{6pt}` between sections and `\itemsep 2pt` between list items). If a generated CV falls below 85% page fill, expand bullet inclusion from the master profile before adjusting spacing; if it exceeds 1 page, tighten `\itemsep` or trim the lowest-priority bullet on the lowest-ranked project.

---

### 8. Header Layout & Spacing Guardrails (Zero Collision Rule)
- **No Negative Vertical Spacing:** Never use negative `\vspace` between the contact header and the first body paragraph/summary. Always close the centered header block properly with `\par\vspace{6pt}` (or an explicit blank line + `\vspace{4pt}`) before starting the summary text so the contact line and summary never overlap or collide.
- **Single-Line Plain Contact Bar:** Put location and all contact links on one clean, centered line separated by vertical pipes (`|`), with NO icons/emojis (`\faMobile`, `\faEnvelope`, etc.):
  `Lucknow, Uttar Pradesh, India | +91-9451116684 | ishanrastogi987654321@gmail.com | LinkedIn | GitHub`
- **Subtle Link Styling:** Configure `\hypersetup{colorlinks=true, urlcolor=black}` (or a dark slate/navy matching the heading accent) instead of bright default blue (`urlcolor=blue`), keeping the links clickable without visual clutter.

---

## Candidate Profile Summary

### Identity & Contact

- **Name:** Ishan Rastogi
- **Location:** Lucknow, Uttar Pradesh, India
- **Phone:** +91-9451116684
- **Email:** ishanrastogi987654321@gmail.com
- **LinkedIn:** https://linkedin.com/in/ishan-rastogi-303550225
- **GitHub:** https://github.com/ishanrastogi98
- **Status:** Undergraduate Student (B.Tech CSE, IIIT Bhopal, Expected Graduation: August 2028)
- **Languages:** English (Professional working proficiency / Fluent), Hindi (Native)

### Education

- **B.Tech in Computer Science and Engineering** (2024 - Present, Expected August 2028) - Indian Institute of Information Technology, Bhopal
  - Current CGPA: 9.42 / 10
  - Coursework: Data Structures & Algorithms, Object-Oriented Programming, Database Management Systems, Operating Systems, Computer Networks
  - Honors: JEE Mains 2024 — 98.84 Percentile (Top 1.2% nationally among 1.4 million candidates)

### Professional Experience

- **Tech Coordinator** (2024 - Present) — **INSPIRE, IIIT Bhopal** (Bhopal, India)
  - Co-developed and maintained the official web platform in a 2-person core engineering team using Next.js 16 and React 19.
  - Coordinated technical workflows including authentication, database integration, and deployment processes.
  - Collaborated with core team members to support scalable systems for events, quizzes, and registrations.

### Independent Projects

- **GPUCloud — Distributed GPU Rental Platform** (2026 - Ongoing)
  - Next.js 16 control plane with Express host agent for compute rentals.
  - Docker tmpfs-backed ephemeral container volumes (1-2GB cap) and GPU device locking.
  - Action-scoped JWTs (60s expiry, unique nonce) and on-demand Cloudflare Tunnels.
  - Background reaper cron with 4-hour session limits and 960-minute lifetime free-tier limit.
  - Razorpay payments with HMAC-SHA256 webhook verification, 20 req/min rate limiter, and PostgreSQL (Neon) with Drizzle ORM using `FOR UPDATE SKIP LOCKED` (0% collision rate).
- **INSPIRE Club Official Website** (2025)
  - Official web portal for IIIT Bhopal technical club (inspire-bhopal.vercel.app) using Next.js 16 and React 19.
  - Firebase Auth/Admin SDK, Firestore, Cloudinary, automated time-bound quiz workflows, and SSR SEO.
- **MindsViewMsg — Anonymous Messaging Platform** (2025)
  - Privacy-first messaging platform (mindsviewmsg.vercel.app) using Next.js 16, TypeScript, NextAuth.js (bcrypt), strict Zod validation, and 5-tier LRU cache rate limiting (e.g. 5 msgs/min).

---

## Verification Checklist

After creating or updating any CV or cover letter, compile and verify **all** of the following before presenting:

### 1. Factual Accuracy & Guardrail Verification

- [ ] Every claim, metric, and skill is grounded in `01-candidate-profile.md` (no fabricated ranks, no unmeasured percentages).
- [ ] Student stage is transparent (Undergraduate at IIIT Bhopal, Class of 2028).
- [ ] No buzzwords added ("open-source" only with repo link, no unwarranted "CI/CD" or "TDD").
- [ ] Single-line contact header uses `Lucknow, Uttar Pradesh, India` with working links.
- [ ] Single-year projects formatted as `2025` (not `2025-2025`).
- [ ] Date fields use single ASCII hyphens.
- [ ] Numbers, CGPA, and units are not in LaTeX math mode (write `9.42/10`, not `$9.42/10$`).

### 2. Compiled PDF Verification (MANDATORY)

- [ ] **CV is strictly 1 page (A4)** — compiled with `lualatex`. Verified via `tools/verify_pdf.py cv/main_<company>_<role>.pdf --pages 1`.
- [ ] **Cover letter is strictly 1 page (A4)** — compiled with `xelatex`. Verified via `tools/verify_pdf.py cover_letters/cover_<company>_<role>.pdf --pages 1`.
- [ ] **Cover letter contains NO bullet points** — written in 3–4 natural prose paragraphs.
- [ ] **Layout is clean** — checked via `tools/verify_layout.py`. No orphaned headers, no holes.
