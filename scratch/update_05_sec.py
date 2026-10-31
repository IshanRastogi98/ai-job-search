from pathlib import Path

cv_path = Path(".claude/skills/job-application-assistant/05-cv-templates.md")
cv_text = cv_path.read_text(encoding="utf-8")

old_sec = """### 6. Page Density & Vertical Fill (85–95% Single-Page Target)

- **Target Coverage:** Every compiled CV must fill 75% to 85% of a single A4 page. Never leave more than 25% whitespace at the bottom (bottom space <= 25%), and never spill onto page 2.
- **Categorized Technical Skills:** Display the Technical Skills section broken out into its full category rows (Languages, Frontend, Backend, Auth & Security, Database & Cloud, Infra & DevOps, etc.) rather than collapsing them into a minimal block.
- **Complete Education & Achievements:** Include full education metadata (degree, institution, dates, CGPA, and relevant coursework) alongside verified honors from the master profile.
- **LaTeX Geometry & Spacing Calibration:**
  - Use balanced A4 margins (`top=0.5in, bottom=0.5in, left=0.55in, right=0.55in`), `10pt` or `10.5pt` body font, and `\\linespread{1.08}`.
  - Use consistent vertical spacing (`\\vspace{4pt}` to `\\vspace{6pt}` between sections and `\\itemsep 2pt` between list items). If a generated CV falls below 85% page fill, expand bullet inclusion from the master profile before adjusting spacing; if it exceeds 1 page, tighten `\\itemsep` or trim the lowest-priority bullet on the lowest-ranked project.

## Document Structure

```latex
\\documentclass[10pt,a4paper,sans]{moderncv}
\\moderncvstyle{banking}
\\moderncvcolor{blue}

% Force the name and section headings to render in moderncv blue (color1).
% Default banking leaves them black: moderncvstylebanking.sty's \\colorlet
% copies (not aliases) the pre-scheme accent colour, so the name colours are
% frozen before \\moderncvcolor runs. Re-let them after. \\namefont is the hook
% every name-style macro routes through, so this also works on moderncv 2.3.1
% (Debian/Ubuntu apt), which has no \\firstnamestyle/\\lastnamestyle at all.
\\renewcommand*{\\namefont}{\\fontsize{34}{36}\\bfseries\\upshape}
\\colorlet{firstnamecolor}{color1}
\\colorlet{lastnamecolor}{color1}
\\colorlet{namecolor}{color1}
\\renewcommand*{\\sectionstyle}[1]{{\\sectionfont\\color{color1}#1}}

\\usepackage[utf8]{inputenc}
% pdflatex fallback only (the documented engine is lualatex, which skips this
% branch). Without T1 font encoding pdflatex builds accented letters with
% \\accent, and the PDF text layer stores them decomposed - `e` + U+0300 rather
% than U+00E8 - so an ATS keyword match on "Genève" fails while the page looks
% right. moderncv 2.5 loads T1 itself under pdflatex; 2.3.1 (Debian/Ubuntu apt)
% does not. \\ifpdftex comes from iftex, which every moderncv version loads.
\\ifpdftex\\usepackage[T1]{fontenc}\\fi
% moderncv loads hyperref itself in an \\AtEndPreamble hook, so \\hypersetup
% must go in an \\AtEndPreamble of our own: on moderncv < 2.4 a top-level
% \\usepackage{hyperref} clashes with the class's own
% \\RequirePackage[unicode]{hyperref}. From 2.4.0 the class passes its options
% through \\PassOptionsToPackage instead, which is what removes that clash.
\\AtEndPreamble{\\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,
    urlcolor=blue,
    pdftitle={Ishan Rastogi - CV},
    % Keep pdfpagemode=UseNone: this block runs after moderncv's own
    % \\AtEndPreamble (moderncv.cls sets pdfpagemode there), so a FullScreen
    % value here would win and open every CV in fullscreen presentation mode.
    pdfpagemode=UseNone,
}}
\\usepackage[scale=0.80]{geometry}
\\usepackage{import}

% Personal data
\\name{Ishan}{Rastogi}
% If you have no address to list, DELETE this whole line. \\address{}{}{} fails
% with "There's no line here to end" on every moderncv version.
\\address{Lucknow, Uttar Pradesh, India}{}{}
\\phone[mobile]{+91-9451116684}
\\email{ishanrastogi987654321@gmail.com}
\\extrainfo{\\href{https://linkedin.com/in/ishan-rastogi-303550225}{LinkedIn}, \\href{https://github.com/ishanrastogi98}{GitHub}}

\\begin{document}
\\makecvtitle

% 1. Profile statement (1-3 sentences, tailored per role)
% 2. Skills section
% 3. Education section
% 4. Professional Experience section
% 5. Selected Publications (if applicable)
% 6. Honors and Awards (if applicable)
% 7. References

\\end{document}
```"""

