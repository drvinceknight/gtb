import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch
from matplotlib.colors import LinearSegmentedColormap

matplotlib.rcParams["font.family"] = "serif"

W, H = 6, 9
DPI = 300
fig = plt.figure(figsize=(W, H), dpi=DPI)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect("equal")
ax.axis("off")

grad = np.linspace(0, 1, 256).reshape(256, 1)
cmap_bg = LinearSegmentedColormap.from_list("bg", ["#0d1b2a", "#1b3a5c"], N=256)
ax.imshow(grad, extent=[0, W, 0, H], aspect="auto",
          cmap=cmap_bg, origin="lower", zorder=0)

NODE_FILL = "#1e4976"
NODE_EDGE = "#4a9edd"
LEAF_FILL = "#14303f"
LEAF_EDGE = "#5ec4a0"
LINE_COL  = "#4a9edd"
TEXT_MAIN = "#f0f4f8"
TEXT_DIM  = "#8ab4d4"
ACCENT    = "#f5a623"
MATCH_COL = "#c97bdb"
GRID_COL  = "#1a3a5c"

for x in np.arange(0, W + 0.3, 0.3):
    ax.axvline(x, color=GRID_COL, lw=0.3, alpha=0.4, zorder=1)
for y in np.arange(0, H + 0.3, 0.3):
    ax.axhline(y, color=GRID_COL, lw=0.3, alpha=0.4, zorder=1)


def node(cx, cy, label, fill=NODE_FILL, edge=NODE_EDGE,
         fontsize=9, textcol=TEXT_MAIN, leaf=False, zorder=5):
    if leaf:
        c = plt.Circle((cx, cy), 0.13, color=fill, ec=edge, lw=1.5, zorder=zorder)
        ax.add_patch(c)
    else:
        box = FancyBboxPatch(
            (cx - 0.55, cy - 0.22), 1.10, 0.44,
            boxstyle="round,pad=0.06",
            facecolor=fill, edgecolor=edge, lw=1.5, zorder=zorder)
        ax.add_patch(box)
    ax.text(cx, cy, label, ha="center", va="center",
            fontsize=fontsize, color=textcol, fontweight="bold", zorder=zorder + 1)


def arrow(x0, y0, x1, y1, label="", lw=1.4, col=LINE_COL):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=col,
                                lw=lw, mutation_scale=10), zorder=4)
    if label:
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        dx, dy = x1 - x0, y1 - y0
        length = (dx**2 + dy**2) ** 0.5
        ox, oy = -dy / length * 0.18, dx / length * 0.18
        ax.text(mx + ox, my + oy, label, ha="center", va="center",
                fontsize=7.5, color=TEXT_DIM, fontstyle="italic", zorder=5)


# Game tree
rx, ry = W / 2, 6.3
node(rx, ry, "Player 1", fontsize=8)

p2L = (rx - 1.5, 5.3)
p2R = (rx + 1.5, 5.3)
node(*p2L, "Player 2", fontsize=8)
node(*p2R, "Player 2", fontsize=8)

arrow(rx, ry - 0.22, p2L[0], p2L[1] + 0.22, label="C")
arrow(rx, ry - 0.22, p2R[0], p2R[1] + 0.22, label="D")

# Information set
ax.plot([p2L[0] + 0.55, p2R[0] - 0.55], [p2L[1], p2R[1]],
        color=NODE_EDGE, lw=1.4, linestyle="--", alpha=0.8, zorder=4)

LL = (p2L[0] - 1.0, 4.15)
LR = (p2L[0] + 1.0, 4.15)
RL = (p2R[0] - 1.0, 4.15)
RR = (p2R[0] + 1.0, 4.15)

for pos in (LL, LR, RL, RR):
    node(*pos, "", fill=LEAF_FILL, edge=LEAF_EDGE, leaf=True)

arrow(*p2L, LL[0], LL[1] + 0.13, label="c")
arrow(*p2L, LR[0], LR[1] + 0.13, label="d")
arrow(*p2R, RL[0], RL[1] + 0.13, label="c")
arrow(*p2R, RR[0], RR[1] + 0.13, label="d")

