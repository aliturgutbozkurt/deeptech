#import "/template.typ": *

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

#module_cover(
  1,
  "Derin Teknoloji Zihniyeti & Fizik Temelli İlkeler",
  "Deeptech Mindset & First-Principles Physics Engineering",
  "Yazılım SaaS vs Derin Teknoloji ayrımı, fiziksel ilkelerden düşünme (first principles), uzun Ar-Ge döngüleri, TRL 1-9 ve bilimsel atılımları ölçekleme.",
  "Software SaaS vs Deeptech R&D paradigms, physics-first principles, CapEx vs OpEx dynamics, TRL 1-9 progression, and scientific scale-up."
)

#include "/content/mod01_deeptech_mindset/lesson_001.typ"
#v(12pt)

#include "/content/mod01_deeptech_mindset/lesson_002.typ"
#v(12pt)

#include "/content/mod01_deeptech_mindset/lesson_003.typ"
#v(12pt)

#include "/content/mod01_deeptech_mindset/lesson_004.typ"
#v(12pt)

#include "/content/mod01_deeptech_mindset/lesson_005.typ"
#v(12pt)

#include "/content/mod01_deeptech_mindset/lesson_006.typ"
#v(12pt)

#include "/content/mod01_deeptech_mindset/lesson_007.typ"
#v(12pt)

#include "/content/mod01_deeptech_mindset/lesson_008.typ"
#v(12pt)

#include "/content/mod01_deeptech_mindset/lesson_009.typ"
#v(12pt)

#include "/content/mod01_deeptech_mindset/lesson_010.typ"
#v(12pt)


#module_cover(
  2,
  "Kuantum Hesaplama Temelleri: Kübitler, Süperpozisyon & Dolaşıklık",
  "Quantum Computing Core: Qubits, Superposition & Entanglement",
  "Kuantum mekaniği prensipleri, Bloch küresi, süperpozisyon durumları, Bell durumları ve kuantum dolaşıklığının hesaplamalı gücü.",
  "Quantum mechanical foundations, Bloch sphere state vectors, superposition linear algebra, Bell states, and computational entanglement."
)

#include "/content/mod02_quantum_computing_core/lesson_011.typ"
#v(12pt)

#include "/content/mod02_quantum_computing_core/lesson_012.typ"
#v(12pt)

#include "/content/mod02_quantum_computing_core/lesson_013.typ"
#v(12pt)

#include "/content/mod02_quantum_computing_core/lesson_014.typ"
#v(12pt)

#include "/content/mod02_quantum_computing_core/lesson_015.typ"
#v(12pt)

#include "/content/mod02_quantum_computing_core/lesson_016.typ"
#v(12pt)

#include "/content/mod02_quantum_computing_core/lesson_017.typ"
#v(12pt)

#include "/content/mod02_quantum_computing_core/lesson_018.typ"
#v(12pt)

#include "/content/mod02_quantum_computing_core/lesson_019.typ"
#v(12pt)

#include "/content/mod02_quantum_computing_core/lesson_020.typ"
#v(12pt)


#module_cover(
  3,
  "Kuantum Algoritmaları & Post-Kuantum Kriptografi (PQC)",
  "Quantum Algorithms & Post-Quantum Cryptography (PQC)",
  "Shor algoritması ve RSA'nın kırılması, Grover arama hızlandırması, Kafes tabanlı (Lattice) kriptografi ve NIST PQC standartları (Kyber, Dilithium).",
  "Shor's factoring polynomial speedup, Grover's quadratic database search, lattice cryptography, and NIST-approved post-quantum algorithms."
)

#include "/content/mod03_quantum_algorithms_crypto/lesson_021.typ"
#v(12pt)

#include "/content/mod03_quantum_algorithms_crypto/lesson_022.typ"
#v(12pt)

#include "/content/mod03_quantum_algorithms_crypto/lesson_023.typ"
#v(12pt)

#include "/content/mod03_quantum_algorithms_crypto/lesson_024.typ"
#v(12pt)

#include "/content/mod03_quantum_algorithms_crypto/lesson_025.typ"
#v(12pt)

#include "/content/mod03_quantum_algorithms_crypto/lesson_026.typ"
#v(12pt)

#include "/content/mod03_quantum_algorithms_crypto/lesson_027.typ"
#v(12pt)

#include "/content/mod03_quantum_algorithms_crypto/lesson_028.typ"
#v(12pt)

#include "/content/mod03_quantum_algorithms_crypto/lesson_029.typ"
#v(12pt)

#include "/content/mod03_quantum_algorithms_crypto/lesson_030.typ"
#v(12pt)


#module_cover(
  4,
  "Kuantum Yazılımı & Qiskit ile Devre Simülasyonu",
  "Quantum Software & Circuit Simulation with Qiskit",
  "Qiskit ve Cirq SDK'ları, kuantum kapıları (Hadamard, CNOT, Phase), hata azaltma (Error Mitigation) ve gürültülü (NISQ) kuantum işlemciler.",
  "Qiskit/Cirq quantum SDKs, unitary gate operations, quantum state tomography, error mitigation techniques, and NISQ regime optimization."
)

#include "/content/mod04_quantum_software_qiskit/lesson_031.typ"
#v(12pt)

#include "/content/mod04_quantum_software_qiskit/lesson_032.typ"
#v(12pt)

#include "/content/mod04_quantum_software_qiskit/lesson_033.typ"
#v(12pt)

#include "/content/mod04_quantum_software_qiskit/lesson_034.typ"
#v(12pt)

#include "/content/mod04_quantum_software_qiskit/lesson_035.typ"
#v(12pt)

#include "/content/mod04_quantum_software_qiskit/lesson_036.typ"
#v(12pt)

#include "/content/mod04_quantum_software_qiskit/lesson_037.typ"
#v(12pt)

#include "/content/mod04_quantum_software_qiskit/lesson_038.typ"
#v(12pt)

#include "/content/mod04_quantum_software_qiskit/lesson_039.typ"
#v(12pt)

#include "/content/mod04_quantum_software_qiskit/lesson_040.typ"
#v(12pt)


#module_cover(
  5,
  "Yarı İletken Fiziği, Transistörler & FinFET/GAAFET Mimarisi",
  "Semiconductor Physics, Transistors & FinFET/GAAFET Architecture",
  "Silikon kristal kafesleri, P-N eklemleri, Moore Kanunu'nun fiziksel sınırları, FinFET ve Gate-All-Around (GAAFET) transistör geometrisi.",
  "Silicon crystal lattice bandgaps, P-N junction drift currents, quantum tunneling limits of Moore's Law, FinFET, and 2nm GAAFET nanosheets."
)

#include "/content/mod05_semiconductor_physics/lesson_041.typ"
#v(12pt)

#include "/content/mod05_semiconductor_physics/lesson_042.typ"
#v(12pt)

#include "/content/mod05_semiconductor_physics/lesson_043.typ"
#v(12pt)

#include "/content/mod05_semiconductor_physics/lesson_044.typ"
#v(12pt)

#include "/content/mod05_semiconductor_physics/lesson_045.typ"
#v(12pt)

#include "/content/mod05_semiconductor_physics/lesson_046.typ"
#v(12pt)

#include "/content/mod05_semiconductor_physics/lesson_047.typ"
#v(12pt)

#include "/content/mod05_semiconductor_physics/lesson_048.typ"
#v(12pt)

#include "/content/mod05_semiconductor_physics/lesson_049.typ"
#v(12pt)

#include "/content/mod05_semiconductor_physics/lesson_050.typ"
#v(12pt)


#module_cover(
  6,
  "Çip Mimarisi, VLSI & RISC-V Açık Standart Tasarım",
  "Chip Architecture, VLSI & Open-Standard RISC-V Design",
  "Komut kümesi mimarileri (ISA), RISC-V açık kaynak devrimi, RTL donanım tanımlama (Verilog/Chisel), mantıksal sentez ve Tape-Out süreci.",
  "Instruction set architecture design, RISC-V modular extensions, RTL synthesis in Verilog, clock-tree routing, and ASIC tape-out pipelines."
)

#include "/content/mod06_chip_architecture_riscv/lesson_051.typ"
#v(12pt)

#include "/content/mod06_chip_architecture_riscv/lesson_052.typ"
#v(12pt)

#include "/content/mod06_chip_architecture_riscv/lesson_053.typ"
#v(12pt)

#include "/content/mod06_chip_architecture_riscv/lesson_054.typ"
#v(12pt)

#include "/content/mod06_chip_architecture_riscv/lesson_055.typ"
#v(12pt)

#include "/content/mod06_chip_architecture_riscv/lesson_056.typ"
#v(12pt)

#include "/content/mod06_chip_architecture_riscv/lesson_057.typ"
#v(12pt)

#include "/content/mod06_chip_architecture_riscv/lesson_058.typ"
#v(12pt)

#include "/content/mod06_chip_architecture_riscv/lesson_059.typ"
#v(12pt)

#include "/content/mod06_chip_architecture_riscv/lesson_060.typ"
#v(12pt)


#module_cover(
  7,
  "Fotonik Hesaplama & Işık Hızında Optik İşlemciler",
  "Photonic Computing & Light-Speed Optical Processors",
  "Silikon fotonik, dalga kılavuzları, Mach-Zehnder interferometreleri ve ışık dalgalarıyla sıfır dirençli matris çarpımı (Optical GEMM).",
  "Silicon photonics waveguides, Mach-Zehnder interferometers, electro-optic modulators, and light-speed analog tensor multiplication."
)

#include "/content/mod07_photonic_computing/lesson_061.typ"
#v(12pt)

