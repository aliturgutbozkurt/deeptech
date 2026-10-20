#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_curriculum.py
Synthesizes the complete 50-Module, 500-Lesson bilingual curriculum for Deeptech Engineering.
Domains: Quantum Computing, Semiconductors, Synthetic Biology, Nuclear Fusion, Robotics, Space, etc.
"""

import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODULES_DATA_DIR = BASE_DIR / "modules_data"
MODULES_DATA_DIR.mkdir(parents=True, exist_ok=True)

MODULE_SPECS = [
    (1, "deeptech_mindset", "Derin Teknoloji Zihniyeti & Fizik Temelli İlkeler", "Deeptech Mindset & First-Principles Physics Engineering",
     "Yazılım SaaS vs Derin Teknoloji ayrımı, fiziksel ilkelerden düşünme (first principles), uzun Ar-Ge döngüleri, TRL 1-9 ve bilimsel atılımları ölçekleme.",
     "Software SaaS vs Deeptech R&D paradigms, physics-first principles, CapEx vs OpEx dynamics, TRL 1-9 progression, and scientific scale-up.",
     "Physics", "FirstPrinciples", "python"),

    (2, "quantum_computing_core", "Kuantum Hesaplama Temelleri: Kübitler, Süperpozisyon & Dolaşıklık", "Quantum Computing Core: Qubits, Superposition & Entanglement",
     "Kuantum mekaniği prensipleri, Bloch küresi, süperpozisyon durumları, Bell durumları ve kuantum dolaşıklığının hesaplamalı gücü.",
     "Quantum mechanical foundations, Bloch sphere state vectors, superposition linear algebra, Bell states, and computational entanglement.",
     "Quantum", "Qubits", "qiskit"),

    (3, "quantum_algorithms_crypto", "Kuantum Algoritmaları & Post-Kuantum Kriptografi (PQC)", "Quantum Algorithms & Post-Quantum Cryptography (PQC)",
     "Shor algoritması ve RSA'nın kırılması, Grover arama hızlandırması, Kafes tabanlı (Lattice) kriptografi ve NIST PQC standartları (Kyber, Dilithium).",
     "Shor's factoring polynomial speedup, Grover's quadratic database search, lattice cryptography, and NIST-approved post-quantum algorithms.",
     "PQC", "Algorithms", "python"),

    (4, "quantum_software_qiskit", "Kuantum Yazılımı & Qiskit ile Devre Simülasyonu", "Quantum Software & Circuit Simulation with Qiskit",
     "Qiskit ve Cirq SDK'ları, kuantum kapıları (Hadamard, CNOT, Phase), hata azaltma (Error Mitigation) ve gürültülü (NISQ) kuantum işlemciler.",
     "Qiskit/Cirq quantum SDKs, unitary gate operations, quantum state tomography, error mitigation techniques, and NISQ regime optimization.",
     "Qiskit", "Circuits", "qiskit"),

    (5, "semiconductor_physics", "Yarı İletken Fiziği, Transistörler & FinFET/GAAFET Mimarisi", "Semiconductor Physics, Transistors & FinFET/GAAFET Architecture",
     "Silikon kristal kafesleri, P-N eklemleri, Moore Kanunu'nun fiziksel sınırları, FinFET ve Gate-All-Around (GAAFET) transistör geometrisi.",
     "Silicon crystal lattice bandgaps, P-N junction drift currents, quantum tunneling limits of Moore's Law, FinFET, and 2nm GAAFET nanosheets.",
     "Semiconductors", "GAAFET", "cpp"),

    (6, "chip_architecture_riscv", "Çip Mimarisi, VLSI & RISC-V Açık Standart Tasarım", "Chip Architecture, VLSI & Open-Standard RISC-V Design",
     "Komut kümesi mimarileri (ISA), RISC-V açık kaynak devrimi, RTL donanım tanımlama (Verilog/Chisel), mantıksal sentez ve Tape-Out süreci.",
     "Instruction set architecture design, RISC-V modular extensions, RTL synthesis in Verilog, clock-tree routing, and ASIC tape-out pipelines.",
     "RISCV", "VLSI", "rust"),

    (7, "photonic_computing", "Fotonik Hesaplama & Işık Hızında Optik İşlemciler", "Photonic Computing & Light-Speed Optical Processors",
     "Silikon fotonik, dalga kılavuzları, Mach-Zehnder interferometreleri ve ışık dalgalarıyla sıfır dirençli matris çarpımı (Optical GEMM).",
     "Silicon photonics waveguides, Mach-Zehnder interferometers, electro-optic modulators, and light-speed analog tensor multiplication.",
     "Photonics", "Optical", "python"),

    (8, "neuromorphic_computing", "Nöromorfik Çipler & Beyin Benzetimli Sinir Ağları (SNN)", "Neuromorphic Computing & Brain-Inspired Spiking Neural Networks",
     "Biyolojik nöron modelleri (Leaky Integrate-and-Fire), olay güdümlü asenkron çipler (Intel Loihi), memristörler ve sinaptik plastisite (STDP).",
     "Biophysical neuron simulations, spike-timing-dependent plasticity (STDP), memristive crossbars, and ultra-low-power event-driven chips.",
     "Neuromorphic", "SNN", "python"),

    (9, "gpu_hardware_architecture", "Modern GPU Mimarisi: Tensor Cores, NVLink & HBM3e", "Modern GPU Hardware Architecture: Tensor Cores & NVLink Interconnects",
     "NVIDIA Hopper/Blackwell mimarisi, Akış Çoklu İşlemcileri (SM), Tensor Cores, yüksek bant genişlikli bellek (HBM3e) ve NVLink anahtarları.",
     "Streaming multiprocessor warp dispatch, Tensor Core mixed-precision arithmetic, HBM3e 3D-stacked silicon, and terabit NVLink topologies.",
     "GPU", "Architecture", "cuda"),

    (10, "cuda_triton_programming", "Paralel Donanım Programlama: CUDA C++ & OpenAI Triton", "High-Performance GPU Programming: CUDA C++ & OpenAI Triton",
     "CUDA thread/block hiyerarşisi, Paylaşımlı Bellek (Shared Memory Tiling), Warp Shuffle operasyonları ve OpenAI Triton ile kernel derleme.",
     "CUDA memory coalescing, shared memory bank conflict resolution, warp-level primitives, and tile-based compiler tuning in OpenAI Triton.",
     "CUDA", "Triton", "cuda"),

    (11, "edge_ai_tinyml", "Uç Birim Yapay Zekâsı (Edge AI), Kuantizasyon & TinyML", "Edge AI, Hardware Quantization (INT4/FP8) & TinyML",
     "Düşük güçlü mikrodenetleyicilerde (ARM Cortex-M) yapay zekâ, model budama (Pruning), INT8/INT4 kuantizasyonu ve ONNX Runtime.",
     "Constrained embedded inference, post-training quantization, structured pruning, memory-mapped neural execution, and micro-kernel runtime.",
     "TinyML", "Quantization", "cpp"),

    (12, "synthetic_biology_crispr", "Sentetik Biyoloji & CRISPR Gen Düzenleme Teknolojileri", "Synthetic Biology & CRISPR-Cas Precision Gene Editing",
     "DNA/RNA sentezi, CRISPR-Cas9/Cas12 makas mekanizması, sgRNA tasarımı, Base Editing ve Prime Editing ile hassas genetik cerrahi.",
     "Molecular biology primitives, CRISPR guide RNA target specificity, off-target cleavage mitigation, prime editing, and synthetic gene circuits.",
     "CRISPR", "SynBio", "python"),

    (13, "bioinformatics_genomics", "Biyoinformatik & Hesaplamalı Genomik (BioPython)", "Bioinformatics & Computational Genomics with BioPython",
     "Yeni Nesil Dizileme (NGS), FASTA/FASTQ işleme, genom hizalama algoritmaları (Smith-Waterman, Burrows-Wheeler) ve varyant analizi.",
     "High-throughput sequencing data structures, Burrows-Wheeler transform indexing, sequence alignment algorithms, and genomic variant calling.",
     "Bioinformatics", "Genomics", "python"),

    (14, "ai_protein_design", "Yapay Zekâ ile Protein Tasarımı: AlphaFold 3 & RFdiffusion", "AI for Structural Biology: AlphaFold 3 & De Novo Protein Design",
     "Protein katlanma problemi, çoklu dizi hizalaması (MSA), Evoformer mimarisi, difüzyon modelleriyle sıfırdan enzim ve ilaç tasarımı.",
     "Structural biology geometric deep learning, invariant point attention, diffusion models for protein backbone generation, and ligand docking.",
     "AlphaFold", "ProteinDesign", "python"),

    (15, "biofabrication_cellular", "Biyo-Üretim, Hücresel Tarım & 3D Biyo-Baskı", "Biofabrication, Cellular Agriculture & 3D Bioprinting",
     "Hassas mikrobiyal fermantasyon, biyoreaktör kinetiği, hücresel temiz et üretimi ve canlı hücrelerle 3D yapay doku basımı.",
     "Bioreactor mass transfer kinetics, microbial strain engineering, hydrogel bio-inks, cell scaffolding, and 3D organoid extrusion.",
     "Biofabrication", "CellularAg", "python"),

    (16, "advanced_materials_nano", "İleri Malzeme Bilimi: Grafen, Karbon Nanotüpler & MXenes", "Advanced Materials Science: Graphene, Carbon Nanotubes & MXenes",
     "2D atomik malzemeler, sp2 karbon bağları, süper iletken nanotüpler, elektrokimyasal MXene tabakaları ve kompozit mukavemet analizleri.",
     "2D crystal crystallography, sp2 hybridization transport properties, single-walled carbon nanotubes, MXene ion intercalation, and nanocomposites.",
     "Materials", "Nanotech", "python"),

    (17, "superconductors_cryogenics", "Süperiletkenlik (HTS), Meissner Etkisi & Kriyogenik", "Superconductivity (HTS), Meissner Effect & Cryogenic Engineering",
     "Sıfır elektriksel direnç, Tip I/II süperiletkenler, YBCO yüksek sıcaklık süperiletkenleri ve seyreltme buzdolapları (Dilution Refrigerators).",
     "Cooper pairing BCS theory, flux pinning dynamics, high-temperature ceramic superconductors (YBCO), and milliKelvin cryogenic dilution stages.",
     "Superconductors", "Cryogenics", "python"),

    (18, "solid_state_batteries", "Yeni Nesil Enerji Depolama: Katı Hal Bataryaları & Lityum-Metal", "Next-Gen Energy Storage: Solid-State & Lithium-Metal Batteries",
     "Sıvı elektrolit riskleri, seramik/polimer katı elektrolitler, lityum dendrit oluşumunu engelleme ve gravimetrik enerji yoğunluğu (>500 Wh/kg).",
     "Solid electrolyte interphase (SEI) mechanics, ionic conductivity of garnets/sulfides, lithium dendrite suppression, and battery cycling physics.",
     "Batteries", "EnergyStorage", "python"),

    (19, "nuclear_fusion", "Nükleer Füzyon Enerjisi: Tokamaklar, Manyetik Hapsolma & Plazma", "Nuclear Fusion Energy: Tokamaks, Magnetic Confinement & Plasma Physics",
     "Deuterium-Tritium reaksiyonu, Lawson kriteri (Q > 1), Tokamak manyetik kafesleri, plazma instabiliteleri ve yüksek manyetik alanlı HTS bobinleri.",
     "Deuterium-tritium fusion cross-sections, Lawson triple product, magnetohydrodynamic plasma equilibrium, and high-field HTS tokamak magnets.",
     "Fusion", "Plasma", "python"),

    (20, "hydrogen_carbon_capture", "Yeşil Hidrojen & Doğrudan Havadan Karbon Yakalama (DAC)", "Green Hydrogen Economy & Direct Air Carbon Capture (DAC)",
     "PEM ve Katı Oksit elektrolizörler, metal-organik kafesler (MOF) ile doğrudan havadan CO2 emilimi ve kimyasal karbon depolama.",
     "Proton exchange membrane electrolysis overpotentials, metal-organic framework (MOF) gas sorption thermodynamics, and geologic sequestration.",
     "ClimateTech", "HydrogenDAC", "python"),

    (21, "space_propulsion_rockets", "Uzay Teknolojileri: Roket İtki Sistemleri & Yörünge Mekaniği", "Space Propulsion & Orbital Mechanics: Tsiolkovsky to Aerospikes",
     "Tsiolkovsky roket denklemi, Özgül İtki (Isp), kademeli yanma döngüleri, İyon iticileri (Hall-effect) ve Hohmann yörünge transferi.",
     "Rocket momentum equations, specific impulse thermodynamics, staged combustion cycle engines, electrostatic Hall thrusters, and orbital maneuvers.",
     "Aerospace", "Propulsion", "python"),

    (22, "satellites_space_comms", "Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi", "LEO Satellite Constellations & Optical Inter-Satellite Links",
     "Alçak Dünya Yörüngesi (LEO) mega-takımyıldızları, Faz dizili antenler (Beamforming), optik lazer haberleşme ve yörünge çöpü önleme.",
     "LEO orbital perturbations, phased-array electronically steered beamforming, free-space optical laser communications, and collision avoidance.",
     "Satellites", "LaserComms", "rust"),

    (23, "autonomous_robotics_kinematics", "Otonom Robotik: İleri/Ters Kinematik & İnsansı Robot Dinamiği", "Autonomous Robotics: Forward/Inverse Kinematics & Humanoid Dynamics",
     "Denavit-Hartenberg (DH) parametreleri, Jakobiyen matrisleri, Singularities, Model Predictive Control (MPC) ve insansı robot denge modelleri.",
     "Rigid body transformations, geometric and numerical inverse kinematics, manipulator Jacobians, and zero-moment point (ZMP) locomotion.",
     "Robotics", "Kinematics", "cpp"),

    (24, "ros2_robot_operating_system", "Robot İşletim Sistemi (ROS 2) & DDS Dağıtık Middleware", "Robot Operating System (ROS 2) & Real-Time Distributed Middleware",
     "ROS 2 mimarisi, Data Distribution Service (DDS), Gerçek zamanlı düğümler (Real-time nodes), Topic/Service/Action protokolleri ve URDF.",
     "ROS 2 micro-ROS architecture, DDS QoS policies, lock-free real-time executor loops, action servers, and robot URDF kinematics trees.",
     "ROS2", "Middleware", "cpp"),

    (25, "spatial_computing_slam", "Mekânsal Hesaplama, SLAM, Görsel Odometri & LiDAR", "Spatial Computing & SLAM: Visual-Inertial Odometry & 3D LiDAR",
     "Eşzamanlı Konumlandırma ve Haritalama (SLAM), Genişletilmiş Kalman Filtresi (EKF), bundle adjustment ve 3D LiDAR nokta bulutu eşleştirme.",
     "Simultaneous localization and mapping state estimation, visual-inertial odometry feature tracking, graph-based SLAM, and iterative closest point (ICP).",
     "SLAM", "LiDAR", "cpp"),

    (26, "brain_computer_interfaces", "Beyin-Bilgisayar Arayüzleri (BCI) & Nöroteknoloji (Neuralink)", "Brain-Computer Interfaces (BCI) & Neural Spike Decoding",
     "İnvaziv ve non-invaziv elektrotlar, aksiyon potansiyelleri (Spikes), Spike Sorting algoritmaları, motor korteks sinyallerini imlece dönüştürme.",
     "Electrophysiological neural recording, microelectrode array impedance, wavelet-based spike sorting, and motor intent decoders.",
     "BCI", "Neurotech", "python"),

    (27, "autonomous_vehicles_perception", "Otonom Araçlar: Sensör Füzyonu, Kalman Filtresi & Occupancy", "Autonomous Driving: Multi-Sensor Fusion & 3D Occupancy Grids",
     "Kamera-Radar-LiDAR sensör füzyonu, Unscented Kalman Filter (UKF), kuşbakışı görünüm (BEV) dönüşümü ve 3D doluluk ağları (Occupancy Networks).",
     "Multi-modal sensor fusion pipelines, probabilistic Bayesian filtering, temporal bird's-eye-view feature projection, and voxel occupancy prediction.",
     "AutonomousVehicles", "SensorFusion", "python"),

    (28, "drones_evtol_uam", "Dronlar, eVTOL & Kentsel Hava Hareketliliği (UAM)", "Drones, eVTOL Aerodynamics & Autonomous Flight Navigation",
     "Çok rotorlu uçuş dinamiği, aerodinamik itki modelleri, RRT* otonom yol planlama algoritmaları, coğrafi çit (Geofencing) ve BVLOS uçuş.",
     "Multirotor aerodynamic thrust equations, state-space PID flight controllers, dynamic obstacle avoidance via RRT*, and urban airspace routing.",
     "eVTOL", "Drones", "cpp"),

    (29, "microfluidics_lab_on_chip", "Mikroakışkanlar & Çip Üstü Laboratuvar (Lab-on-a-Chip)", "Microfluidics & Lab-on-a-Chip Micro-Electro-Mechanical Systems",
     "Laminer akış ve düşük Reynolds sayıları, damlacık mikroakışkanları (Droplet microfluidics), PDMS çip üretimi ve tek hücre analizi.",
     "Laminar flow microfluidics, capillary diffusion kinetics, microfluidic droplet compartmentalization, and point-of-care bio-MEMS.",
     "Microfluidics", "BioMEMS", "python"),

    (30, "bioelectronics_neural_implants", "Biyo-Elektronik, Optogenetik & Esnek Nöral İmplantlar", "Bioelectronics, Optogenetics & Biocompatible Neural Implants",
     "Biyouyumlu esnek polimerler (Parylene, Polyimide), optogenetik ışık stimülasyonu, kanalrodopsin proteinleri ve doku tepkisi optimizasyonu.",
     "Biocompatible flexible micro-substrates, channelrhodopsin light-gated ion channels, foreign-body response mitigation, and closed-loop neuromodulation.",
     "Bioelectronics", "Optogenetics", "python"),

    (31, "optics_holographic_displays", "İleri Optik, Holografik Ekranlar & Dalga Kılavuzu (AR/VR)", "Advanced Optics, Holographic Displays & Waveguides for AR/VR",
     "Mekânsal Işık Modülatörleri (SLM), Kırınımsal optik elemanlar (DOE), holografik dalga kılavuzu birleştiricileri ve retina projeksiyonu.",
     "Spatial light modulation phase interference, diffractive optical waveguide pupil expansion, computer-generated holography, and micro-displays.",
     "Optics", "Holography", "python"),

    (32, "supercomputing_exascale", "Süper Bilgisayarlar: Exascale Altyapı, InfiniBand & MPI", "Supercomputing & Exascale Architecture: InfiniBand, RDMA & MPI",
     "Eksasabit (10^18 FLOP) hesaplama, InfiniBand NDR anahtarlama matrisleri, Uzaktan Doğrudan Bellek Erişimi (RDMA) ve MPI paralelleştirme.",
     "Exascale interconnect topologies, RoCEv2/InfiniBand kernel-bypass networking, distributed MPI collective operations, and Slurm workload orchestration.",
     "HPC", "Exascale", "cpp"),

    (33, "distributed_ai_superclusters", "Dağıtık Yapay Zekâ Eğitimi: 3D Paralellik & Megatron-LM", "Distributed AI Superclusters: 3D Parallelism & Megatron-LM",
     "Trilyon parametreli modeller, Tensör Paralelliği, Boru Hattı Paralelliği, DeepSpeed ZeRO bellek optimizasyonu ve GPU küme tasarımı.",
     "Tensor and pipeline model partitioning, zero-redundancy optimizer memory sharding, all-reduce communication overlaps, and cluster fault resilience.",
     "DistributedAI", "DeepSpeed", "python"),

    (34, "analog_in_memory_computing", "Bellek İçi Hesaplama (IMC) & Analog Yapay Zekâ Çipleri", "Analog In-Memory Computing & Neuromorphic Resistive RAM (RRAM)",
     "Ohm ve Kirchhoff kanunlarıyla analog matris çarpımı, RRAM ve Faz Değişimli Bellek (PCM) hücreleri, analog-dijital çevirici (ADC) darboğazları.",
     "Ohm's Law analog multiply-accumulate crossbar arrays, memristive state drift compensation, ADC/DAC energy trade-offs, and analog inference.",
     "AnalogAI", "Memristors", "python"),

    (35, "agtech_precision_farming", "Tarım Teknolojileri (AgTech): Hassas Tarım & Otonom Sistemler", "AgTech: Precision Agriculture, Hyperspectral Imaging & Aeroponics",
     "Hipospektral drone görüntüleme, bitki NDVI indeksleri, otonom yabani ot temizleme lazerleri ve dikey aeroponik sera otomasyonu.",
     "Hyperspectral crop reflectance index calculation, autonomous laser weeding computer vision, root-zone nutrient dosing, and vertical farming telemetry.",
     "AgTech", "Aeroponics", "python"),

    (36, "water_tech_desalination", "Su Teknolojileri: Grafen Oksit Membranlar & İleri Arıtma", "Advanced Water Technologies: Graphene Membranes & Desalination",
     "Ters Ozmoz (RO) termodinamik verimliliği, nanoporöz grafen su filtreleme, ileri ozmoz ve termal güneş enerjili tuzdan arındırma sistemleri.",
     "Thermodynamic limits of seawater reverse osmosis, sub-nanometer graphene oxide selective transport, forward osmosis, and fouling-resistant coatings.",
     "WaterTech", "Desalination", "python"),

    (37, "advanced_manufacturing_3d", "İleri İmalat: Metal 3D Baskı (DMLS) & Katmanlı Üretim", "Advanced Additive Manufacturing: Direct Metal Laser Sintering (DMLS)",
     "Lazer Toz Yatağı Füzyonu (LPBF), titanyum ve Inconel alaşımları, termal gerinim simülasyonları ve topoloji optimizasyonu ile hafif parça tasarımı.",
     "Laser powder bed fusion metallurgy, melt-pool thermo-capillary convection, finite-element residual stress modeling, and generative topology optimization.",
     "AdditiveMfg", "DMLS", "python"),

    (38, "zero_knowledge_hardware", "Sıfır Bilgi İspatları (ZKP) & Kriptografik Donanım Hızlandırma", "Zero-Knowledge Hardware Acceleration: ASICs/FPGAs for ZK-SNARKs",
     "ZK-SNARK ve STARK matematik temelleri, Sayı Teorik Dönüşümleri (NTT), Çok Noktalı Skalar Çarpımı (MSM) ve FPGA/ASIC hızlandırıcılar.",
     "Elliptic curve pairing cryptography, multi-scalar multiplication (MSM) hardware pipelines, number theoretic transform (NTT) accelerators, and ZK rollups.",
     "ZKP", "Cryptography", "rust"),

    (39, "autonomous_chemistry_labs", "Otonom Kimya & Kendi Kendini Yöneten Robotik Laboratuvarlar", "Autonomous Chemistry & Self-Driving Discovery Laboratories",
     "Sıvı taşıma robotları, Bayesyen optimizasyon ile reaksiyon koşulu keşfi, kapalı döngü sentez ve kimyasal uzay tarama algoritmaları.",
     "Automated liquid-handling robotics, active learning Bayesian optimization for chemical yields, closed-loop spectroscopy feedback, and molecular search.",
     "SelfDrivingLabs", "Chemistry", "python"),

    (40, "climatetech_ai_weather", "İklim Teknolojileri & Yapay Zekâ ile Hava Tahmini (GraphCast)", "Climate Tech & Global AI Weather Prediction: GraphCast & Models",
     "Sayısal hava tahmin modelleri vs Graflı Sinir Ağları (GNN), GraphCast mimarisi, okyanus akıntı modellemesi ve küresel iklim simülasyonları.",
     "Numerical weather differential equations, spherical mesh graph neural networks (GraphCast), climate ensemble forecasting, and oceanic energy balances.",
     "ClimateAI", "GraphCast", "python"),

    (41, "deepsea_extreme_environments", "Derin Deniz Robotikleri (AUV) & Aşırı Ortam Teknolojileri", "Deep Sea Exploration: Autonomous Underwater Vehicles & High Pressure",
     "1000 bar hidrostatik basınç mühendisliği, akustik su altı telemetrisi, batimetrik sonar haritalama ve hidrotermal menfez keşif robotları.",
     "Hyperbaric titanium pressure vessel design, acoustic OFDM underwater communications, synthetic aperture sonar bathymetry, and benthic autonomy.",
     "DeepSea", "AUV", "cpp"),

    (42, "biomedical_imaging_microscopy", "Biyomedikal Görüntüleme: Cryo-EM & Süper Çözünürlüklü Mikroskopi", "Biomedical Imaging: Cryo-EM Reconstruction & Super-Resolution",
     "Elektron kriyomikroskopisi (Cryo-EM), tek partikül 3D rekonstrüksiyonu, STED mikroskopisi ve optik koherens tomografi (OCT).",
     "Single-particle cryo-electron microscopy Fourier projection slice theorem, diffraction-limit overcoming STED depletion, and interferometric OCT imaging.",
     "Imaging", "CryoEM", "python"),

    (43, "extreme_sensors_actuators", "Aşırı Rejim Sensörleri: Terahertz, Piezoelektrik & MEMS", "Extreme Regime Sensors: Terahertz, Piezoelectrics & Resonant MEMS",
     "Terahertz elektromanyetik dalga spektroskopisi, yüksek sıcaklık piezoelektrik dönüştürücüler, atomik kuvvet mikroskobu (AFM) konsolları.",
     "Terahertz time-domain spectroscopy, high-temperature piezoelectric perovskite ceramics, resonant micro-cantilevers, and sub-angstrom deflection.",
     "Sensors", "MEMS", "python"),

    (44, "cyber_physical_digital_twins", "Siber-Fiziksel Sistemler & Endüstriyel Dijital İkizler", "Cyber-Physical Systems & Industrial Digital Twins",
     "Fizik motorları ile gerçek zamanlı telemetri eşleştirme, kalman filtreleme ile durum kestirimi, endüstriyel OPC UA ve MQTT protokolleri.",
     "Real-time physical co-simulation, state-space digital twin reconciliation, industrial IoT pub/sub bridges, and predictive mechanical failure prognosis.",
     "DigitalTwins", "CyberPhysical", "python"),

    (45, "deeptech_ip_patents", "Deeptech Fikri Mülkiyet (IP) Stratejisi: Patentler & Ticari Sırlar", "Deeptech Intellectual Property: Patents, Trade Secrets & Freedom to Operate",
     "Patentlenebilirlik kriterleri, PCT uluslararası başvuru stratejisi, Ticari Sır (Trade Secret) vs Patent ikilemi ve Özgürce Çalışabilirlik (FTO).",
     "Evaluating novel scientific inventions, drafting enforceable claims, strategic defensive publishing, and conducting rigorous Freedom to Operate (FTO) audits.",
     "IPStrategy", "Patents", "python"),

    (46, "hardtech_venture_capital", "Hard Tech Girişim Sermayesi (VC) & Teknoloji Hazırlık Seviyeleri (TRL)", "Hard Tech Venture Capital, Milestones & TRL 1-9 De-risking",
     "Deeptech yatırım tezleri, laboratuvar aşamasından ticari ürüne (TRL 1-9) geçiş, ölüm vadisi (Valley of Death) finansmanı ve dilüsyonsuz hibeler.",
     "Scientific de-risking milestones, milestone-based tranche financing, bridging the commercialization valley of death, and public non-dilutive grants.",
     "VentureCapital", "TRL", "python"),

    (47, "techno_economic_analysis", "Tekno-Ekonomik Analiz (TEA) & Birinci Tesis (FOAK) Ölçekleme", "Techno-Economic Analysis (TEA) & First-of-a-Kind (FOAK) Scale-Up",
     "Seviyelendirilmiş Enerji/Ürün Maliyeti (LCOE/LCOP), ölçek ekonomisi hesaplamaları, pilot tesisten Gigafactory'ye geçiş ve FOAK risk yönetimi.",
     "Levelized cost of production models, chemical process Aspen simulations, capital expenditure amortization curves, and FOAK commercial scale-up.",
     "TEA", "ScaleUp", "python"),

    (48, "deeptech_regulations_fda_faa", "Düzenleyici Kurum Stratejileri: FDA, FAA & Nükleer Onay Süreçleri", "Deeptech Regulatory Pathways: FDA Approvals, FAA Certifications & Safety",
     "Biyoteknoloji FDA Faz I/II/III klinik denemeleri, havacılıkta FAA uçuşa elverişlilik sertifikasyonu, nükleer NRC lisanslama adımları.",
     "FDA 510(k) and PMA medical device approval pathways, FAA part 21 airworthiness type certification for eVTOL, and nuclear licensing protocols.",
     "Regulation", "Compliance", "python"),

    (49, "cross_disciplinary_teams", "Disiplinlerarası Liderlik: Fizikçiler, Biyologlar & Yazılımcılar", "Cross-Disciplinary Engineering Leadership & Frontier Culture",
     "Farklı bilim dallarından gelen dahi araştırmacıları yönetme, ortak bilimsel lügat (Ubiquitous Scientific Language) oluşturma ve laboratuvar güvenliği.",
     "Bridging disparate epistemologies (theoretical physics vs software agile), creating unified cross-domain nomenclature, and establishing high-velocity R&D rigor.",
     "Leadership", "Culture", "python"),

    (50, "deeptech_grand_roadmap", "2050 Deeptech Büyük Yol Haritası: Tip 1 Medeniyet Hedefleri", "The 2050 Deeptech Grand Roadmap: Toward a Type-1 Planetary Civilization",
     "Yapay Süper Zekâ (ASI) destekli bilimsel keşifler, hücresel yaşlanmanın tersine çevrilmesi, gezegenler arası yaşam ve insanlığın teknolojik geleceği.",
     "Autonomous AI-driven scientific discovery loops, longevity biotechnology escape velocity, Kardashev Type-1 planetary energy mastery, and interstellar horizon.",
     "FutureVision", "Type1Civilization", "python")
]

def generate_lesson_code(lang, tag1, tag2, mod_id, lesson_idx):
    if lang == "qiskit":
        return f"""# Qiskit: {tag1} Kuantum Devre Simülasyonu
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 1. 2 Kübitlik Devre Tanımla
qc = QuantumCircuit(2, 2)
qc.h(0)         # Hadamard: Süperpozisyon oluştur
qc.cx(0, 1)     # CNOT: Kuantum Dolaşıklığı (Entanglement) sağla
qc.measure([0, 1], [0, 1])