for pos, pay in zip((LL, LR, RL, RR), ["(3,3)", "(0,5)", "(5,0)", "(1,1)"]):
    ax.text(pos[0], pos[1] - 0.22, pay, ha="center", va="top",
            fontsize=7, color=LEAF_EDGE, fontfamily="monospace", zorder=5)


# Payoff matrix
mx0, my0 = 0.65, 2.30
cell_w, cell_h = 0.82, 0.50

ax.text(mx0 + cell_w, my0 + cell_h * 2 + 0.30, "Player 2",
        ha="center", fontsize=7.5, color=TEXT_DIM, fontstyle="italic")
ax.text(mx0 - 0.42, my0 + cell_h * 0.95, "Player 1",
        ha="center", fontsize=7.5, color=TEXT_DIM, fontstyle="italic", rotation=90)

for ci, cl in enumerate(["c", "d"]):
    ax.text(mx0 + (ci + 0.5) * cell_w, my0 + cell_h * 2 + 0.10, cl,
            ha="center", va="center", fontsize=8.5,
            color=TEXT_MAIN, fontweight="bold")
for ri, rl in enumerate(["C", "D"]):
    ax.text(mx0 - 0.14, my0 + (1 - ri + 0.5) * cell_h, rl,
            ha="center", va="center", fontsize=8.5,
            color=TEXT_MAIN, fontweight="bold")

matrix_vals = [["3, 3", "0, 5"], ["5, 0", "1, 1"]]
ne_cell = (1, 1)
for ri in range(2):
    for ci in range(2):
        is_ne = (ri, ci) == ne_cell
        rect = FancyBboxPatch(
            (mx0 + ci * cell_w + 0.04, my0 + (1 - ri) * cell_h + 0.03),
            cell_w - 0.08, cell_h - 0.06,
            boxstyle="round,pad=0.04",
            facecolor="#1a3f28" if is_ne else "#0f2236",
            edgecolor=ACCENT if is_ne else NODE_EDGE,
            lw=2.0 if is_ne else 1.0, zorder=4)
        ax.add_patch(rect)
        ax.text(mx0 + (ci + 0.5) * cell_w,
                my0 + (1 - ri + 0.5) * cell_h,
                matrix_vals[ri][ci],
                ha="center", va="center", fontsize=8,
                color=ACCENT if is_ne else TEXT_MAIN,
                fontfamily="monospace",
                fontweight="bold" if is_ne else "normal", zorder=5)


# Stable matching
match_x_L = 0.60
match_x_R = 2.10
match_ys  = [1.22, 1.55, 1.88]
stable    = [(0, 0), (1, 2), (2, 1)]

for i in range(3):
    for j in range(3):
        ax.plot([match_x_L + 0.10, match_x_R - 0.10],
                [match_ys[i], match_ys[j]],
                color=MATCH_COL, lw=0.5, alpha=0.20, zorder=3)

for (i, j) in stable:
    ax.plot([match_x_L + 0.10, match_x_R - 0.10],
            [match_ys[i], match_ys[j]],
            color=MATCH_COL, lw=2.0, alpha=0.9, zorder=4)

for lbl, y in zip(["A", "B", "C"], match_ys):
    ax.add_patch(plt.Circle((match_x_L, y), 0.10,
                             color="#1d1040", ec=MATCH_COL, lw=1.8, zorder=5))
    ax.text(match_x_L, y, lbl, ha="center", va="center",
            fontsize=7, color=TEXT_MAIN, fontweight="bold", zorder=6)

for lbl, y in zip(["1", "2", "3"], match_ys):
    ax.add_patch(plt.Circle((match_x_R, y), 0.10,
                             color="#1d1040", ec=MATCH_COL, lw=1.8, zorder=5))
    ax.text(match_x_R, y, lbl, ha="center", va="center",
            fontsize=7, color=TEXT_MAIN, fontweight="bold", zorder=6)

ax.text((match_x_L + match_x_R) / 2, 1.08, "Stable Matching",
        ha="center", fontsize=7, color=MATCH_COL, fontstyle="italic", zorder=5)


# Population dynamics simplex
sv1 = np.array([3.05, 1.10])
sv2 = np.array([5.65, 1.10])
sv3 = np.array([4.35, 3.46])

