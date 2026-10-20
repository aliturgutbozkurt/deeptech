#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_all.py
Master generator and parallel compiler for the 50-Module, 500-Lesson Bilingual ELI5
Deeptech (Derin Teknolojiler) Masterclass.

Outputs:
  - content/modXX_.../lesson_YYY.typ (500 files)
  - content/modXX_.../module_XX.typ (50 files)
  - book.typ (Master unified mega-book)
  - output/individual/lesson_XXX.pdf (500 PDFs)
  - output/modules/module_XX.pdf (50 PDFs)
  - output/book/Deeptech_Masterclass_ELI5.pdf (1 Master Mega-Book PDF)
  - web/data/lessons.json & lessons.js (Interactive Web Companion)
"""

import os
import sys
import glob
import json
import re
import subprocess
import importlib.util
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

BASE_DIR = Path(__file__).resolve().parent
MODULES_DATA_DIR = BASE_DIR / "modules_data"
CONTENT_DIR = BASE_DIR / "content"
OUTPUT_DIR = BASE_DIR / "output"
WEB_DIR = BASE_DIR / "web"

def load_all_modules():
    mod_files = sorted(glob.glob(str(MODULES_DATA_DIR / "mod*.py")))
    modules = []
    for f in mod_files:
        spec = importlib.util.spec_from_file_location(Path(f).stem, f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        modules.append(mod.MODULE)
    modules.sort(key=lambda m: m['id'])
    return modules

MODULES = load_all_modules()

def sanitize_typst_text(s: str) -> str:
    """Escapes dollar signs, unescaped angle brackets, @, and # outside backticks."""
    if not s:
        return ""
    # Dollar signs trigger math mode
    s = s.replace("$", "\\$")
    # Angle brackets can trigger label syntax
    s = re.sub(r"(?<!\\)<", r"\<", s)
    # At signs trigger reference/citation
    s = re.sub(r"(?<!\\)@", r"\@", s)
    # Backticks code spans protection
    parts = s.split("`")
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r"(?<!\\)_", r"\_", parts[i])
        parts[i] = re.sub(r"(?<!\\)#", r"\#", parts[i])
    s = "`".join(parts)
    return s

def escape_typst_string_literal(s: str) -> str:
    """Escapes backslashes and double quotes inside Typst string literals."""
    if not s:
        return ""
    return s.replace('\\', '\\\\').replace('"', '\\"')

def detect_code_lang(code_str: str) -> str:
    if "__global__" in code_str or "cudaMalloc" in code_str or "cudaMemcpy" in code_str:
        return "cuda"
    if "#include <" in code_str or "std::cout" in code_str:
        return "cpp"
    if "fn " in code_str or "pub struct" in code_str or "let mut" in code_str:
        return "rust"
    if "from qiskit" in code_str or "QuantumCircuit" in code_str:
        return "python"
    return "python"