# 2. Aer Simülatöründe Çalıştır
simulator = AerSimulator()
job = simulator.run(qc, shots=1024)
result = job.result().get_counts()

print("⚛️ Kuantum Ölçüm Sonuçları (Bell Durumu):", result)
# Beklenen: ~50% '00' ve ~50% '11' (Kusursuz kuantum korelasyonu)"""

    elif lang == "cuda":
        return f"""// CUDA C++: {tag1} Yüksek Hızlı Donanım Kerneli
#include <cuda_runtime.h>
#include <iostream>

__global__ void {tag1}Kernel(float* d_out, const float* d_in, int n) {{
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < n) {{
        // Tensor Core / Warp Hızlı Paralel Matematik
        d_out[idx] = d_in[idx] * 2.0f + 1.0f;
    }}
}}

int main() {{
    int n = 1 << 20; // 1 Milyon Eleman
    size_t bytes = n * sizeof(float);
    float *d_in, *d_out;
    cudaMalloc(&d_in, bytes);
    cudaMalloc(&d_out, bytes);

    int blockSize = 256;
    int numBlocks = (n + blockSize - 1) / blockSize;
    {tag1}Kernel<<<numBlocks, blockSize>>>(d_out, d_in, n);
    cudaDeviceSynchronize();

    std::cout << "⚡ CUDA Kerneli 1M eleman üzerinde başarıyla çalıştırıldı." << std::endl;
    cudaFree(d_in); cudaFree(d_out);
    return 0;
}}"""

    elif lang == "rust":
        return f"""// Rust: {tag1} & {tag2} Yüksek Güvenilirlikli Sistem Kodu
pub struct {tag1}Controller {{
    pub telemetry_active: bool,
    pub sample_rate_hz: u32,
}}

impl {tag1}Controller {{
    pub fn new(rate: u32) -> Self {{
        Self {{ telemetry_active: true, sample_rate_hz: rate }}
    }}

    pub fn process_telemetry(&self, raw_input: &[u8]) -> Result<String, &'static str> {{
        if raw_input.is_empty() {{
            return Err("Girdi sinyali boş!");
        }}
        // Bellek güvenli, sıfır maliyetli soyutlama (Zero-Cost Abstraction)
        Ok(format!("Sinyal işlendi: {{}} bayt @ {{}} Hz", raw_input.len(), self.sample_rate_hz))
    }}
}}

fn main() {{
    let controller = {tag1}Controller::new(10_000);
    let sample_data = [0xAA, 0xBB, 0xCC, 0xDD];
    match controller.process_telemetry(&sample_data) {{
        Ok(msg) => println!("🚀 Rust Deeptech Engine: {{}}", msg),
        Err(e) => eprintln!("❌ Hata: {{}}", e),
    }}
}}"""

    elif lang == "cpp":
        return f"""// C++20: {tag1} & {tag2} Düşük Gecikmeli Fizik Motoru
#include <iostream>
#include <vector>
#include <span>
#include <chrono>

class {tag1}Engine {{
public:
    void computeKinematics(std::span<const double> inputs, std::vector<double>& outputs) {{
        outputs.clear();
        outputs.reserve(inputs.size());
        for (double val : inputs) {{
            // Yüksek performanslı vektörize (SIMD) işlem
            outputs.push_back(val * 1.41421356);
        }}
    }}
}};

int main() {{
    {tag1}Engine engine;
    std::vector<double> sensorReadings = {{1.0, 2.5, 3.8, 4.2}};
    std::vector<double> transformed;
    engine.computeKinematics(sensorReadings, transformed);
    std::cout << "🔬 C++20 {tag1} Motoru Hesaplaması Tamamlandı. Çıktı Boyutu: " << transformed.size() << std::endl;
    return 0;
}}"""

    else: # Python Default for Bio, Materials, TEA, etc.
        return f"""# Python 3: {tag1} & {tag2} Bilimsel Hesaplama ve Simülasyon
import numpy as np

def simulate_{tag1.lower()}_dynamics(steps: int = 1000, dt: float = 1e-3):
    # Fiziksel diferansiyel denklem integrasyonu (Runge-Kutta / Euler)
    time = np.linspace(0, steps * dt, steps)
    state = np.zeros((steps, 3)) # [Konum, Hız, Enerji]
    state[0] = [1.0, 0.0, 0.5]

    for i in range(1, steps):
        # Durum geçişi ve fiziksel korunum denklemi
        state[i, 0] = state[i-1, 0] + state[i-1, 1] * dt
        state[i, 1] = state[i-1, 1] - 9.81 * np.sin(state[i-1, 0]) * dt
        state[i, 2] = 0.5 * state[i, 1]**2 + 9.81 * (1.0 - np.cos(state[i, 0]))

    return time, state

if __name__ == "__main__":
    t, s = simulate_{tag1.lower()}_dynamics()
    print(f"🔬 {tag1} Simülasyonu Tamamlandı! Son Enerji: {{s[-1, 2]:.4f}} Joule.")"""

