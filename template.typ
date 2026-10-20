// ==============================================================================
// DEEPTECH (DERİN TEKNOLOJİLER) MASTERCLASS - TYPST TEMPLATE (v0.15+ COMPATIBLE)
// 500 Ders • 50 Bölüm • Çift Dilli (TR & EN) • Kuantum, Biyoteknoloji, Çipler, Robotik
// ==============================================================================

#let setup_book(title: "", author: "Antigravity & Deeptech Frontier Guild", body) = {
  set document(title: title, author: author)
  set text(font: ("Avenir Next", "Helvetica Neue", "Arial"), size: 9pt, lang: "tr")
  set page(
    paper: "a4",
    margin: (x: 1.8cm, top: 2.2cm, bottom: 2.2cm),
    header: context {
      let cur_page = counter(page).get().first()
      if cur_page > 2 [
        #text(size: 8pt, fill: rgb("64748b"))[
          #grid(
            columns: (1fr, 1fr),
            [Deeptech Masterclass • 500 Lessons Frontier Blueprint],
            [#align(right)[Aptala Anlatır Gibi Derin Teknolojiler]]
          )
        ]
        #v(-2pt)
        #line(length: 100%, stroke: 0.5pt + rgb("e2e8f0"))
      ]
    },
    footer: context {
      let cur_page = counter(page).get().first()
      if cur_page > 2 [
        #line(length: 100%, stroke: 0.5pt + rgb("e2e8f0"))
        #v(2pt)
        #text(size: 8pt, fill: rgb("64748b"))[
          #grid(
            columns: (1fr, 1fr),
            [Quantum • Biotech • Semiconductors • Robotics • Clean Energy • Space],
            [#align(right)[Sayfa / Page #counter(page).display()]]
          )
        ]
      ]
    }
  )
  set par(justify: true, leading: 0.58em)
  body
}

#let diagram_box(body) = {
  v(4pt)
  rect(
    width: 100%,
    fill: rgb("030712"), // Deep Cosmic Black
    stroke: (left: 4.5pt + rgb("06b6d4"), rest: 0.5pt + rgb("164e63")),
    radius: (right: 6pt),
    inset: (x: 11pt, y: 9pt),
    [
      #grid(
        columns: (1fr, 1fr),
        gutter: 10pt,
        [#text(weight: "bold", fill: rgb("22d3ee"), size: 9.5pt)[⚡ Derin Teknoloji & Fiziksel Süreç Şeması]],
        [#align(right)[#text(weight: "bold", fill: rgb("67e8f9"), size: 9.5pt)[⚡ Frontier Physics & Architecture Schematic]]]
      )
      #v(3pt)
      #body
    ]
  )
  v(4pt)
}

#let eli5_box(body) = {
  v(4pt)
  rect(
    width: 100%,
    fill: rgb("eff6ff"), // Soft Blue
    stroke: (left: 4.5pt + rgb("2563eb"), rest: 0.5pt + rgb("bfdbfe")),
    radius: (right: 6pt),
    inset: (x: 11pt, y: 9pt),
    [
      #grid(
        columns: (1fr, 1fr),
        gutter: 10pt,
        [#text(weight: "bold", fill: rgb("1e40af"), size: 9.5pt)[💡 Aptala Anlatım (ELI5 Metaforu)]],
        [#align(right)[#text(weight: "bold", fill: rgb("1d4ed8"), size: 9.5pt)[💡 ELI5 Real-Life Metaphor]]]
      )
      #v(4pt)
      #body
    ]
  )
  v(4pt)
}

#let deep_dive_box(body) = {
  v(4pt)
  rect(
    width: 100%,
    fill: rgb("f8fafc"), // Slate
    stroke: (left: 4.5pt + rgb("7c3aed"), rest: 0.5pt + rgb("ddd6fe")),
    radius: (right: 6pt),
    inset: (x: 11pt, y: 9pt),
    [
      #grid(
        columns: (1fr, 1fr),
        gutter: 10pt,
        [#text(weight: "bold", fill: rgb("5b21b6"), size: 9.5pt)[🔬 Deeptech & Mühendislik Seviyesi Teknik Derinlik]],
        [#align(right)[#text(weight: "bold", fill: rgb("6d28d9"), size: 9.5pt)[🔬 Deeptech Engineering Deep-Dive]]]
      )
      #v(4pt)
      #body
    ]
  )
  v(4pt)
}

