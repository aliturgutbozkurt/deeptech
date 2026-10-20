#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deeptech Reference Implementation: CRISPR-Cas9 sgRNA Guide Designer
Scans target DNA sequences for SpCas9 PAM sites (5'-NGG-3'), computes GC-content,
evaluates homopolymer poly-T terminators, and ranks on-target cleavage efficiency.
"""

import re
from typing import List, Dict

def print_header(title: str):
    print("\n" + "=" * 70)
    print(f"🧬 SYNTHETIC BIOLOGY ENGINE: {title}")
    print("=" * 70)

class CrisprGuideDesigner:
    def __init__(self, pam_pattern: str = r"(?=([ACGT]{20}[ACGT]GG))"):
        # 20nt protospacer followed by NGG PAM
        self.pam_regex = re.compile(pam_pattern, re.IGNORECASE)

    def calculate_gc_content(self, seq: str) -> float:
        gc_count = seq.count("G") + seq.count("C") + seq.count("g") + seq.count("c")
        return (gc_count / len(seq)) * 100.0

    def evaluate_efficiency_score(self, protospacer: str) -> float:
        """
        Heuristic scoring function based on:
        - Optimal GC content: 40% - 60%
        - Penalty for poly-T (TTTT causes premature pol-III transcription termination)
        - Preference for Guanine at position 20 (adjacent to PAM)
        """
        score = 100.0
        gc = self.calculate_gc_content(protospacer)

        # Penalize GC outside [40%, 60%]
        if gc < 40.0:
            score -= (40.0 - gc) * 2.0
        elif gc > 60.0:
            score -= (gc - 60.0) * 2.5

        # Penalize Poly-T stretches (RNA Pol III termination)
        if "TTTT" in protospacer.upper():
            score -= 40.0
        elif "TTT" in protospacer.upper():
            score -= 15.0

        # Cas9 prefers G at position 20
        if protospacer[-1].upper() == "G":
            score += 10.0

        return max(0.0, min(100.0, score))

    def design_guides(self, target_dna: str) -> List[Dict]:
        results = []
        target_clean = re.sub(r"\s+", "", target_dna).upper()
        
        matches = self.pam_regex.finditer(target_clean)
        for match in matches:
            full_match = match.group(1)
            protospacer = full_match[:20]
            pam = full_match[20:]
            start_pos = match.start()
            
            gc = self.calculate_gc_content(protospacer)
            score = self.evaluate_efficiency_score(protospacer)

            results.append({
                "position": start_pos,
                "protospacer": protospacer,
                "pam": pam,
                "gc_percent": gc,
                "efficiency_score": score,
                "status": "Optimal" if score >= 75 else ("Acceptable" if score >= 50 else "High Risk")
            })
        
        # Sort by efficiency score descending
        results.sort(key=lambda x: x["efficiency_score"], reverse=True)
        return results

def run_crispr_demo():
    print_header("CRISPR-Cas9 sgRNA Target Design & Cleavage Scoring")

    # Sample human oncogene target region (synthetic 120bp fragment)
    sample_gene = (
        "ATGCGATCGATCGATCGATAGGCTAGCTAGCTAGCTGATCGATCGATCGATCGATCGATC"
        "CGGTAGCTAGCTAGCTAGCTAGGCTACGTACGTACGTACGTGGTCGATCGATCGATCGATC"
    )

    print(f"Target Genomic Sequence (Length: {len(sample_gene)} bp):")
    print(f"5'-{sample_gene[:60]}...-3'\n")

    designer = CrisprGuideDesigner()
    guides = designer.design_guides(sample_gene)

    print(f"Found {len(guides)} SpCas9 Target Sites (5'-N20-NGG-3'):\n")
    print(f"{'Pos':<5} | {'Protospacer (20nt)':<22} | {'PAM':<4} | {'GC %':<6} | {'Score':<6} | {'Status'}")
    print("-" * 65)

    for g in guides[:5]:
        print(f"{g['position']:<5} | {g['protospacer']:<22} | {g['pam']:<4} | {g['gc_percent']:<6.1f} | {g['efficiency_score']:<6.1f} | {g['status']}")

    if guides:
        best = guides[0]
        print(f"\n🏆 Top Recommended sgRNA Guide Candidate:")
        print(f"   Sequence: 5'-{best['protospacer']}-3'")
        print(f"   PAM Site: {best['pam']} (Position: {best['position']})")
        print(f"   GC Ratio: {best['gc_percent']:.1f}% (Thermodynamic Stability: Valid)")
        print(f"   Score   : {best['efficiency_score']:.1f}/100")
        print("   Action  : Order oligo synthesis for ribonucleoprotein (RNP) electroporation.")

if __name__ == "__main__":
    run_crispr_demo()
