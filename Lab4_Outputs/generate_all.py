"""Generate Lab 4 graphs, sampled-data CSVs, observations, and manifest."""
from pathlib import Path
import csv
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import pi

ROOT = Path(__file__).resolve().parent
GRAPHS, TABLES = ROOT / "graphs", ROOT / "tables"
GRAPHS.mkdir(parents=True, exist_ok=True)
TABLES.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"figure.figsize": (8, 5), "figure.dpi": 200, "savefig.dpi": 200})
manifest, observations = [], []


def record(label, stem, title, x, curves, xlabel, ylabel, obs, draw="plot", ylim=None, xlim=None):
    x = np.asarray(x, dtype=float)
    curves = {name: np.asarray(v, dtype=float) for name, v in curves.items()}
    csvname, pngname = stem + ".csv", stem + ".png"
    with (TABLES / csvname).open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([xlabel, *curves.keys()])
        for i, xv in enumerate(x):
            w.writerow([f"{xv:.10g}", *[f"{v[i]:.10g}" if np.isfinite(v[i]) else "" for v in curves.values()]])
    fig, ax = plt.subplots(figsize=(8, 5), dpi=200)
    for name, values in curves.items():
        if draw == "step":
            ax.step(x, values, where="post", label=name)
        else:
            ax.plot(x, values, label=name)
    ax.set_title(f"{label}: {title}")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    if len(curves) > 1:
        ax.legend()
    if ylim:
        ax.set_ylim(*ylim)
    if xlim:
        ax.set_xlim(*xlim)
    fig.tight_layout()
    fig.savefig(GRAPHS / pngname, dpi=200)
    plt.close(fig)
    caption = f"{label}: {title}."
    manifest.extend([
        {"task": label, "type": "graph", "file": f"graphs/{pngname}", "caption": caption, "observation": obs},
        {"task": label, "type": "table", "file": f"tables/{csvname}", "caption": f"Sampled values for {label}.", "observation": obs},
    ])
    observations.append(f"### {label}\n\n{obs}")


# Page 32: cfstep(5,0), with 0.01-second spacing on -5 < t <= 5.
t = np.arange(-5 + .01, 5.0001, .01)
u = (t >= 0).astype(float)
record("p32 Unit Step Function", "p32_unit_step", "Unit step u(t)", t, {"u(t)": u}, "Time (s)", "u(t)",
       f"The step is zero before 0 s and one from 0 s onward. The sampled range is {u.min():.0f} to {u.max():.0f}. The transition occurs at t=0 s.", "step", (-.15, 1.15))

# Page 33, 2.1: four sinusoidal examples, A=1, f=1 Hz.
t = np.arange(0, 1.0001, .01)
record("p33 2.1 Sinusoidal Signal", "p33_sinusoidal_examples", "1 Hz phase examples", t,
       {"cos(2 pi t)": np.cos(2*pi*t), "cos(2 pi t + pi/2)": np.cos(2*pi*t+pi/2),
        "cos(2 pi t - pi/2)": np.cos(2*pi*t-pi/2), "sin(2 pi t)": np.sin(2*pi*t)},
       "Time (s)", "Amplitude",
       "All four curves have unit amplitude and one cycle over one second. The cosine curves shifted by plus or minus pi/2 align with the sine curve or its negative. Their common period is 1 s.", ylim=(-1.15, 1.15))

# Page 33, 2.2(i): h(t) = 1 on [-1,0], -1 on (0,2].
t = np.arange(-1, 2.0001, .01)
h = np.where((t >= -1) & (t <= 0), 1., np.where((t > 0) & (t <= 2), -1., 0.))
record("p33 2.2(i) Piecewise h(t)", "p33_piecewise_h", "Piecewise signal h(t)", t, {"h(t)": h}, "Time (s)", "h(t)",
       "The signal equals 1 on -1<=t<=0 and -1 on 0<t<=2. It changes level at t=0 and is zero outside the defined intervals. The plotted interval follows the manual definition.", "step", (-1.25, 1.25))

# Page 33, 2.2(ii): x(t)=e^t on [-1,0], e^-t on (0,1].
t = np.arange(-1, 1.0001, .01)
xexp = np.where(t <= 0, np.exp(t), np.exp(-t))
record("p33 2.2(ii) Piecewise Exponential", "p33_piecewise_exponential", "Piecewise exponential x(t)", t, {"x(t)": xexp}, "Time (s)", "x(t)",
       f"The branches meet at x(0)={xexp[len(xexp)//2]:.0f}. The signal is symmetric about t=0 and decreases toward both endpoints. Its endpoint values are approximately {xexp[0]:.4f}.", ylim=(0, 1.1))

