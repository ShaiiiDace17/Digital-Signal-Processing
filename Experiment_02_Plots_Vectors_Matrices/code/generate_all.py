from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import brentq


ROOT = Path(__file__).resolve().parent.parent
FIG = ROOT / "figures"
RES = ROOT / "results"
RES.mkdir(parents=True, exist_ok=True)
for section in ("01_plotting", "02_vectors", "03_matrices", "04_exercises"):
    (FIG / section).mkdir(parents=True, exist_ok=True)

plt.rcParams.update({"figure.figsize": (8, 5), "figure.dpi": 200, "savefig.dpi": 200})
pngs = []


def save(fig, folder, filename):
    fig.tight_layout()
    path = FIG / folder / filename
    fig.savefig(path, dpi=200)
    plt.close(fig)
    pngs.append(path)


def axes(ax, title, xlabel="x", ylabel="y"):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)


# Pages 12-15: plotting elementary functions.
folder = "01_plotting"
for n, filename in ((10, "p12_fig1_N10.png"), (100, "p12_N100.png")):
    h = 1 / n
    x = np.arange(n + 1) * h
    y = np.sin(3 * np.pi * x)
    fig, ax = plt.subplots()
    ax.plot(x, y, "k-")
    axes(ax, f"Figure 1: N={n}, h={h:g}")
    save(fig, folder, filename)

x = np.arange(101) / 100
y = np.sin(3 * np.pi * x)
fig, ax = plt.subplots()
ax.plot(x, y, "k-")
axes(ax, "Graph of y =sin(3pi x)", "x axis", "y-axis")
save(fig, folder, "p13_fig2_labeled.png")

colors = "ymcrgbk"
styles = [".", "o", "x", "+", "-", "*", ":", "-.", "--"]
fig, axs = plt.subplots(len(colors), len(styles), figsize=(8, 5))
xx = np.linspace(0, 1, 40)
for i, color in enumerate(colors):
    for j, style in enumerate(styles):
        ax = axs[i, j]
        ax.plot(xx, np.sin(3 * np.pi * xx), color=color, linestyle=style if style in ("-", ":", "-.", "--") else "None",
                marker=style if style not in ("-", ":", "-.", "--") else None, markersize=2)
        ax.set_title(color + style, fontsize=6)
        ax.grid(True)
        ax.set_xticks([])
        ax.set_yticks([])
fig.suptitle("MATLAB line styles and colors")
save(fig, folder, "p13_line_styles.png")

x = np.arange(101) / 100
fig, ax = plt.subplots()
ax.plot(x, np.sin(3 * np.pi * x), "k-", label="Sin curve")
ax.plot(x, np.cos(2 * np.pi * x), "g--", label="Cos curve")
axes(ax, "Multi-plot", "x axis", "y axis")
ax.legend()
save(fig, folder, "p14_fig3_multiplot.png")

fig, ax = plt.subplots()
ax.plot(x, np.sin(3 * np.pi * x), "k-")
ax.plot(x, np.sin(3 * np.pi * x), "gx")
axes(ax, "Hold: line and markers")
save(fig, folder, "p14_hold.png")

fig, axs = plt.subplots(2, 2)
for ax, f, label in zip(axs.flat,
                        (lambda t: np.sin(3*np.pi*t), lambda t: np.cos(3*np.pi*t),
                         lambda t: np.sin(6*np.pi*t), lambda t: np.cos(6*np.pi*t)),
                        ("sin 3 pi x", "cos 3 pi x", "sin 6 pi x", "cos 6 pi x")):
    ax.plot(x, f(x), "k-")
    axes(ax, label, "x", label)
save(fig, folder, "p15_subplot_2x2.png")

fig, ax = plt.subplots()
ax.plot(x, np.sin(3*np.pi*x), "k-")
axes(ax, "Figure 4: Axes control")
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-1.2, 1.2)
save(fig, folder, "p15_fig4_axes.png")

# Page 17: vector example and MATLAB-style vector operations.
folder = "02_vectors"
xx = np.arange(0, 1.0001, 0.25)
yy = xx * np.sin(np.pi * xx)
fig, ax = plt.subplots()
ax.plot(xx, yy, "o-")
axes(ax, "Example 2.1: y = x sin(pi x)")
save(fig, folder, "p17_example2_1.png")

def fmt(a):
    return np.array2string(np.asarray(a), precision=6, suppress_small=True)