def generate_lesson_typ(m: dict, l: dict) -> str:
    takeaways_typ = ""
    for item in l.get('takeaways', []):
        tr_item = escape_typst_string_literal(item[0])
        en_item = escape_typst_string_literal(item[1])
        takeaways_typ += f'    ("{tr_item}", "{en_item}"),\n'

    eli5_tr = sanitize_typst_text(l['eli5_tr'])
    eli5_en = sanitize_typst_text(l['eli5_en'])
    deep_tr = sanitize_typst_text(l['deep_tr'])
    deep_en = sanitize_typst_text(l['deep_en'])
    warning_tr = sanitize_typst_text(l['warning_tr'])
    warning_en = sanitize_typst_text(l['warning_en'])

    title_tr = escape_typst_string_literal(l['title_tr'])
    title_en = escape_typst_string_literal(l['title_en'])
    mod_title_tr = escape_typst_string_literal(m['title_tr'])
    mod_title_en = escape_typst_string_literal(m['title_en'])

    code_raw = l.get('java_code', l.get('code', ''))
    code_lang = detect_code_lang(code_raw)
    diagram_clean = l.get('diagram', '').replace('```', "'''")

    content = f'''#import "/template.typ": *

#show: doc => setup_book(title: "Ders {l['num']}: {title_tr}", doc)

#lesson_header(
  {l['num']},
  "{title_tr}",
  "{title_en}",
  "{mod_title_tr}",
  "{mod_title_en}"
)

#diagram_box[
```text
{diagram_clean}
```
]

#eli5_box[
  #grid(
    columns: (1fr, 1fr),
    gutter: 12pt,
    [
      #text(weight: "bold", fill: rgb("1e40af"), size: 8.5pt)[🇹🇷 TÜRKÇE (ELI5)]\\
      #v(2pt)
      {eli5_tr}
    ],
    [
      #text(weight: "bold", fill: rgb("1d4ed8"), size: 8.5pt)[🇬🇧 ENGLISH (ELI5)]\\
      #v(2pt)
      #text(fill: rgb("334155"))[{eli5_en}]
    ]
  )
]

#deep_dive_box[
  #grid(
    columns: (1fr, 1fr),
    gutter: 12pt,
    [
      #text(weight: "bold", fill: rgb("5b21b6"), size: 8.5pt)[🇹🇷 DEEPTECH MÜHENDİSLİK ANALİZİ]\\
      #v(2pt)
      {deep_tr}
    ],
    [
      #text(weight: "bold", fill: rgb("6d28d9"), size: 8.5pt)[🇬🇧 FRONTIER TECHNICAL DEEP-DIVE]\\
      #v(2pt)
      #text(fill: rgb("334155"))[{deep_en}]
    ]
  )
]

#code_box[
```{code_lang}
{code_raw}
```
]

#warning_box[
  #grid(
    columns: (1fr, 1fr),
    gutter: 12pt,
    [
      #text(weight: "bold", fill: rgb("9f1239"), size: 8.5pt)[🇹🇷 FİZİKSEL DARBOĞAZ & TİCARİLEŞME TUZAĞI]\\
      #v(2pt)
      {warning_tr}
    ],
    [
      #text(weight: "bold", fill: rgb("be123c"), size: 8.5pt)[🇬🇧 PHYSICAL LIMIT & COMMERCIALIZATION TRAP]\\
      #v(2pt)
      #text(fill: rgb("881337"))[{warning_en}]
    ]
  )
]

#takeaways_box((
{takeaways_typ}))
'''
    return content

def generate_module_typ(m: dict) -> str:
    desc_tr = escape_typst_string_literal(m['desc_tr'])
    desc_en = escape_typst_string_literal(m['desc_en'])
    title_tr = escape_typst_string_literal(m['title_tr'])
    title_en = escape_typst_string_literal(m['title_en'])

    content = f'''#import "/template.typ": *

#show: doc => setup_book(title: "Bölüm {m['id']}: {title_tr}", doc)

#module_cover(
  {m['id']},
  "{title_tr}",
  "{title_en}",
  "{desc_tr}",
  "{desc_en}"
)

'''
    for l in m['lessons']:
        filename = f"lesson_{l['num']:03d}.typ"
        content += f'#include "{filename}"\n#v(14pt)\n\n'
    return content

