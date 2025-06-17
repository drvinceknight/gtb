import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
from mpl_toolkits.mplot3d.art3d import Poly3DCollection



# Compute convex hull
vertices = np.array(
    [
        [ 0.        ,  0.        ,  0.        ],
        [ 2.5       ,  0.        ,  0.        ],
        [ 0.        , -0.        ,  2.25      ],
        [ 1.36871508, -0.        ,  1.81005587],
        [ 1.75824176,  1.48351648,  0.        ],
        [ 1.33549827,  0.84940126,  1.18368175],
        [ 0.        ,  1.8       ,  0.        ],
        [ 0.        ,  0.81818182,  1.63636364],
    ]
)
hull = ConvexHull(vertices)

# Plotting
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

# Plot the vertices and add labels
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color="black", s=40, label="Vertices")

x, y, z = vertices[0]
ax.text(x, y-.15, z, f"$v_0$", fontsize=10, color="red")

x, y, z = vertices[1]
ax.text(x, y-.15, z, f"$v_1$", fontsize=10, color="red")

x, y, z = vertices[2]
ax.text(x, y-.15, z, f"$v_2$", fontsize=10, color="red")

x, y, z = vertices[3]
ax.text(x, y-.15, z, f"$v_3$", fontsize=10, color="red")

x, y, z = vertices[4]
ax.text(x+.05, y+.05, z, f"$v_4$", fontsize=10, color="red")

x, y, z = vertices[5]
ax.text(x+.05, y+.05, z, f"$v_5$", fontsize=10, color="red")

x, y, z = vertices[6]
ax.text(x+.05, y+.05, z, f"$v_6$", fontsize=10, color="red")

x, y, z = vertices[7]
ax.text(x+.05, y+.05, z, f"$v_7$", fontsize=10, color="red")

# Plot the convex hull faces
faces = [vertices[simplex] for simplex in hull.simplices]
face_collection = Poly3DCollection(faces, alpha=0.2, edgecolor='gray')
ax.add_collection3d(face_collection)

# Plot the edges
edges = set()
for simplex in hull.simplices:
    for i in range(3):  # each simplex is a triangle
        a, b = sorted((simplex[i], simplex[(i + 1) % 3]))
        edges.add((a, b))

for i, j in edges:
    x = [vertices[i][0], vertices[j][0]]
    y = [vertices[i][1], vertices[j][1]]
    z = [vertices[i][2], vertices[j][2]]
    ax.plot(x, y, z, color="blue")

# Labels and view
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_zlabel("$x_3$")
ax.view_init(elev=20, azim=5)
plt.tight_layout()
plt.savefig("main.png", transparent=True, dpi=300)