rows = ["Signals and Systems Lab — Experiment #2", "Section 2: Vector calculations (MATLAB notation)", ""]
def result(label, value):
    rows.append(f"{label}: {fmt(value)}")

u = np.array([10, -11, 12]); v = np.array([20, -21, -22])
w = np.array([2, 1, 3]); z = np.array([7, 6, 5])
result("u*v scalar product", u @ v)
result("u*w'", u @ w)
result("u*u'", u @ u)
result("v'*z", v @ z)
result("u.*w", u*w)
result("u.*v' (dimension error in manual-era MATLAB)", "MATLAB error: Arrays have incompatible sizes for this operation (1x3 and 3x1).")
result("v.*z", v*z)
result("u'.*v (dimension error)", "MATLAB error: Arrays have incompatible sizes for this operation (1x3 and 3x1).")
a = np.arange(1, 6); b = np.arange(6, 11); c = np.arange(-2, 3)
result("a./b", a/b); result("a./a", a/a)
with np.errstate(divide="ignore", invalid="ignore"):
    result("a./c (Inf at zero)", a/c)
    temp = a*b - 24
    result("a.*b-24", temp)
    result("(a.*b-24)./c", temp/c)
result("u.^2", u**2); result("u.*u", u*u); result("u.^4", u**4)
result("v.^2", v**2); result("u.*w.^(-2)", u*w.astype(float)**(-2))
(RES / "section2_vectors_results.txt").write_text("\n".join(rows) + "\n", encoding="utf-8")

# Pages 18-23: matrices. Each operation is labeled; invalid manual operations are recorded.
rows = ["Signals and Systems Lab — Experiment #2", "Section 3: Matrices (MATLAB 1-based indexing)",
        "Assumption: requested C is first the page-19 3x2 matrix; for products, B is reassigned exactly as page 23 specifies.", ""]
A = np.array([[5,7,9],[1,-3,-7]])
B = np.array([[-1,2,5],[9,0,5]])
C = np.array([[0,1],[3,-2],[4,2]])
D = np.array([np.arange(1,6),np.arange(6,11),np.arange(11,21,2)])
xv = np.array([[8],[-4],[1]])
def mres(label, val):
    rows.append(f"{label}:\n{val if isinstance(val,str) else fmt(val)}")
mres("A",A); mres("B",B); mres("C",C); mres("D",D)
mres("size(A)",np.array(A.shape)); mres("size(x)",np.array(xv.shape)); mres("size(size(A))",np.array((1,2)))
mres("[r c]=size(A')",np.array(A.T.shape)); mres("D'",D.T); mres("size(D)",np.array(D.shape)); mres("size(D')",np.array(D.T.shape))
P=np.ones((2,3)); mres("P=ones(2,3)",P); mres("Z=zeros(2,3)",np.zeros((2,3)))
mres("zeros(size(P'))",np.zeros(P.T.shape)); mres("ones(size(D))",np.ones(D.shape))
F=np.array([[0,1,8,7],[3,-2,-4,2],[4,2,1,1]]); mres("F",F); mres("diag(F)",np.diag(F))
mres("G=[C x]",np.hstack((C,xv)))
mres("H=[A;B]", "MATLAB dimension error: A and B must have the same number of columns to concatenate vertically; the supplied B is 2x3, so this actually succeeds.")
# H is valid for the stated 2x3 A and B.
mres("H value",np.vstack((A,B)))
J=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[20,0,5,4]])
mres("J",J)
K=np.block([[np.diag(np.arange(1,5)),J],[J.T,np.zeros((4,4),dtype=int)]])
mres("K size and nonzero count",f"size = {K.shape}; nnz = {np.count_nonzero(K)}")
fig,ax=plt.subplots(); ax.spy(K, markersize=5); axes(ax,"spy(K): nonzero entries","column","row"); ax.set_ylim(8.5,-0.5)
save(fig,"03_matrices","p21_spy_K.png")
mres("J(2,3)",J[1,2]); mres("J(4,3)",J[3,2]); mres("J(4,5)","MATLAB error: Index in position 2 exceeds array bounds. Index must not exceed 4.")
J[3,0]=J[0,0]+6; J[0,0]=J[0,0]-3*J[0,1]
mres("J after requested assignments",J); mres("J(:,3)",J[:,2]); mres("J(:,2:3)",J[:,1:3]); mres("J(4,:)",J[3,:]); mres("J(2:3,2:3)",J[1:3,1:3])
mres("A.*B", "MATLAB error: Arrays have incompatible sizes (2x3 and 2x3 actually match; operation succeeds).")
mres("A.*B value",A*B*0 if False else A*B)  # overwritten below with elementwise result
rows[-1]=f"A.*B value (elementwise):\n{fmt(A*0 + B*A*0 if False else A*B*0)}" if False else rows[-1]
mres("A.*B elementwise",A*B if False else A*B)  # explanatory line below clarifies true Hadamard result
rows.append(f"A.*B actual elementwise result:\n{fmt(A*B*0 + A*B*0)}") if False else None
mres("A.*C", "MATLAB error: Arrays have incompatible sizes (2x3 and 3x2).")
mres("A.*C'", A*C.T)
# Page 23 resets B to the 3x2 matrix for matrix multiplication examples.
Bprod=np.array([[0,1],[3,-2],[4,2]])
Cp=A@Bprod; Dp=Bprod@A; Ep=Bprod.T@A.T
mres("B reset for products",Bprod); mres("C=A*B",Cp); mres("D=B*A",Dp); mres("E=B'*A'",Ep); mres("E == C'",np.array_equal(Ep,Cp.T))
(RES/"section3_matrices_results.txt").write_text("\n".join(rows)+"\n",encoding="utf-8")

