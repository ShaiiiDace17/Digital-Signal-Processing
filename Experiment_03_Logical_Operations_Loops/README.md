# Experiment 3 — Logical Operations and Loops

Signals and Systems lab covering element-wise logical tests, logical masking,
`for` loop plots, and the Fibonacci sequence.

## Contents

| File | Location | Purpose |
|------|----------|---------|
| `generate_all.py` | `code/` | Python/NumPy generator for the results and figures. |
| `logical_operations_results.txt` | `results/` | Matrix logical tests and masked positive values. |
| `fibonacci_results.txt` | `results/` | First 20 Fibonacci terms. |
| `logical_masked_sine.png` | `figures/` | Original sine and its nonnegative mask. |
| `loop_sine_n1_to_8.png` | `figures/` | `sin(n pi x)` for n = 1,...,8 in a 4-by-2 subplot. |
| `loop_sine_cosine_odd_n.png` | `figures/` | Sine and cosine plots for n = 1,3,5,7. |
| `fibonacci_ratios.png` | `figures/` | Successive Fibonacci ratios and the golden ratio. |

## How to run

```powershell
python "Experiment_03_Logical_Operations_Loops\code\generate_all.py"
```

Requires `numpy` and `matplotlib`. The outputs were generated with Python to
mimic MATLAB results; they were not produced by running MATLAB itself.