#let code_box(body) = {
  v(4pt)
  rect(
    width: 100%,
    fill: rgb("090514"), // Cosmic Dark Violet
    stroke: (left: 4.5pt + rgb("a855f7"), rest: 0.5pt + rgb("3b0764")),
    radius: (right: 6pt),
    inset: (x: 11pt, y: 9pt),
    [
      #grid(
        columns: (1fr, 1fr),
        gutter: 10pt,
        [#text(weight: "bold", fill: rgb("c084fc"), size: 9.5pt)[💻 Uygulamalı Kod & Simülasyon (Python / Rust / Qiskit / CUDA)]],
        [#align(right)[#text(weight: "bold", fill: rgb("d8b4fe"), size: 9.5pt)[💻 Applied Code & Simulation]]]
      )
      #v(4pt)
      #body
    ]
  )
  v(4pt)
}

#let warning_box(body) = {
  v(4pt)
  rect(
    width: 100%,
    fill: rgb("fff1f2"), // Rose
    stroke: (left: 4.5pt + rgb("e11d48"), rest: 0.5pt + rgb("fecdd3")),
    radius: (right: 6pt),
    inset: (x: 11pt, y: 9pt),
    [
      #grid(
        columns: (1fr, 1fr),
        gutter: 10pt,
        [#text(weight: "bold", fill: rgb("9f1239"), size: 9.5pt)[⚠️ Fiziksel Darboğaz & Ticarileşme Tuzağı]],
        [#align(right)[#text(weight: "bold", fill: rgb("be123c"), size: 9.5pt)[⚠️ Physical Limit & Commercialization Trap]]]
      )
      #v(4pt)
      #body
    ]
  )
  v(4pt)
}

#let takeaways_box(takeaways) = {
  v(4pt)
  rect(
    width: 100%,
    fill: rgb("f0fdf4"), // Emerald
    stroke: (left: 4.5pt + rgb("16a34a"), rest: 0.5pt + rgb("bbf7d0")),
    radius: (right: 6pt),
    inset: (x: 11pt, y: 9pt),
    [
      #grid(
        columns: (1fr, 1fr),
        gutter: 10pt,
        [#text(weight: "bold", fill: rgb("15803d"), size: 9.5pt)[🎯 Deeptech Mühendisinin Altın Çıkarımları]],
        [#align(right)[#text(weight: "bold", fill: rgb("166534"), size: 9.5pt)[🎯 Core Deeptech Takeaways]]]
      )
      #v(4pt)
      #for item in takeaways [
        #grid(
          columns: (1fr, 1fr),
          gutter: 10pt,
          [#text(size: 8pt)[• #item.at(0)]],
          [#text(size: 8pt, fill: rgb("475569"))[• #item.at(1)]]
        )
        #v(2pt)
      ]
    ]
  )
  v(4pt)
}

#let lesson_header(lesson_num, title_tr, title_en, module_name_tr, module_name_en) = {
  v(3pt)
  rect(
    width: 100%,
    fill: rgb("081120"), // Deep Space Navy
    radius: 7pt,
    inset: (x: 12pt, y: 10pt),
    [
      #grid(
        columns: (auto, 1fr),
        gutter: 12pt,
        [
          #circle(radius: 17pt, fill: rgb("06b6d4"))[
            #align(center + horizon)[#text(weight: "bold", fill: white, size: 11pt)[#lesson_num]]
          ]
        ],
        [
          #text(size: 7.5pt, fill: rgb("38bdf8"), weight: "bold")[
            BÖLÜM: #upper(module_name_tr)  |  MODULE: #upper(module_name_en)
          ]
          #v(2pt)
          #text(size: 12pt, fill: white, weight: "bold")[#title_tr]
          #v(2pt)
          #text(size: 10pt, fill: rgb("c084fc"), weight: "medium")[#title_en]
        ]
      )
    ]
  )
  v(5pt)
}

