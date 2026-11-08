# Experiment 2 — Plotting, Vectors, and Matrices

Signals and Systems lab covering elementary-function plotting, vector
operations, matrix operations, and the end-of-chapter exercises.

## Contents

| File | Location | Purpose |
|------|----------|---------|
| `generate_all.py` | `code/` | Python/NumPy generator that creates all figures and result logs (writes `results/` and `figures/`). |
| `section2_vectors_results.txt` | `results/` | Vector calculations: dot/scalar products, element-wise products/division, powers, dimension errors. |
| `section3_matrices_results.txt` | `results/` | Matrix calculations: sizes, transpose, concatenation, indexing, element-wise vs matrix products, `spy(K)`. |
| `p12_*`, `p13_*`, `p14_*`, `p15_*` | `figures/01_plotting/` | Plotting elementary functions: line styles, colors, `hold`, labeled axes, `subplot`. |
| `p17_example2_1.png` | `figures/02_vectors/` | Example 2.1 vector plot, `y = x sin(pi x)`. |
| `p21_spy_K.png` | `figures/03_matrices/` | `spy(K)` visualization of non-zero matrix entries. |
| `p23_*`, `p24_*` | `figures/04_exercises/` | Exercise plots: `x(t)`, `cos(x)=x` intersection/zoom, and Exercise 3 parts i–iv plus a combined 2x2. |

## How to run

```powershell
python "Experiment_02_Plots_Vectors_Matrices\code\generate_all.py"
```

Requires `numpy`, `scipy`, and `matplotlib`. It recreates `results/` and
`figures/` in place.

## Note

These outputs were generated with Python/NumPy/Matplotlib to mimic MATLAB
results; they were not produced by running MATLAB itself.
