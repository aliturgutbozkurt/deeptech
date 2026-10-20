#import "/template.typ": *

#show: doc => setup_book(title: "Ders 201: Uzay Teknolojileri: Roket İtki Sistemleri & Yörünge Mekaniği - Temel Fizik İlkeleri, Bilimsel Temel ve Tarihsel Gelişim", doc)

#lesson_header(
  201,
  "Uzay Teknolojileri: Roket İtki Sistemleri & Yörünge Mekaniği - Temel Fizik İlkeleri, Bilimsel Temel ve Tarihsel Gelişim",
  "Space Propulsion & Orbital Mechanics: Tsiolkovsky to Aerospikes - Foundational Physics Principles, Scientific Genesis & Evolution",
  "Uzay Teknolojileri: Roket İtki Sistemleri & Yörünge Mekaniği",
  "Space Propulsion & Orbital Mechanics: Tsiolkovsky to Aerospikes"
)

#diagram_box[
```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                 DEEPTECH FİZİKSEL SÜREÇ VE MİMARİ AKIŞ ŞEMASI                │
└─────────────────────────────────────────────────────────────────────────────┘
  [ Bilimsel Gözlem / Laboratuvar ] ──► [ Matematiksel Teori & Simülasyon ]
                                                       │
                                                       ▼
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ AEROSPACE MÜHENDİSLİK DÜZLEMİ (PROPULSION ÇÖZÜCÜSÜ)                          │
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
   veya kuantum yasalarını ihlal eden bir hata milyonlarca dolarlık fabrikayı batırır!" 
```
]

#eli5_box[
  #grid(
    columns: (1fr, 1fr),
    gutter: 12pt,
    [
      #text(weight: "bold", fill: rgb("1e40af"), size: 8.5pt)[🇹🇷 TÜRKÇE (ELI5)]\
      #v(2pt)
      Evde yemek yapmayı düşünün: Bir web sitesi kodlamak ekmek arasına peynir koymaya benzer; hata yaparsanız peyniri çıkarıp zeytin koyabilirsiniz. Ancak derin teknoloji (Aerospace), unun içindeki molekülleri laboratuvarda yeniden dizip 300 derece fırında elmas gibi parlayan yeni bir ekmek türü icat etmeye benzer! Burada sadece reçeteyi bilmek yetmez; fırının atom seviyesindeki ısısını (Propulsion), basıncını ve moleküler bağlarını mükemmel kontrol etmelisiniz. Bir derecelik hata her şeyi kömür eder!
    ],
    [
      #text(weight: "bold", fill: rgb("1d4ed8"), size: 8.5pt)[🇬🇧 ENGLISH (ELI5)]\
      #v(2pt)
      #text(fill: rgb("334155"))[Think of culinary arts: Building typical consumer software is like making a grilled cheese sandwich; if you drop the slice, you grab another one from the fridge in two seconds. Deeptech (Aerospace), however, is like synthesizing entirely new protein macromolecules at the sub-atomic scale to bake a bread that glows like diamonds and never stales! You are not just following a recipe; you are manipulating thermodynamics (Propulsion), atomic pressure, and quantum lattice bonds. A fraction of a degree off, and the entire batch turns to graphite!]
    ]
  )
]

