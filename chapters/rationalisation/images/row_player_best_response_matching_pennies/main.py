from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams.update({"figure.facecolor": "white", "axes.facecolor": "white"})

x = np.linspace(0, 1, 100)

fig, ax = plt.subplots()
ax.plot(x, 2 * x - 1, label=r"$u_1(r_1, \sigma_2) = 2x - 1$")
ax.plot(x, 1 - 2 * x, label=r"$u_1(r_2, \sigma_2) = 1 - 2x$")
ax.set_xlabel("$x$")
ax.set_ylabel("Expected utility")
ax.set_title("Row player's expected utility as a function of column player's strategy")
ax.legend()

fig.savefig(Path(__file__).parent / "main.png", bbox_inches="tight", dpi=150)
