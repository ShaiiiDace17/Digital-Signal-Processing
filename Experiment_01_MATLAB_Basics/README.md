# Experiment 1 — MATLAB Basics

Signals and Systems lab covering the MATLAB environment: arithmetic and operator
precedence, numeric formats, variables and `ans`, suppressing output, built-in
math/trig/complex functions, vectors and colon notation, extraction, transpose,
saving a workspace, and the chapter exercises.

## Contents

| File | Location | Purpose |
|------|----------|---------|
| `matlab_basics_demo.m` | `code/` | Full MATLAB script for every section and exercise. Run in MATLAB (F5 or type the name at `>>`). It writes `session.txt` and `variables.mat` into `lab_outputs`. |
| `generate_lab_outputs.py` | `code/` | Python/NumPy generator that reproduces the same values as a preview (writes `results/` and `figures/`). |
| `session.txt` | `results/` | Command-Window style log of all Experiment 1 sections and exercises. |
| `variables.mat` | `results/` | Saved workspace variables (MAT-file) for the run. |
| `session_preview.png` | `figures/` | Image rendering of `session.txt` for quick viewing. |

## How to run

- **Real MATLAB:** open `code/matlab_basics_demo.m` and press Run/F5.
- **Preview (no MATLAB):**
  ```powershell
  python "Experiment_01_MATLAB_Basics\code\generate_lab_outputs.py"
  ```

## Note

The `.txt`, `.mat`, and `.png` here were generated with Python/NumPy to mimic
MATLAB output, not by MATLAB itself. Run the `.m` file in MATLAB for an authentic
session log.
