from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent.parent
FIG = ROOT / "figures"
RES = ROOT / "results"
FIG.mkdir(parents=True, exist_ok=True)
RES.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"figure.figsize": (8, 5), "figure.dpi": 200, "savefig.dpi": 200})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(FIG / name, dpi=200)
    plt.close(fig)


def axes(ax, title, xlabel="x", ylabel="y"):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)


def fmt(a):
    arr = np.asarray(a)
    if arr.dtype == bool:
        arr = arr.astype(int)
    return np.array2string(arr, separator=" ", precision=6, suppress_small=True)


# Logical operations from the lab handout.
xmat = np.array([[-2, np.pi, 5], [-5, -3, -1]])
y = xmat >= -1
logical = [
    ("x >= -1", y),
    ("x > y (with y = x >= -1)", xmat > y),
    ("x > 3 & x < 4", (xmat > 3) & (xmat < 4)),
    ("x > 3 | x == -3", (xmat > 3) | (xmat == -3)),
    ("x > 3 | x == -3 | x <= -5", (xmat > 3) | (xmat == -3) | (xmat <= -5)),
    ("L = x >= 0", xmat >= 0),
    ("pos = x .* L", xmat * (xmat >= 0)),
]
rows = ["Signals and Systems Lab — Experiment #3", "Section 1: Logical operations", "", "x =", fmt(xmat), ""]
for label, value in logical:
    rows.extend((f"{label}:", fmt(value), ""))
(RES / "logical_operations_results.txt").write_text("\n".join(rows), encoding="utf-8")

x = np.arange(0, 6.0001, 0.05)
signal = np.sin(np.pi * x)
positive = (signal >= 0) * signal
fig, ax = plt.subplots()
ax.plot(x, signal, ":", label="y = sin(pi x)")
ax.plot(x, positive, "-", label="Y = (y >= 0) .* y")
axes(ax, "Logical mask: positive half cycles", "x", "Amplitude")
ax.legend()
save(fig, "logical_masked_sine.png")

# Loop subplot examples.
xloop = np.arange(-1, 1.0001, 0.05)
fig, axs = plt.subplots(4, 2)
for n in range(1, 9):
    ax = axs.flat[n - 1]
    ax.plot(xloop, np.sin(n * np.pi * xloop))
    axes(ax, f"n = {n}", "x", "sin(n pi x)")
save(fig, "loop_sine_n1_to_8.png")

fig, axs = plt.subplots(4, 2)
for i, n in enumerate(range(1, 9, 2)):
    ax_sin, ax_cos = axs.flat[2 * i], axs.flat[2 * i + 1]
    ax_sin.plot(xloop, np.sin(n * np.pi * xloop), label=f"sin({n} pi x)")
    axes(ax_sin, f"Sine, n = {n}", "x", "Amplitude")
    ax_sin.legend(fontsize=7)
    ax_cos.plot(xloop, np.cos(n * np.pi * xloop), label=f"cos({n} pi x)")
    axes(ax_cos, f"Cosine, n = {n}", "x", "Amplitude")
    ax_cos.legend(fontsize=7)
save(fig, "loop_sine_cosine_odd_n.png")

# First 20 Fibonacci terms, using the handout's F(1)=0, F(2)=1 convention.
f = [0, 1]
for _ in range(2, 20):
    f.append(f[-1] + f[-2])
with np.errstate(divide="ignore", invalid="ignore"):
    ratios = np.array(f[1:], dtype=float) / np.array(f[:-1], dtype=float)
ratios[0] = np.nan  # F(2)/F(1) is undefined.
(RES / "fibonacci_results.txt").write_text(
    "Signals and Systems Lab — Experiment #3\nSection 2: Fibonacci sequence\n\n"
    + "Term   Fibonacci value\n"
    + "".join(f"{i:>4}   {value}\n" for i, value in enumerate(f, start=1)),
    encoding="utf-8",
)
fig, ax = plt.subplots()
ax.plot(np.arange(1, 20), ratios, "o", label="F(n+1) / F(n)")
golden = (np.sqrt(5) + 1) / 2
ax.plot(np.arange(0, 20), np.full(20, golden), "--", label="Golden ratio")
axes(ax, "Fibonacci ratios approach the golden ratio", "n", "Ratio")
ax.legend()
save(fig, "fibonacci_ratios.png")