#include "/content/mod07_photonic_computing/lesson_062.typ"
#v(12pt)

#include "/content/mod07_photonic_computing/lesson_063.typ"
#v(12pt)

#include "/content/mod07_photonic_computing/lesson_064.typ"
#v(12pt)

#include "/content/mod07_photonic_computing/lesson_065.typ"
#v(12pt)

#include "/content/mod07_photonic_computing/lesson_066.typ"
#v(12pt)

#include "/content/mod07_photonic_computing/lesson_067.typ"
#v(12pt)

#include "/content/mod07_photonic_computing/lesson_068.typ"
#v(12pt)

#include "/content/mod07_photonic_computing/lesson_069.typ"
#v(12pt)

#include "/content/mod07_photonic_computing/lesson_070.typ"
#v(12pt)


#module_cover(
  8,
  "Nöromorfik Çipler & Beyin Benzetimli Sinir Ağları (SNN)",
  "Neuromorphic Computing & Brain-Inspired Spiking Neural Networks",
  "Biyolojik nöron modelleri (Leaky Integrate-and-Fire), olay güdümlü asenkron çipler (Intel Loihi), memristörler ve sinaptik plastisite (STDP).",
  "Biophysical neuron simulations, spike-timing-dependent plasticity (STDP), memristive crossbars, and ultra-low-power event-driven chips."
)

#include "/content/mod08_neuromorphic_computing/lesson_071.typ"
#v(12pt)

#include "/content/mod08_neuromorphic_computing/lesson_072.typ"
#v(12pt)

#include "/content/mod08_neuromorphic_computing/lesson_073.typ"
#v(12pt)

#include "/content/mod08_neuromorphic_computing/lesson_074.typ"
#v(12pt)

#include "/content/mod08_neuromorphic_computing/lesson_075.typ"
#v(12pt)

#include "/content/mod08_neuromorphic_computing/lesson_076.typ"
#v(12pt)

#include "/content/mod08_neuromorphic_computing/lesson_077.typ"
#v(12pt)

#include "/content/mod08_neuromorphic_computing/lesson_078.typ"
#v(12pt)

#include "/content/mod08_neuromorphic_computing/lesson_079.typ"
#v(12pt)

#include "/content/mod08_neuromorphic_computing/lesson_080.typ"
#v(12pt)


#module_cover(
  9,
  "Modern GPU Mimarisi: Tensor Cores, NVLink & HBM3e",
  "Modern GPU Hardware Architecture: Tensor Cores & NVLink Interconnects",
  "NVIDIA Hopper/Blackwell mimarisi, Akış Çoklu İşlemcileri (SM), Tensor Cores, yüksek bant genişlikli bellek (HBM3e) ve NVLink anahtarları.",
  "Streaming multiprocessor warp dispatch, Tensor Core mixed-precision arithmetic, HBM3e 3D-stacked silicon, and terabit NVLink topologies."
)

#include "/content/mod09_gpu_hardware_architecture/lesson_081.typ"
#v(12pt)

#include "/content/mod09_gpu_hardware_architecture/lesson_082.typ"
#v(12pt)

#include "/content/mod09_gpu_hardware_architecture/lesson_083.typ"
#v(12pt)

#include "/content/mod09_gpu_hardware_architecture/lesson_084.typ"
#v(12pt)

#include "/content/mod09_gpu_hardware_architecture/lesson_085.typ"
#v(12pt)

#include "/content/mod09_gpu_hardware_architecture/lesson_086.typ"
#v(12pt)

#include "/content/mod09_gpu_hardware_architecture/lesson_087.typ"
#v(12pt)

#include "/content/mod09_gpu_hardware_architecture/lesson_088.typ"
#v(12pt)

#include "/content/mod09_gpu_hardware_architecture/lesson_089.typ"
#v(12pt)

#include "/content/mod09_gpu_hardware_architecture/lesson_090.typ"
#v(12pt)


#module_cover(
  10,
  "Paralel Donanım Programlama: CUDA C++ & OpenAI Triton",
  "High-Performance GPU Programming: CUDA C++ & OpenAI Triton",
  "CUDA thread/block hiyerarşisi, Paylaşımlı Bellek (Shared Memory Tiling), Warp Shuffle operasyonları ve OpenAI Triton ile kernel derleme.",
  "CUDA memory coalescing, shared memory bank conflict resolution, warp-level primitives, and tile-based compiler tuning in OpenAI Triton."
)

#include "/content/mod10_cuda_triton_programming/lesson_091.typ"
#v(12pt)

#include "/content/mod10_cuda_triton_programming/lesson_092.typ"
#v(12pt)

#include "/content/mod10_cuda_triton_programming/lesson_093.typ"
#v(12pt)

#include "/content/mod10_cuda_triton_programming/lesson_094.typ"
#v(12pt)

#include "/content/mod10_cuda_triton_programming/lesson_095.typ"
#v(12pt)

#include "/content/mod10_cuda_triton_programming/lesson_096.typ"
#v(12pt)

#include "/content/mod10_cuda_triton_programming/lesson_097.typ"
#v(12pt)

#include "/content/mod10_cuda_triton_programming/lesson_098.typ"
#v(12pt)

#include "/content/mod10_cuda_triton_programming/lesson_099.typ"
#v(12pt)

#include "/content/mod10_cuda_triton_programming/lesson_100.typ"
#v(12pt)


#module_cover(
  11,
  "Uç Birim Yapay Zekâsı (Edge AI), Kuantizasyon & TinyML",
  "Edge AI, Hardware Quantization (INT4/FP8) & TinyML",
  "Düşük güçlü mikrodenetleyicilerde (ARM Cortex-M) yapay zekâ, model budama (Pruning), INT8/INT4 kuantizasyonu ve ONNX Runtime.",
  "Constrained embedded inference, post-training quantization, structured pruning, memory-mapped neural execution, and micro-kernel runtime."
)

#include "/content/mod11_edge_ai_tinyml/lesson_101.typ"
#v(12pt)

#include "/content/mod11_edge_ai_tinyml/lesson_102.typ"
#v(12pt)

#include "/content/mod11_edge_ai_tinyml/lesson_103.typ"
#v(12pt)

#include "/content/mod11_edge_ai_tinyml/lesson_104.typ"
#v(12pt)

#include "/content/mod11_edge_ai_tinyml/lesson_105.typ"
#v(12pt)

#include "/content/mod11_edge_ai_tinyml/lesson_106.typ"
#v(12pt)

#include "/content/mod11_edge_ai_tinyml/lesson_107.typ"
#v(12pt)

#include "/content/mod11_edge_ai_tinyml/lesson_108.typ"
#v(12pt)

#include "/content/mod11_edge_ai_tinyml/lesson_109.typ"
#v(12pt)

#include "/content/mod11_edge_ai_tinyml/lesson_110.typ"
#v(12pt)


#module_cover(
  12,
  "Sentetik Biyoloji & CRISPR Gen Düzenleme Teknolojileri",
  "Synthetic Biology & CRISPR-Cas Precision Gene Editing",
  "DNA/RNA sentezi, CRISPR-Cas9/Cas12 makas mekanizması, sgRNA tasarımı, Base Editing ve Prime Editing ile hassas genetik cerrahi.",
  "Molecular biology primitives, CRISPR guide RNA target specificity, off-target cleavage mitigation, prime editing, and synthetic gene circuits."
)

#include "/content/mod12_synthetic_biology_crispr/lesson_111.typ"
#v(12pt)

#include "/content/mod12_synthetic_biology_crispr/lesson_112.typ"
#v(12pt)

#include "/content/mod12_synthetic_biology_crispr/lesson_113.typ"
#v(12pt)

#include "/content/mod12_synthetic_biology_crispr/lesson_114.typ"
#v(12pt)

#include "/content/mod12_synthetic_biology_crispr/lesson_115.typ"
#v(12pt)

#include "/content/mod12_synthetic_biology_crispr/lesson_116.typ"
#v(12pt)

#include "/content/mod12_synthetic_biology_crispr/lesson_117.typ"
#v(12pt)

#include "/content/mod12_synthetic_biology_crispr/lesson_118.typ"
#v(12pt)

#include "/content/mod12_synthetic_biology_crispr/lesson_119.typ"
#v(12pt)

#include "/content/mod12_synthetic_biology_crispr/lesson_120.typ"
#v(12pt)


#module_cover(
  13,
  "Biyoinformatik & Hesaplamalı Genomik (BioPython)",
  "Bioinformatics & Computational Genomics with BioPython",
  "Yeni Nesil Dizileme (NGS), FASTA/FASTQ işleme, genom hizalama algoritmaları (Smith-Waterman, Burrows-Wheeler) ve varyant analizi.",
  "High-throughput sequencing data structures, Burrows-Wheeler transform indexing, sequence alignment algorithms, and genomic variant calling."
)

#include "/content/mod13_bioinformatics_genomics/lesson_121.typ"
#v(12pt)

#include "/content/mod13_bioinformatics_genomics/lesson_122.typ"
#v(12pt)

#include "/content/mod13_bioinformatics_genomics/lesson_123.typ"
#v(12pt)

#include "/content/mod13_bioinformatics_genomics/lesson_124.typ"
#v(12pt)

#include "/content/mod13_bioinformatics_genomics/lesson_125.typ"
#v(12pt)

#include "/content/mod13_bioinformatics_genomics/lesson_126.typ"
#v(12pt)

#include "/content/mod13_bioinformatics_genomics/lesson_127.typ"
#v(12pt)

#include "/content/mod13_bioinformatics_genomics/lesson_128.typ"
#v(12pt)

