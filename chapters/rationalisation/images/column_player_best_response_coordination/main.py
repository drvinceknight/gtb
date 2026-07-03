from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams.update({"figure.facecolor": "white", "axes.facecolor": "white"})

x = np.linspace(0, 1, 100)

fig, ax = plt.subplots()
ax.plot(x, 2 * x, label=r"$u_2(\sigma_1, c_1) = 2x$")
ax.plot(x, 3 - 2 * x, label=r"$u_2(\sigma_1, c_2) = 3 - 2x$")
ax.set_xlabel("$x$")
ax.set_ylabel("Expected utility")
ax.set_title("Column player's expected utility as a function of row player's strategy")
ax.legend()

fig.savefig(Path(__file__).parent / "main.png", bbox_inches="tight", dpi=150)