def generate_lesson_data(mod_id, lesson_idx, mod_title_tr, mod_title_en, tag1, tag2, lang):
    global_num = (mod_id - 1) * 10 + lesson_idx
    
    lesson_topics = [
        ("Temel Fizik İlkeleri, Bilimsel Temel ve Tarihsel Gelişim",
         "Foundational Physics Principles, Scientific Genesis & Evolution"),
        ("Matematiksel Modelleme, Durum Denklemleri ve Simülasyon",
         "Mathematical Formulations, State Equations & Simulation Dynamics"),
        ("Laboratuvardan Pilot Üretime: Cihaz ve Donanım Mimarisi",
         "From Lab Bench to Pilot: Hardware Tooling & Architecture"),
        ("Fiziksel Darboğazlar, Malzeme Sınırları ve Termodinamik Engeller",
         "Physical Bottlenecks, Material Limits & Thermodynamic Walls"),
        ("Uygulamalı Kodlama, Algoritmik Çözücüler ve Veri Hatları",
         "Applied Computation, Algorithmic Solvers & Data Pipelines"),
        ("Hata Düzeltme, Gürültü Azaltma ve Sinyal İzolasyonu",
         "Error Mitigation, Noise Suppression & Signal Isolation"),
        ("Ölçekleme Mühendisliği, Dayanıklılık ve Süreç Optimizasyonu",
         "Scale-Up Engineering, Endurance & Process Optimization"),
        ("Deneysel Doğrulama, Karakterizasyon ve Spektroskopi Metotları",
         "Empirical Validation, Characterization & Metrology Workflows"),
        ("Tekno-Ekonomik Analiz, Birim Maliyetler ve Ticari Fizibilite",
         "Techno-Economic Modeling, Unit Economics & Commercial Viability"),
        ("Gelecek Vizyonu, 2035-2050 Yol Haritası ve Frontier Kariyer Kılavuzu",
         "Frontier Horizon, 2035-2050 Technology Roadmap & Career Mastery")
    ]
    
    sub_title_tr, sub_title_en = lesson_topics[lesson_idx - 1]
    title_tr = f"{mod_title_tr} - {sub_title_tr}"
    title_en = f"{mod_title_en} - {sub_title_en}"

    diagram = f"""┌─────────────────────────────────────────────────────────────────────────────┐
│                 DEEPTECH FİZİKSEL SÜREÇ VE MİMARİ AKIŞ ŞEMASI                │
└─────────────────────────────────────────────────────────────────────────────┘
  [ Bilimsel Gözlem / Laboratuvar ] ──► [ Matematiksel Teori & Simülasyon ]
                                                       │
                                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ {tag1.upper()} MÜHENDİSLİK DÜZLEMİ ({tag2.upper()} ÇÖZÜCÜSÜ)                          │
  │  1. Giriş Parametreleri  ──► Sıcaklık, Basınç, Manyetik Alan / Kuantum  │
  │  2. Fiziksel Reaksiyon   ──► Maddenin Durumu / Dalga Fonksiyonu İcrası │
  │  3. Çıktı ve Sinyal      ──► Spektrometre / Lazer / Transistör Akımı    │
  └────────────────────────────────────┬────────────────────────────────────┘
                                       │
                    ┌──────────────────┴──────────────────┐
                    ▼                                     ▼
        [ Karakterizasyon: Cryo-EM ]            [ Üretim: Fab / Pilot Tesis ]
        (Nanometre Altı Analiz)                 (TRL 6+ Endüstriyel Ölçek)

  🎯 DEEPTECH ALTIN KURALI:
  "Yazılımda bir bug'ı düzeltmek birkaç saniye sürer; derin teknolojide termodinamik
   veya kuantum yasalarını ihlal eden bir hata milyonlarca dolarlık fabrikayı batırır!" """

    eli5_tr = (
        f"Evde yemek yapmayı düşünün: Bir web sitesi kodlamak ekmek arasına peynir koymaya benzer; hata yaparsanız "
        f"peyniri çıkarıp zeytin koyabilirsiniz. Ancak derin teknoloji ({tag1}), unun içindeki molekülleri laboratuvarda "
        f"yeniden dizip 300 derece fırında elmas gibi parlayan yeni bir ekmek türü icat etmeye benzer! "
        f"Burada sadece reçeteyi bilmek yetmez; fırının atom seviyesindeki ısısını ({tag2}), basıncını ve moleküler bağlarını "
        f"mükemmel kontrol etmelisiniz. Bir derecelik hata her şeyi kömür eder!"
    )

    eli5_en = (
        f"Think of culinary arts: Building typical consumer software is like making a grilled cheese sandwich; "
        f"if you drop the slice, you grab another one from the fridge in two seconds. Deeptech ({tag1}), however, "
        f"is like synthesizing entirely new protein macromolecules at the sub-atomic scale to bake a bread that "
        f"glows like diamonds and never stales! You are not just following a recipe; you are manipulating thermodynamics "
        f"({tag2}), atomic pressure, and quantum lattice bonds. A fraction of a degree off, and the entire batch turns to graphite!"
    )

    deep_tr = (
        f"Derin Teknoloji Mühendisliği Seviyesinde {mod_title_tr} Analizi: "
        f"{tag1} disiplini, temel doğa yasalarının sınırlarında çalışmayı gerektirir. "
        f"1) Fiziksel İlkeler (First Principles): Karmaşık sistemleri benzetmelerle değil, termodinamik, elektrodinamik veya "
        f"kuantum mekaniğinin temel aksiyomlarına indirgeyerek çözün. "
        f"2) Donanım-Yazılım Birlikteliği (Co-Design): {tag2} sistemlerinde yazılım donanımdan soyutlanamaz; algoritma çipin fiziksel "
        f"ısınma sınırlarına veya reaktörün plazma stabilitesine göre tasarlanır. "
        f"3) Ölçekleme Faktörü (Scale-Up Frontier): Laboratuvar tezgahındaki 1 miligramlık başarı, tonlarca kimyasal veya milyonlarca "
        f"transistörlük endüstriyel üretim hattına aktarılırken yeni fiziksel dinamikler doğurur. "
        f"4) Kariyer Ödünleşimi: Yalnızca kod yazan bir yazılımcı olmak yerine, atomları ve fotonları yöneten disiplinlerarası bir "
        f"Frontier Mühendisi olmanız gerekir."
    )

    deep_en = (
        f"Frontier Deeptech Engineering Deep-Dive for {mod_title_en}: "
        f"Working within {tag1} demands operating directly at the boundaries of natural physics. "
        f"1) First-Principles Decomposition: Discard conventional analogies; reconstruct technical architectures from thermodynamic, "
        f"quantum electrodynamic, or cellular invariants. "
        f"2) Hardware-Algorithm Co-Design: In {tag2}, compute kernels cannot be decoupled from physical physics; algorithms must be shaped "
        f"by thermal dissipation ceilings, shot noise limits, or magnetic confinement geometries. "
        f"3) Non-Linear Scale-Up Dynamics: What functions deterministically across a 10-micron lab-scale substrate routinely breaks under "
        f"viscous shearing or parasitic capacitance when expanded to megawatt industrial capacity. "
        f"4) Frontier Career Trajectory: Deeptech rewards cross-disciplinary bilingualism—engineers who fluidly traverse differential "
        f"calculus, cleanroom fabrication protocols, and high-performance kernel compilation."
    )

    java_code = generate_lesson_code(lang, tag1, tag2, mod_id, lesson_idx)

    warning_tr = (
        f"{tag1} projelerinde 'yazılımla her şeyi çözeriz' zihniyeti ölümcül bir tuzaktır! "
        f"Fiziksel dünyada {tag2} sınırları (sensör gürültüsü, sinyal zayıflaması, ısınma) simülasyondakinden daima daha acımasızdır."
    )

    warning_en = (
        f"Assuming software agility can overcome immutable physical laws is the premier failure mode in {tag1}! "
        f"In real-world {tag2} implementations, thermal dissipation, shot noise, and material fatigue are unforgiving."
    )

    takeaways = [
        (f"{tag1} geliştirmelerinde kararlarınızı benzetmelere değil, temel fizik yasalarına (first principles) dayandırın.",
         f"Ground all {tag1} engineering decisions in first-principles physics rather than conventional software analogies."),
        (f"Donanım ve yazılımı ayrı düşünmeyin; algoritmayı fiziksel malzemenin ({tag2}) sınırlarına göre birlikte tasarlayın.",
         f"Co-design algorithms strictly around the material and thermodynamic boundaries of {tag2}."),
        (f"Laboratuvardaki küçük ölçekli başarı ile fabrikanın endüstriyel ölçeği arasındaki termodinamik farkları hesaba katın.",
         f"Account for non-linear physical scaling anomalies when transitioning from lab bench to industrial output.")
    ]

    return {
        "num": global_num,
        "title_tr": title_tr,
        "title_en": title_en,
        "diagram": diagram,
        "eli5_tr": eli5_tr,
        "eli5_en": eli5_en,
        "deep_tr": deep_tr,
        "deep_en": deep_en,
        "java_code": java_code,
        "warning_tr": warning_tr,
        "warning_en": warning_en,
        "takeaways": takeaways
    }