#include "/content/mod13_bioinformatics_genomics/lesson_129.typ"
#v(12pt)

#include "/content/mod13_bioinformatics_genomics/lesson_130.typ"
#v(12pt)


#module_cover(
  14,
  "Yapay Zekâ ile Protein Tasarımı: AlphaFold 3 & RFdiffusion",
  "AI for Structural Biology: AlphaFold 3 & De Novo Protein Design",
  "Protein katlanma problemi, çoklu dizi hizalaması (MSA), Evoformer mimarisi, difüzyon modelleriyle sıfırdan enzim ve ilaç tasarımı.",
  "Structural biology geometric deep learning, invariant point attention, diffusion models for protein backbone generation, and ligand docking."
)

#include "/content/mod14_ai_protein_design/lesson_131.typ"
#v(12pt)

#include "/content/mod14_ai_protein_design/lesson_132.typ"
#v(12pt)

#include "/content/mod14_ai_protein_design/lesson_133.typ"
#v(12pt)

#include "/content/mod14_ai_protein_design/lesson_134.typ"
#v(12pt)

#include "/content/mod14_ai_protein_design/lesson_135.typ"
#v(12pt)

#include "/content/mod14_ai_protein_design/lesson_136.typ"
#v(12pt)

#include "/content/mod14_ai_protein_design/lesson_137.typ"
#v(12pt)

#include "/content/mod14_ai_protein_design/lesson_138.typ"
#v(12pt)

#include "/content/mod14_ai_protein_design/lesson_139.typ"
#v(12pt)

#include "/content/mod14_ai_protein_design/lesson_140.typ"
#v(12pt)


#module_cover(
  15,
  "Biyo-Üretim, Hücresel Tarım & 3D Biyo-Baskı",
  "Biofabrication, Cellular Agriculture & 3D Bioprinting",
  "Hassas mikrobiyal fermantasyon, biyoreaktör kinetiği, hücresel temiz et üretimi ve canlı hücrelerle 3D yapay doku basımı.",
  "Bioreactor mass transfer kinetics, microbial strain engineering, hydrogel bio-inks, cell scaffolding, and 3D organoid extrusion."
)

#include "/content/mod15_biofabrication_cellular/lesson_141.typ"
#v(12pt)

#include "/content/mod15_biofabrication_cellular/lesson_142.typ"
#v(12pt)

#include "/content/mod15_biofabrication_cellular/lesson_143.typ"
#v(12pt)

#include "/content/mod15_biofabrication_cellular/lesson_144.typ"
#v(12pt)

#include "/content/mod15_biofabrication_cellular/lesson_145.typ"
#v(12pt)

#include "/content/mod15_biofabrication_cellular/lesson_146.typ"
#v(12pt)

#include "/content/mod15_biofabrication_cellular/lesson_147.typ"
#v(12pt)

#include "/content/mod15_biofabrication_cellular/lesson_148.typ"
#v(12pt)

#include "/content/mod15_biofabrication_cellular/lesson_149.typ"
#v(12pt)

#include "/content/mod15_biofabrication_cellular/lesson_150.typ"
#v(12pt)


#module_cover(
  16,
  "İleri Malzeme Bilimi: Grafen, Karbon Nanotüpler & MXenes",
  "Advanced Materials Science: Graphene, Carbon Nanotubes & MXenes",
  "2D atomik malzemeler, sp2 karbon bağları, süper iletken nanotüpler, elektrokimyasal MXene tabakaları ve kompozit mukavemet analizleri.",
  "2D crystal crystallography, sp2 hybridization transport properties, single-walled carbon nanotubes, MXene ion intercalation, and nanocomposites."
)

#include "/content/mod16_advanced_materials_nano/lesson_151.typ"
#v(12pt)

#include "/content/mod16_advanced_materials_nano/lesson_152.typ"
#v(12pt)

#include "/content/mod16_advanced_materials_nano/lesson_153.typ"
#v(12pt)

#include "/content/mod16_advanced_materials_nano/lesson_154.typ"
#v(12pt)

#include "/content/mod16_advanced_materials_nano/lesson_155.typ"
#v(12pt)

#include "/content/mod16_advanced_materials_nano/lesson_156.typ"
#v(12pt)

#include "/content/mod16_advanced_materials_nano/lesson_157.typ"
#v(12pt)

#include "/content/mod16_advanced_materials_nano/lesson_158.typ"
#v(12pt)

#include "/content/mod16_advanced_materials_nano/lesson_159.typ"
#v(12pt)

#include "/content/mod16_advanced_materials_nano/lesson_160.typ"
#v(12pt)


#module_cover(
  17,
  "Süperiletkenlik (HTS), Meissner Etkisi & Kriyogenik",
  "Superconductivity (HTS), Meissner Effect & Cryogenic Engineering",
  "Sıfır elektriksel direnç, Tip I/II süperiletkenler, YBCO yüksek sıcaklık süperiletkenleri ve seyreltme buzdolapları (Dilution Refrigerators).",
  "Cooper pairing BCS theory, flux pinning dynamics, high-temperature ceramic superconductors (YBCO), and milliKelvin cryogenic dilution stages."
)

#include "/content/mod17_superconductors_cryogenics/lesson_161.typ"
#v(12pt)

#include "/content/mod17_superconductors_cryogenics/lesson_162.typ"
#v(12pt)

#include "/content/mod17_superconductors_cryogenics/lesson_163.typ"
#v(12pt)

#include "/content/mod17_superconductors_cryogenics/lesson_164.typ"
#v(12pt)

#include "/content/mod17_superconductors_cryogenics/lesson_165.typ"
#v(12pt)

#include "/content/mod17_superconductors_cryogenics/lesson_166.typ"
#v(12pt)

#include "/content/mod17_superconductors_cryogenics/lesson_167.typ"
#v(12pt)

#include "/content/mod17_superconductors_cryogenics/lesson_168.typ"
#v(12pt)

#include "/content/mod17_superconductors_cryogenics/lesson_169.typ"
#v(12pt)

#include "/content/mod17_superconductors_cryogenics/lesson_170.typ"
#v(12pt)


#module_cover(
  18,
  "Yeni Nesil Enerji Depolama: Katı Hal Bataryaları & Lityum-Metal",
  "Next-Gen Energy Storage: Solid-State & Lithium-Metal Batteries",
  "Sıvı elektrolit riskleri, seramik/polimer katı elektrolitler, lityum dendrit oluşumunu engelleme ve gravimetrik enerji yoğunluğu (>500 Wh/kg).",
  "Solid electrolyte interphase (SEI) mechanics, ionic conductivity of garnets/sulfides, lithium dendrite suppression, and battery cycling physics."
)

#include "/content/mod18_solid_state_batteries/lesson_171.typ"
#v(12pt)

#include "/content/mod18_solid_state_batteries/lesson_172.typ"
#v(12pt)

#include "/content/mod18_solid_state_batteries/lesson_173.typ"
#v(12pt)

#include "/content/mod18_solid_state_batteries/lesson_174.typ"
#v(12pt)

#include "/content/mod18_solid_state_batteries/lesson_175.typ"
#v(12pt)

#include "/content/mod18_solid_state_batteries/lesson_176.typ"
#v(12pt)

#include "/content/mod18_solid_state_batteries/lesson_177.typ"
#v(12pt)

#include "/content/mod18_solid_state_batteries/lesson_178.typ"
#v(12pt)

#include "/content/mod18_solid_state_batteries/lesson_179.typ"
#v(12pt)

#include "/content/mod18_solid_state_batteries/lesson_180.typ"
#v(12pt)


#module_cover(
  19,
  "Nükleer Füzyon Enerjisi: Tokamaklar, Manyetik Hapsolma & Plazma",
  "Nuclear Fusion Energy: Tokamaks, Magnetic Confinement & Plasma Physics",
  "Deuterium-Tritium reaksiyonu, Lawson kriteri (Q > 1), Tokamak manyetik kafesleri, plazma instabiliteleri ve yüksek manyetik alanlı HTS bobinleri.",
  "Deuterium-tritium fusion cross-sections, Lawson triple product, magnetohydrodynamic plasma equilibrium, and high-field HTS tokamak magnets."
)

#include "/content/mod19_nuclear_fusion/lesson_181.typ"
#v(12pt)

#include "/content/mod19_nuclear_fusion/lesson_182.typ"
#v(12pt)

#include "/content/mod19_nuclear_fusion/lesson_183.typ"
#v(12pt)

#include "/content/mod19_nuclear_fusion/lesson_184.typ"
#v(12pt)

#include "/content/mod19_nuclear_fusion/lesson_185.typ"
#v(12pt)

#include "/content/mod19_nuclear_fusion/lesson_186.typ"
#v(12pt)

#include "/content/mod19_nuclear_fusion/lesson_187.typ"
#v(12pt)

#include "/content/mod19_nuclear_fusion/lesson_188.typ"
#v(12pt)

#include "/content/mod19_nuclear_fusion/lesson_189.typ"
#v(12pt)

#include "/content/mod19_nuclear_fusion/lesson_190.typ"
#v(12pt)


#module_cover(
  20,
  "Yeşil Hidrojen & Doğrudan Havadan Karbon Yakalama (DAC)",
  "Green Hydrogen Economy & Direct Air Carbon Capture (DAC)",
  "PEM ve Katı Oksit elektrolizörler, metal-organik kafesler (MOF) ile doğrudan havadan CO2 emilimi ve kimyasal karbon depolama.",
  "Proton exchange membrane electrolysis overpotentials, metal-organic framework (MOF) gas sorption thermodynamics, and geologic sequestration."
)

#include "/content/mod20_hydrogen_carbon_capture/lesson_191.typ"
#v(12pt)