#let module_cover(module_num, title_tr, title_en, desc_tr, desc_en) = {
  pagebreak()
  v(20pt)
  align(center)[
    #rect(
      width: 100%,
      fill: rgb("020617"),
      radius: 10pt,
      inset: (x: 20pt, y: 24pt),
      [
        #text(size: 12pt, fill: rgb("38bdf8"), weight: "bold")[BÖLÜM #module_num / MODULE #module_num]
        #v(6pt)
        #text(size: 18pt, fill: white, weight: "bold")[#title_tr]
        #v(4pt)
        #text(size: 14pt, fill: rgb("94a3b8"), weight: "medium")[#title_en]
        #v(12pt)
        #line(length: 60%, stroke: 1.5pt + rgb("06b6d4"))
        #v(12pt)
        #grid(
          columns: (1fr, 1fr),
          gutter: 16pt,
          [
            #align(left)[
              #text(size: 9pt, fill: rgb("cbd5e1"))[#desc_tr]
            ]
          ],
          [
            #align(left)[
              #text(size: 9pt, fill: rgb("94a3b8"))[#desc_en]
            ]
          ]
        )
      ]
    )
  ]
  v(16pt)
}

#let book_front_cover() = {
  set page(header: none, footer: none, margin: 0pt)
  rect(
    width: 100%,
    height: 100%,
    fill: rgb("02040a"), // Ultra Deep Quantum Void
    inset: (x: 3.2cm, y: 3.2cm),
    [
      #v(20pt)
      #rect(fill: rgb("082f49"), radius: 4pt, inset: (x: 10pt, y: 6pt))[
        #text(size: 9.5pt, fill: rgb("bae6fd"), weight: "bold")[FRONTIER DEEPTECH ENGINEERING MASTERCLASS • BILINGUAL EDITION]
      ]
      #v(16pt)
      #text(size: 32pt, fill: white, weight: "bold")[
        Aptala Anlatır Gibi\ Derin Teknolojiler
      ]
      #v(8pt)
      #text(size: 18pt, fill: rgb("38bdf8"), weight: "medium")[
        Deeptech Masterclass: 500 Lessons & 50 Modules for Frontier Engineers
      ]
      #v(12pt)
      #text(size: 11pt, fill: rgb("94a3b8"))[
        50 Bölüm • 500 Ders • Kuantum • Çipler • Sentetik Biyoloji • Nükleer Füzyon • Robotik • Uzay • Çift Dilli (TR & EN)
      ]
      #v(24pt)
      #line(length: 100%, stroke: 2pt + rgb("06b6d4"))
      #v(24pt)
      #grid(
        columns: (1fr, 1fr, 1fr),
        gutter: 12pt,
        [
          #rect(fill: rgb("081120"), radius: 6pt, inset: 10pt, width: 100%)[
            #text(weight: "bold", fill: white, size: 9.5pt)[⚛️ Kuantum & Çip Mimarisi]\
            #v(2pt)
            #text(size: 8pt, fill: rgb("94a3b8"))[Qubits, Qiskit, FinFET, GAAFET, RISC-V, Fotonik ve Nöromorfik Çipler]
          ]
        ],
        [
          #rect(fill: rgb("081120"), radius: 6pt, inset: 10pt, width: 100%)[
            #text(weight: "bold", fill: white, size: 9.5pt)[🧬 Biyo-Mühendislik & Yapay Zekâ]\
            #v(2pt)
            #text(size: 8pt, fill: rgb("94a3b8"))[CRISPR, AlphaFold 3, BioPython, Sentetik Biyoloji, Beyin-Bilgisayar Arayüzü (BCI)]
          ]
        ],
        [
          #rect(fill: rgb("081120"), radius: 6pt, inset: 10pt, width: 100%)[
            #text(weight: "bold", fill: white, size: 9.5pt)[🚀 İleri Enerji, Robotik & Uzay]\
            #v(2pt)
            #text(size: 8pt, fill: rgb("94a3b8"))[Nükleer Füzyon, Katı Hal Bataryaları, ROS 2, SLAM, İyon İtki ve Yörünge Mekaniği]
          ]
        ]
      )
      #v(40pt)
      #align(bottom)[
        #text(size: 9pt, fill: rgb("64748b"))[
          Yayın Sürümü: 1.0.0 • 500 Derslik Geleceğin Teknolojileri Kılavuzu • 2026
        ]
      ]
    ]
  )
}
