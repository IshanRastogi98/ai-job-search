---
framework_version: 1.2.0
---

# Candidate Profile

<!-- Master Resume and Single Source of Truth for Ishan Rastogi -->

## Permanent Guardrails for Applications

### 1. Truthfulness & Zero Fabrication (Global Rule)
- **Source of Truth:** Every claim, metric, project title, and technical skill must come strictly from this master profile. Reorder, trim, and emphasize existing bullets to match a job description, but NEVER invent new metrics, unverified percentage gains, academic ranks (e.g. no "Rank 1"), or unverified claims.
- **No Unmeasured Numbers:** Only use exact metrics present in this profile (e.g., 9.42/10 CGPA, 98.84 percentile, 0% job-collision rate, 60-second JWT expiry, 1-2GB tmpfs cap, 4-hour session limit, 960-minute free-tier cap, 20 req/min rate limit, 5 msgs/min rate limit). Never invent unmeasured percentage improvements or performance gains.
- **No Defenseless Practices or Buzzwords:** Never claim "open-source" without an explicit public repository link. Do not add CI/CD, GitHub Actions, TDD, unit testing, or buzzwords like "high-throughput" or "production-grade" unless explicitly documented in this profile.
- **Role & Scope Fidelity:** Maintain exact project names and role scopes. Do not upgrade collaborative or 2-person team roles into solo management or director claims.

### 2. Candidate Stage & Skills Filtering
- **Fresher / Student Transparency:** Always state clearly that Ishan is an undergraduate B.Tech CSE student at IIIT Bhopal (2024–Present, Expected Graduation: August 2028) targeting internships, part-time, or student-eligible engineering roles.
- **20-Minute Quiz Rule for Skills:** Only list technical skills that are directly backed by a project or experience entry on the CV. Omit any tools, libraries, or languages that have no project evidence.

### 3. Content Quality & Structure
- **Summary:** Maximum 1–2 concise lines without generic fluff.
- **Bullet Density:** 2–4 strongest, outcome-led bullets per project/experience. Drop weaker bullets to save vertical space.
- **Zero Repetition:** Do not repeat the same sentences across summary, skills, project bullets, and cover letter.

### 4. Cover Letter Standards
- **Format:** Strictly 1 page, written in 3–4 short, natural prose paragraphs. NEVER use bullet points in a cover letter.
- **Tone & Content:** Eliminate generic filler ("strong enthusiasm", "passionate about", "gold standard"). Reference 1–2 specific projects in narrative form, connect them to the company's product/mission, and plainly state availability and student timeline.

### 5. Layout, LaTeX & Formatting Guardrails
- **Strict 1-Page Limit (Fresher/Intern Standard):** Every compiled CV and every Cover Letter MUST fit strictly on 1 single page (A4 size). Automatically adjust spacing or trim secondary bullets if a CV ever spills onto page 2.
- **LaTeX Hygiene:** Never wrap numbers, fractions, or units (like `9.42/10` or `5 req/min`) in LaTeX math mode (`$...$`) or tildes (`~`). Render single-year projects as `2025` (never `2025-2025`). Use clean ASCII hyphens for date ranges.
- **Visual Consistency:** Single clean font, 10–10.5pt body text, plain standard bullets (no emojis or decorative icons), left-aligned text, single-line contact header (`Bhopal, Madhya Pradesh, India` with working clickable links for GitHub, LinkedIn, and live demos), and ensure headings never sit orphaned at the bottom of a page.

---

## Identity
- **Name:** Ishan Rastogi
- **Location:** Bhopal, Madhya Pradesh, India
- **Phone:** +91-9451116684
- **Email:** ishanrastogi987654321@gmail.com
- **LinkedIn:** https://linkedin.com/in/ishan-rastogi-303550225
- **GitHub:** https://github.com/ishanrastogi98
- **Status:** Undergraduate Student (B.Tech CSE, IIIT Bhopal, Class of 2028) & Tech Coordinator at INSPIRE
- **Constraints:** Highly prefers Remote (India & International). Open to on-site/hybrid internships in major Indian tech hubs (Bengaluru, Hyderabad, Pune, Gurugram/Noida). Targeting Summer 2027 internships, 6-month internships, and remote part-time/contract SWE roles.

### Languages
| Language | Level | Notes |
|----------|-------|-------|
| English | Professional working proficiency / Fluent | Primary working language for codebase, documentation, and communication |
| Hindi | Native | Native fluency |

---

## Education

| Degree | Period | Institution | Details |
|--------|--------|-------------|---------|
| B.Tech in Computer Science and Engineering | 2024 - Present (Expected August 2028) | Indian Institute of Information Technology, Bhopal | Current CGPA: 9.42 / 10. Core Topics: Data Structures & Algorithms, Object-Oriented Programming, Database Management Systems, Operating Systems, Computer Networks. JEE Mains 2024: 98.84 Percentile. |