# Page 33, 2.2(iii): sin(x), x^2, and 1/x branches.
t = np.arange(-5, 5.0001, .01)
fp = np.empty_like(t)
mneg, mquad, mrecip = t < 0, (t >= 0) & (t <= 1), t > 1
fp[mneg], fp[mquad], fp[mrecip] = np.sin(t[mneg]), t[mquad]**2, 1/t[mrecip]
record("p33 2.2(iii) Piecewise f(x)", "p33_piecewise_f", "Piecewise signal f(x)", t, {"f(x)": fp}, "x", "f(x)",
       f"For x<0 the sine branch ranges from {fp[mneg].min():.4f} to {fp[mneg].max():.4f} on the plotted interval. The quadratic branch rises from 0 to 1 on [0,1]. For x>1 the reciprocal branch decreases toward zero.", ylim=(-1.2, 1.2))

# Page 34, 2.2(iv): sketch only; its expression is unreadable (details in notes.md).
t = np.arange(0, 5.0001, .01)
pulse = ((t >= 2) & (t < 4)).astype(float)
record("p34 2.2(iv) Rectangular Pulse", "p34_rectangular_pulse", "Rectangular pulse from the step function", t,
       {"x(t) (sketch transcription)": pulse}, "Time (s)", "x(t)",
       "The visible sketch shows a pulse beginning at 2 s and ending at 4 s. This plot transcribes its apparent unit height; the manual does not show a readable analytic expression. See notes.md for the source limitation.", "step", (-.15, 1.2), (0, 5))

# Page 34, 2.3: angle is 60 degrees = pi/3 radians.
t = np.arange(0, 4.0001, .001)
env = 4*np.exp(-2*t)
fd = env*np.cos(6*t-pi/3)
record("p34 2.3 Exponentially Varying Sinusoid", "p34_damped_sinusoid", "Damped sinusoid and envelopes", t,
       {"f(t)": fd, "+4 exp(-2t)": env, "-4 exp(-2t)": -env}, "Time (s)", "Amplitude",
       f"The oscillation is bounded by envelopes that decay from +/-4 at t=0 to +/-{env[-1]:.6f} at t=4 s. Its angular frequency remains 6 rad/s while the amplitude decays. The phase offset of 60 degrees is converted to pi/3 radians.", ylim=(-4.2, 4.2))

# Page 34, 2.4: V(t)=Y(t) cos(30t).
t = np.arange(-5, 10.0001, .001)
Y = np.where(t <= 0, 2*np.exp(t), 2-t)
W = np.cos(30*t)
record("p34 2.4 Multiplication of Two Signals", "p34_signal_product", "Y(t) and V(t)=Y(t)W(t)", t,
       {"Y(t)": Y, "V(t)=Y(t) cos(30t)": Y*W}, "Time (s)", "Amplitude",
       f"At t=0 both branches of Y(t) equal {Y[np.argmin(abs(t))]:.0f}. The negative-time exponential approaches 2, and the positive-time branch decreases linearly to {Y[-1]:.0f} at 10 s. Multiplication by cos(30t) produces rapid oscillations bounded by |Y(t)|.", ylim=(-10, 10))

# Page 35, 3.1.1: unit step delayed by two seconds.
t = np.arange(-5, 6.0001, .01)
record("p35 3.1.1 Time Shift", "p35_shifted_unit_step", "u(t-2)", t, {"u(t-2)": (t >= 2).astype(float)}, "Time (s)", "x(t)",
       "The shifted unit step is zero until t=2 s and one afterward. Its transition is delayed by 2 s relative to u(t). The amplitude and shape are unchanged.", "step", (-.15, 1.15))

# Page 35, 3.1.2: cos(pi*t) on [-.5,.5], shifted right by .5.
t = np.arange(-.5, 1.0001, .005)
orig = np.where((t >= -.5) & (t <= .5), np.cos(pi*t), np.nan)
delayed = np.where((t >= 0) & (t <= 1), np.cos(pi*(t-.5)), np.nan)
record("p35 3.1.2 Time Shift", "p35_shifted_cosine", "cosine shifted right by 0.5 s", t,
       {"x(t)": orig, "x(t-0.5)": delayed}, "Time (s)", "x(t)",
       "The original cosine is supported on [-0.5,0.5] and peaks at t=0. The delayed curve has the same shape and peaks at t=0.5. The shift moves its features 0.5 s to the right without changing amplitude.", ylim=(-.1, 1.1))