#deep_dive_box[
  #grid(
    columns: (1fr, 1fr),
    gutter: 12pt,
    [
      #text(weight: "bold", fill: rgb("5b21b6"), size: 8.5pt)[🇹🇷 DEEPTECH MÜHENDİSLİK ANALİZİ]\
      #v(2pt)
      Derin Teknoloji Mühendisliği Seviyesinde Uzay Teknolojileri: Roket İtki Sistemleri & Yörünge Mekaniği Analizi: Aerospace disiplini, temel doğa yasalarının sınırlarında çalışmayı gerektirir. 1) Fiziksel İlkeler (First Principles): Karmaşık sistemleri benzetmelerle değil, termodinamik, elektrodinamik veya kuantum mekaniğinin temel aksiyomlarına indirgeyerek çözün. 2) Donanım-Yazılım Birlikteliği (Co-Design): Propulsion sistemlerinde yazılım donanımdan soyutlanamaz; algoritma çipin fiziksel ısınma sınırlarına veya reaktörün plazma stabilitesine göre tasarlanır. 3) Ölçekleme Faktörü (Scale-Up Frontier): Laboratuvar tezgahındaki 1 miligramlık başarı, tonlarca kimyasal veya milyonlarca transistörlük endüstriyel üretim hattına aktarılırken yeni fiziksel dinamikler doğurur. 4) Kariyer Ödünleşimi: Yalnızca kod yazan bir yazılımcı olmak yerine, atomları ve fotonları yöneten disiplinlerarası bir Frontier Mühendisi olmanız gerekir.
    ],
    [
      #text(weight: "bold", fill: rgb("6d28d9"), size: 8.5pt)[🇬🇧 FRONTIER TECHNICAL DEEP-DIVE]\
      #v(2pt)
      #text(fill: rgb("334155"))[Frontier Deeptech Engineering Deep-Dive for Space Propulsion & Orbital Mechanics: Tsiolkovsky to Aerospikes: Working within Aerospace demands operating directly at the boundaries of natural physics. 1) First-Principles Decomposition: Discard conventional analogies; reconstruct technical architectures from thermodynamic, quantum electrodynamic, or cellular invariants. 2) Hardware-Algorithm Co-Design: In Propulsion, compute kernels cannot be decoupled from physical physics; algorithms must be shaped by thermal dissipation ceilings, shot noise limits, or magnetic confinement geometries. 3) Non-Linear Scale-Up Dynamics: What functions deterministically across a 10-micron lab-scale substrate routinely breaks under viscous shearing or parasitic capacitance when expanded to megawatt industrial capacity. 4) Frontier Career Trajectory: Deeptech rewards cross-disciplinary bilingualism—engineers who fluidly traverse differential calculus, cleanroom fabrication protocols, and high-performance kernel compilation.]
    ]
  )
]

#code_box[
```python
# Python 3: Aerospace & Propulsion Bilimsel Hesaplama ve Simülasyon
import numpy as np

def simulate_aerospace_dynamics(steps: int = 1000, dt: float = 1e-3):
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
    t, s = simulate_aerospace_dynamics()
    print(f"🔬 Aerospace Simülasyonu Tamamlandı! Son Enerji: {s[-1, 2]:.4f} Joule.")
```
]

#warning_box[
  #grid(
    columns: (1fr, 1fr),
    gutter: 12pt,
    [
      #text(weight: "bold", fill: rgb("9f1239"), size: 8.5pt)[🇹🇷 FİZİKSEL DARBOĞAZ & TİCARİLEŞME TUZAĞI]\
      #v(2pt)
      Aerospace projelerinde 'yazılımla her şeyi çözeriz' zihniyeti ölümcül bir tuzaktır! Fiziksel dünyada Propulsion sınırları (sensör gürültüsü, sinyal zayıflaması, ısınma) simülasyondakinden daima daha acımasızdır.
    ],
    [
      #text(weight: "bold", fill: rgb("be123c"), size: 8.5pt)[🇬🇧 PHYSICAL LIMIT & COMMERCIALIZATION TRAP]\
      #v(2pt)
      #text(fill: rgb("881337"))[Assuming software agility can overcome immutable physical laws is the premier failure mode in Aerospace! In real-world Propulsion implementations, thermal dissipation, shot noise, and material fatigue are unforgiving.]
    ]
  )
]

#takeaways_box((
    ("Aerospace geliştirmelerinde kararlarınızı benzetmelere değil, temel fizik yasalarına (first principles) dayandırın.", "Ground all Aerospace engineering decisions in first-principles physics rather than conventional software analogies."),
    ("Donanım ve yazılımı ayrı düşünmeyin; algoritmayı fiziksel malzemenin (Propulsion) sınırlarına göre birlikte tasarlayın.", "Co-design algorithms strictly around the material and thermodynamic boundaries of Propulsion."),
    ("Laboratuvardaki küçük ölçekli başarı ile fabrikanın endüstriyel ölçeği arasındaki termodinamik farkları hesaba katın.", "Account for non-linear physical scaling anomalies when transitioning from lab bench to industrial output."),
))