---

## Professional Experience

### Tech Coordinator — INSPIRE, IIIT Bhopal (2024 - Present)
*Bhopal, India (Official Technical Club of IIIT Bhopal)*
- Co-developed and maintained the club official web platform as part of a 2-person core engineering team, using Next.js 16 and React 19.
- Coordinated technical workflows including authentication, database integration, and deployment processes.
- Collaborated with core team members to support scalable systems for events, quizzes, and registrations.

---

## Independent Projects

### GPUCloud — Distributed GPU Rental Platform (2026 - Ongoing)
*Tech Stack:* Next.js 16, React 19, TypeScript, Express, PostgreSQL (Neon), Drizzle ORM, Docker (Dockerode), Cloudflare Tunnels, JWT, Razorpay, Supabase Storage, NextAuth.js v5, Pino, Zod, Tailwind CSS, shadcn/ui, Radix UI.
- Built a distributed platform for GPU owners to rent out idle compute time, pairing a Next.js control plane with an Express host agent.
- Enforced strict container isolation using Docker tmpfs-backed ephemeral volumes capped at 1-2GB per session and GPU device locking to prevent cross-session VRAM contention, with atomic rollback on provisioning failure.
- Secured host-client communication with action-scoped JWTs (60-second expiry, unique nonce), validated by custom auth middleware; exposed containers dynamically via Cloudflare Tunnels.
- Engineered a background reaper cron enforcing 4-hour session caps and a 960-minute lifetime free-tier limit, with two-way reconciliation to reclaim orphaned containers after network partitions.
- Integrated Razorpay payments with HMAC-SHA256 webhook verification, an in-memory token-bucket rate limiter (20 req/min per IP), and modeled relational data in PostgreSQL (Neon) via Drizzle ORM with atomic `FOR UPDATE SKIP LOCKED` queueing (0% job-collision rate under concurrent load).

### INSPIRE — IIIT Bhopal Club Official Website (2025)
*Live:* https://inspire-bhopal.vercel.app  
*Tech Stack:* Next.js 16, React 19, Firebase Auth, Firebase Admin SDK, Firestore, Tailwind CSS, Material UI (MUI), Zod, React Hook Form, Framer Motion, Cloudinary.
- Developed the official website for IIIT Bhopal's technical club using Next.js 16 and React 19, implementing dynamic metadata, server-side rendering (SSR), and dynamic routing for SEO.
- Built authentication, session management, and role-based access control (RBAC) using Firebase Auth and Firebase Admin SDK.
- Designed automated quiz workflows with time-bound server-side evaluation and validated submissions, integrating Firestore and Cloudinary for media and resource management.

### MindsViewMsg — Anonymous Messaging Platform (2025)
*Live:* https://mindsviewmsg.vercel.app  
*Tech Stack:* Next.js 16, React 19, TypeScript, NextAuth.js, MongoDB, Mongoose, Zod, Tailwind CSS, Radix UI, Framer Motion, bcrypt, LRU Cache.
- Built a privacy-first anonymous messaging application using Next.js 16, TypeScript, NextAuth.js, and bcrypt credential hashing.
- Designed strict server-side validation using Zod to block malformed payloads and prevent injection abuse.
- Implemented per-route LRU-based rate limiting across 5 endpoint tiers (e.g., 5 messages/min, 5 verification attempts per 10 min, 3 code resends per 15 min) to throttle abuse and mitigate spam requests.

---

## Technical Skills (Filtered by 20-Minute Quiz Rule)

### Languages & Runtimes
- TypeScript, JavaScript (Node.js, ES6+), Python, C, C++

### Frontend Engineering
- React 19, Next.js 16 (App Router), Tailwind CSS, Radix UI, shadcn/ui, Material UI, HTML5, CSS3

### Backend & Systems
- Express.js, Next.js API Routes, RESTful APIs, WebSockets, Docker (Dockerode), Cloudflare Tunnels, Action-Scoped JWTs, Pino Logging

### Databases & Cloud Storage
- PostgreSQL (Neon), Drizzle ORM, Row-Level Locking (`FOR UPDATE SKIP LOCKED`), MongoDB, Mongoose, Firebase Firestore, Supabase Storage

### Payments & Auth
- Razorpay Checkout & HMAC-SHA256 Webhooks, NextAuth.js v5, Firebase Auth / Admin SDK, bcrypt

### Engineering Tools & AI Workflows
- Git, GitHub, Claude Code, Vercel, Postman, Zod

---

## Honors and Awards
- **Joint Entrance Examination (JEE) Mains 2024**: 98.84 Percentile (National level engineering entrance examination in India among 1.4 million candidates).

---

## References
- References available upon request.