#include "/content/mod20_hydrogen_carbon_capture/lesson_192.typ"
#v(12pt)

#include "/content/mod20_hydrogen_carbon_capture/lesson_193.typ"
#v(12pt)

#include "/content/mod20_hydrogen_carbon_capture/lesson_194.typ"
#v(12pt)

#include "/content/mod20_hydrogen_carbon_capture/lesson_195.typ"
#v(12pt)

#include "/content/mod20_hydrogen_carbon_capture/lesson_196.typ"
#v(12pt)

#include "/content/mod20_hydrogen_carbon_capture/lesson_197.typ"
#v(12pt)

#include "/content/mod20_hydrogen_carbon_capture/lesson_198.typ"
#v(12pt)

#include "/content/mod20_hydrogen_carbon_capture/lesson_199.typ"
#v(12pt)

#include "/content/mod20_hydrogen_carbon_capture/lesson_200.typ"
#v(12pt)


#module_cover(
  21,
  "Uzay Teknolojileri: Roket İtki Sistemleri & Yörünge Mekaniği",
  "Space Propulsion & Orbital Mechanics: Tsiolkovsky to Aerospikes",
  "Tsiolkovsky roket denklemi, Özgül İtki (Isp), kademeli yanma döngüleri, İyon iticileri (Hall-effect) ve Hohmann yörünge transferi.",
  "Rocket momentum equations, specific impulse thermodynamics, staged combustion cycle engines, electrostatic Hall thrusters, and orbital maneuvers."
)

#include "/content/mod21_space_propulsion_rockets/lesson_201.typ"
#v(12pt)

#include "/content/mod21_space_propulsion_rockets/lesson_202.typ"
#v(12pt)

#include "/content/mod21_space_propulsion_rockets/lesson_203.typ"
#v(12pt)

#include "/content/mod21_space_propulsion_rockets/lesson_204.typ"
#v(12pt)

#include "/content/mod21_space_propulsion_rockets/lesson_205.typ"
#v(12pt)

#include "/content/mod21_space_propulsion_rockets/lesson_206.typ"
#v(12pt)

#include "/content/mod21_space_propulsion_rockets/lesson_207.typ"
#v(12pt)

#include "/content/mod21_space_propulsion_rockets/lesson_208.typ"
#v(12pt)

#include "/content/mod21_space_propulsion_rockets/lesson_209.typ"
#v(12pt)

#include "/content/mod21_space_propulsion_rockets/lesson_210.typ"
#v(12pt)


#module_cover(
  22,
  "Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi",
  "LEO Satellite Constellations & Optical Inter-Satellite Links",
  "Alçak Dünya Yörüngesi (LEO) mega-takımyıldızları, Faz dizili antenler (Beamforming), optik lazer haberleşme ve yörünge çöpü önleme.",
  "LEO orbital perturbations, phased-array electronically steered beamforming, free-space optical laser communications, and collision avoidance."
)

#include "/content/mod22_satellites_space_comms/lesson_211.typ"
#v(12pt)

#include "/content/mod22_satellites_space_comms/lesson_212.typ"
#v(12pt)

#include "/content/mod22_satellites_space_comms/lesson_213.typ"
#v(12pt)

#include "/content/mod22_satellites_space_comms/lesson_214.typ"
#v(12pt)

#include "/content/mod22_satellites_space_comms/lesson_215.typ"
#v(12pt)

#include "/content/mod22_satellites_space_comms/lesson_216.typ"
#v(12pt)

#include "/content/mod22_satellites_space_comms/lesson_217.typ"
#v(12pt)

#include "/content/mod22_satellites_space_comms/lesson_218.typ"
#v(12pt)

#include "/content/mod22_satellites_space_comms/lesson_219.typ"
#v(12pt)

#include "/content/mod22_satellites_space_comms/lesson_220.typ"
#v(12pt)


#module_cover(
  23,
  "Otonom Robotik: İleri/Ters Kinematik & İnsansı Robot Dinamiği",
  "Autonomous Robotics: Forward/Inverse Kinematics & Humanoid Dynamics",
  "Denavit-Hartenberg (DH) parametreleri, Jakobiyen matrisleri, Singularities, Model Predictive Control (MPC) ve insansı robot denge modelleri.",
  "Rigid body transformations, geometric and numerical inverse kinematics, manipulator Jacobians, and zero-moment point (ZMP) locomotion."
)

#include "/content/mod23_autonomous_robotics_kinematics/lesson_221.typ"
#v(12pt)

#include "/content/mod23_autonomous_robotics_kinematics/lesson_222.typ"
#v(12pt)

#include "/content/mod23_autonomous_robotics_kinematics/lesson_223.typ"
#v(12pt)

#include "/content/mod23_autonomous_robotics_kinematics/lesson_224.typ"
#v(12pt)

#include "/content/mod23_autonomous_robotics_kinematics/lesson_225.typ"
#v(12pt)

#include "/content/mod23_autonomous_robotics_kinematics/lesson_226.typ"
#v(12pt)

#include "/content/mod23_autonomous_robotics_kinematics/lesson_227.typ"
#v(12pt)

#include "/content/mod23_autonomous_robotics_kinematics/lesson_228.typ"
#v(12pt)

#include "/content/mod23_autonomous_robotics_kinematics/lesson_229.typ"
#v(12pt)

#include "/content/mod23_autonomous_robotics_kinematics/lesson_230.typ"
#v(12pt)


#module_cover(
  24,
  "Robot İşletim Sistemi (ROS 2) & DDS Dağıtık Middleware",
  "Robot Operating System (ROS 2) & Real-Time Distributed Middleware",
  "ROS 2 mimarisi, Data Distribution Service (DDS), Gerçek zamanlı düğümler (Real-time nodes), Topic/Service/Action protokolleri ve URDF.",
  "ROS 2 micro-ROS architecture, DDS QoS policies, lock-free real-time executor loops, action servers, and robot URDF kinematics trees."
)

#include "/content/mod24_ros2_robot_operating_system/lesson_231.typ"
#v(12pt)

#include "/content/mod24_ros2_robot_operating_system/lesson_232.typ"
#v(12pt)

#include "/content/mod24_ros2_robot_operating_system/lesson_233.typ"
#v(12pt)

#include "/content/mod24_ros2_robot_operating_system/lesson_234.typ"
#v(12pt)

#include "/content/mod24_ros2_robot_operating_system/lesson_235.typ"
#v(12pt)

#include "/content/mod24_ros2_robot_operating_system/lesson_236.typ"
#v(12pt)

#include "/content/mod24_ros2_robot_operating_system/lesson_237.typ"
#v(12pt)

#include "/content/mod24_ros2_robot_operating_system/lesson_238.typ"
#v(12pt)

#include "/content/mod24_ros2_robot_operating_system/lesson_239.typ"
#v(12pt)

#include "/content/mod24_ros2_robot_operating_system/lesson_240.typ"
#v(12pt)


#module_cover(
  25,
  "Mekânsal Hesaplama, SLAM, Görsel Odometri & LiDAR",
  "Spatial Computing & SLAM: Visual-Inertial Odometry & 3D LiDAR",
  "Eşzamanlı Konumlandırma ve Haritalama (SLAM), Genişletilmiş Kalman Filtresi (EKF), bundle adjustment ve 3D LiDAR nokta bulutu eşleştirme.",
  "Simultaneous localization and mapping state estimation, visual-inertial odometry feature tracking, graph-based SLAM, and iterative closest point (ICP)."
)

#include "/content/mod25_spatial_computing_slam/lesson_241.typ"
#v(12pt)

#include "/content/mod25_spatial_computing_slam/lesson_242.typ"
#v(12pt)

#include "/content/mod25_spatial_computing_slam/lesson_243.typ"
#v(12pt)

#include "/content/mod25_spatial_computing_slam/lesson_244.typ"
#v(12pt)

#include "/content/mod25_spatial_computing_slam/lesson_245.typ"
#v(12pt)

#include "/content/mod25_spatial_computing_slam/lesson_246.typ"
#v(12pt)

#include "/content/mod25_spatial_computing_slam/lesson_247.typ"
#v(12pt)

#include "/content/mod25_spatial_computing_slam/lesson_248.typ"
#v(12pt)

#include "/content/mod25_spatial_computing_slam/lesson_249.typ"
#v(12pt)

#include "/content/mod25_spatial_computing_slam/lesson_250.typ"
#v(12pt)


#module_cover(
  26,
  "Beyin-Bilgisayar Arayüzleri (BCI) & Nöroteknoloji (Neuralink)",
  "Brain-Computer Interfaces (BCI) & Neural Spike Decoding",
  "İnvaziv ve non-invaziv elektrotlar, aksiyon potansiyelleri (Spikes), Spike Sorting algoritmaları, motor korteks sinyallerini imlece dönüştürme.",
  "Electrophysiological neural recording, microelectrode array impedance, wavelet-based spike sorting, and motor intent decoders."
)

#include "/content/mod26_brain_computer_interfaces/lesson_251.typ"
#v(12pt)

#include "/content/mod26_brain_computer_interfaces/lesson_252.typ"
#v(12pt)

#include "/content/mod26_brain_computer_interfaces/lesson_253.typ"
#v(12pt)

#include "/content/mod26_brain_computer_interfaces/lesson_254.typ"
#v(12pt)

#include "/content/mod26_brain_computer_interfaces/lesson_255.typ"
#v(12pt)

#include "/content/mod26_brain_computer_interfaces/lesson_256.typ"
#v(12pt)

#include "/content/mod26_brain_computer_interfaces/lesson_257.typ"
#v(12pt)

