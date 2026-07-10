import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Polygon as MplPolygon
from PIL import Image

matplotlib.rcParams["font.family"] = "serif"

SIZE = 512

fig = plt.figure(figsize=(1, 1), dpi=SIZE)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.axis("off")

grad = np.linspace(0, 1, 256).reshape(256, 1)
cmap_bg = LinearSegmentedColormap.from_list("bg", ["#0d1b2a", "#1b3a5c"], N=256)
ax.imshow(grad, extent=[0, 1, 0, 1], aspect="auto",
          cmap=cmap_bg, origin="lower", zorder=0)

# Colours sampled from cover.png (replicator dynamics panel)
TEAL   = "#3e8376"
ACCENT = "#f5a623"
WHITE  = "#edf1f5"

margin = 0.10
sv1 = np.array([margin,      margin])
sv2 = np.array([1 - margin,  margin])
sv3 = np.array([0.5, min(margin + np.sqrt(3)/2 * (1 - 2*margin), 1 - margin)])

ax.add_patch(MplPolygon([sv1, sv2, sv3], closed=True,
                         fill=False, edgecolor=TEAL, lw=3.5, zorder=3))

def bary_to_cart(b1, b2, b3):
    return b1 * sv1 + b2 * sv2 + b3 * sv3

center = bary_to_cart(1/3, 1/3, 1/3)

cmap_traj = LinearSegmentedColormap.from_list("traj", [TEAL, "#a9d0c8", WHITE], N=256)

n = 400
for r_idx, r in enumerate([0.06, 0.13, 0.20]):
    t = np.linspace(0, 2 * np.pi, n)
    b1 = 1/3 + r * np.cos(t)
    b2 = 1/3 + r * np.cos(t + 2 * np.pi / 3)
    b3 = np.clip(1 - b1 - b2, 0.005, None)
    total = b1 + b2 + b3
    b1, b2, b3 = b1/total, b2/total, b3/total
    pts = np.array([bary_to_cart(b1[i], b2[i], b3[i]) for i in range(n)])
    ax.plot(pts[:, 0], pts[:, 1], color=cmap_traj(r_idx / 2),
            lw=1.6, zorder=4)

ax.plot(*center, "o", color=ACCENT, ms=9, zorder=6)

fig.savefig("favicon.png", dpi=SIZE)
plt.close(fig)
print("favicon.png written")

src = Image.open("favicon.png").convert("RGBA")
sizes = [16, 32, 48, 64, 128, 256]
icons = [src.resize((s, s), Image.LANCZOS) for s in sizes]
# Save from the largest frame: PIL drops any size larger than the base image
icons[-1].save("favicon.ico", format="ICO", sizes=[(s, s) for s in sizes],
               append_images=icons[:-1])
print("favicon.ico written")
