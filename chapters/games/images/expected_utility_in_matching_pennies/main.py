import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams.update({"figure.facecolor": "white", "axes.facecolor": "white"})

x = np.linspace(0, 1, 100)

fig, ax = plt.subplots()
ax.plot(x, 1 - 2 * x, label=r"$u_1$ (column plays tails)")
ax.plot(x, 2 * x - 1, label=r"$u_2$ (row plays tails)")
ax.set_xlabel("Probability of playing Heads")
ax.set_ylabel("Expected Utility")
ax.legend()
ax.set_title("Expected Utility vs Strategy")

fig.savefig("main.png", bbox_inches="tight", dpi=150)
