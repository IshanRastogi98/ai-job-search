from pathlib import Path

# 1. Update CLAUDE.md
claude_path = Path("CLAUDE.md")
claude_text = claude_path.read_text(encoding="utf-8")

# Fix target coverage line if needed
claude_text = claude_text.replace(
    "Every compiled CV must fill 75% to 85% of a single A4 page. Never leave more than 25% whitespace at the bottom (bottom space <= 25%), and never spill onto page 2.",
    "Every compiled CV must fill 85% to 95% of a single A4 page. Never leave more than 15% whitespace at the bottom (bottom space <= 15%), and never spill onto page 2."
)

header_rules = """### 8. Header Layout & Spacing Guardrails (Zero Collision Rule)
- **No Negative Vertical Spacing:** Never use negative `\\vspace` between the contact header and the first body paragraph/summary. Always close the centered header block properly with `\\par\\vspace{6pt}` (or an explicit blank line + `\\vspace{4pt}`) before starting the summary text so the contact line and summary never overlap or collide.
- **Single-Line Plain Contact Bar:** Put location and all contact links on one clean, centered line separated by vertical pipes (`|`), with NO icons/emojis (`\\faMobile`, `\\faEnvelope`, etc.):
  `Lucknow, Uttar Pradesh, India | +91-9451116684 | ishanrastogi987654321@gmail.com | LinkedIn | GitHub`
- **Subtle Link Styling:** Configure `\\hypersetup{colorlinks=true, urlcolor=black}` (or a dark slate/navy matching the heading accent) instead of bright default blue (`urlcolor=blue`), keeping the links clickable without visual clutter."""

if "### 8. Header Layout & Spacing Guardrails" not in claude_text:
    target_pos = claude_text.find("## Candidate Profile Summary")
    if target_pos != -1:
        claude_text = claude_text[:target_pos] + header_rules + "\n\n---\n\n" + claude_text[target_pos:]
        print("Added Header Rules to CLAUDE.md")
    else:
        print("Warning: Candidate Profile Summary not found in CLAUDE.md")

claude_path.write_text(claude_text, encoding="utf-8")

# 2. Update 05-cv-templates.md
cv_path = Path(".claude/skills/job-application-assistant/05-cv-templates.md")
cv_text = cv_path.read_text(encoding="utf-8")

cv_header_rules = """### 7. Header Layout & Spacing Guardrails (Zero Collision Rule)
- **No Negative Vertical Spacing:** Never use negative `\\vspace` between the contact header and the first body paragraph/summary. Always close the centered header block properly with `\\par\\vspace{6pt}` (or an explicit blank line + `\\vspace{4pt}`) before starting the summary text so the contact line and summary never overlap or collide.
- **Single-Line Plain Contact Bar:** Put location and all contact links on one clean, centered line separated by vertical pipes (`|`), with NO icons/emojis (`\\faMobile`, `\\faEnvelope`, etc.):
  `Lucknow, Uttar Pradesh, India | +91-9451116684 | ishanrastogi987654321@gmail.com | LinkedIn | GitHub`
- **Subtle Link Styling:** Configure `\\hypersetup{colorlinks=true, urlcolor=black}` (or a dark slate/navy matching the heading accent) instead of bright default blue (`urlcolor=blue`), keeping the links clickable without visual clutter.\n\n"""

if "### 7. Header Layout & Spacing Guardrails" not in cv_text:
    target_pos = cv_text.find("## Document Structure (Strict 1-Page Standard)")
    if target_pos != -1:
        cv_text = cv_text[:target_pos] + cv_header_rules + cv_text[target_pos:]
        print("Added Header Rules to 05-cv-templates.md")
    else:
        print("Warning: Document Structure not found in 05-cv-templates.md")