#include "/content/mod26_brain_computer_interfaces/lesson_258.typ"
#v(12pt)

#include "/content/mod26_brain_computer_interfaces/lesson_259.typ"
#v(12pt)

#include "/content/mod26_brain_computer_interfaces/lesson_260.typ"
#v(12pt)


#module_cover(
  27,
  "Otonom Araçlar: Sensör Füzyonu, Kalman Filtresi & Occupancy",
  "Autonomous Driving: Multi-Sensor Fusion & 3D Occupancy Grids",
  "Kamera-Radar-LiDAR sensör füzyonu, Unscented Kalman Filter (UKF), kuşbakışı görünüm (BEV) dönüşümü ve 3D doluluk ağları (Occupancy Networks).",
  "Multi-modal sensor fusion pipelines, probabilistic Bayesian filtering, temporal bird's-eye-view feature projection, and voxel occupancy prediction."
)

#include "/content/mod27_autonomous_vehicles_perception/lesson_261.typ"
#v(12pt)

#include "/content/mod27_autonomous_vehicles_perception/lesson_262.typ"
#v(12pt)

#include "/content/mod27_autonomous_vehicles_perception/lesson_263.typ"
#v(12pt)

#include "/content/mod27_autonomous_vehicles_perception/lesson_264.typ"
#v(12pt)

#include "/content/mod27_autonomous_vehicles_perception/lesson_265.typ"
#v(12pt)

#include "/content/mod27_autonomous_vehicles_perception/lesson_266.typ"
#v(12pt)

#include "/content/mod27_autonomous_vehicles_perception/lesson_267.typ"
#v(12pt)

#include "/content/mod27_autonomous_vehicles_perception/lesson_268.typ"
#v(12pt)

#include "/content/mod27_autonomous_vehicles_perception/lesson_269.typ"
#v(12pt)

#include "/content/mod27_autonomous_vehicles_perception/lesson_270.typ"
#v(12pt)


#module_cover(
  28,
  "Dronlar, eVTOL & Kentsel Hava Hareketliliği (UAM)",
  "Drones, eVTOL Aerodynamics & Autonomous Flight Navigation",
  "Çok rotorlu uçuş dinamiği, aerodinamik itki modelleri, RRT* otonom yol planlama algoritmaları, coğrafi çit (Geofencing) ve BVLOS uçuş.",
  "Multirotor aerodynamic thrust equations, state-space PID flight controllers, dynamic obstacle avoidance via RRT*, and urban airspace routing."
)

#include "/content/mod28_drones_evtol_uam/lesson_271.typ"
#v(12pt)

#include "/content/mod28_drones_evtol_uam/lesson_272.typ"
#v(12pt)

#include "/content/mod28_drones_evtol_uam/lesson_273.typ"
#v(12pt)

#include "/content/mod28_drones_evtol_uam/lesson_274.typ"
#v(12pt)

#include "/content/mod28_drones_evtol_uam/lesson_275.typ"
#v(12pt)

#include "/content/mod28_drones_evtol_uam/lesson_276.typ"
#v(12pt)

#include "/content/mod28_drones_evtol_uam/lesson_277.typ"
#v(12pt)

#include "/content/mod28_drones_evtol_uam/lesson_278.typ"
#v(12pt)

#include "/content/mod28_drones_evtol_uam/lesson_279.typ"
#v(12pt)

#include "/content/mod28_drones_evtol_uam/lesson_280.typ"
#v(12pt)


#module_cover(
  29,
  "Mikroakışkanlar & Çip Üstü Laboratuvar (Lab-on-a-Chip)",
  "Microfluidics & Lab-on-a-Chip Micro-Electro-Mechanical Systems",
  "Laminer akış ve düşük Reynolds sayıları, damlacık mikroakışkanları (Droplet microfluidics), PDMS çip üretimi ve tek hücre analizi.",
  "Laminar flow microfluidics, capillary diffusion kinetics, microfluidic droplet compartmentalization, and point-of-care bio-MEMS."
)

#include "/content/mod29_microfluidics_lab_on_chip/lesson_281.typ"
#v(12pt)

#include "/content/mod29_microfluidics_lab_on_chip/lesson_282.typ"
#v(12pt)

#include "/content/mod29_microfluidics_lab_on_chip/lesson_283.typ"
#v(12pt)

#include "/content/mod29_microfluidics_lab_on_chip/lesson_284.typ"
#v(12pt)

#include "/content/mod29_microfluidics_lab_on_chip/lesson_285.typ"
#v(12pt)

#include "/content/mod29_microfluidics_lab_on_chip/lesson_286.typ"
#v(12pt)

#include "/content/mod29_microfluidics_lab_on_chip/lesson_287.typ"
#v(12pt)

#include "/content/mod29_microfluidics_lab_on_chip/lesson_288.typ"
#v(12pt)

#include "/content/mod29_microfluidics_lab_on_chip/lesson_289.typ"
#v(12pt)

#include "/content/mod29_microfluidics_lab_on_chip/lesson_290.typ"
#v(12pt)


#module_cover(
  30,
  "Biyo-Elektronik, Optogenetik & Esnek Nöral İmplantlar",
  "Bioelectronics, Optogenetics & Biocompatible Neural Implants",
  "Biyouyumlu esnek polimerler (Parylene, Polyimide), optogenetik ışık stimülasyonu, kanalrodopsin proteinleri ve doku tepkisi optimizasyonu.",
  "Biocompatible flexible micro-substrates, channelrhodopsin light-gated ion channels, foreign-body response mitigation, and closed-loop neuromodulation."
)

#include "/content/mod30_bioelectronics_neural_implants/lesson_291.typ"
#v(12pt)

#include "/content/mod30_bioelectronics_neural_implants/lesson_292.typ"
#v(12pt)

#include "/content/mod30_bioelectronics_neural_implants/lesson_293.typ"
#v(12pt)

#include "/content/mod30_bioelectronics_neural_implants/lesson_294.typ"
#v(12pt)

#include "/content/mod30_bioelectronics_neural_implants/lesson_295.typ"
#v(12pt)

#include "/content/mod30_bioelectronics_neural_implants/lesson_296.typ"
#v(12pt)

#include "/content/mod30_bioelectronics_neural_implants/lesson_297.typ"
#v(12pt)

#include "/content/mod30_bioelectronics_neural_implants/lesson_298.typ"
#v(12pt)

#include "/content/mod30_bioelectronics_neural_implants/lesson_299.typ"
#v(12pt)

#include "/content/mod30_bioelectronics_neural_implants/lesson_300.typ"
#v(12pt)


#module_cover(
  31,
  "İleri Optik, Holografik Ekranlar & Dalga Kılavuzu (AR/VR)",
  "Advanced Optics, Holographic Displays & Waveguides for AR/VR",
  "Mekânsal Işık Modülatörleri (SLM), Kırınımsal optik elemanlar (DOE), holografik dalga kılavuzu birleştiricileri ve retina projeksiyonu.",
  "Spatial light modulation phase interference, diffractive optical waveguide pupil expansion, computer-generated holography, and micro-displays."
)

#include "/content/mod31_optics_holographic_displays/lesson_301.typ"
#v(12pt)

#include "/content/mod31_optics_holographic_displays/lesson_302.typ"
#v(12pt)

#include "/content/mod31_optics_holographic_displays/lesson_303.typ"
#v(12pt)

#include "/content/mod31_optics_holographic_displays/lesson_304.typ"
#v(12pt)

#include "/content/mod31_optics_holographic_displays/lesson_305.typ"
#v(12pt)

#include "/content/mod31_optics_holographic_displays/lesson_306.typ"
#v(12pt)

#include "/content/mod31_optics_holographic_displays/lesson_307.typ"
#v(12pt)

#include "/content/mod31_optics_holographic_displays/lesson_308.typ"
#v(12pt)

#include "/content/mod31_optics_holographic_displays/lesson_309.typ"
#v(12pt)

#include "/content/mod31_optics_holographic_displays/lesson_310.typ"
#v(12pt)


#module_cover(
  32,
  "Süper Bilgisayarlar: Exascale Altyapı, InfiniBand & MPI",
  "Supercomputing & Exascale Architecture: InfiniBand, RDMA & MPI",
  "Eksasabit (10^18 FLOP) hesaplama, InfiniBand NDR anahtarlama matrisleri, Uzaktan Doğrudan Bellek Erişimi (RDMA) ve MPI paralelleştirme.",
  "Exascale interconnect topologies, RoCEv2/InfiniBand kernel-bypass networking, distributed MPI collective operations, and Slurm workload orchestration."
)

#include "/content/mod32_supercomputing_exascale/lesson_311.typ"
#v(12pt)

#include "/content/mod32_supercomputing_exascale/lesson_312.typ"
#v(12pt)

#include "/content/mod32_supercomputing_exascale/lesson_313.typ"
#v(12pt)

#include "/content/mod32_supercomputing_exascale/lesson_314.typ"
#v(12pt)

#include "/content/mod32_supercomputing_exascale/lesson_315.typ"
#v(12pt)

#include "/content/mod32_supercomputing_exascale/lesson_316.typ"
#v(12pt)

#include "/content/mod32_supercomputing_exascale/lesson_317.typ"
#v(12pt)

#include "/content/mod32_supercomputing_exascale/lesson_318.typ"
#v(12pt)

#include "/content/mod32_supercomputing_exascale/lesson_319.typ"
#v(12pt)

#include "/content/mod32_supercomputing_exascale/lesson_320.typ"
#v(12pt)


