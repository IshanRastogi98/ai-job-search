# Search Queries for Job Scraper

<!-- SETUP: Customize these queries based on your skills, target roles, and location -->

## Installed portal CLIs (primary for `/scrape`)

`/scrape` discovers every portal skill under `.agents/skills/*/SKILL.md` and runs its CLI first. Shipped country-agnostic CLIs include `linkedin-search` and `freehire-search`; any skill you add with `/add-portal` is included the same way. You do **not** need a matching `site:` line below for those CLIs to run.

The `site:` query templates in this file are the **WebSearch fallback** — for portals without a CLI, company career pages, or when a CLI fails.

**Language scope:** English is the declared working and CV language. All queries are optimized in English.

## Search Sites

Primary:
- **linkedin.com/jobs** - LinkedIn job listings (filter: Remote, India, Bengaluru, Hyderabad, Pune, Gurugram, Noida); also covered by `linkedin-search` CLI
- **wellfound.com** - High-growth startups and modern product companies (Full Stack, Remote, Internships)
- **cuvette.tech** - Tech internships and early-career software engineering roles in India
- **instahyre.com** - Premium tech and product startups in India

Secondary (company career pages via Google):
- Direct Google searches with `site:` filters for target engineering startups and tech companies

## Query Categories

Queries are grouped by priority.

### Priority 1: Full Stack Development (Next.js / React / TypeScript)

These match your strongest core stack and day-to-day focus:

```
site:linkedin.com/jobs "Full Stack Developer" "Next.js" Remote
site:linkedin.com/jobs "Full Stack Engineer" "React" "TypeScript" India
site:wellfound.com "Full Stack" "Next.js" "TypeScript"
site:linkedin.com/jobs "Full Stack Intern" "Next.js"
site:linkedin.com/jobs "React Developer" "Node.js" Remote
```

### Priority 2: Software Engineering & Backend Systems

These match your systems, backend, and infrastructure capabilities:

```
site:linkedin.com/jobs "Software Engineer" "Node.js" "PostgreSQL" Remote
site:linkedin.com/jobs "Backend Developer" "TypeScript" "Docker" India
site:linkedin.com/jobs "Software Developer" "TypeScript" "REST API" Remote
site:wellfound.com "Software Engineer" "TypeScript" "PostgreSQL"
```

### Priority 3: Software Engineering Internships (Summer 2027 / 6-Month)

Targeted at high-impact internship terms and student developer opportunities:

```
site:linkedin.com/jobs "Software Engineer Intern" India Remote OR Bengaluru OR Hyderabad OR Pune OR Gurugram
site:linkedin.com/jobs "SDE Intern" "Full Stack" 2027 OR 2028
site:cuvette.tech "Software Development Intern" "React" OR "Node.js"
site:linkedin.com/jobs "Software Engineering Intern" "TypeScript" "Next.js"
```

### Priority 4: Broader Cloud & Web Engineering

Wider net for modern web and cloud infrastructure roles:

```
site:linkedin.com/jobs "Frontend Engineer" "React" "Tailwind" Remote
site:linkedin.com/jobs "Cloud Engineer" "Docker" Remote
site:wellfound.com "Frontend Developer" "React 19" OR "Next.js"
```

## Location Filter

When evaluating results, verify the role meets the following preferences:
- **Ideal:** Remote (Worldwide or India)
- **Ideal (Local):** Bhopal, Madhya Pradesh
- **Acceptable (Major Indian Tech Hubs):** Bengaluru, Hyderabad, Pune, Gurugram, Noida, Delhi-NCR (for Summer 2027 / 6-month on-site or hybrid internships)
- **Borderline:** Other tier-1/tier-2 hubs with negotiable remote flexibility
- **Too Far / Exclude:** Unpaid internships; mandatory on-site roles outside major hubs without relocation/housing support

## Language Filter

Your declared languages are:
- **English:** Professional working proficiency / Fluent
- **Hindi:** Native

Apply `04-job-evaluation.md`'s Language Gate: any posting requiring a language other than English or Hindi as a job condition is excluded before scoring.

## Date Filter

Only include jobs posted within the last 14 days, or with an application deadline that has not yet passed. If a posting date cannot be determined, include it but flag as "date unknown".

## Adapting Queries

If specifying a focus area, select queries from the matching category and also generate 2-3 custom queries for that focus. For example:
- `/scrape internship` -> Priority 3 internship queries + targeted SDE intern queries
- `/scrape remote nextjs` -> Priority 1 queries scoped strictly to Remote
