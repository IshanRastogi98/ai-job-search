import os, sys, subprocess
from pathlib import Path

mik = r"C:\Users\Ishan Rastogi\AppData\Local\Programs\MiKTeX\miktex\bin\x64"
os.environ["PATH"] = mik + os.pathsep + os.environ["PATH"]
os.environ["PYTHONIOENCODING"] = "utf-8"

ROOT = Path("cv")

diagrid_tex = r"""%% CV - Ishan Rastogi (Tailored for Diagrid - Fullstack Software Engineer)
\documentclass[10pt,a4paper,sans]{moderncv}
\moderncvstyle{banking}
\moderncvcolor{blue}

\renewcommand*{\namefont}{\fontsize{20}{22}\bfseries\upshape}
\colorlet{firstnamecolor}{color1}
\colorlet{lastnamecolor}{color1}
\colorlet{namecolor}{color1}
\renewcommand*{\sectionstyle}[1]{{\sectionfont\color{color1}#1}}

\usepackage[utf8]{inputenc}
\ifpdftex\usepackage[T1]{fontenc}\fi
\AtEndPreamble{\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,
    urlcolor=blue,
    pdftitle={Ishan Rastogi - CV (Diagrid)},
    pdfpagemode=UseNone,
}}
\usepackage[top=0.45in,bottom=0.45in,left=0.55in,right=0.55in]{geometry}
\linespread{1.04}
\usepackage{import}

% Personal data (Single-line contact header)
\name{Ishan}{Rastogi}
\address{Lucknow, Uttar Pradesh, India}{}{}
\phone[mobile]{+91-9451116684}
\email{ishanrastogi987654321@gmail.com}
\extrainfo{\href{https://linkedin.com/in/ishan-rastogi-303550225}{LinkedIn} | \href{https://github.com/ishanrastogi98}{GitHub}}

\begin{document}
\makecvtitle
\vspace{-22pt}

% ============================================================
%     PROFILE STATEMENT
% ============================================================
\small{Computer Science undergraduate at IIIT Bhopal (Class of 2028, 9.42/10 CGPA) with hands-on experience in TypeScript, Node.js, React, and container isolation. Builder of distributed compute orchestration systems with atomic concurrency controls and secure host-client protocols, seeking engineering internship or part-time roles.}

\vspace{3pt}

% ============================================================
%     EDUCATION & ACHIEVEMENTS
% ============================================================
\section{Education \& Achievements}
\vspace{2pt}
\begin{itemize}
\item{\cventry{2024-Present}{B.Tech in Computer Science and Engineering}{Indian Institute of Information Technology, Bhopal}{Bhopal, India}{}{\vspace{0.5pt}
In progress, expected August 2028. Current CGPA: \textbf{9.42 / 10}. Coursework: Data Structures \& Algorithms, Operating Systems, Database Management Systems, Computer Networks, Object-Oriented Programming.\\
\textbf{Honors}: Joint Entrance Examination (JEE) Mains 2024 --- \textbf{98.84 Percentile} (Top 1.2\% nationally among 1.4 million candidates).
}}
\end{itemize}

\vspace{-2pt}

% ============================================================
%     TECHNICAL SKILLS
% ============================================================
\section{Technical Skills}
\vspace{2pt}
\begin{itemize}
\item \textbf{Languages \& Runtimes}: TypeScript, JavaScript (Node.js, ES6+), Python, C, C++.
\item \textbf{Frontend Engineering}: React 19, Next.js 16 (App Router), Tailwind CSS, Radix UI, shadcn/ui, Material UI, HTML5, CSS3.
\item \textbf{Backend \& Distributed Systems}: Express.js, Next.js API Routes, RESTful APIs, WebSockets, Docker (Dockerode), Cloudflare Tunnels, Action-Scoped JWTs, Pino.
\item \textbf{Databases \& Storage}: PostgreSQL (Neon), Drizzle ORM, Concurrency Locking (\texttt{FOR UPDATE SKIP LOCKED}), MongoDB, Mongoose, Firebase Firestore, Supabase Storage.
\item \textbf{Payments, Security \& AI}: Razorpay Webhooks, NextAuth.js v5, Firebase Auth / Admin SDK, bcrypt, Claude Code, Git, GitHub, Postman, Zod.
\end{itemize}

\vspace{-2pt}

% ============================================================
%     FEATURED PROJECTS
% ============================================================
\section{Featured Projects}
\vspace{2pt}
\begin{itemize}

\item{\cventry{2026-Ongoing}{GPUCloud: Distributed Compute Orchestration Platform}{Personal Project}{}{}{\vspace{0.5pt}
\textit{Tech Stack: Next.js 16, React 19, TypeScript, Express, PostgreSQL (Neon), Drizzle ORM, Docker (Dockerode), Cloudflare Tunnels, Action-Scoped JWTs, Razorpay, Supabase Storage, Pino, Zod, Tailwind CSS.}
\begin{itemize}
    \item {Architected an end-to-end distributed system pairing a Next.js control plane with an Express host agent for remote container allocation.}
    \item {Enforced strict container isolation using Docker tmpfs-backed volumes (1-2GB cap) and GPU device locking, with atomic rollback on failure.}
    \item {Secured host-client communication with action-scoped JWTs (60s expiry, unique nonce) and dynamically routed containers via Cloudflare Tunnels.}
    \item {Engineered a background reaper cron enforcing 4-hour session caps and a 960-minute lifetime free-tier limit, with two-way state reconciliation.}
    \item {Integrated Razorpay payments with HMAC-SHA256 webhook verification, an in-memory rate limiter (20 req/min per IP), and modeled relational data in PostgreSQL (Neon) via Drizzle ORM with atomic \texttt{FOR UPDATE SKIP LOCKED} queueing (0\% collision rate under load).}
\end{itemize}}}

\vspace{2pt}

\item{\cventry{2025}{INSPIRE: Official Engineering Web Platform}{\urlstyle{same}\href{https://inspire-bhopal.vercel.app}{inspire-bhopal.vercel.app}}{}{}{\vspace{0.5pt}
\textit{Tech Stack: Next.js 16, React 19, Firebase Auth, Firebase Admin SDK, Firestore, Tailwind CSS, Material UI (MUI), Zod, React Hook Form, Cloudinary.}
\begin{itemize}
    \item {Engineered the official technical club web portal using Next.js 16 and React 19, implementing dynamic metadata, SSR, and dynamic routing for SEO.}
    \item {Built authentication, session management, and role-based access control (RBAC) using Firebase Auth and Firebase Admin SDK.}
    \item {Designed automated evaluation pipelines for time-bound competitive quizzes, processing concurrent user submissions with server-side validation.}
\end{itemize}}}

\vspace{2pt}

\item{\cventry{2025}{MindsViewMsg: Anonymous Messaging Platform}{\urlstyle{same}\href{https://mindsviewmsg.vercel.app}{mindsviewmsg.vercel.app}}{}{}{\vspace{0.5pt}
\textit{Tech Stack: Next.js 16, React 19, TypeScript, NextAuth.js, MongoDB, Mongoose, Zod, Tailwind CSS, Radix UI, Framer Motion, bcrypt, LRU Cache.}
\begin{itemize}
    \item {Developed a privacy-first web application using Next.js 16, TypeScript, NextAuth.js (bcrypt), and strict server-side validation via Zod schemas.}
    \item {Implemented a 5-tier LRU cache rate limiter across sensitive endpoints (throttling requests to 5 msgs/min) to mitigate abusive traffic.}
    \item {Constructed structured MongoDB and Mongoose database models with strict schema constraints and sanitized error telemetry.}
\end{itemize}}}

\end{itemize}

\vspace{-2pt}

% ============================================================
%     EXPERIENCE & LEADERSHIP
% ============================================================
\section{Experience \& Leadership}
\vspace{2pt}
\begin{itemize}

\item{\cventry{2024-Present}{Tech Coordinator}{INSPIRE, IIIT Bhopal}{Bhopal, India}{}{\vspace{0.5pt}
\begin{itemize}
    \item {Co-developed and maintained the club official web platform as part of a 2-person core engineering team, using Next.js 16 and React 19.}
    \item {Coordinated technical workflows including authentication, database integration, and deployment processes across student platforms.}
    \item {Collaborated with core team members to support scalable systems for events, quizzes, and registrations, utilizing Claude Code for accelerated iteration.}
\end{itemize}}}

\end{itemize}

\end{document}
"""

Path("cv/test_diagrid.tex").write_text(diagrid_tex, encoding="utf-8")
r = subprocess.run(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "test_diagrid.tex"], cwd="cv", capture_output=True, text=True, errors="replace")
print("Compile returncode:", r.returncode)
if r.returncode != 0:
    print(r.stdout[-1500:])

v = subprocess.run([sys.executable, "tools/verify_pdf.py", "cv/test_diagrid.pdf", "--pages", "1"], capture_output=True, text=True, errors="replace")
print("verify_pdf:", v.stdout.strip(), v.stderr.strip())

l = subprocess.run([sys.executable, "tools/verify_layout.py", "cv/test_diagrid.pdf"], capture_output=True, text=True, errors="replace")
print("verify_layout:\n", l.stdout.strip(), l.stderr.strip())