#module_cover(
  33,
  "Dağıtık Yapay Zekâ Eğitimi: 3D Paralellik & Megatron-LM",
  "Distributed AI Superclusters: 3D Parallelism & Megatron-LM",
  "Trilyon parametreli modeller, Tensör Paralelliği, Boru Hattı Paralelliği, DeepSpeed ZeRO bellek optimizasyonu ve GPU küme tasarımı.",
  "Tensor and pipeline model partitioning, zero-redundancy optimizer memory sharding, all-reduce communication overlaps, and cluster fault resilience."
)

#include "/content/mod33_distributed_ai_superclusters/lesson_321.typ"
#v(12pt)

#include "/content/mod33_distributed_ai_superclusters/lesson_322.typ"
#v(12pt)

#include "/content/mod33_distributed_ai_superclusters/lesson_323.typ"
#v(12pt)

#include "/content/mod33_distributed_ai_superclusters/lesson_324.typ"
#v(12pt)

#include "/content/mod33_distributed_ai_superclusters/lesson_325.typ"
#v(12pt)

#include "/content/mod33_distributed_ai_superclusters/lesson_326.typ"
#v(12pt)

#include "/content/mod33_distributed_ai_superclusters/lesson_327.typ"
#v(12pt)

#include "/content/mod33_distributed_ai_superclusters/lesson_328.typ"
#v(12pt)

#include "/content/mod33_distributed_ai_superclusters/lesson_329.typ"
#v(12pt)

#include "/content/mod33_distributed_ai_superclusters/lesson_330.typ"
#v(12pt)


#module_cover(
  34,
  "Bellek İçi Hesaplama (IMC) & Analog Yapay Zekâ Çipleri",
  "Analog In-Memory Computing & Neuromorphic Resistive RAM (RRAM)",
  "Ohm ve Kirchhoff kanunlarıyla analog matris çarpımı, RRAM ve Faz Değişimli Bellek (PCM) hücreleri, analog-dijital çevirici (ADC) darboğazları.",
  "Ohm's Law analog multiply-accumulate crossbar arrays, memristive state drift compensation, ADC/DAC energy trade-offs, and analog inference."
)

#include "/content/mod34_analog_in_memory_computing/lesson_331.typ"
#v(12pt)

#include "/content/mod34_analog_in_memory_computing/lesson_332.typ"
#v(12pt)

#include "/content/mod34_analog_in_memory_computing/lesson_333.typ"
#v(12pt)

#include "/content/mod34_analog_in_memory_computing/lesson_334.typ"
#v(12pt)

#include "/content/mod34_analog_in_memory_computing/lesson_335.typ"
#v(12pt)

#include "/content/mod34_analog_in_memory_computing/lesson_336.typ"
#v(12pt)

#include "/content/mod34_analog_in_memory_computing/lesson_337.typ"
#v(12pt)

#include "/content/mod34_analog_in_memory_computing/lesson_338.typ"
#v(12pt)

#include "/content/mod34_analog_in_memory_computing/lesson_339.typ"
#v(12pt)

#include "/content/mod34_analog_in_memory_computing/lesson_340.typ"
#v(12pt)


#module_cover(
  35,
  "Tarım Teknolojileri (AgTech): Hassas Tarım & Otonom Sistemler",
  "AgTech: Precision Agriculture, Hyperspectral Imaging & Aeroponics",
  "Hipospektral drone görüntüleme, bitki NDVI indeksleri, otonom yabani ot temizleme lazerleri ve dikey aeroponik sera otomasyonu.",
  "Hyperspectral crop reflectance index calculation, autonomous laser weeding computer vision, root-zone nutrient dosing, and vertical farming telemetry."
)

#include "/content/mod35_agtech_precision_farming/lesson_341.typ"
#v(12pt)

#include "/content/mod35_agtech_precision_farming/lesson_342.typ"
#v(12pt)

#include "/content/mod35_agtech_precision_farming/lesson_343.typ"
#v(12pt)

#include "/content/mod35_agtech_precision_farming/lesson_344.typ"
#v(12pt)

#include "/content/mod35_agtech_precision_farming/lesson_345.typ"
#v(12pt)

#include "/content/mod35_agtech_precision_farming/lesson_346.typ"
#v(12pt)

#include "/content/mod35_agtech_precision_farming/lesson_347.typ"
#v(12pt)

#include "/content/mod35_agtech_precision_farming/lesson_348.typ"
#v(12pt)

#include "/content/mod35_agtech_precision_farming/lesson_349.typ"
#v(12pt)

#include "/content/mod35_agtech_precision_farming/lesson_350.typ"
#v(12pt)


#module_cover(
  36,
  "Su Teknolojileri: Grafen Oksit Membranlar & İleri Arıtma",
  "Advanced Water Technologies: Graphene Membranes & Desalination",
  "Ters Ozmoz (RO) termodinamik verimliliği, nanoporöz grafen su filtreleme, ileri ozmoz ve termal güneş enerjili tuzdan arındırma sistemleri.",
  "Thermodynamic limits of seawater reverse osmosis, sub-nanometer graphene oxide selective transport, forward osmosis, and fouling-resistant coatings."
)

#include "/content/mod36_water_tech_desalination/lesson_351.typ"
#v(12pt)

#include "/content/mod36_water_tech_desalination/lesson_352.typ"
#v(12pt)

#include "/content/mod36_water_tech_desalination/lesson_353.typ"
#v(12pt)

#include "/content/mod36_water_tech_desalination/lesson_354.typ"
#v(12pt)

#include "/content/mod36_water_tech_desalination/lesson_355.typ"
#v(12pt)

#include "/content/mod36_water_tech_desalination/lesson_356.typ"
#v(12pt)

#include "/content/mod36_water_tech_desalination/lesson_357.typ"
#v(12pt)

#include "/content/mod36_water_tech_desalination/lesson_358.typ"
#v(12pt)

#include "/content/mod36_water_tech_desalination/lesson_359.typ"
#v(12pt)

#include "/content/mod36_water_tech_desalination/lesson_360.typ"
#v(12pt)


#module_cover(
  37,
  "İleri İmalat: Metal 3D Baskı (DMLS) & Katmanlı Üretim",
  "Advanced Additive Manufacturing: Direct Metal Laser Sintering (DMLS)",
  "Lazer Toz Yatağı Füzyonu (LPBF), titanyum ve Inconel alaşımları, termal gerinim simülasyonları ve topoloji optimizasyonu ile hafif parça tasarımı.",
  "Laser powder bed fusion metallurgy, melt-pool thermo-capillary convection, finite-element residual stress modeling, and generative topology optimization."
)

#include "/content/mod37_advanced_manufacturing_3d/lesson_361.typ"
#v(12pt)

#include "/content/mod37_advanced_manufacturing_3d/lesson_362.typ"
#v(12pt)

#include "/content/mod37_advanced_manufacturing_3d/lesson_363.typ"
#v(12pt)

#include "/content/mod37_advanced_manufacturing_3d/lesson_364.typ"
#v(12pt)

#include "/content/mod37_advanced_manufacturing_3d/lesson_365.typ"
#v(12pt)

#include "/content/mod37_advanced_manufacturing_3d/lesson_366.typ"
#v(12pt)

#include "/content/mod37_advanced_manufacturing_3d/lesson_367.typ"
#v(12pt)

#include "/content/mod37_advanced_manufacturing_3d/lesson_368.typ"
#v(12pt)

#include "/content/mod37_advanced_manufacturing_3d/lesson_369.typ"
#v(12pt)

#include "/content/mod37_advanced_manufacturing_3d/lesson_370.typ"
#v(12pt)


#module_cover(
  38,
  "Sıfır Bilgi İspatları (ZKP) & Kriptografik Donanım Hızlandırma",
  "Zero-Knowledge Hardware Acceleration: ASICs/FPGAs for ZK-SNARKs",
  "ZK-SNARK ve STARK matematik temelleri, Sayı Teorik Dönüşümleri (NTT), Çok Noktalı Skalar Çarpımı (MSM) ve FPGA/ASIC hızlandırıcılar.",
  "Elliptic curve pairing cryptography, multi-scalar multiplication (MSM) hardware pipelines, number theoretic transform (NTT) accelerators, and ZK rollups."
)

#include "/content/mod38_zero_knowledge_hardware/lesson_371.typ"
#v(12pt)

#include "/content/mod38_zero_knowledge_hardware/lesson_372.typ"
#v(12pt)

#include "/content/mod38_zero_knowledge_hardware/lesson_373.typ"
#v(12pt)

#include "/content/mod38_zero_knowledge_hardware/lesson_374.typ"
#v(12pt)

#include "/content/mod38_zero_knowledge_hardware/lesson_375.typ"
#v(12pt)

#include "/content/mod38_zero_knowledge_hardware/lesson_376.typ"
#v(12pt)

#include "/content/mod38_zero_knowledge_hardware/lesson_377.typ"
#v(12pt)

#include "/content/mod38_zero_knowledge_hardware/lesson_378.typ"
#v(12pt)

#include "/content/mod38_zero_knowledge_hardware/lesson_379.typ"
#v(12pt)

#include "/content/mod38_zero_knowledge_hardware/lesson_380.typ"
#v(12pt)


#module_cover(
  39,
  "Otonom Kimya & Kendi Kendini Yöneten Robotik Laboratuvarlar",
  "Autonomous Chemistry & Self-Driving Discovery Laboratories",
  "Sıvı taşıma robotları, Bayesyen optimizasyon ile reaksiyon koşulu keşfi, kapalı döngü sentez ve kimyasal uzay tarama algoritmaları.",
  "Automated liquid-handling robotics, active learning Bayesian optimization for chemical yields, closed-loop spectroscopy feedback, and molecular search."
)