def bary_to_cart(b1, b2, b3):
    return b1 * sv1 + b2 * sv2 + b3 * sv3

ax.add_patch(plt.Polygon([sv1, sv2, sv3], closed=True, fill=False,
                          edgecolor=LEAF_EDGE, lw=1.5, alpha=0.6, zorder=3))

for pt, lbl in zip([sv1, sv2, sv3], ["H", "D", "R"]):
    offset = np.array([0, -0.22]) if pt[1] < 2 else np.array([0, 0.22])
    ax.text(pt[0] + offset[0], pt[1] + offset[1], lbl,
            ha="center", va="center",
            fontsize=8.5, color=LEAF_EDGE, fontweight="bold", zorder=6)

n_steps = 400
cmap_traj = LinearSegmentedColormap.from_list(
    "traj", [LEAF_EDGE, "#b0f0d8", "#f0f4f8"], N=256)

for r_idx, r in enumerate([0.04, 0.09, 0.16, 0.22]):
    t_arr = np.linspace(0, 2 * np.pi, n_steps)
    b1 = 1/3 + r * np.cos(t_arr)
    b2 = 1/3 + r * np.cos(t_arr + 2 * np.pi / 3)
    b3 = np.clip(1 - b1 - b2, 0.005, None)
    total = b1 + b2 + b3
    b1, b2, b3 = b1/total, b2/total, b3/total
    pts = np.array([bary_to_cart(b1[i], b2[i], b3[i]) for i in range(n_steps)])
    ax.plot(pts[:, 0], pts[:, 1], color=cmap_traj(r_idx / 3),
            lw=1.1, alpha=0.55 + 0.15 * r_idx, zorder=4)

r = 0.22
t_arr = np.linspace(0, 2 * np.pi, n_steps)
b1 = 1/3 + r * np.cos(t_arr)
b2 = 1/3 + r * np.cos(t_arr + 2 * np.pi / 3)
b3 = np.clip(1 - b1 - b2, 0.005, None)
total = b1 + b2 + b3
b1, b2, b3 = b1/total, b2/total, b3/total
idx = n_steps // 6
p0 = bary_to_cart(b1[idx], b2[idx], b3[idx])
p1 = bary_to_cart(b1[idx + 8], b2[idx + 8], b3[idx + 8])
ax.annotate("", xy=p1, xytext=p0,
            arrowprops=dict(arrowstyle="-|>", color=TEXT_MAIN,
                            lw=1.0, mutation_scale=8), zorder=5)

center = bary_to_cart(1/3, 1/3, 1/3)
ax.plot(*center, "o", color=ACCENT, ms=4, zorder=6)

ax.text((sv1[0] + sv2[0]) / 2, 0.90, "Replicator Dynamics",
        ha="center", fontsize=7, color=LEAF_EDGE, fontstyle="italic", zorder=5)


# Title
title_y = 8.35
for word, y in [("GAME", title_y), ("THEORY", title_y - 0.85)]:
    ax.text(W / 2, y, word, ha="center", va="center",
            fontsize=52, color=TEXT_MAIN, fontweight="bold", fontfamily="serif",
            zorder=10,
            path_effects=[pe.withStroke(linewidth=3, foreground="#0d1b2a")])

rule_y = title_y - 1.3
ax.plot([0.7, W - 0.7], [rule_y, rule_y], color=ACCENT, lw=1.5, zorder=6)
ax.text(W / 2, rule_y - 0.25, "Theory · Software · Research",
        ha="center", va="top",
        fontsize=10, color=TEXT_DIM, fontfamily="serif", fontstyle="italic",
        zorder=10)

# Author
ax.plot([0.7, W - 0.7], [0.80, 0.80], color=ACCENT, lw=1.5, zorder=6)
ax.text(W / 2, 0.58, "VINCE KNIGHT",
        ha="center", va="center",
        fontsize=16, color=TEXT_MAIN, fontweight="bold", fontfamily="serif",
        zorder=10)
ax.text(W / 2, 0.28, "Illustrated by James Brown",
        ha="center", va="center",
        fontsize=10, color=TEXT_DIM, fontfamily="serif", fontstyle="italic",
        zorder=10)

fig.savefig("cover.png", dpi=DPI)
print("cover.png written")