# Update document structure sample in 05-cv-templates.md
sample_old = r"""\AtEndPreamble{\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,
    urlcolor=blue,
    pdftitle={Ishan Rastogi - CV},
    pdfpagemode=UseNone,
}}
\usepackage[top=0.5in,bottom=0.5in,left=0.55in,right=0.55in]{geometry}
\linespread{1.08}
\usepackage{import}

% Personal data (Single-line contact header)
\name{Ishan}{Rastogi}
\address{Lucknow, Uttar Pradesh, India}{}{}
\phone[mobile]{+91-9451116684}
\email{ishanrastogi987654321@gmail.com}
\extrainfo{\href{https://linkedin.com/in/ishan-rastogi-303550225}{LinkedIn} | \href{https://github.com/ishanrastogi98}{GitHub}}

\begin{document}
\makecvtitle
\vspace{-16pt}"""

sample_new = r"""\AtEndPreamble{\hypersetup{
    colorlinks=true,
    linkcolor=black,
    filecolor=black,
    urlcolor=black,
    pdftitle={Ishan Rastogi - CV},
    pdfpagemode=UseNone,
}}
\usepackage[top=0.5in,bottom=0.5in,left=0.55in,right=0.55in]{geometry}
\linespread{0.98}
\usepackage{import}

\name{Ishan}{Rastogi}

% Single-line plain contact bar (Zero Collision Rule)
\renewcommand*{\makecvtitle}{%
  \begin{center}%
    {\namefont{\color{color1}Ishan Rastogi}}\par\vspace{3pt}%
    {\small%
      Lucknow, Uttar Pradesh, India%
      \ \textbar\ %
      +91-9451116684%
      \ \textbar\ %
      \href{mailto:ishanrastogi987654321@gmail.com}{ishanrastogi987654321@gmail.com}%
      \ \textbar\ %
      \href{https://linkedin.com/in/ishan-rastogi-303550225}{LinkedIn}%
      \ \textbar\ %
      \href{https://github.com/ishanrastogi98}{GitHub}%
    }\par\vspace{4pt}%
  \end{center}%
}

\begin{document}
\makecvtitle"""

if sample_old in cv_text:
    cv_text = cv_text.replace(sample_old, sample_new)
    print("Updated sample in 05-cv-templates.md")
else:
    print("Warning: sample_old not found in 05-cv-templates.md")

cv_path.write_text(cv_text, encoding="utf-8")

# 3. Update cv/main_example.tex
ex_path = Path("cv/main_example.tex")
ex_text = ex_path.read_text(encoding="utf-8")

# Replace urlcolor=blue with urlcolor=black, linkcolor=black
ex_text = ex_text.replace(
    "    linkcolor=blue,\n    filecolor=magenta,\n    urlcolor=blue,",
    "    linkcolor=black,\n    filecolor=black,\n    urlcolor=black,"
)

old_ex_header = r"""% personal data
\name{Ishan}{Rastogi}
\address{Lucknow, Uttar Pradesh, India}{}{}
\phone[mobile]{+91-9451116684}
\email{ishanrastogi987654321@gmail.com}
\extrainfo{\href{https://linkedin.com/in/ishan-rastogi-303550225}{LinkedIn}, \href{https://github.com/ishanrastogi98}{GitHub}}

\begin{document}

\makecvtitle"""

new_ex_header = r"""\name{Ishan}{Rastogi}

% Single-line plain contact bar (Zero Collision Rule)
\renewcommand*{\makecvtitle}{%
  \begin{center}%
    {\namefont{\color{color1}Ishan Rastogi}}\par\vspace{3pt}%
    {\small%
      Lucknow, Uttar Pradesh, India%
      \ \textbar\ %
      +91-9451116684%
      \ \textbar\ %
      \href{mailto:ishanrastogi987654321@gmail.com}{ishanrastogi987654321@gmail.com}%
      \ \textbar\ %
      \href{https://linkedin.com/in/ishan-rastogi-303550225}{LinkedIn}%
      \ \textbar\ %
      \href{https://github.com/ishanrastogi98}{GitHub}%
    }\par\vspace{4pt}%
  \end{center}%
}

\begin{document}

\makecvtitle"""

if old_ex_header in ex_text:
    ex_text = ex_text.replace(old_ex_header, new_ex_header)
    print("Updated header in cv/main_example.tex")
else:
    print("Warning: old_ex_header not found in cv/main_example.tex")

ex_path.write_text(ex_text, encoding="utf-8")
print("All instructions and main_example.tex updated!")
