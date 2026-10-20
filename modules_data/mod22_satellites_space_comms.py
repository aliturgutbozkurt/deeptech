# -*- coding: utf-8 -*-
"""
Module 22: LEO Satellite Constellations & Optical Inter-Satellite Links (Lessons 211-220)
"""

MODULE = {
    "id": 22,
    "dir": "mod22_satellites_space_comms",
    "title_tr": "Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi",
    "title_en": "LEO Satellite Constellations & Optical Inter-Satellite Links",
    "desc_tr": "Alçak Dünya Yörüngesi (LEO) mega-takımyıldızları, Faz dizili antenler (Beamforming), optik lazer haberleşme ve yörünge çöpü önleme.",
    "desc_en": "LEO orbital perturbations, phased-array electronically steered beamforming, free-space optical laser communications, and collision avoidance.",
    "lessons": [
        {
            "num": 211,
            "title_tr": """Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi - Temel Fizik İlkeleri, Bilimsel Temel ve Tarihsel Gelişim""",
            "title_en": """LEO Satellite Constellations & Optical Inter-Satellite Links - Foundational Physics Principles, Scientific Genesis & Evolution""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
│                 DEEPTECH FİZİKSEL SÜREÇ VE MİMARİ AKIŞ ŞEMASI                │
└─────────────────────────────────────────────────────────────────────────────┘
  [ Bilimsel Gözlem / Laboratuvar ] ──► [ Matematiksel Teori & Simülasyon ]
                                                       │
                                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ SATELLITES MÜHENDİSLİK DÜZLEMİ (LASERCOMMS ÇÖZÜCÜSÜ)                          │
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
   veya kuantum yasalarını ihlal eden bir hata milyonlarca dolarlık fabrikayı batırır!" """,
            "eli5_tr": """Evde yemek yapmayı düşünün: Bir web sitesi kodlamak ekmek arasına peynir koymaya benzer; hata yaparsanız peyniri çıkarıp zeytin koyabilirsiniz. Ancak derin teknoloji (Satellites), unun içindeki molekülleri laboratuvarda yeniden dizip 300 derece fırında elmas gibi parlayan yeni bir ekmek türü icat etmeye benzer! Burada sadece reçeteyi bilmek yetmez; fırının atom seviyesindeki ısısını (LaserComms), basıncını ve moleküler bağlarını mükemmel kontrol etmelisiniz. Bir derecelik hata her şeyi kömür eder!""",
            "eli5_en": """Think of culinary arts: Building typical consumer software is like making a grilled cheese sandwich; if you drop the slice, you grab another one from the fridge in two seconds. Deeptech (Satellites), however, is like synthesizing entirely new protein macromolecules at the sub-atomic scale to bake a bread that glows like diamonds and never stales! You are not just following a recipe; you are manipulating thermodynamics (LaserComms), atomic pressure, and quantum lattice bonds. A fraction of a degree off, and the entire batch turns to graphite!""",
            "deep_tr": """Derin Teknoloji Mühendisliği Seviyesinde Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi Analizi: Satellites disiplini, temel doğa yasalarının sınırlarında çalışmayı gerektirir. 1) Fiziksel İlkeler (First Principles): Karmaşık sistemleri benzetmelerle değil, termodinamik, elektrodinamik veya kuantum mekaniğinin temel aksiyomlarına indirgeyerek çözün. 2) Donanım-Yazılım Birlikteliği (Co-Design): LaserComms sistemlerinde yazılım donanımdan soyutlanamaz; algoritma çipin fiziksel ısınma sınırlarına veya reaktörün plazma stabilitesine göre tasarlanır. 3) Ölçekleme Faktörü (Scale-Up Frontier): Laboratuvar tezgahındaki 1 miligramlık başarı, tonlarca kimyasal veya milyonlarca transistörlük endüstriyel üretim hattına aktarılırken yeni fiziksel dinamikler doğurur. 4) Kariyer Ödünleşimi: Yalnızca kod yazan bir yazılımcı olmak yerine, atomları ve fotonları yöneten disiplinlerarası bir Frontier Mühendisi olmanız gerekir.""",
            "deep_en": """Frontier Deeptech Engineering Deep-Dive for LEO Satellite Constellations & Optical Inter-Satellite Links: Working within Satellites demands operating directly at the boundaries of natural physics. 1) First-Principles Decomposition: Discard conventional analogies; reconstruct technical architectures from thermodynamic, quantum electrodynamic, or cellular invariants. 2) Hardware-Algorithm Co-Design: In LaserComms, compute kernels cannot be decoupled from physical physics; algorithms must be shaped by thermal dissipation ceilings, shot noise limits, or magnetic confinement geometries. 3) Non-Linear Scale-Up Dynamics: What functions deterministically across a 10-micron lab-scale substrate routinely breaks under viscous shearing or parasitic capacitance when expanded to megawatt industrial capacity. 4) Frontier Career Trajectory: Deeptech rewards cross-disciplinary bilingualism—engineers who fluidly traverse differential calculus, cleanroom fabrication protocols, and high-performance kernel compilation.""",
            "java_code": """// Rust: Satellites & LaserComms Yüksek Güvenilirlikli Sistem Kodu
pub struct SatellitesController {
    pub telemetry_active: bool,
    pub sample_rate_hz: u32,
}

impl SatellitesController {
    pub fn new(rate: u32) -> Self {
        Self { telemetry_active: true, sample_rate_hz: rate }
    }

    pub fn process_telemetry(&self, raw_input: &[u8]) -> Result<String, &'static str> {
        if raw_input.is_empty() {
            return Err("Girdi sinyali boş!");
        }
        // Bellek güvenli, sıfır maliyetli soyutlama (Zero-Cost Abstraction)
        Ok(format!("Sinyal işlendi: {} bayt @ {} Hz", raw_input.len(), self.sample_rate_hz))
    }
}

fn main() {
    let controller = SatellitesController::new(10_000);
    let sample_data = [0xAA, 0xBB, 0xCC, 0xDD];
    match controller.process_telemetry(&sample_data) {
        Ok(msg) => println!("🚀 Rust Deeptech Engine: {}", msg),
        Err(e) => eprintln!("❌ Hata: {}", e),
    }
}""",
            "warning_tr": """Satellites projelerinde 'yazılımla her şeyi çözeriz' zihniyeti ölümcül bir tuzaktır! Fiziksel dünyada LaserComms sınırları (sensör gürültüsü, sinyal zayıflaması, ısınma) simülasyondakinden daima daha acımasızdır.""",
            "warning_en": """Assuming software agility can overcome immutable physical laws is the premier failure mode in Satellites! In real-world LaserComms implementations, thermal dissipation, shot noise, and material fatigue are unforgiving.""",
            "takeaways": [
                ("Satellites geliştirmelerinde kararlarınızı benzetmelere değil, temel fizik yasalarına (first principles) dayandırın.", "Ground all Satellites engineering decisions in first-principles physics rather than conventional software analogies."),
                ("Donanım ve yazılımı ayrı düşünmeyin; algoritmayı fiziksel malzemenin (LaserComms) sınırlarına göre birlikte tasarlayın.", "Co-design algorithms strictly around the material and thermodynamic boundaries of LaserComms."),
                ("Laboratuvardaki küçük ölçekli başarı ile fabrikanın endüstriyel ölçeği arasındaki termodinamik farkları hesaba katın.", "Account for non-linear physical scaling anomalies when transitioning from lab bench to industrial output."),
            ]
        },
        {
            "num": 212,
            "title_tr": """Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi - Matematiksel Modelleme, Durum Denklemleri ve Simülasyon""",
            "title_en": """LEO Satellite Constellations & Optical Inter-Satellite Links - Mathematical Formulations, State Equations & Simulation Dynamics""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
│                 DEEPTECH FİZİKSEL SÜREÇ VE MİMARİ AKIŞ ŞEMASI                │
└─────────────────────────────────────────────────────────────────────────────┘
  [ Bilimsel Gözlem / Laboratuvar ] ──► [ Matematiksel Teori & Simülasyon ]
                                                       │
                                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ SATELLITES MÜHENDİSLİK DÜZLEMİ (LASERCOMMS ÇÖZÜCÜSÜ)                          │
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
   veya kuantum yasalarını ihlal eden bir hata milyonlarca dolarlık fabrikayı batırır!" """,
            "eli5_tr": """Evde yemek yapmayı düşünün: Bir web sitesi kodlamak ekmek arasına peynir koymaya benzer; hata yaparsanız peyniri çıkarıp zeytin koyabilirsiniz. Ancak derin teknoloji (Satellites), unun içindeki molekülleri laboratuvarda yeniden dizip 300 derece fırında elmas gibi parlayan yeni bir ekmek türü icat etmeye benzer! Burada sadece reçeteyi bilmek yetmez; fırının atom seviyesindeki ısısını (LaserComms), basıncını ve moleküler bağlarını mükemmel kontrol etmelisiniz. Bir derecelik hata her şeyi kömür eder!""",
            "eli5_en": """Think of culinary arts: Building typical consumer software is like making a grilled cheese sandwich; if you drop the slice, you grab another one from the fridge in two seconds. Deeptech (Satellites), however, is like synthesizing entirely new protein macromolecules at the sub-atomic scale to bake a bread that glows like diamonds and never stales! You are not just following a recipe; you are manipulating thermodynamics (LaserComms), atomic pressure, and quantum lattice bonds. A fraction of a degree off, and the entire batch turns to graphite!""",
            "deep_tr": """Derin Teknoloji Mühendisliği Seviyesinde Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi Analizi: Satellites disiplini, temel doğa yasalarının sınırlarında çalışmayı gerektirir. 1) Fiziksel İlkeler (First Principles): Karmaşık sistemleri benzetmelerle değil, termodinamik, elektrodinamik veya kuantum mekaniğinin temel aksiyomlarına indirgeyerek çözün. 2) Donanım-Yazılım Birlikteliği (Co-Design): LaserComms sistemlerinde yazılım donanımdan soyutlanamaz; algoritma çipin fiziksel ısınma sınırlarına veya reaktörün plazma stabilitesine göre tasarlanır. 3) Ölçekleme Faktörü (Scale-Up Frontier): Laboratuvar tezgahındaki 1 miligramlık başarı, tonlarca kimyasal veya milyonlarca transistörlük endüstriyel üretim hattına aktarılırken yeni fiziksel dinamikler doğurur. 4) Kariyer Ödünleşimi: Yalnızca kod yazan bir yazılımcı olmak yerine, atomları ve fotonları yöneten disiplinlerarası bir Frontier Mühendisi olmanız gerekir.""",
            "deep_en": """Frontier Deeptech Engineering Deep-Dive for LEO Satellite Constellations & Optical Inter-Satellite Links: Working within Satellites demands operating directly at the boundaries of natural physics. 1) First-Principles Decomposition: Discard conventional analogies; reconstruct technical architectures from thermodynamic, quantum electrodynamic, or cellular invariants. 2) Hardware-Algorithm Co-Design: In LaserComms, compute kernels cannot be decoupled from physical physics; algorithms must be shaped by thermal dissipation ceilings, shot noise limits, or magnetic confinement geometries. 3) Non-Linear Scale-Up Dynamics: What functions deterministically across a 10-micron lab-scale substrate routinely breaks under viscous shearing or parasitic capacitance when expanded to megawatt industrial capacity. 4) Frontier Career Trajectory: Deeptech rewards cross-disciplinary bilingualism—engineers who fluidly traverse differential calculus, cleanroom fabrication protocols, and high-performance kernel compilation.""",
            "java_code": """// Rust: Satellites & LaserComms Yüksek Güvenilirlikli Sistem Kodu
pub struct SatellitesController {
    pub telemetry_active: bool,
    pub sample_rate_hz: u32,
}

impl SatellitesController {
    pub fn new(rate: u32) -> Self {
        Self { telemetry_active: true, sample_rate_hz: rate }
    }

    pub fn process_telemetry(&self, raw_input: &[u8]) -> Result<String, &'static str> {
        if raw_input.is_empty() {
            return Err("Girdi sinyali boş!");
        }
        // Bellek güvenli, sıfır maliyetli soyutlama (Zero-Cost Abstraction)
        Ok(format!("Sinyal işlendi: {} bayt @ {} Hz", raw_input.len(), self.sample_rate_hz))
    }
}

fn main() {
    let controller = SatellitesController::new(10_000);
    let sample_data = [0xAA, 0xBB, 0xCC, 0xDD];
    match controller.process_telemetry(&sample_data) {
        Ok(msg) => println!("🚀 Rust Deeptech Engine: {}", msg),
        Err(e) => eprintln!("❌ Hata: {}", e),
    }
}""",
            "warning_tr": """Satellites projelerinde 'yazılımla her şeyi çözeriz' zihniyeti ölümcül bir tuzaktır! Fiziksel dünyada LaserComms sınırları (sensör gürültüsü, sinyal zayıflaması, ısınma) simülasyondakinden daima daha acımasızdır.""",
            "warning_en": """Assuming software agility can overcome immutable physical laws is the premier failure mode in Satellites! In real-world LaserComms implementations, thermal dissipation, shot noise, and material fatigue are unforgiving.""",
            "takeaways": [
                ("Satellites geliştirmelerinde kararlarınızı benzetmelere değil, temel fizik yasalarına (first principles) dayandırın.", "Ground all Satellites engineering decisions in first-principles physics rather than conventional software analogies."),
                ("Donanım ve yazılımı ayrı düşünmeyin; algoritmayı fiziksel malzemenin (LaserComms) sınırlarına göre birlikte tasarlayın.", "Co-design algorithms strictly around the material and thermodynamic boundaries of LaserComms."),
                ("Laboratuvardaki küçük ölçekli başarı ile fabrikanın endüstriyel ölçeği arasındaki termodinamik farkları hesaba katın.", "Account for non-linear physical scaling anomalies when transitioning from lab bench to industrial output."),
            ]
        },
        {
            "num": 213,
            "title_tr": """Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi - Laboratuvardan Pilot Üretime: Cihaz ve Donanım Mimarisi""",
            "title_en": """LEO Satellite Constellations & Optical Inter-Satellite Links - From Lab Bench to Pilot: Hardware Tooling & Architecture""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
│                 DEEPTECH FİZİKSEL SÜREÇ VE MİMARİ AKIŞ ŞEMASI                │
└─────────────────────────────────────────────────────────────────────────────┘
  [ Bilimsel Gözlem / Laboratuvar ] ──► [ Matematiksel Teori & Simülasyon ]
                                                       │
                                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ SATELLITES MÜHENDİSLİK DÜZLEMİ (LASERCOMMS ÇÖZÜCÜSÜ)                          │
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
   veya kuantum yasalarını ihlal eden bir hata milyonlarca dolarlık fabrikayı batırır!" """,
            "eli5_tr": """Evde yemek yapmayı düşünün: Bir web sitesi kodlamak ekmek arasına peynir koymaya benzer; hata yaparsanız peyniri çıkarıp zeytin koyabilirsiniz. Ancak derin teknoloji (Satellites), unun içindeki molekülleri laboratuvarda yeniden dizip 300 derece fırında elmas gibi parlayan yeni bir ekmek türü icat etmeye benzer! Burada sadece reçeteyi bilmek yetmez; fırının atom seviyesindeki ısısını (LaserComms), basıncını ve moleküler bağlarını mükemmel kontrol etmelisiniz. Bir derecelik hata her şeyi kömür eder!""",
            "eli5_en": """Think of culinary arts: Building typical consumer software is like making a grilled cheese sandwich; if you drop the slice, you grab another one from the fridge in two seconds. Deeptech (Satellites), however, is like synthesizing entirely new protein macromolecules at the sub-atomic scale to bake a bread that glows like diamonds and never stales! You are not just following a recipe; you are manipulating thermodynamics (LaserComms), atomic pressure, and quantum lattice bonds. A fraction of a degree off, and the entire batch turns to graphite!""",
            "deep_tr": """Derin Teknoloji Mühendisliği Seviyesinde Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi Analizi: Satellites disiplini, temel doğa yasalarının sınırlarında çalışmayı gerektirir. 1) Fiziksel İlkeler (First Principles): Karmaşık sistemleri benzetmelerle değil, termodinamik, elektrodinamik veya kuantum mekaniğinin temel aksiyomlarına indirgeyerek çözün. 2) Donanım-Yazılım Birlikteliği (Co-Design): LaserComms sistemlerinde yazılım donanımdan soyutlanamaz; algoritma çipin fiziksel ısınma sınırlarına veya reaktörün plazma stabilitesine göre tasarlanır. 3) Ölçekleme Faktörü (Scale-Up Frontier): Laboratuvar tezgahındaki 1 miligramlık başarı, tonlarca kimyasal veya milyonlarca transistörlük endüstriyel üretim hattına aktarılırken yeni fiziksel dinamikler doğurur. 4) Kariyer Ödünleşimi: Yalnızca kod yazan bir yazılımcı olmak yerine, atomları ve fotonları yöneten disiplinlerarası bir Frontier Mühendisi olmanız gerekir.""",
            "deep_en": """Frontier Deeptech Engineering Deep-Dive for LEO Satellite Constellations & Optical Inter-Satellite Links: Working within Satellites demands operating directly at the boundaries of natural physics. 1) First-Principles Decomposition: Discard conventional analogies; reconstruct technical architectures from thermodynamic, quantum electrodynamic, or cellular invariants. 2) Hardware-Algorithm Co-Design: In LaserComms, compute kernels cannot be decoupled from physical physics; algorithms must be shaped by thermal dissipation ceilings, shot noise limits, or magnetic confinement geometries. 3) Non-Linear Scale-Up Dynamics: What functions deterministically across a 10-micron lab-scale substrate routinely breaks under viscous shearing or parasitic capacitance when expanded to megawatt industrial capacity. 4) Frontier Career Trajectory: Deeptech rewards cross-disciplinary bilingualism—engineers who fluidly traverse differential calculus, cleanroom fabrication protocols, and high-performance kernel compilation.""",
            "java_code": """// Rust: Satellites & LaserComms Yüksek Güvenilirlikli Sistem Kodu
pub struct SatellitesController {
    pub telemetry_active: bool,
    pub sample_rate_hz: u32,
}

impl SatellitesController {
    pub fn new(rate: u32) -> Self {
        Self { telemetry_active: true, sample_rate_hz: rate }
    }

    pub fn process_telemetry(&self, raw_input: &[u8]) -> Result<String, &'static str> {
        if raw_input.is_empty() {
            return Err("Girdi sinyali boş!");
        }
        // Bellek güvenli, sıfır maliyetli soyutlama (Zero-Cost Abstraction)
        Ok(format!("Sinyal işlendi: {} bayt @ {} Hz", raw_input.len(), self.sample_rate_hz))
    }
}

fn main() {
    let controller = SatellitesController::new(10_000);
    let sample_data = [0xAA, 0xBB, 0xCC, 0xDD];
    match controller.process_telemetry(&sample_data) {
        Ok(msg) => println!("🚀 Rust Deeptech Engine: {}", msg),
        Err(e) => eprintln!("❌ Hata: {}", e),
    }
}""",
            "warning_tr": """Satellites projelerinde 'yazılımla her şeyi çözeriz' zihniyeti ölümcül bir tuzaktır! Fiziksel dünyada LaserComms sınırları (sensör gürültüsü, sinyal zayıflaması, ısınma) simülasyondakinden daima daha acımasızdır.""",
            "warning_en": """Assuming software agility can overcome immutable physical laws is the premier failure mode in Satellites! In real-world LaserComms implementations, thermal dissipation, shot noise, and material fatigue are unforgiving.""",
            "takeaways": [
                ("Satellites geliştirmelerinde kararlarınızı benzetmelere değil, temel fizik yasalarına (first principles) dayandırın.", "Ground all Satellites engineering decisions in first-principles physics rather than conventional software analogies."),
                ("Donanım ve yazılımı ayrı düşünmeyin; algoritmayı fiziksel malzemenin (LaserComms) sınırlarına göre birlikte tasarlayın.", "Co-design algorithms strictly around the material and thermodynamic boundaries of LaserComms."),
                ("Laboratuvardaki küçük ölçekli başarı ile fabrikanın endüstriyel ölçeği arasındaki termodinamik farkları hesaba katın.", "Account for non-linear physical scaling anomalies when transitioning from lab bench to industrial output."),
            ]
        },
        {
            "num": 214,
            "title_tr": """Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi - Fiziksel Darboğazlar, Malzeme Sınırları ve Termodinamik Engeller""",
            "title_en": """LEO Satellite Constellations & Optical Inter-Satellite Links - Physical Bottlenecks, Material Limits & Thermodynamic Walls""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
│                 DEEPTECH FİZİKSEL SÜREÇ VE MİMARİ AKIŞ ŞEMASI                │
└─────────────────────────────────────────────────────────────────────────────┘
  [ Bilimsel Gözlem / Laboratuvar ] ──► [ Matematiksel Teori & Simülasyon ]
                                                       │
                                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ SATELLITES MÜHENDİSLİK DÜZLEMİ (LASERCOMMS ÇÖZÜCÜSÜ)                          │
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
   veya kuantum yasalarını ihlal eden bir hata milyonlarca dolarlık fabrikayı batırır!" """,
            "eli5_tr": """Evde yemek yapmayı düşünün: Bir web sitesi kodlamak ekmek arasına peynir koymaya benzer; hata yaparsanız peyniri çıkarıp zeytin koyabilirsiniz. Ancak derin teknoloji (Satellites), unun içindeki molekülleri laboratuvarda yeniden dizip 300 derece fırında elmas gibi parlayan yeni bir ekmek türü icat etmeye benzer! Burada sadece reçeteyi bilmek yetmez; fırının atom seviyesindeki ısısını (LaserComms), basıncını ve moleküler bağlarını mükemmel kontrol etmelisiniz. Bir derecelik hata her şeyi kömür eder!""",
            "eli5_en": """Think of culinary arts: Building typical consumer software is like making a grilled cheese sandwich; if you drop the slice, you grab another one from the fridge in two seconds. Deeptech (Satellites), however, is like synthesizing entirely new protein macromolecules at the sub-atomic scale to bake a bread that glows like diamonds and never stales! You are not just following a recipe; you are manipulating thermodynamics (LaserComms), atomic pressure, and quantum lattice bonds. A fraction of a degree off, and the entire batch turns to graphite!""",
            "deep_tr": """Derin Teknoloji Mühendisliği Seviyesinde Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi Analizi: Satellites disiplini, temel doğa yasalarının sınırlarında çalışmayı gerektirir. 1) Fiziksel İlkeler (First Principles): Karmaşık sistemleri benzetmelerle değil, termodinamik, elektrodinamik veya kuantum mekaniğinin temel aksiyomlarına indirgeyerek çözün. 2) Donanım-Yazılım Birlikteliği (Co-Design): LaserComms sistemlerinde yazılım donanımdan soyutlanamaz; algoritma çipin fiziksel ısınma sınırlarına veya reaktörün plazma stabilitesine göre tasarlanır. 3) Ölçekleme Faktörü (Scale-Up Frontier): Laboratuvar tezgahındaki 1 miligramlık başarı, tonlarca kimyasal veya milyonlarca transistörlük endüstriyel üretim hattına aktarılırken yeni fiziksel dinamikler doğurur. 4) Kariyer Ödünleşimi: Yalnızca kod yazan bir yazılımcı olmak yerine, atomları ve fotonları yöneten disiplinlerarası bir Frontier Mühendisi olmanız gerekir.""",
            "deep_en": """Frontier Deeptech Engineering Deep-Dive for LEO Satellite Constellations & Optical Inter-Satellite Links: Working within Satellites demands operating directly at the boundaries of natural physics. 1) First-Principles Decomposition: Discard conventional analogies; reconstruct technical architectures from thermodynamic, quantum electrodynamic, or cellular invariants. 2) Hardware-Algorithm Co-Design: In LaserComms, compute kernels cannot be decoupled from physical physics; algorithms must be shaped by thermal dissipation ceilings, shot noise limits, or magnetic confinement geometries. 3) Non-Linear Scale-Up Dynamics: What functions deterministically across a 10-micron lab-scale substrate routinely breaks under viscous shearing or parasitic capacitance when expanded to megawatt industrial capacity. 4) Frontier Career Trajectory: Deeptech rewards cross-disciplinary bilingualism—engineers who fluidly traverse differential calculus, cleanroom fabrication protocols, and high-performance kernel compilation.""",
            "java_code": """// Rust: Satellites & LaserComms Yüksek Güvenilirlikli Sistem Kodu
pub struct SatellitesController {
    pub telemetry_active: bool,
    pub sample_rate_hz: u32,
}

impl SatellitesController {
    pub fn new(rate: u32) -> Self {
        Self { telemetry_active: true, sample_rate_hz: rate }
    }

    pub fn process_telemetry(&self, raw_input: &[u8]) -> Result<String, &'static str> {
        if raw_input.is_empty() {
            return Err("Girdi sinyali boş!");
        }
        // Bellek güvenli, sıfır maliyetli soyutlama (Zero-Cost Abstraction)
        Ok(format!("Sinyal işlendi: {} bayt @ {} Hz", raw_input.len(), self.sample_rate_hz))
    }
}

fn main() {
    let controller = SatellitesController::new(10_000);
    let sample_data = [0xAA, 0xBB, 0xCC, 0xDD];
    match controller.process_telemetry(&sample_data) {
        Ok(msg) => println!("🚀 Rust Deeptech Engine: {}", msg),
        Err(e) => eprintln!("❌ Hata: {}", e),
    }
}""",
            "warning_tr": """Satellites projelerinde 'yazılımla her şeyi çözeriz' zihniyeti ölümcül bir tuzaktır! Fiziksel dünyada LaserComms sınırları (sensör gürültüsü, sinyal zayıflaması, ısınma) simülasyondakinden daima daha acımasızdır.""",
            "warning_en": """Assuming software agility can overcome immutable physical laws is the premier failure mode in Satellites! In real-world LaserComms implementations, thermal dissipation, shot noise, and material fatigue are unforgiving.""",
            "takeaways": [
                ("Satellites geliştirmelerinde kararlarınızı benzetmelere değil, temel fizik yasalarına (first principles) dayandırın.", "Ground all Satellites engineering decisions in first-principles physics rather than conventional software analogies."),
                ("Donanım ve yazılımı ayrı düşünmeyin; algoritmayı fiziksel malzemenin (LaserComms) sınırlarına göre birlikte tasarlayın.", "Co-design algorithms strictly around the material and thermodynamic boundaries of LaserComms."),
                ("Laboratuvardaki küçük ölçekli başarı ile fabrikanın endüstriyel ölçeği arasındaki termodinamik farkları hesaba katın.", "Account for non-linear physical scaling anomalies when transitioning from lab bench to industrial output."),
            ]
        },
        {
            "num": 215,
            "title_tr": """Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi - Uygulamalı Kodlama, Algoritmik Çözücüler ve Veri Hatları""",
            "title_en": """LEO Satellite Constellations & Optical Inter-Satellite Links - Applied Computation, Algorithmic Solvers & Data Pipelines""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
│                 DEEPTECH FİZİKSEL SÜREÇ VE MİMARİ AKIŞ ŞEMASI                │
└─────────────────────────────────────────────────────────────────────────────┘
  [ Bilimsel Gözlem / Laboratuvar ] ──► [ Matematiksel Teori & Simülasyon ]
                                                       │
                                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ SATELLITES MÜHENDİSLİK DÜZLEMİ (LASERCOMMS ÇÖZÜCÜSÜ)                          │
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
   veya kuantum yasalarını ihlal eden bir hata milyonlarca dolarlık fabrikayı batırır!" """,
            "eli5_tr": """Evde yemek yapmayı düşünün: Bir web sitesi kodlamak ekmek arasına peynir koymaya benzer; hata yaparsanız peyniri çıkarıp zeytin koyabilirsiniz. Ancak derin teknoloji (Satellites), unun içindeki molekülleri laboratuvarda yeniden dizip 300 derece fırında elmas gibi parlayan yeni bir ekmek türü icat etmeye benzer! Burada sadece reçeteyi bilmek yetmez; fırının atom seviyesindeki ısısını (LaserComms), basıncını ve moleküler bağlarını mükemmel kontrol etmelisiniz. Bir derecelik hata her şeyi kömür eder!""",
            "eli5_en": """Think of culinary arts: Building typical consumer software is like making a grilled cheese sandwich; if you drop the slice, you grab another one from the fridge in two seconds. Deeptech (Satellites), however, is like synthesizing entirely new protein macromolecules at the sub-atomic scale to bake a bread that glows like diamonds and never stales! You are not just following a recipe; you are manipulating thermodynamics (LaserComms), atomic pressure, and quantum lattice bonds. A fraction of a degree off, and the entire batch turns to graphite!""",
            "deep_tr": """Derin Teknoloji Mühendisliği Seviyesinde Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi Analizi: Satellites disiplini, temel doğa yasalarının sınırlarında çalışmayı gerektirir. 1) Fiziksel İlkeler (First Principles): Karmaşık sistemleri benzetmelerle değil, termodinamik, elektrodinamik veya kuantum mekaniğinin temel aksiyomlarına indirgeyerek çözün. 2) Donanım-Yazılım Birlikteliği (Co-Design): LaserComms sistemlerinde yazılım donanımdan soyutlanamaz; algoritma çipin fiziksel ısınma sınırlarına veya reaktörün plazma stabilitesine göre tasarlanır. 3) Ölçekleme Faktörü (Scale-Up Frontier): Laboratuvar tezgahındaki 1 miligramlık başarı, tonlarca kimyasal veya milyonlarca transistörlük endüstriyel üretim hattına aktarılırken yeni fiziksel dinamikler doğurur. 4) Kariyer Ödünleşimi: Yalnızca kod yazan bir yazılımcı olmak yerine, atomları ve fotonları yöneten disiplinlerarası bir Frontier Mühendisi olmanız gerekir.""",
            "deep_en": """Frontier Deeptech Engineering Deep-Dive for LEO Satellite Constellations & Optical Inter-Satellite Links: Working within Satellites demands operating directly at the boundaries of natural physics. 1) First-Principles Decomposition: Discard conventional analogies; reconstruct technical architectures from thermodynamic, quantum electrodynamic, or cellular invariants. 2) Hardware-Algorithm Co-Design: In LaserComms, compute kernels cannot be decoupled from physical physics; algorithms must be shaped by thermal dissipation ceilings, shot noise limits, or magnetic confinement geometries. 3) Non-Linear Scale-Up Dynamics: What functions deterministically across a 10-micron lab-scale substrate routinely breaks under viscous shearing or parasitic capacitance when expanded to megawatt industrial capacity. 4) Frontier Career Trajectory: Deeptech rewards cross-disciplinary bilingualism—engineers who fluidly traverse differential calculus, cleanroom fabrication protocols, and high-performance kernel compilation.""",
            "java_code": """// Rust: Satellites & LaserComms Yüksek Güvenilirlikli Sistem Kodu
pub struct SatellitesController {
    pub telemetry_active: bool,
    pub sample_rate_hz: u32,
}

impl SatellitesController {
    pub fn new(rate: u32) -> Self {
        Self { telemetry_active: true, sample_rate_hz: rate }
    }

    pub fn process_telemetry(&self, raw_input: &[u8]) -> Result<String, &'static str> {
        if raw_input.is_empty() {
            return Err("Girdi sinyali boş!");
        }
        // Bellek güvenli, sıfır maliyetli soyutlama (Zero-Cost Abstraction)
        Ok(format!("Sinyal işlendi: {} bayt @ {} Hz", raw_input.len(), self.sample_rate_hz))
    }
}

fn main() {
    let controller = SatellitesController::new(10_000);
    let sample_data = [0xAA, 0xBB, 0xCC, 0xDD];
    match controller.process_telemetry(&sample_data) {
        Ok(msg) => println!("🚀 Rust Deeptech Engine: {}", msg),
        Err(e) => eprintln!("❌ Hata: {}", e),
    }
}""",
            "warning_tr": """Satellites projelerinde 'yazılımla her şeyi çözeriz' zihniyeti ölümcül bir tuzaktır! Fiziksel dünyada LaserComms sınırları (sensör gürültüsü, sinyal zayıflaması, ısınma) simülasyondakinden daima daha acımasızdır.""",
            "warning_en": """Assuming software agility can overcome immutable physical laws is the premier failure mode in Satellites! In real-world LaserComms implementations, thermal dissipation, shot noise, and material fatigue are unforgiving.""",
            "takeaways": [
                ("Satellites geliştirmelerinde kararlarınızı benzetmelere değil, temel fizik yasalarına (first principles) dayandırın.", "Ground all Satellites engineering decisions in first-principles physics rather than conventional software analogies."),
                ("Donanım ve yazılımı ayrı düşünmeyin; algoritmayı fiziksel malzemenin (LaserComms) sınırlarına göre birlikte tasarlayın.", "Co-design algorithms strictly around the material and thermodynamic boundaries of LaserComms."),
                ("Laboratuvardaki küçük ölçekli başarı ile fabrikanın endüstriyel ölçeği arasındaki termodinamik farkları hesaba katın.", "Account for non-linear physical scaling anomalies when transitioning from lab bench to industrial output."),
            ]
        },
        {
            "num": 216,
            "title_tr": """Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi - Hata Düzeltme, Gürültü Azaltma ve Sinyal İzolasyonu""",
            "title_en": """LEO Satellite Constellations & Optical Inter-Satellite Links - Error Mitigation, Noise Suppression & Signal Isolation""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
│                 DEEPTECH FİZİKSEL SÜREÇ VE MİMARİ AKIŞ ŞEMASI                │
└─────────────────────────────────────────────────────────────────────────────┘
  [ Bilimsel Gözlem / Laboratuvar ] ──► [ Matematiksel Teori & Simülasyon ]
                                                       │
                                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ SATELLITES MÜHENDİSLİK DÜZLEMİ (LASERCOMMS ÇÖZÜCÜSÜ)                          │
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
   veya kuantum yasalarını ihlal eden bir hata milyonlarca dolarlık fabrikayı batırır!" """,
            "eli5_tr": """Evde yemek yapmayı düşünün: Bir web sitesi kodlamak ekmek arasına peynir koymaya benzer; hata yaparsanız peyniri çıkarıp zeytin koyabilirsiniz. Ancak derin teknoloji (Satellites), unun içindeki molekülleri laboratuvarda yeniden dizip 300 derece fırında elmas gibi parlayan yeni bir ekmek türü icat etmeye benzer! Burada sadece reçeteyi bilmek yetmez; fırının atom seviyesindeki ısısını (LaserComms), basıncını ve moleküler bağlarını mükemmel kontrol etmelisiniz. Bir derecelik hata her şeyi kömür eder!""",
            "eli5_en": """Think of culinary arts: Building typical consumer software is like making a grilled cheese sandwich; if you drop the slice, you grab another one from the fridge in two seconds. Deeptech (Satellites), however, is like synthesizing entirely new protein macromolecules at the sub-atomic scale to bake a bread that glows like diamonds and never stales! You are not just following a recipe; you are manipulating thermodynamics (LaserComms), atomic pressure, and quantum lattice bonds. A fraction of a degree off, and the entire batch turns to graphite!""",
            "deep_tr": """Derin Teknoloji Mühendisliği Seviyesinde Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi Analizi: Satellites disiplini, temel doğa yasalarının sınırlarında çalışmayı gerektirir. 1) Fiziksel İlkeler (First Principles): Karmaşık sistemleri benzetmelerle değil, termodinamik, elektrodinamik veya kuantum mekaniğinin temel aksiyomlarına indirgeyerek çözün. 2) Donanım-Yazılım Birlikteliği (Co-Design): LaserComms sistemlerinde yazılım donanımdan soyutlanamaz; algoritma çipin fiziksel ısınma sınırlarına veya reaktörün plazma stabilitesine göre tasarlanır. 3) Ölçekleme Faktörü (Scale-Up Frontier): Laboratuvar tezgahındaki 1 miligramlık başarı, tonlarca kimyasal veya milyonlarca transistörlük endüstriyel üretim hattına aktarılırken yeni fiziksel dinamikler doğurur. 4) Kariyer Ödünleşimi: Yalnızca kod yazan bir yazılımcı olmak yerine, atomları ve fotonları yöneten disiplinlerarası bir Frontier Mühendisi olmanız gerekir.""",
            "deep_en": """Frontier Deeptech Engineering Deep-Dive for LEO Satellite Constellations & Optical Inter-Satellite Links: Working within Satellites demands operating directly at the boundaries of natural physics. 1) First-Principles Decomposition: Discard conventional analogies; reconstruct technical architectures from thermodynamic, quantum electrodynamic, or cellular invariants. 2) Hardware-Algorithm Co-Design: In LaserComms, compute kernels cannot be decoupled from physical physics; algorithms must be shaped by thermal dissipation ceilings, shot noise limits, or magnetic confinement geometries. 3) Non-Linear Scale-Up Dynamics: What functions deterministically across a 10-micron lab-scale substrate routinely breaks under viscous shearing or parasitic capacitance when expanded to megawatt industrial capacity. 4) Frontier Career Trajectory: Deeptech rewards cross-disciplinary bilingualism—engineers who fluidly traverse differential calculus, cleanroom fabrication protocols, and high-performance kernel compilation.""",
            "java_code": """// Rust: Satellites & LaserComms Yüksek Güvenilirlikli Sistem Kodu
pub struct SatellitesController {
    pub telemetry_active: bool,
    pub sample_rate_hz: u32,
}

impl SatellitesController {
    pub fn new(rate: u32) -> Self {
        Self { telemetry_active: true, sample_rate_hz: rate }
    }

    pub fn process_telemetry(&self, raw_input: &[u8]) -> Result<String, &'static str> {
        if raw_input.is_empty() {
            return Err("Girdi sinyali boş!");
        }
        // Bellek güvenli, sıfır maliyetli soyutlama (Zero-Cost Abstraction)
        Ok(format!("Sinyal işlendi: {} bayt @ {} Hz", raw_input.len(), self.sample_rate_hz))
    }
}

fn main() {
    let controller = SatellitesController::new(10_000);
    let sample_data = [0xAA, 0xBB, 0xCC, 0xDD];
    match controller.process_telemetry(&sample_data) {
        Ok(msg) => println!("🚀 Rust Deeptech Engine: {}", msg),
        Err(e) => eprintln!("❌ Hata: {}", e),
    }
}""",
            "warning_tr": """Satellites projelerinde 'yazılımla her şeyi çözeriz' zihniyeti ölümcül bir tuzaktır! Fiziksel dünyada LaserComms sınırları (sensör gürültüsü, sinyal zayıflaması, ısınma) simülasyondakinden daima daha acımasızdır.""",
            "warning_en": """Assuming software agility can overcome immutable physical laws is the premier failure mode in Satellites! In real-world LaserComms implementations, thermal dissipation, shot noise, and material fatigue are unforgiving.""",
            "takeaways": [
                ("Satellites geliştirmelerinde kararlarınızı benzetmelere değil, temel fizik yasalarına (first principles) dayandırın.", "Ground all Satellites engineering decisions in first-principles physics rather than conventional software analogies."),
                ("Donanım ve yazılımı ayrı düşünmeyin; algoritmayı fiziksel malzemenin (LaserComms) sınırlarına göre birlikte tasarlayın.", "Co-design algorithms strictly around the material and thermodynamic boundaries of LaserComms."),
                ("Laboratuvardaki küçük ölçekli başarı ile fabrikanın endüstriyel ölçeği arasındaki termodinamik farkları hesaba katın.", "Account for non-linear physical scaling anomalies when transitioning from lab bench to industrial output."),
            ]
        },
        {
            "num": 217,
            "title_tr": """Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi - Ölçekleme Mühendisliği, Dayanıklılık ve Süreç Optimizasyonu""",
            "title_en": """LEO Satellite Constellations & Optical Inter-Satellite Links - Scale-Up Engineering, Endurance & Process Optimization""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
│                 DEEPTECH FİZİKSEL SÜREÇ VE MİMARİ AKIŞ ŞEMASI                │
└─────────────────────────────────────────────────────────────────────────────┘
  [ Bilimsel Gözlem / Laboratuvar ] ──► [ Matematiksel Teori & Simülasyon ]
                                                       │
                                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ SATELLITES MÜHENDİSLİK DÜZLEMİ (LASERCOMMS ÇÖZÜCÜSÜ)                          │
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
   veya kuantum yasalarını ihlal eden bir hata milyonlarca dolarlık fabrikayı batırır!" """,
            "eli5_tr": """Evde yemek yapmayı düşünün: Bir web sitesi kodlamak ekmek arasına peynir koymaya benzer; hata yaparsanız peyniri çıkarıp zeytin koyabilirsiniz. Ancak derin teknoloji (Satellites), unun içindeki molekülleri laboratuvarda yeniden dizip 300 derece fırında elmas gibi parlayan yeni bir ekmek türü icat etmeye benzer! Burada sadece reçeteyi bilmek yetmez; fırının atom seviyesindeki ısısını (LaserComms), basıncını ve moleküler bağlarını mükemmel kontrol etmelisiniz. Bir derecelik hata her şeyi kömür eder!""",
            "eli5_en": """Think of culinary arts: Building typical consumer software is like making a grilled cheese sandwich; if you drop the slice, you grab another one from the fridge in two seconds. Deeptech (Satellites), however, is like synthesizing entirely new protein macromolecules at the sub-atomic scale to bake a bread that glows like diamonds and never stales! You are not just following a recipe; you are manipulating thermodynamics (LaserComms), atomic pressure, and quantum lattice bonds. A fraction of a degree off, and the entire batch turns to graphite!""",
            "deep_tr": """Derin Teknoloji Mühendisliği Seviyesinde Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi Analizi: Satellites disiplini, temel doğa yasalarının sınırlarında çalışmayı gerektirir. 1) Fiziksel İlkeler (First Principles): Karmaşık sistemleri benzetmelerle değil, termodinamik, elektrodinamik veya kuantum mekaniğinin temel aksiyomlarına indirgeyerek çözün. 2) Donanım-Yazılım Birlikteliği (Co-Design): LaserComms sistemlerinde yazılım donanımdan soyutlanamaz; algoritma çipin fiziksel ısınma sınırlarına veya reaktörün plazma stabilitesine göre tasarlanır. 3) Ölçekleme Faktörü (Scale-Up Frontier): Laboratuvar tezgahındaki 1 miligramlık başarı, tonlarca kimyasal veya milyonlarca transistörlük endüstriyel üretim hattına aktarılırken yeni fiziksel dinamikler doğurur. 4) Kariyer Ödünleşimi: Yalnızca kod yazan bir yazılımcı olmak yerine, atomları ve fotonları yöneten disiplinlerarası bir Frontier Mühendisi olmanız gerekir.""",
            "deep_en": """Frontier Deeptech Engineering Deep-Dive for LEO Satellite Constellations & Optical Inter-Satellite Links: Working within Satellites demands operating directly at the boundaries of natural physics. 1) First-Principles Decomposition: Discard conventional analogies; reconstruct technical architectures from thermodynamic, quantum electrodynamic, or cellular invariants. 2) Hardware-Algorithm Co-Design: In LaserComms, compute kernels cannot be decoupled from physical physics; algorithms must be shaped by thermal dissipation ceilings, shot noise limits, or magnetic confinement geometries. 3) Non-Linear Scale-Up Dynamics: What functions deterministically across a 10-micron lab-scale substrate routinely breaks under viscous shearing or parasitic capacitance when expanded to megawatt industrial capacity. 4) Frontier Career Trajectory: Deeptech rewards cross-disciplinary bilingualism—engineers who fluidly traverse differential calculus, cleanroom fabrication protocols, and high-performance kernel compilation.""",
            "java_code": """// Rust: Satellites & LaserComms Yüksek Güvenilirlikli Sistem Kodu
pub struct SatellitesController {
    pub telemetry_active: bool,
    pub sample_rate_hz: u32,
}

impl SatellitesController {
    pub fn new(rate: u32) -> Self {
        Self { telemetry_active: true, sample_rate_hz: rate }
    }

    pub fn process_telemetry(&self, raw_input: &[u8]) -> Result<String, &'static str> {
        if raw_input.is_empty() {
            return Err("Girdi sinyali boş!");
        }
        // Bellek güvenli, sıfır maliyetli soyutlama (Zero-Cost Abstraction)
        Ok(format!("Sinyal işlendi: {} bayt @ {} Hz", raw_input.len(), self.sample_rate_hz))
    }
}

fn main() {
    let controller = SatellitesController::new(10_000);
    let sample_data = [0xAA, 0xBB, 0xCC, 0xDD];
    match controller.process_telemetry(&sample_data) {
        Ok(msg) => println!("🚀 Rust Deeptech Engine: {}", msg),
        Err(e) => eprintln!("❌ Hata: {}", e),
    }
}""",
            "warning_tr": """Satellites projelerinde 'yazılımla her şeyi çözeriz' zihniyeti ölümcül bir tuzaktır! Fiziksel dünyada LaserComms sınırları (sensör gürültüsü, sinyal zayıflaması, ısınma) simülasyondakinden daima daha acımasızdır.""",
            "warning_en": """Assuming software agility can overcome immutable physical laws is the premier failure mode in Satellites! In real-world LaserComms implementations, thermal dissipation, shot noise, and material fatigue are unforgiving.""",
            "takeaways": [
                ("Satellites geliştirmelerinde kararlarınızı benzetmelere değil, temel fizik yasalarına (first principles) dayandırın.", "Ground all Satellites engineering decisions in first-principles physics rather than conventional software analogies."),
                ("Donanım ve yazılımı ayrı düşünmeyin; algoritmayı fiziksel malzemenin (LaserComms) sınırlarına göre birlikte tasarlayın.", "Co-design algorithms strictly around the material and thermodynamic boundaries of LaserComms."),
                ("Laboratuvardaki küçük ölçekli başarı ile fabrikanın endüstriyel ölçeği arasındaki termodinamik farkları hesaba katın.", "Account for non-linear physical scaling anomalies when transitioning from lab bench to industrial output."),
            ]
        },
        {
            "num": 218,
            "title_tr": """Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi - Deneysel Doğrulama, Karakterizasyon ve Spektroskopi Metotları""",
            "title_en": """LEO Satellite Constellations & Optical Inter-Satellite Links - Empirical Validation, Characterization & Metrology Workflows""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
│                 DEEPTECH FİZİKSEL SÜREÇ VE MİMARİ AKIŞ ŞEMASI                │
└─────────────────────────────────────────────────────────────────────────────┘
  [ Bilimsel Gözlem / Laboratuvar ] ──► [ Matematiksel Teori & Simülasyon ]
                                                       │
                                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ SATELLITES MÜHENDİSLİK DÜZLEMİ (LASERCOMMS ÇÖZÜCÜSÜ)                          │
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
   veya kuantum yasalarını ihlal eden bir hata milyonlarca dolarlık fabrikayı batırır!" """,
            "eli5_tr": """Evde yemek yapmayı düşünün: Bir web sitesi kodlamak ekmek arasına peynir koymaya benzer; hata yaparsanız peyniri çıkarıp zeytin koyabilirsiniz. Ancak derin teknoloji (Satellites), unun içindeki molekülleri laboratuvarda yeniden dizip 300 derece fırında elmas gibi parlayan yeni bir ekmek türü icat etmeye benzer! Burada sadece reçeteyi bilmek yetmez; fırının atom seviyesindeki ısısını (LaserComms), basıncını ve moleküler bağlarını mükemmel kontrol etmelisiniz. Bir derecelik hata her şeyi kömür eder!""",
            "eli5_en": """Think of culinary arts: Building typical consumer software is like making a grilled cheese sandwich; if you drop the slice, you grab another one from the fridge in two seconds. Deeptech (Satellites), however, is like synthesizing entirely new protein macromolecules at the sub-atomic scale to bake a bread that glows like diamonds and never stales! You are not just following a recipe; you are manipulating thermodynamics (LaserComms), atomic pressure, and quantum lattice bonds. A fraction of a degree off, and the entire batch turns to graphite!""",
            "deep_tr": """Derin Teknoloji Mühendisliği Seviyesinde Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi Analizi: Satellites disiplini, temel doğa yasalarının sınırlarında çalışmayı gerektirir. 1) Fiziksel İlkeler (First Principles): Karmaşık sistemleri benzetmelerle değil, termodinamik, elektrodinamik veya kuantum mekaniğinin temel aksiyomlarına indirgeyerek çözün. 2) Donanım-Yazılım Birlikteliği (Co-Design): LaserComms sistemlerinde yazılım donanımdan soyutlanamaz; algoritma çipin fiziksel ısınma sınırlarına veya reaktörün plazma stabilitesine göre tasarlanır. 3) Ölçekleme Faktörü (Scale-Up Frontier): Laboratuvar tezgahındaki 1 miligramlık başarı, tonlarca kimyasal veya milyonlarca transistörlük endüstriyel üretim hattına aktarılırken yeni fiziksel dinamikler doğurur. 4) Kariyer Ödünleşimi: Yalnızca kod yazan bir yazılımcı olmak yerine, atomları ve fotonları yöneten disiplinlerarası bir Frontier Mühendisi olmanız gerekir.""",
            "deep_en": """Frontier Deeptech Engineering Deep-Dive for LEO Satellite Constellations & Optical Inter-Satellite Links: Working within Satellites demands operating directly at the boundaries of natural physics. 1) First-Principles Decomposition: Discard conventional analogies; reconstruct technical architectures from thermodynamic, quantum electrodynamic, or cellular invariants. 2) Hardware-Algorithm Co-Design: In LaserComms, compute kernels cannot be decoupled from physical physics; algorithms must be shaped by thermal dissipation ceilings, shot noise limits, or magnetic confinement geometries. 3) Non-Linear Scale-Up Dynamics: What functions deterministically across a 10-micron lab-scale substrate routinely breaks under viscous shearing or parasitic capacitance when expanded to megawatt industrial capacity. 4) Frontier Career Trajectory: Deeptech rewards cross-disciplinary bilingualism—engineers who fluidly traverse differential calculus, cleanroom fabrication protocols, and high-performance kernel compilation.""",
            "java_code": """// Rust: Satellites & LaserComms Yüksek Güvenilirlikli Sistem Kodu
pub struct SatellitesController {
    pub telemetry_active: bool,
    pub sample_rate_hz: u32,
}

impl SatellitesController {
    pub fn new(rate: u32) -> Self {
        Self { telemetry_active: true, sample_rate_hz: rate }
    }

    pub fn process_telemetry(&self, raw_input: &[u8]) -> Result<String, &'static str> {
        if raw_input.is_empty() {
            return Err("Girdi sinyali boş!");
        }
        // Bellek güvenli, sıfır maliyetli soyutlama (Zero-Cost Abstraction)
        Ok(format!("Sinyal işlendi: {} bayt @ {} Hz", raw_input.len(), self.sample_rate_hz))
    }
}

fn main() {
    let controller = SatellitesController::new(10_000);
    let sample_data = [0xAA, 0xBB, 0xCC, 0xDD];
    match controller.process_telemetry(&sample_data) {
        Ok(msg) => println!("🚀 Rust Deeptech Engine: {}", msg),
        Err(e) => eprintln!("❌ Hata: {}", e),
    }
}""",
            "warning_tr": """Satellites projelerinde 'yazılımla her şeyi çözeriz' zihniyeti ölümcül bir tuzaktır! Fiziksel dünyada LaserComms sınırları (sensör gürültüsü, sinyal zayıflaması, ısınma) simülasyondakinden daima daha acımasızdır.""",
            "warning_en": """Assuming software agility can overcome immutable physical laws is the premier failure mode in Satellites! In real-world LaserComms implementations, thermal dissipation, shot noise, and material fatigue are unforgiving.""",
            "takeaways": [
                ("Satellites geliştirmelerinde kararlarınızı benzetmelere değil, temel fizik yasalarına (first principles) dayandırın.", "Ground all Satellites engineering decisions in first-principles physics rather than conventional software analogies."),
                ("Donanım ve yazılımı ayrı düşünmeyin; algoritmayı fiziksel malzemenin (LaserComms) sınırlarına göre birlikte tasarlayın.", "Co-design algorithms strictly around the material and thermodynamic boundaries of LaserComms."),
                ("Laboratuvardaki küçük ölçekli başarı ile fabrikanın endüstriyel ölçeği arasındaki termodinamik farkları hesaba katın.", "Account for non-linear physical scaling anomalies when transitioning from lab bench to industrial output."),
            ]
        },
        {
            "num": 219,
            "title_tr": """Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi - Tekno-Ekonomik Analiz, Birim Maliyetler ve Ticari Fizibilite""",
            "title_en": """LEO Satellite Constellations & Optical Inter-Satellite Links - Techno-Economic Modeling, Unit Economics & Commercial Viability""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
│                 DEEPTECH FİZİKSEL SÜREÇ VE MİMARİ AKIŞ ŞEMASI                │
└─────────────────────────────────────────────────────────────────────────────┘
  [ Bilimsel Gözlem / Laboratuvar ] ──► [ Matematiksel Teori & Simülasyon ]
                                                       │
                                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ SATELLITES MÜHENDİSLİK DÜZLEMİ (LASERCOMMS ÇÖZÜCÜSÜ)                          │
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
   veya kuantum yasalarını ihlal eden bir hata milyonlarca dolarlık fabrikayı batırır!" """,
            "eli5_tr": """Evde yemek yapmayı düşünün: Bir web sitesi kodlamak ekmek arasına peynir koymaya benzer; hata yaparsanız peyniri çıkarıp zeytin koyabilirsiniz. Ancak derin teknoloji (Satellites), unun içindeki molekülleri laboratuvarda yeniden dizip 300 derece fırında elmas gibi parlayan yeni bir ekmek türü icat etmeye benzer! Burada sadece reçeteyi bilmek yetmez; fırının atom seviyesindeki ısısını (LaserComms), basıncını ve moleküler bağlarını mükemmel kontrol etmelisiniz. Bir derecelik hata her şeyi kömür eder!""",
            "eli5_en": """Think of culinary arts: Building typical consumer software is like making a grilled cheese sandwich; if you drop the slice, you grab another one from the fridge in two seconds. Deeptech (Satellites), however, is like synthesizing entirely new protein macromolecules at the sub-atomic scale to bake a bread that glows like diamonds and never stales! You are not just following a recipe; you are manipulating thermodynamics (LaserComms), atomic pressure, and quantum lattice bonds. A fraction of a degree off, and the entire batch turns to graphite!""",
            "deep_tr": """Derin Teknoloji Mühendisliği Seviyesinde Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi Analizi: Satellites disiplini, temel doğa yasalarının sınırlarında çalışmayı gerektirir. 1) Fiziksel İlkeler (First Principles): Karmaşık sistemleri benzetmelerle değil, termodinamik, elektrodinamik veya kuantum mekaniğinin temel aksiyomlarına indirgeyerek çözün. 2) Donanım-Yazılım Birlikteliği (Co-Design): LaserComms sistemlerinde yazılım donanımdan soyutlanamaz; algoritma çipin fiziksel ısınma sınırlarına veya reaktörün plazma stabilitesine göre tasarlanır. 3) Ölçekleme Faktörü (Scale-Up Frontier): Laboratuvar tezgahındaki 1 miligramlık başarı, tonlarca kimyasal veya milyonlarca transistörlük endüstriyel üretim hattına aktarılırken yeni fiziksel dinamikler doğurur. 4) Kariyer Ödünleşimi: Yalnızca kod yazan bir yazılımcı olmak yerine, atomları ve fotonları yöneten disiplinlerarası bir Frontier Mühendisi olmanız gerekir.""",
            "deep_en": """Frontier Deeptech Engineering Deep-Dive for LEO Satellite Constellations & Optical Inter-Satellite Links: Working within Satellites demands operating directly at the boundaries of natural physics. 1) First-Principles Decomposition: Discard conventional analogies; reconstruct technical architectures from thermodynamic, quantum electrodynamic, or cellular invariants. 2) Hardware-Algorithm Co-Design: In LaserComms, compute kernels cannot be decoupled from physical physics; algorithms must be shaped by thermal dissipation ceilings, shot noise limits, or magnetic confinement geometries. 3) Non-Linear Scale-Up Dynamics: What functions deterministically across a 10-micron lab-scale substrate routinely breaks under viscous shearing or parasitic capacitance when expanded to megawatt industrial capacity. 4) Frontier Career Trajectory: Deeptech rewards cross-disciplinary bilingualism—engineers who fluidly traverse differential calculus, cleanroom fabrication protocols, and high-performance kernel compilation.""",
            "java_code": """// Rust: Satellites & LaserComms Yüksek Güvenilirlikli Sistem Kodu
pub struct SatellitesController {
    pub telemetry_active: bool,
    pub sample_rate_hz: u32,
}

impl SatellitesController {
    pub fn new(rate: u32) -> Self {
        Self { telemetry_active: true, sample_rate_hz: rate }
    }

    pub fn process_telemetry(&self, raw_input: &[u8]) -> Result<String, &'static str> {
        if raw_input.is_empty() {
            return Err("Girdi sinyali boş!");
        }
        // Bellek güvenli, sıfır maliyetli soyutlama (Zero-Cost Abstraction)
        Ok(format!("Sinyal işlendi: {} bayt @ {} Hz", raw_input.len(), self.sample_rate_hz))
    }
}

fn main() {
    let controller = SatellitesController::new(10_000);
    let sample_data = [0xAA, 0xBB, 0xCC, 0xDD];
    match controller.process_telemetry(&sample_data) {
        Ok(msg) => println!("🚀 Rust Deeptech Engine: {}", msg),
        Err(e) => eprintln!("❌ Hata: {}", e),
    }
}""",
            "warning_tr": """Satellites projelerinde 'yazılımla her şeyi çözeriz' zihniyeti ölümcül bir tuzaktır! Fiziksel dünyada LaserComms sınırları (sensör gürültüsü, sinyal zayıflaması, ısınma) simülasyondakinden daima daha acımasızdır.""",
            "warning_en": """Assuming software agility can overcome immutable physical laws is the premier failure mode in Satellites! In real-world LaserComms implementations, thermal dissipation, shot noise, and material fatigue are unforgiving.""",
            "takeaways": [
                ("Satellites geliştirmelerinde kararlarınızı benzetmelere değil, temel fizik yasalarına (first principles) dayandırın.", "Ground all Satellites engineering decisions in first-principles physics rather than conventional software analogies."),
                ("Donanım ve yazılımı ayrı düşünmeyin; algoritmayı fiziksel malzemenin (LaserComms) sınırlarına göre birlikte tasarlayın.", "Co-design algorithms strictly around the material and thermodynamic boundaries of LaserComms."),
                ("Laboratuvardaki küçük ölçekli başarı ile fabrikanın endüstriyel ölçeği arasındaki termodinamik farkları hesaba katın.", "Account for non-linear physical scaling anomalies when transitioning from lab bench to industrial output."),
            ]
        },
        {
            "num": 220,
            "title_tr": """Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi - Gelecek Vizyonu, 2035-2050 Yol Haritası ve Frontier Kariyer Kılavuzu""",
            "title_en": """LEO Satellite Constellations & Optical Inter-Satellite Links - Frontier Horizon, 2035-2050 Technology Roadmap & Career Mastery""",
            "diagram": """┌─────────────────────────────────────────────────────────────────────────────┐
│                 DEEPTECH FİZİKSEL SÜREÇ VE MİMARİ AKIŞ ŞEMASI                │
└─────────────────────────────────────────────────────────────────────────────┘
  [ Bilimsel Gözlem / Laboratuvar ] ──► [ Matematiksel Teori & Simülasyon ]
                                                       │
                                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ SATELLITES MÜHENDİSLİK DÜZLEMİ (LASERCOMMS ÇÖZÜCÜSÜ)                          │
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
   veya kuantum yasalarını ihlal eden bir hata milyonlarca dolarlık fabrikayı batırır!" """,
            "eli5_tr": """Evde yemek yapmayı düşünün: Bir web sitesi kodlamak ekmek arasına peynir koymaya benzer; hata yaparsanız peyniri çıkarıp zeytin koyabilirsiniz. Ancak derin teknoloji (Satellites), unun içindeki molekülleri laboratuvarda yeniden dizip 300 derece fırında elmas gibi parlayan yeni bir ekmek türü icat etmeye benzer! Burada sadece reçeteyi bilmek yetmez; fırının atom seviyesindeki ısısını (LaserComms), basıncını ve moleküler bağlarını mükemmel kontrol etmelisiniz. Bir derecelik hata her şeyi kömür eder!""",
            "eli5_en": """Think of culinary arts: Building typical consumer software is like making a grilled cheese sandwich; if you drop the slice, you grab another one from the fridge in two seconds. Deeptech (Satellites), however, is like synthesizing entirely new protein macromolecules at the sub-atomic scale to bake a bread that glows like diamonds and never stales! You are not just following a recipe; you are manipulating thermodynamics (LaserComms), atomic pressure, and quantum lattice bonds. A fraction of a degree off, and the entire batch turns to graphite!""",
            "deep_tr": """Derin Teknoloji Mühendisliği Seviyesinde Uydu Takımyıldızları (LEO) & Uzay Lazer İletişimi Analizi: Satellites disiplini, temel doğa yasalarının sınırlarında çalışmayı gerektirir. 1) Fiziksel İlkeler (First Principles): Karmaşık sistemleri benzetmelerle değil, termodinamik, elektrodinamik veya kuantum mekaniğinin temel aksiyomlarına indirgeyerek çözün. 2) Donanım-Yazılım Birlikteliği (Co-Design): LaserComms sistemlerinde yazılım donanımdan soyutlanamaz; algoritma çipin fiziksel ısınma sınırlarına veya reaktörün plazma stabilitesine göre tasarlanır. 3) Ölçekleme Faktörü (Scale-Up Frontier): Laboratuvar tezgahındaki 1 miligramlık başarı, tonlarca kimyasal veya milyonlarca transistörlük endüstriyel üretim hattına aktarılırken yeni fiziksel dinamikler doğurur. 4) Kariyer Ödünleşimi: Yalnızca kod yazan bir yazılımcı olmak yerine, atomları ve fotonları yöneten disiplinlerarası bir Frontier Mühendisi olmanız gerekir.""",
            "deep_en": """Frontier Deeptech Engineering Deep-Dive for LEO Satellite Constellations & Optical Inter-Satellite Links: Working within Satellites demands operating directly at the boundaries of natural physics. 1) First-Principles Decomposition: Discard conventional analogies; reconstruct technical architectures from thermodynamic, quantum electrodynamic, or cellular invariants. 2) Hardware-Algorithm Co-Design: In LaserComms, compute kernels cannot be decoupled from physical physics; algorithms must be shaped by thermal dissipation ceilings, shot noise limits, or magnetic confinement geometries. 3) Non-Linear Scale-Up Dynamics: What functions deterministically across a 10-micron lab-scale substrate routinely breaks under viscous shearing or parasitic capacitance when expanded to megawatt industrial capacity. 4) Frontier Career Trajectory: Deeptech rewards cross-disciplinary bilingualism—engineers who fluidly traverse differential calculus, cleanroom fabrication protocols, and high-performance kernel compilation.""",
            "java_code": """// Rust: Satellites & LaserComms Yüksek Güvenilirlikli Sistem Kodu
pub struct SatellitesController {
    pub telemetry_active: bool,
    pub sample_rate_hz: u32,
}

impl SatellitesController {
    pub fn new(rate: u32) -> Self {
        Self { telemetry_active: true, sample_rate_hz: rate }
    }

    pub fn process_telemetry(&self, raw_input: &[u8]) -> Result<String, &'static str> {
        if raw_input.is_empty() {
            return Err("Girdi sinyali boş!");
        }
        // Bellek güvenli, sıfır maliyetli soyutlama (Zero-Cost Abstraction)
        Ok(format!("Sinyal işlendi: {} bayt @ {} Hz", raw_input.len(), self.sample_rate_hz))
    }
}

fn main() {
    let controller = SatellitesController::new(10_000);
    let sample_data = [0xAA, 0xBB, 0xCC, 0xDD];
    match controller.process_telemetry(&sample_data) {
        Ok(msg) => println!("🚀 Rust Deeptech Engine: {}", msg),
        Err(e) => eprintln!("❌ Hata: {}", e),
    }
}""",
            "warning_tr": """Satellites projelerinde 'yazılımla her şeyi çözeriz' zihniyeti ölümcül bir tuzaktır! Fiziksel dünyada LaserComms sınırları (sensör gürültüsü, sinyal zayıflaması, ısınma) simülasyondakinden daima daha acımasızdır.""",
            "warning_en": """Assuming software agility can overcome immutable physical laws is the premier failure mode in Satellites! In real-world LaserComms implementations, thermal dissipation, shot noise, and material fatigue are unforgiving.""",
            "takeaways": [
                ("Satellites geliştirmelerinde kararlarınızı benzetmelere değil, temel fizik yasalarına (first principles) dayandırın.", "Ground all Satellites engineering decisions in first-principles physics rather than conventional software analogies."),
                ("Donanım ve yazılımı ayrı düşünmeyin; algoritmayı fiziksel malzemenin (LaserComms) sınırlarına göre birlikte tasarlayın.", "Co-design algorithms strictly around the material and thermodynamic boundaries of LaserComms."),
                ("Laboratuvardaki küçük ölçekli başarı ile fabrikanın endüstriyel ölçeği arasındaki termodinamik farkları hesaba katın.", "Account for non-linear physical scaling anomalies when transitioning from lab bench to industrial output."),
            ]
        },
    ]
}
