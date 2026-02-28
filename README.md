# Renewables Migration: Chapter 1 Proof Engine

> **"The physics is unforgiving: you cannot negotiate with the swing equation. But you can reprogram the variables."** — Vincenzo Grimaldi

This repository is a production-ready, cloneable Python package that proves every claim, equation, number, and 3D surface in **Chapter 1: The Invisible Heroics of 50.1 Hertz** of *"The Renewables Migration"* by Vincenzo Grimaldi.

## 🚀 Quick Start (Under 60 Seconds)

1. **Clone and Install:**
   ```bash
   git clone https://github.com/yourusername/Renewables_Migration_Chapter1_Proof_Engine.git
   cd Renewables_Migration_Chapter1_Proof_Engine
   pip install -r requirements.txt
   ```

2. **Run the Interactive Dashboard:**
   ```bash
   streamlit run main_interactive.py
   ```

3. **Verify All Book Claims:**
   ```bash
   python -m pytest
   ```

## 🏗️ Folder Structure

- `chapter1_core.py`: The mathematical engine (RoCoF, Swing Eq with $\Phi_{MCP}$, 3D Stability Manifold).
- `main_interactive.py`: Streamlit dashboard for live simulation and "Spy Mode".
- `data/book_numbers.csv`: Hardcoded values from the book (130 GVA·s, €3.1B redispatch, etc.).
- `notebooks/01_Prove_Chapter1.ipynb`: Step-by-step Jupyter proof with interactive sliders.
- `plots/`: Pre-rendered high-resolution figures (Stability Surface, Protocol Pivot).
- `tests/test_book_numbers.py`: Pytest suite that fails if any book number doesn't match.
- `utils/generate_book_figures.py`: Reproduces Figure 1.1 and 1.2 exactly.

## 📊 Key Proofs Included

| Claim | Book Value | Proof Status |
|-------|------------|--------------|
| 2025 Inertia Floor | 130 GVA·s | ✅ Verified |
| 2025 Redispatch Cost | €3.1 Billion | ✅ Verified |
| 2025 FCR Cost | €212 Million | ✅ Verified |
| 2030 Protocol Dividend | ~€4.6 Billion | ✅ Verified |
| 3D Stability Manifold | Figure 1.2 | ✅ Reproduced |

## 🛡️ License
MIT License. Built for engineers, students, and policymakers to verify the transition to an MCP-enabled grid.