def generate_master_book_typ() -> str:
    content = '''#import "/template.typ": *

#show: doc => setup_book(
  title: "Aptala Anlatır Gibi Derin Teknolojiler: 500 Derslik Deeptech Masterclass",
  author: "Antigravity & Deeptech Frontier Guild",
  doc
)

#book_front_cover()

#pagebreak()
#v(16pt)
#align(center)[
  #text(size: 20pt, weight: "bold", fill: rgb("020617"))[Önsöz ve Başlarken / Preface & Getting Started]
]
#v(12pt)

#grid(
  columns: (1fr, 1fr),
  gutter: 18pt,
  [
    == 🇹🇷 Bu Eğitim Hakkında
    Geleneksel yazılım dünyasında "hızlı hareket et ve bir şeyleri kır" (move fast and break things) mottosu geçerliydi; çünkü bir yazılım hatasını gidermek git commit veya bulut güncellemesi kadar kolaydır. *Derin Teknoloji (Deeptech)* dünyasında ise doğa ve fizik kuralları asla taviz vermez! Yanlış hesaplanmış bir plazma reaktörü manyetik bobini, sub-nanometre seviyesindeki litografi kusuru veya hatalı tasarlanmış bir CRISPR kılavuz RNA'sı milyonlarca dolarlık yatırımı ve aylarca süren çalışmaları yok edebilir.

    Bu 500 derslik devasa kılavuz; Kuantum Hesaplama, Yarı İletken Fiziği, Sentetik Biyoloji, Nükleer Füzyon, Nöromorfik Çipler, Otonom Robotik, BCI (Beyin-Bilgisayar Arayüzleri) ve Uzay İtki Sistemleri gibi geleceği şekillendiren 50 kritik disiplini *bir aptala anlatır gibi* anlaşılır kılar. Her derste fiziksel mimari şeması, çift dilli ELI5 analizi, derin teknik formüller, uygulanabilir kod simülasyonları ve kritik fiziksel tuzaklar yer alır.
  ],
  [
    == 🇬🇧 About This Masterclass
    In traditional software development, the mantra was "move fast and break things"—because patching a runtime exception is as effortless as a git push. In the frontier domain of *Deeptech*, however, the laws of physics and thermodynamics do not negotiate! An unshielded magnetic fluctuation in a fusion tokamak, a single atomic vacancy in a GAAFET transistor, or an off-target guide RNA cleavage can obliterate millions of dollars and years of cleanroom fabrication.

    This comprehensive 500-lesson blueprint demystifies 50 foundational frontier disciplines—including Quantum Computing, Semiconductor Nanophysics, CRISPR Gene Editing, Tokamak Fusion, Neuromorphic SNNs, Robotics Kinematics, Brain-Computer Interfaces, and Space Propulsion—using crystal-clear *Explain Like I'm 5 (ELI5)* metaphors paired with deep scientific rigor. Every lesson integrates architectural schematics, bilingual pedagogy, high-performance simulation code, and hard physical boundary warnings.
  ]
)

#v(16pt)
#line(length: 100%, stroke: 0.8pt + rgb("e2e8f0"))
#v(10pt)

#outline(
  title: [İçindekiler / Table of Contents],
  depth: 2,
  indent: auto
)

#pagebreak()
'''
    for m in MODULES:
        content += f'''
#module_cover(
  {m['id']},
  "{escape_typst_string_literal(m['title_tr'])}",
  "{escape_typst_string_literal(m['title_en'])}",
  "{escape_typst_string_literal(m['desc_tr'])}",
  "{escape_typst_string_literal(m['desc_en'])}"
)

'''
        for l in m['lessons']:
            rel_path = f"/content/{m['dir']}/lesson_{l['num']:03d}.typ"
            content += f'#include "{rel_path}"\n#v(12pt)\n\n'

    content += '''
#pagebreak()
#v(40pt)
#align(center)[
  #rect(fill: rgb("020617"), radius: 10pt, inset: (x: 24pt, y: 32pt), width: 92%)[
    #text(size: 26pt, fill: rgb("38bdf8"), weight: "bold")[🌌 TEBRİKLER! / CONGRATULATIONS!]\
    #v(12pt)
    #text(size: 14pt, fill: white)[500 Derslik Derin Teknoloji Mühendisliği Zirvesini Tamamladınız!]\
    #v(6pt)
    #text(size: 11pt, fill: rgb("94a3b8"))[You have mastered the entire 500-Lesson Frontier Deeptech Engineering Curriculum!]\
    #v(20pt)
    #line(length: 60%, stroke: 1.5pt + rgb("06b6d4"))
    #v(15pt)
    #text(size: 9.5pt, fill: rgb("cbd5e1"))[
      Quantum • Semiconductors • CRISPR • Fusion • Robotics • BCI • Space • Advanced Materials • Clean Energy
    ]
  ]
]
'''
    return content