def generate_module_file(spec):
    mod_id, dir_name, title_tr, title_en, desc_tr, desc_en, tag1, tag2, lang = spec
    lessons = []
    for l_idx in range(1, 11):
        lessons.append(generate_lesson_data(mod_id, l_idx, title_tr, title_en, tag1, tag2, lang))

    filename = MODULES_DATA_DIR / f"mod{mod_id:02d}_{dir_name}.py"
    
    code = f'''# -*- coding: utf-8 -*-
"""
Module {mod_id}: {title_en} (Lessons {(mod_id-1)*10 + 1}-{mod_id*10})
"""

MODULE = {{
    "id": {mod_id},
    "dir": "mod{mod_id:02d}_{dir_name}",
    "title_tr": "{title_tr}",
    "title_en": "{title_en}",
    "desc_tr": "{desc_tr}",
    "desc_en": "{desc_en}",
    "lessons": [
'''
    for l in lessons:
        code += f'''        {{
            "num": {l['num']},
            "title_tr": """{l['title_tr']}""",
            "title_en": """{l['title_en']}""",
            "diagram": """{l['diagram']}""",
            "eli5_tr": """{l['eli5_tr']}""",
            "eli5_en": """{l['eli5_en']}""",
            "deep_tr": """{l['deep_tr']}""",
            "deep_en": """{l['deep_en']}""",
            "java_code": """{l['java_code']}""",
            "warning_tr": """{l['warning_tr']}""",
            "warning_en": """{l['warning_en']}""",
            "takeaways": [
'''
        for t in l['takeaways']:
            tr_esc = t[0].replace('"', '\\"')
            en_esc = t[1].replace('"', '\\"')
            code += f'                ("{tr_esc}", "{en_esc}"),\n'
        code += '''            ]
        },
'''
    code += '''    ]
}
'''
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"✔ Generated Module {mod_id:02d}: {filename.name}")

if __name__ == "__main__":
    print("🚀 Generating all 50 Deeptech Modules and 500 Lessons...")
    for spec in MODULE_SPECS:
        generate_module_file(spec)
    print(f"🎉 Successfully generated all 50 module data files in {MODULES_DATA_DIR}!")
