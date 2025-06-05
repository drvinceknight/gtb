import matplotlib.pyplot as plt
import nashpy as nash
import numpy as np

M_r = np.array([[3, 1, 2], [4, 2, 1]])
M_c = np.array([[1, 3, 2], [0, 2, 4]])
game = nash.Game(M_r, M_c)
x0 = np.array([1/2, 1/2])
y0 = np.array([1/3, 1/3, 1/3])
timepoints = np.linspace(0, 20, 1_000)

xs, ys = game.asymmetric_replicator_dynamics(x0=x0, y0=y0, timepoints=timepoints)


fig, axarray = plt.subplots(nrows=1, ncols=2, figsize=(14, 5))

ax = axarray[0]
ax.plot(xs) 
ax.set_title("Servers") 
ax.legend(["Power", "Spin"]) 
ax.set_ylim(0, 1)
ax.set_xlabel("$t$")
ax.set_ylabel("$x$")

ax = axarray[1]
ax.plot(ys) 
ax.set_title("Returners") 
ax.legend(["Prepare for Power", "Cover Wide Spin", "Take Aggressive Position"]) 
ax.set_ylim(0, 1)
ax.set_xlabel("$t$")
ax.set_ylabel("$y$")

fig.tight_layout()
fig.savefig("main.png", dpi=300)
