"""Create a Python-generated MATLAB-style session preview and MAT-file.

This computes the Experiment 1 examples for preview; it does not execute MATLAB.
Requires numpy, scipy, and matplotlib.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")                 # Headless file output; no GUI/Tk required.
import matplotlib.pyplot as plt
from scipy.io import savemat

exp = Path(__file__).resolve().parent.parent
results = exp / "results"
figures = exp / "figures"
results.mkdir(parents=True, exist_ok=True)
figures.mkdir(parents=True, exist_ok=True)
values = {}
lines = ["SIGNALS AND SYSTEMS LAB - EXPERIMENT 1: MATLAB BASICS", ""]

def section(title):
    lines.extend([title, "-" * len(title)])

def show(name, value):
    values[name] = value
    lines.append(f"{name} = {np.array2string(np.asarray(value), precision=6)}")

section("1. Introduction")
show("2 + 3", 2 + 3)
lines.append("Run the .m script from the MATLAB Editor with Run/F5 or by filename at >>.")

section("2. MATLAB as a calculator")
for n, v in {"8+3": 8+3, "8-3": 8-3, "8*3": 8*3, "8/3": 8/3, "2^4": 2**4,
             "2+3/4*5": 2+3/4*5, "2+3/(4*5)": 2+3/(4*5), "20/5*2": 20/5*2}.items():
    show(n, v)

section("3. Numbers and formats")
for n, v in {"integerValue": 1362, "realValue": 1.234, "complexValue": 3.21+4.3j,
             "infinityValue": np.inf, "nanValue": np.nan}.items(): show(n, v)
lines.append("format short / long / bank changes display, not numeric precision.")

section("4. Variables and ans")
show("ans after 7+5", 12); show("namedValue", 10); show("namedValuePlusFive", 15)
lines.append("Legal: NetCost, Left2Pay, sample_value. Illegal examples are commented in the .m file.")

section("5. Suppressing output")
show("semicolon assignments [hidden first second third]", [42, 2, 3, 5])
lines.append("Semicolons suppress automatic display; multiple statements can share a line.")

section("6. Built-in functions")
theta = np.pi/6; z = 3+4j
funcs = {"sinReal": np.sin(theta), "cosReal": np.cos(theta), "tanReal": np.tan(theta),
         "asinReal": np.arcsin(.5), "acosReal": np.arccos(.5), "atanReal": np.arctan(1),
         "sqrtReal": np.sqrt(9), "expReal": np.exp(1), "logReal": np.log(np.exp(2)),
         "log10Real": np.log10(1000), "absReal": abs(-7), "z": z, "absComplex": abs(z),
         "angleComplex": np.angle(z), "realComplex": z.real, "imagComplex": z.imag,
         "conjComplex": np.conj(z), "sqrtComplex": np.sqrt(-1+0j), "expComplex": np.exp(1+1j),
         "logComplex": np.log(-1+0j), "sinComplex": np.sin(1+1j), "cosComplex": np.cos(1+1j),
         "tanComplex": np.tan(1+1j), "asinComplex": np.arcsin(2+0j),
         "acosComplex": np.arccos(2+0j), "atanComplex": np.arctan(1+1j)}
for n, v in funcs.items(): show(n, v)

section("7. Vectors, colon notation, extraction, transpose")
row = np.array([1, 2, 3, 4]); other = np.array([10, 20, 30, 40]); col = row[:, None]
for n, v in {"rowVector": row, "rowSum": row+other, "scalarTimesRow": 3*row,
             "thirdElement": row[2], "columnVector": col, "columnSum": col+other[:, None],
             "scalarTimesColumn": 2*col, "secondElement": col[1, 0], "1:5": np.arange(1,6),
             "2:2:10": np.arange(2,11,2), "5:-1:1": np.arange(5,0,-1),
             "subvector positions 2:4": row[1:4], "alternate positions 1:2:4": row[::2],
             "complexRow": np.array([1+3j, 2-2j]),
             "complexConjugateTranspose": np.conj([1+3j, 2-2j]).reshape(-1,1),
             "complexPlainTranspose": np.array([1+3j, 2-2j]).reshape(-1,1)}.items(): show(n, v)

section("8. Keeping a record")
lines.append("who / whos list saved workspace variables; load restores the MAT-file values.")

section("9. Exercises")
y1 = 2*np.cos(np.exp(1-4j))
show("Exercise 1.1 y", y1); show("Exercise 1.1 magnitude", abs(y1)); show("Exercise 1.1 phase (radians)", np.angle(y1))
show("Exercise 1.2 photo polynomial at x=2", 5*2**3+2*2**2+9*2+16)  # 82
show("Exercise 1.2 typed expression at x=2", 5*2+2*2+9*2+16)         # 48
v = np.array([2+3, 4]); show("Exercise 1.3 v", v); show("Exercise 1.3 v1", v); show("Exercise 1.3 sum", v+v)
lines.append("Photo Exercise 1.2 includes x^3 and x^2; typed version omits those powers.")
lines.append("Photo Exercise 1.3 spacing may instead mean vectors of unequal lengths; see .m comments.")

text = "\n".join(lines) + "\n"
(results / "session.txt").write_text(text, encoding="utf-8")
savemat(results / "variables.mat", values, do_compression=True)
fig, ax = plt.subplots(figsize=(15, max(9, len(lines)*0.22)), dpi=120)
fig.patch.set_facecolor("#101820"); ax.set_facecolor("#101820"); ax.axis("off")
ax.text(.015, .99, text, va="top", ha="left", family="DejaVu Sans Mono", fontsize=9,
        color="#e8f1f2", transform=ax.transAxes, linespacing=1.35)
fig.savefig(figures / "session_preview.png", facecolor=fig.get_facecolor(), bbox_inches="tight")
plt.close(fig)
print(f"Generated results in {results} and figures in {figures}")