new_sec = """### 6. Page Density & Vertical Fill (85–95% Single-Page Target)
- **Target Coverage:** Every compiled CV must fill 85% to 95% of a single A4 page. Never leave more than 15% whitespace at the bottom (bottom space <= 15%), and never spill onto page 2.
- **Categorized Technical Skills:** Display the Technical Skills section broken out into its full category rows (Languages, Frontend, Backend, Auth & Security, Database & Cloud, Infra & DevOps, etc.) rather than collapsing them into a minimal block.
- **Complete Education & Achievements:** Include full education metadata (degree, institution, dates, CGPA, and relevant coursework) alongside verified honors from the master profile.
- **LaTeX Geometry & Spacing Calibration:**
  - Use balanced A4 margins (`top=0.5in, bottom=0.5in, left=0.55in, right=0.55in`), `10pt` or `10.5pt` body font, and `\\linespread{0.98}`.
  - Use consistent vertical spacing (`\\vspace{4pt}` to `\\vspace{6pt}` between sections and `\\itemsep 2pt` between list items). If a generated CV falls below 85% page fill, expand bullet inclusion from the master profile before adjusting spacing; if it exceeds 1 page, tighten `\\itemsep` or trim the lowest-priority bullet on the lowest-ranked project.

### 7. Header Layout & Spacing Guardrails (Zero Collision Rule)
- **No Negative Vertical Spacing:** Never use negative `\\vspace` between the contact header and the first body paragraph/summary. Always close the centered header block properly with `\\par\\vspace{6pt}` (or an explicit blank line + `\\vspace{4pt}`) before starting the summary text so the contact line and summary never overlap or collide.
- **Single-Line Plain Contact Bar:** Put location and all contact links on one clean, centered line separated by vertical pipes (`|`), with NO icons/emojis (`\\faMobile`, `\\faEnvelope`, etc.):
  `Lucknow, Uttar Pradesh, India | +91-9451116684 | ishanrastogi987654321@gmail.com | LinkedIn | GitHub`
- **Subtle Link Styling:** Configure `\\hypersetup{colorlinks=true, urlcolor=black}` (or a dark slate/navy matching the heading accent) instead of bright default blue (`urlcolor=blue`), keeping the links clickable without visual clutter.

## Document Structure (Strict 1-Page Standard)

```latex
\\documentclass[10pt,a4paper,sans]{moderncv}
\\moderncvstyle{banking}
\\moderncvcolor{blue}

\\renewcommand*{\\namefont}{\\fontsize{20}{22}\\bfseries\\upshape}
\\colorlet{firstnamecolor}{color1}
\\colorlet{lastnamecolor}{color1}
\\colorlet{namecolor}{color1}
\\renewcommand*{\\sectionstyle}[1]{{\\sectionfont\\color{color1}#1}}

\\usepackage[utf8]{inputenc}
\\ifpdftex\\usepackage[T1]{fontenc}\\fi
\\AtEndPreamble{\\hypersetup{
    colorlinks=true,
    linkcolor=black,
    filecolor=black,
    urlcolor=black,
    pdftitle={Ishan Rastogi - CV},
    pdfpagemode=UseNone,
}}
\\usepackage[top=0.5in,bottom=0.5in,left=0.55in,right=0.55in]{geometry}
\\linespread{0.98}
\\usepackage{import}

\\name{Ishan}{Rastogi}

% Single-line plain contact bar (Zero Collision Rule)
\\renewcommand*{\\makecvtitle}{%
  \\begin{center}%
    {\\namefont{\\color{color1}Ishan Rastogi}}\\par\\vspace{3pt}%
    {\\small%
      Lucknow, Uttar Pradesh, India%
      \\ \\textbar\\ %
      +91-9451116684%
      \\ \\textbar\\ %
      \\href{mailto:ishanrastogi987654321@gmail.com}{ishanrastogi987654321@gmail.com}%
      \\ \\textbar\\ %
      \\href{https://linkedin.com/in/ishan-rastogi-303550225}{LinkedIn}%
      \\ \\textbar\\ %
      \\href{https://github.com/ishanrastogi98}{GitHub}%
    }\\par\\vspace{4pt}%
  \\end{center}%
}

\\begin{document}
\\makecvtitle

% 1. Profile statement (1-2 lines, transparent student status)
% 2. Education & Achievements (IIIT Bhopal, CGPA 9.42/10, JEE Mains 98.84%tile)
% 3. Technical Skills (5 categorized rows)
% 4. Featured Projects (Dynamic ranking, 5 bullets primary, 2-3 secondary, explicit Tech Stack line)
% 5. Experience & Leadership (INSPIRE Tech Coordinator - 3 bullets)

\\end{document}
```"""

if old_sec in cv_text:
    cv_text = cv_text.replace(old_sec, new_sec)
    print("Replaced old_sec in 05-cv-templates.md")
else:
    print("Warning: old_sec not found")

cv_path.write_text(cv_text, encoding="utf-8")
