import os
import sys
import subprocess
from pathlib import Path

# Set up MikTeX PATH
miktex_bin = r"C:\Users\Ishan Rastogi\AppData\Local\Programs\MiKTeX\miktex\bin\x64"
if miktex_bin not in os.environ["PATH"]:
    os.environ["PATH"] = miktex_bin + os.pathsep + os.environ["PATH"]

os.environ["PYTHONIOENCODING"] = "utf-8"

ROOT = Path(__file__).resolve().parent.parent

cv_files = [
    "main_diagrid_fullstack_software_engineer.tex",
    "main_cityfurnish_full_stack_engineer.tex",
    "main_digiaccel_learning_software_engineer.tex",
]

cover_files = [
    "cover_diagrid_fullstack_software_engineer.tex",
    "cover_cityfurnish_full_stack_engineer.tex",
    "cover_digiaccel_learning_software_engineer.tex",
]

print("=== 1. COMPILING CVs (lualatex) ===")
for cv in cv_files:
    tex_path = ROOT / "cv" / cv
    pdf_path = tex_path.with_suffix(".pdf")
    print(f"\n--- Compiling {cv} ---")
    cmd = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", cv]
    res = subprocess.run(cmd, cwd=str(ROOT / "cv"), capture_output=True, text=True, errors="replace")
    if res.returncode != 0:
        print(f"FAILED compiling {cv}!")
        print(res.stdout[-1500:])
        sys.exit(1)
    else:
        print(f"SUCCESS: {pdf_path.name} compiled.")

print("\n=== 2. COMPILING COVER LETTERS (xelatex) ===")
for cl in cover_files:
    tex_path = ROOT / "cover_letters" / cl
    pdf_path = tex_path.with_suffix(".pdf")
    print(f"\n--- Compiling {cl} ---")
    cmd = ["xelatex", "-interaction=nonstopmode", "-halt-on-error", cl]
    res = subprocess.run(cmd, cwd=str(ROOT / "cover_letters"), capture_output=True, text=True, errors="replace")
    if res.returncode != 0:
        print(f"FAILED compiling {cl}!")
        print(res.stdout[-1500:])
        sys.exit(1)
    else:
        print(f"SUCCESS: {pdf_path.name} compiled.")

print("\n=== 3. VERIFYING PDFs WITH verify_pdf.py (STRICT 1-PAGE LIMIT) ===")
for cv in cv_files:
    pdf_path = ROOT / "cv" / cv.replace(".tex", ".pdf")
    txt_path = ROOT / "cv" / cv.replace(".tex", ".txt")
    cmd = [sys.executable, str(ROOT / "tools" / "verify_pdf.py"), str(pdf_path), "--pages", "1", "--dump-text", str(txt_path)]
    res = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    print(f"{pdf_path.name} (pages=1):", res.stdout.strip(), res.stderr.strip())
    if res.returncode != 0:
        print(f"Error on {pdf_path.name}")
        sys.exit(res.returncode)

for cl in cover_files:
    pdf_path = ROOT / "cover_letters" / cl.replace(".tex", ".pdf")
    cmd = [sys.executable, str(ROOT / "tools" / "verify_pdf.py"), str(pdf_path), "--pages", "1"]
    res = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    print(f"{pdf_path.name} (pages=1):", res.stdout.strip(), res.stderr.strip())
    if res.returncode != 0:
        print(f"Error on {pdf_path.name}")
        sys.exit(res.returncode)

print("\n=== 4. VERIFYING LAYOUT WITH verify_layout.py ===")
for cv in cv_files:
    pdf_path = ROOT / "cv" / cv.replace(".tex", ".pdf")
    cmd = [sys.executable, str(ROOT / "tools" / "verify_layout.py"), str(pdf_path)]
    res = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    print(f"{pdf_path.name}:", res.stdout.strip(), res.stderr.strip())

for cl in cover_files:
    pdf_path = ROOT / "cover_letters" / cl.replace(".tex", ".pdf")
    cmd = [sys.executable, str(ROOT / "tools" / "verify_layout.py"), str(pdf_path)]
    res = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    print(f"{pdf_path.name}:", res.stdout.strip(), res.stderr.strip())

print("\n=== ALL COMPILATIONS AND VERIFICATIONS COMPLETED SUCCESSFULLY! ===")