#include "/content/mod39_autonomous_chemistry_labs/lesson_381.typ"
#v(12pt)

#include "/content/mod39_autonomous_chemistry_labs/lesson_382.typ"
#v(12pt)

#include "/content/mod39_autonomous_chemistry_labs/lesson_383.typ"
#v(12pt)

#include "/content/mod39_autonomous_chemistry_labs/lesson_384.typ"
#v(12pt)

#include "/content/mod39_autonomous_chemistry_labs/lesson_385.typ"
#v(12pt)

#include "/content/mod39_autonomous_chemistry_labs/lesson_386.typ"
#v(12pt)

#include "/content/mod39_autonomous_chemistry_labs/lesson_387.typ"
#v(12pt)

#include "/content/mod39_autonomous_chemistry_labs/lesson_388.typ"
#v(12pt)

#include "/content/mod39_autonomous_chemistry_labs/lesson_389.typ"
#v(12pt)

#include "/content/mod39_autonomous_chemistry_labs/lesson_390.typ"
#v(12pt)


#module_cover(
  40,
  "İklim Teknolojileri & Yapay Zekâ ile Hava Tahmini (GraphCast)",
  "Climate Tech & Global AI Weather Prediction: GraphCast & Models",
  "Sayısal hava tahmin modelleri vs Graflı Sinir Ağları (GNN), GraphCast mimarisi, okyanus akıntı modellemesi ve küresel iklim simülasyonları.",
  "Numerical weather differential equations, spherical mesh graph neural networks (GraphCast), climate ensemble forecasting, and oceanic energy balances."
)

#include "/content/mod40_climatetech_ai_weather/lesson_391.typ"
#v(12pt)

#include "/content/mod40_climatetech_ai_weather/lesson_392.typ"
#v(12pt)

#include "/content/mod40_climatetech_ai_weather/lesson_393.typ"
#v(12pt)

#include "/content/mod40_climatetech_ai_weather/lesson_394.typ"
#v(12pt)

#include "/content/mod40_climatetech_ai_weather/lesson_395.typ"
#v(12pt)

#include "/content/mod40_climatetech_ai_weather/lesson_396.typ"
#v(12pt)

#include "/content/mod40_climatetech_ai_weather/lesson_397.typ"
#v(12pt)

#include "/content/mod40_climatetech_ai_weather/lesson_398.typ"
#v(12pt)

#include "/content/mod40_climatetech_ai_weather/lesson_399.typ"
#v(12pt)

#include "/content/mod40_climatetech_ai_weather/lesson_400.typ"
#v(12pt)


#module_cover(
  41,
  "Derin Deniz Robotikleri (AUV) & Aşırı Ortam Teknolojileri",
  "Deep Sea Exploration: Autonomous Underwater Vehicles & High Pressure",
  "1000 bar hidrostatik basınç mühendisliği, akustik su altı telemetrisi, batimetrik sonar haritalama ve hidrotermal menfez keşif robotları.",
  "Hyperbaric titanium pressure vessel design, acoustic OFDM underwater communications, synthetic aperture sonar bathymetry, and benthic autonomy."
)

#include "/content/mod41_deepsea_extreme_environments/lesson_401.typ"
#v(12pt)

#include "/content/mod41_deepsea_extreme_environments/lesson_402.typ"
#v(12pt)

#include "/content/mod41_deepsea_extreme_environments/lesson_403.typ"
#v(12pt)

#include "/content/mod41_deepsea_extreme_environments/lesson_404.typ"
#v(12pt)

#include "/content/mod41_deepsea_extreme_environments/lesson_405.typ"
#v(12pt)

#include "/content/mod41_deepsea_extreme_environments/lesson_406.typ"
#v(12pt)

#include "/content/mod41_deepsea_extreme_environments/lesson_407.typ"
#v(12pt)

#include "/content/mod41_deepsea_extreme_environments/lesson_408.typ"
#v(12pt)

#include "/content/mod41_deepsea_extreme_environments/lesson_409.typ"
#v(12pt)

#include "/content/mod41_deepsea_extreme_environments/lesson_410.typ"
#v(12pt)


#module_cover(
  42,
  "Biyomedikal Görüntüleme: Cryo-EM & Süper Çözünürlüklü Mikroskopi",
  "Biomedical Imaging: Cryo-EM Reconstruction & Super-Resolution",
  "Elektron kriyomikroskopisi (Cryo-EM), tek partikül 3D rekonstrüksiyonu, STED mikroskopisi ve optik koherens tomografi (OCT).",
  "Single-particle cryo-electron microscopy Fourier projection slice theorem, diffraction-limit overcoming STED depletion, and interferometric OCT imaging."
)

#include "/content/mod42_biomedical_imaging_microscopy/lesson_411.typ"
#v(12pt)

#include "/content/mod42_biomedical_imaging_microscopy/lesson_412.typ"
#v(12pt)

#include "/content/mod42_biomedical_imaging_microscopy/lesson_413.typ"
#v(12pt)

#include "/content/mod42_biomedical_imaging_microscopy/lesson_414.typ"
#v(12pt)

#include "/content/mod42_biomedical_imaging_microscopy/lesson_415.typ"
#v(12pt)

#include "/content/mod42_biomedical_imaging_microscopy/lesson_416.typ"
#v(12pt)

#include "/content/mod42_biomedical_imaging_microscopy/lesson_417.typ"
#v(12pt)

#include "/content/mod42_biomedical_imaging_microscopy/lesson_418.typ"
#v(12pt)

#include "/content/mod42_biomedical_imaging_microscopy/lesson_419.typ"
#v(12pt)

#include "/content/mod42_biomedical_imaging_microscopy/lesson_420.typ"
#v(12pt)


#module_cover(
  43,
  "Aşırı Rejim Sensörleri: Terahertz, Piezoelektrik & MEMS",
  "Extreme Regime Sensors: Terahertz, Piezoelectrics & Resonant MEMS",
  "Terahertz elektromanyetik dalga spektroskopisi, yüksek sıcaklık piezoelektrik dönüştürücüler, atomik kuvvet mikroskobu (AFM) konsolları.",
  "Terahertz time-domain spectroscopy, high-temperature piezoelectric perovskite ceramics, resonant micro-cantilevers, and sub-angstrom deflection."
)

#include "/content/mod43_extreme_sensors_actuators/lesson_421.typ"
#v(12pt)

#include "/content/mod43_extreme_sensors_actuators/lesson_422.typ"
#v(12pt)

#include "/content/mod43_extreme_sensors_actuators/lesson_423.typ"
#v(12pt)

#include "/content/mod43_extreme_sensors_actuators/lesson_424.typ"
#v(12pt)

#include "/content/mod43_extreme_sensors_actuators/lesson_425.typ"
#v(12pt)

#include "/content/mod43_extreme_sensors_actuators/lesson_426.typ"
#v(12pt)

#include "/content/mod43_extreme_sensors_actuators/lesson_427.typ"
#v(12pt)

#include "/content/mod43_extreme_sensors_actuators/lesson_428.typ"
#v(12pt)

#include "/content/mod43_extreme_sensors_actuators/lesson_429.typ"
#v(12pt)

#include "/content/mod43_extreme_sensors_actuators/lesson_430.typ"
#v(12pt)


#module_cover(
  44,
  "Siber-Fiziksel Sistemler & Endüstriyel Dijital İkizler",
  "Cyber-Physical Systems & Industrial Digital Twins",
  "Fizik motorları ile gerçek zamanlı telemetri eşleştirme, kalman filtreleme ile durum kestirimi, endüstriyel OPC UA ve MQTT protokolleri.",
  "Real-time physical co-simulation, state-space digital twin reconciliation, industrial IoT pub/sub bridges, and predictive mechanical failure prognosis."
)

#include "/content/mod44_cyber_physical_digital_twins/lesson_431.typ"
#v(12pt)

#include "/content/mod44_cyber_physical_digital_twins/lesson_432.typ"
#v(12pt)

#include "/content/mod44_cyber_physical_digital_twins/lesson_433.typ"
#v(12pt)

#include "/content/mod44_cyber_physical_digital_twins/lesson_434.typ"
#v(12pt)

#include "/content/mod44_cyber_physical_digital_twins/lesson_435.typ"
#v(12pt)

#include "/content/mod44_cyber_physical_digital_twins/lesson_436.typ"
#v(12pt)

#include "/content/mod44_cyber_physical_digital_twins/lesson_437.typ"
#v(12pt)

#include "/content/mod44_cyber_physical_digital_twins/lesson_438.typ"
#v(12pt)

#include "/content/mod44_cyber_physical_digital_twins/lesson_439.typ"
#v(12pt)

#include "/content/mod44_cyber_physical_digital_twins/lesson_440.typ"
#v(12pt)


#module_cover(
  45,
  "Deeptech Fikri Mülkiyet (IP) Stratejisi: Patentler & Ticari Sırlar",
  "Deeptech Intellectual Property: Patents, Trade Secrets & Freedom to Operate",
  "Patentlenebilirlik kriterleri, PCT uluslararası başvuru stratejisi, Ticari Sır (Trade Secret) vs Patent ikilemi ve Özgürce Çalışabilirlik (FTO).",
  "Evaluating novel scientific inventions, drafting enforceable claims, strategic defensive publishing, and conducting rigorous Freedom to Operate (FTO) audits."
)

#include "/content/mod45_deeptech_ip_patents/lesson_441.typ"
#v(12pt)

#include "/content/mod45_deeptech_ip_patents/lesson_442.typ"
#v(12pt)

#include "/content/mod45_deeptech_ip_patents/lesson_443.typ"
#v(12pt)