def generate_web_json():
    clean_modules = []
    for m in MODULES:
        clean_lessons = []
        for l in m['lessons']:
            code_val = l.get('java_code', l.get('code', ''))
            clean_lessons.append({
                "num": l['num'],
                "title_tr": l['title_tr'],
                "title_en": l['title_en'],
                "diagram": l.get('diagram', ''),
                "eli5_tr": l['eli5_tr'],
                "eli5_en": l['eli5_en'],
                "deep_tr": l['deep_tr'],
                "deep_en": l['deep_en'],
                "code": code_val,
                "warning_tr": l['warning_tr'],
                "warning_en": l['warning_en'],
                "takeaways": l.get('takeaways', [])
            })
        clean_modules.append({
            "id": m['id'],
            "dir": m['dir'],
            "title_tr": m['title_tr'],
            "title_en": m['title_en'],
            "desc_tr": m['desc_tr'],
            "desc_en": m['desc_en'],
            "lessons": clean_lessons
        })

    data = {
        "title_tr": "Aptala Anlatır Gibi Derin Teknolojiler",
        "title_en": "Explain Like I'm 5: Deeptech Frontier Masterclass",
        "description": "500 Ders • 50 Bölüm • Çift Dilli (TR & EN) • Kuantum, Biyoteknoloji, Çipler, Robotik, Füzyon & Uzay",
        "modules": clean_modules
    }
    web_data_dir = WEB_DIR / "data"
    web_data_dir.mkdir(parents=True, exist_ok=True)
    with open(web_data_dir / "lessons.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    with open(web_data_dir / "lessons.js", "w", encoding="utf-8") as f:
        f.write("window.LESSONS_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n")
    print(f"✔ Exported web data to {web_data_dir / 'lessons.json'} and lessons.js")

def write_all_typst_files():
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    for m in MODULES:
        mod_dir = CONTENT_DIR / m['dir']
        mod_dir.mkdir(parents=True, exist_ok=True)
        for l in m['lessons']:
            lesson_typ = generate_lesson_typ(m, l)
            lesson_path = mod_dir / f"lesson_{l['num']:03d}.typ"
            with open(lesson_path, "w", encoding="utf-8") as f:
                f.write(lesson_typ)
        
        module_typ = generate_module_typ(m)
        module_path = mod_dir / f"module_{m['id']:02d}.typ"
        with open(module_path, "w", encoding="utf-8") as f:
            f.write(module_typ)
    
    book_typ = generate_master_book_typ()
    with open(BASE_DIR / "book.typ", "w", encoding="utf-8") as f:
        f.write(book_typ)
    print("✔ All 551 Typst source files generated successfully!")

def compile_single_typst(args):
    src, out = args
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "typst", "compile",
        "--root", str(BASE_DIR),
        str(src),
        str(out)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.returncode == 0, src.name, res.stderr

def compile_all_pdfs():
    (OUTPUT_DIR / "individual").mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "modules").mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "book").mkdir(parents=True, exist_ok=True)

    print("\n--- 1. Compiling Master Book PDF (500 Lessons) ---")
    book_src = BASE_DIR / "book.typ"
    book_out = OUTPUT_DIR / "book" / "Deeptech_Masterclass_ELI5.pdf"
    ok, name, err = compile_single_typst((book_src, book_out))
    if ok:
        size_mb = book_out.stat().st_size / (1024 * 1024)
        print(f"✔ Master Mega-Book PDF created: {book_out.name} ({size_mb:.2f} MB)")
    else:
        print(f"❌ Error compiling book: {err}")

    print("\n--- 2. Compiling 50 Module PDFs (Parallel) ---")
    module_tasks = []
    for m in MODULES:
        mod_src = CONTENT_DIR / m['dir'] / f"module_{m['id']:02d}.typ"
        mod_out = OUTPUT_DIR / "modules" / f"module_{m['id']:02d}.pdf"
        module_tasks.append((mod_src, mod_out))

    with ProcessPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(compile_single_typst, t) for t in module_tasks]
        mod_success = sum(1 for f in as_completed(futures) if f.result()[0])
    print(f"✔ Compiled {mod_success}/50 Module PDFs successfully!")

    print("\n--- 3. Compiling 500 Individual Lesson PDFs (Parallel) ---")
    lesson_tasks = []
    for m in MODULES:
        for l in m['lessons']:
            les_src = CONTENT_DIR / m['dir'] / f"lesson_{l['num']:03d}.typ"
            les_out = OUTPUT_DIR / "individual" / f"lesson_{l['num']:03d}.pdf"
            lesson_tasks.append((les_src, les_out))

    with ProcessPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(compile_single_typst, t) for t in lesson_tasks]
        les_success = sum(1 for f in as_completed(futures) if f.result()[0])
    print(f"✔ Compiled {les_success}/500 Individual Lesson PDFs successfully!")
    print(f"\n🎉 Total PDFs created: {1 + mod_success + les_success} / 551!")

if __name__ == "__main__":
    print("🚀 Starting Complete 500-Lesson Deeptech Curriculum Generation...")
    write_all_typst_files()
    generate_web_json()

    mode = sys.argv[1] if len(sys.argv) > 1 else "--all"
    if mode == "--all":
        compile_all_pdfs()
    elif mode == "--book":
        book_src = BASE_DIR / "book.typ"
        book_out = OUTPUT_DIR / "book" / "Deeptech_Masterclass_ELI5.pdf"
        compile_single_typst((book_src, book_out))
    elif mode == "--json-only":
        pass