# Page 35, 3.1.3: triangle read from the diagram, shifted right by 2.
t = np.arange(0, 6.0001, .005)
tri = np.where((t >= 0) & (t <= 2), t, np.where((t > 2) & (t <= 3), 2*(3-t), 0.))
tri2 = np.where((t >= 2) & (t <= 4), t-2, np.where((t > 4) & (t <= 5), 2*(5-t), 0.))
record("p35 3.1.3 Time Shift", "p35_shifted_triangle", "triangular signal shifted right by 2 s", t,
       {"original f(t)": tri, "shifted f(t-2)": tri2}, "Time (s)", "f(t)",
       "The diagram's triangle rises from (0,0) to (2,2), then falls to (3,0). The shifted curve retains its peak height and moves the peak to t=4. Its support moves from [0,3] to [2,5].", ylim=(-.1, 2.2))

# Page 36, 3.2: time scaling of x(t)=cos(pi*t), specified on [-.5,.5].
t = np.arange(-1, 1.0001, .0025)
base = np.where(abs(t) <= .5, np.cos(pi*t), np.nan)
compressed = np.where(abs(2*t) <= .5, np.cos(pi*2*t), np.nan)
expanded = np.where(abs(t/2) <= .5, np.cos(pi*t/2), np.nan)
record("p36 3.2 Time Scaling", "p36_time_scaling", "x(t), x(2t), and x(t/2)", t,
       {"x(t)": base, "x(2t)": compressed, "x(t/2)": expanded}, "Time (s)", "x(t)",
       "The original cosine is supported on [-0.5,0.5]. The x(2t) version is compressed to [-0.25,0.25], while x(t/2) expands to [-1,1]. All preserve the peak amplitude of 1 at t=0.", ylim=(-.1, 1.1))

# Page 37, 3.3: invert f(t)=exp(t/2) on [-5,-1].
t = np.arange(-5, 5.0001, .005)
f0 = np.where((t >= -5) & (t <= -1), np.exp(t/2), np.nan)
f1 = np.where((t >= 1) & (t <= 5), np.exp(-t/2), np.nan)
record("p37 3.3 Time Inversion", "p37_time_inversion", "f(t) and f(-t)", t, {"f(t)": f0, "f(-t)": f1}, "Time (s)", "f(t)",
       f"The original exponential rises from {np.exp(-2.5):.4f} at -5 s to {np.exp(-.5):.4f} at -1 s. Time inversion reflects it onto [1,5], where it is exp(-t/2). The reflected curve has the same values in reverse time order.", ylim=(0, .7))

# Page 38, exercise (a) and operations (b)(i)-(iii).
def exercise_x(s):
    s = np.asarray(s, dtype=float)
    return np.where(s < -4, 0., np.where(s <= 3, s+2, s-2))

t = np.arange(-8, 8.0001, .005)
record("p38 Exercise (a) Piecewise Signal", "p38_ex_a_piecewise", "defined piecewise x(t)", t, {"x(t)": exercise_x(t)}, "Time (s)", "x(t)",
       "The signal is zero for t<-4, equals t+2 on [-4,3], and equals t-2 for t>3. At -4 it takes the middle-branch value -2, and at 3 it takes value 5. The right branch starts just after 3 near 1, so there is a jump there.", "step", (-3, 6))

t = np.arange(-8, 10.0001, .005)
record("p38 Exercise (b)(i) x(t-1)", "p38_ex_b_i_shift", "time-shifted x(t-1)", t, {"x(t-1)": exercise_x(t-1)}, "Time (s)", "x(t)",
       "The transformation x(t-1) delays the signal by 1 time unit. Its breakpoints move from -4 and 3 to -3 and 4. The branch values are those of x evaluated one unit earlier.", "step", (-3, 7))

t = np.arange(-20, 20.0001, .01)
record("p38 Exercise (b)(ii) x(t/3)", "p38_ex_b_ii_scale", "time-expanded x(t/3)", t, {"x(t/3)": exercise_x(t/3)}, "Time (s)", "x(t)",
       "The transformation x(t/3) expands the time axis by a factor of 3. Its breakpoints move to -12 and 9. The branch values are evaluated at one-third of the plotted time.", "step", (-3, 10))

t = np.arange(-10, 10.0001, .005)
record("p38 Exercise (b)(iii) x(-t)", "p38_ex_b_iii_inversion", "time-inverted x(-t)", t, {"x(-t)": exercise_x(-t)}, "Time (s)", "x(t)",
       "Time inversion reflects the piecewise signal across t=0. The original breakpoints -4 and 3 appear at 4 and -3. The values are obtained by evaluating x at the negative of the plotted time.", "step", (-3, 8))

(ROOT / "observations.md").write_text("# Laboratory Experiment 4 — Observations\n\n" + "\n\n".join(observations) + "\n", encoding="utf-8")
(ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