#include "/content/mod45_deeptech_ip_patents/lesson_444.typ"
#v(12pt)

#include "/content/mod45_deeptech_ip_patents/lesson_445.typ"
#v(12pt)

#include "/content/mod45_deeptech_ip_patents/lesson_446.typ"
#v(12pt)

#include "/content/mod45_deeptech_ip_patents/lesson_447.typ"
#v(12pt)

#include "/content/mod45_deeptech_ip_patents/lesson_448.typ"
#v(12pt)

#include "/content/mod45_deeptech_ip_patents/lesson_449.typ"
#v(12pt)

#include "/content/mod45_deeptech_ip_patents/lesson_450.typ"
#v(12pt)


#module_cover(
  46,
  "Hard Tech Girişim Sermayesi (VC) & Teknoloji Hazırlık Seviyeleri (TRL)",
  "Hard Tech Venture Capital, Milestones & TRL 1-9 De-risking",
  "Deeptech yatırım tezleri, laboratuvar aşamasından ticari ürüne (TRL 1-9) geçiş, ölüm vadisi (Valley of Death) finansmanı ve dilüsyonsuz hibeler.",
  "Scientific de-risking milestones, milestone-based tranche financing, bridging the commercialization valley of death, and public non-dilutive grants."
)

#include "/content/mod46_hardtech_venture_capital/lesson_451.typ"
#v(12pt)

#include "/content/mod46_hardtech_venture_capital/lesson_452.typ"
#v(12pt)

#include "/content/mod46_hardtech_venture_capital/lesson_453.typ"
#v(12pt)

#include "/content/mod46_hardtech_venture_capital/lesson_454.typ"
#v(12pt)

#include "/content/mod46_hardtech_venture_capital/lesson_455.typ"
#v(12pt)

#include "/content/mod46_hardtech_venture_capital/lesson_456.typ"
#v(12pt)

#include "/content/mod46_hardtech_venture_capital/lesson_457.typ"
#v(12pt)

#include "/content/mod46_hardtech_venture_capital/lesson_458.typ"
#v(12pt)

#include "/content/mod46_hardtech_venture_capital/lesson_459.typ"
#v(12pt)

#include "/content/mod46_hardtech_venture_capital/lesson_460.typ"
#v(12pt)


#module_cover(
  47,
  "Tekno-Ekonomik Analiz (TEA) & Birinci Tesis (FOAK) Ölçekleme",
  "Techno-Economic Analysis (TEA) & First-of-a-Kind (FOAK) Scale-Up",
  "Seviyelendirilmiş Enerji/Ürün Maliyeti (LCOE/LCOP), ölçek ekonomisi hesaplamaları, pilot tesisten Gigafactory'ye geçiş ve FOAK risk yönetimi.",
  "Levelized cost of production models, chemical process Aspen simulations, capital expenditure amortization curves, and FOAK commercial scale-up."
)

#include "/content/mod47_techno_economic_analysis/lesson_461.typ"
#v(12pt)

#include "/content/mod47_techno_economic_analysis/lesson_462.typ"
#v(12pt)

#include "/content/mod47_techno_economic_analysis/lesson_463.typ"
#v(12pt)

#include "/content/mod47_techno_economic_analysis/lesson_464.typ"
#v(12pt)

#include "/content/mod47_techno_economic_analysis/lesson_465.typ"
#v(12pt)

#include "/content/mod47_techno_economic_analysis/lesson_466.typ"
#v(12pt)

#include "/content/mod47_techno_economic_analysis/lesson_467.typ"
#v(12pt)

#include "/content/mod47_techno_economic_analysis/lesson_468.typ"
#v(12pt)

#include "/content/mod47_techno_economic_analysis/lesson_469.typ"
#v(12pt)

#include "/content/mod47_techno_economic_analysis/lesson_470.typ"
#v(12pt)


#module_cover(
  48,
  "Düzenleyici Kurum Stratejileri: FDA, FAA & Nükleer Onay Süreçleri",
  "Deeptech Regulatory Pathways: FDA Approvals, FAA Certifications & Safety",
  "Biyoteknoloji FDA Faz I/II/III klinik denemeleri, havacılıkta FAA uçuşa elverişlilik sertifikasyonu, nükleer NRC lisanslama adımları.",
  "FDA 510(k) and PMA medical device approval pathways, FAA part 21 airworthiness type certification for eVTOL, and nuclear licensing protocols."
)

#include "/content/mod48_deeptech_regulations_fda_faa/lesson_471.typ"
#v(12pt)

#include "/content/mod48_deeptech_regulations_fda_faa/lesson_472.typ"
#v(12pt)

#include "/content/mod48_deeptech_regulations_fda_faa/lesson_473.typ"
#v(12pt)

#include "/content/mod48_deeptech_regulations_fda_faa/lesson_474.typ"
#v(12pt)

#include "/content/mod48_deeptech_regulations_fda_faa/lesson_475.typ"
#v(12pt)

#include "/content/mod48_deeptech_regulations_fda_faa/lesson_476.typ"
#v(12pt)

#include "/content/mod48_deeptech_regulations_fda_faa/lesson_477.typ"
#v(12pt)

#include "/content/mod48_deeptech_regulations_fda_faa/lesson_478.typ"
#v(12pt)

#include "/content/mod48_deeptech_regulations_fda_faa/lesson_479.typ"
#v(12pt)

#include "/content/mod48_deeptech_regulations_fda_faa/lesson_480.typ"
#v(12pt)


#module_cover(
  49,
  "Disiplinlerarası Liderlik: Fizikçiler, Biyologlar & Yazılımcılar",
  "Cross-Disciplinary Engineering Leadership & Frontier Culture",
  "Farklı bilim dallarından gelen dahi araştırmacıları yönetme, ortak bilimsel lügat (Ubiquitous Scientific Language) oluşturma ve laboratuvar güvenliği.",
  "Bridging disparate epistemologies (theoretical physics vs software agile), creating unified cross-domain nomenclature, and establishing high-velocity R&D rigor."
)

#include "/content/mod49_cross_disciplinary_teams/lesson_481.typ"
#v(12pt)

#include "/content/mod49_cross_disciplinary_teams/lesson_482.typ"
#v(12pt)

#include "/content/mod49_cross_disciplinary_teams/lesson_483.typ"
#v(12pt)

#include "/content/mod49_cross_disciplinary_teams/lesson_484.typ"
#v(12pt)

#include "/content/mod49_cross_disciplinary_teams/lesson_485.typ"
#v(12pt)

#include "/content/mod49_cross_disciplinary_teams/lesson_486.typ"
#v(12pt)

#include "/content/mod49_cross_disciplinary_teams/lesson_487.typ"
#v(12pt)

#include "/content/mod49_cross_disciplinary_teams/lesson_488.typ"
#v(12pt)

#include "/content/mod49_cross_disciplinary_teams/lesson_489.typ"
#v(12pt)

#include "/content/mod49_cross_disciplinary_teams/lesson_490.typ"
#v(12pt)


#module_cover(
  50,
  "2050 Deeptech Büyük Yol Haritası: Tip 1 Medeniyet Hedefleri",
  "The 2050 Deeptech Grand Roadmap: Toward a Type-1 Planetary Civilization",
  "Yapay Süper Zekâ (ASI) destekli bilimsel keşifler, hücresel yaşlanmanın tersine çevrilmesi, gezegenler arası yaşam ve insanlığın teknolojik geleceği.",
  "Autonomous AI-driven scientific discovery loops, longevity biotechnology escape velocity, Kardashev Type-1 planetary energy mastery, and interstellar horizon."
)

#include "/content/mod50_deeptech_grand_roadmap/lesson_491.typ"
#v(12pt)

#include "/content/mod50_deeptech_grand_roadmap/lesson_492.typ"
#v(12pt)

#include "/content/mod50_deeptech_grand_roadmap/lesson_493.typ"
#v(12pt)

#include "/content/mod50_deeptech_grand_roadmap/lesson_494.typ"
#v(12pt)

#include "/content/mod50_deeptech_grand_roadmap/lesson_495.typ"
#v(12pt)

#include "/content/mod50_deeptech_grand_roadmap/lesson_496.typ"
#v(12pt)

#include "/content/mod50_deeptech_grand_roadmap/lesson_497.typ"
#v(12pt)

#include "/content/mod50_deeptech_grand_roadmap/lesson_498.typ"
#v(12pt)

#include "/content/mod50_deeptech_grand_roadmap/lesson_499.typ"
#v(12pt)

#include "/content/mod50_deeptech_grand_roadmap/lesson_500.typ"
#v(12pt)


#pagebreak()
#v(40pt)
#align(center)[
  #rect(fill: rgb("020617"), radius: 10pt, inset: (x: 24pt, y: 32pt), width: 92%)[
    #text(size: 26pt, fill: rgb("38bdf8"), weight: "bold")[🌌 TEBRİKLER! / CONGRATULATIONS!]    #v(12pt)
    #text(size: 14pt, fill: white)[500 Derslik Derin Teknoloji Mühendisliği Zirvesini Tamamladınız!]    #v(6pt)
    #text(size: 11pt, fill: rgb("94a3b8"))[You have mastered the entire 500-Lesson Frontier Deeptech Engineering Curriculum!]    #v(20pt)
    #line(length: 60%, stroke: 1.5pt + rgb("06b6d4"))
    #v(15pt)
    #text(size: 9.5pt, fill: rgb("cbd5e1"))[
      Quantum • Semiconductors • CRISPR • Fusion • Robotics • BCI • Space • Advanced Materials • Clean Energy
    ]
  ]
]