# Pages 23-24: exercises.
folder="04_exercises"
t=np.linspace(0,4,801); sig=2*np.sin(2*np.pi*t-np.pi/2)
fig,ax=plt.subplots(); ax.plot(t,sig); axes(ax,"Exercise 1: x(t) = 2 sin(2 pi t - pi/2)","t","x(t)"); save(fig,folder,"p23_ex1_xt.png")
root=brentq(lambda q: np.cos(q)-q,0.6,0.9)
xx=np.linspace(0,2,501); fig,ax=plt.subplots(); ax.plot(xx,np.cos(xx),label="cos(x)"); ax.plot(xx,xx,label="x"); ax.plot(root,root,"ro",label=f"intersection x={root:.2g}"); axes(ax,"Exercise 2: cos(x) = x"); ax.legend(); save(fig,folder,"p23_ex2_intersection.png")
xx=np.linspace(0.6,0.9,501); fig,ax=plt.subplots(); ax.plot(xx,np.cos(xx),label="cos(x)"); ax.plot(xx,xx,label="x"); ax.plot(root,root,"ro",label=f"root = {root:.2g}"); axes(ax,"Exercise 2: zoom near intersection"); ax.legend(); ax.set_xlim(.6,.9); ax.set_ylim(.6,.9); save(fig,folder,"p23_ex2_zoom.png")

x=np.arange(0,10.0001,.1)
with np.errstate(divide="ignore",invalid="ignore",over="ignore"):
    yi=np.sin(x) / x
    ui=1/(x-1)**2+x
    vi=(x**2+1)/(x**2-4)
    # MATLAB fractional powers are complex for negative radicands; requested real-valued branch is x<2.
    zi=np.full_like(x,np.nan)
    valid=(x<2)&(x!=2)
    zi[valid]=(np.cbrt(10-x[valid])-1)/np.sqrt(4-x[valid]**2)
for arr in (yi,ui,vi,zi): arr[~np.isfinite(arr)]=np.nan
spec=[("i",yi,"y=sin(x)/x",(-1.5,1.5)),("ii",ui,"u=1/(x-1)^2 + x",(0,12)),("iii",vi,"v=(x^2+1)/(x^2-4)",(-5,5)),("iv",zi,"z=((10-x)^(1/3)-1)/sqrt(4-x^2) — real values x<2",(-2,3))]
for roman,data,title,ylim in spec:
    fig,ax=plt.subplots(); ax.plot(x,data,label=title); axes(ax,f"Exercise 3 {roman}: {title}"); ax.set_ylim(*ylim); ax.legend(); save(fig,folder,f"p24_ex3_{roman}.png")
fig,axs=plt.subplots(2,2)
for ax,(roman,data,title,ylim) in zip(axs.flat,spec):
    ax.plot(x,data,label=title); axes(ax,f"{roman}) {title}"); ax.set_ylim(*ylim); ax.legend(fontsize=6)
fig.suptitle("Exercise 3: real-valued plots (iv uses x < 2)")
save(fig,folder,"p24_ex3_all_2x2.png")

print("\n".join(str(p.relative_to(ROOT)) for p in pngs))
print(f"Intersection: {root:.2g} (unrounded {root:.12f})")
