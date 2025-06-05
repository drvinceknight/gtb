import ternary
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

scale = 40  # Higher scale = finer grid

def replicator_dynamics(x, r, sigma):
    x_C, x_D, x_L = x
    P_C = r * x_C / (x_C + x_D) - 1
    P_D = r * x_C / (x_C + x_D)
    P_L = sigma
    phi = x_C * P_C + x_D * P_D + x_L * P_L
    dx = [
        x_C * (P_C - phi),
        x_D * (P_D - phi),
        x_L * (P_L - phi)
    ]
    return np.array(dx)

def normalize(v):
    norm = np.linalg.norm(v)
    return v / norm if norm != 0 else v



fig, tax = ternary.figure(scale=scale)
fig.set_size_inches(6, 5)
tax.boundary()
tax.gridlines(multiple=5, color="gray", linewidth=0.5)

ticks_offset = 0.02
tax.ticks(axis='lbr', ticks=list(np.linspace(0, 1, 5)), tick_formats="%.2f",
          offset=ticks_offset)
tax.clear_matplotlib_ticks()

step_size = 1  # controls grid density
arrow_scale = 0.8  # controls arrow length

r = 3
sigma = .6

for i in range(0, scale + 1, step_size):
    for j in range(0, scale + 1 - i, step_size):
        k = scale - i - j
        x = np.array([i, j, k]) / scale
        dx = replicator_dynamics(x, r=r, sigma=sigma)
        dx = normalize(dx) * (arrow_scale / scale)
        tip = x + dx

        if np.all(tip >= 0) and np.isclose(np.sum(tip), 1.0, atol=1e-2):
            # Convert barycentric coordinates to 2D
            start_xy = ternary.helpers.project_point((i, j, k))
            end_xy = ternary.helpers.project_point((tip[0]*scale, tip[1]*scale, tip[2]*scale))
            vec = np.array(end_xy) - np.array(start_xy)
            plt.arrow(
                start_xy[0], start_xy[1],
                vec[0], vec[1],
                head_width=0.2,
                head_length=0.3,
                fc='blue', ec='blue',
                length_includes_head=True,
                alpha=0.6
            )

# Labels
axis_label_offset = 0.2
tax.left_axis_label("Loners", fontsize=12, offset=axis_label_offset)
tax.right_axis_label("Defectors", fontsize=12, offset=axis_label_offset)
tax.bottom_axis_label("Cooperators", fontsize=12, offset=axis_label_offset)
# Remove box around plot
tax.ax.axis('off')
plt.tight_layout()
tax.savefig("main.png", bbox_inches='tight', dpi=300)
