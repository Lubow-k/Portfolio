from matplotlib.patches import Path, PathPatch
import matplotlib.pyplot as plt

n = 8
m  = 8

plt.xlim(0, n)
plt.ylim(0, m)

ax = plt.gca()

vertices_1 = [(0, 6), (2, 8), (2, 4), (4, 6), (4, 2), (6,4), (6, 0), (8,2)]
vertices_2 = [(0, 6), (2, 4), (2, 8), (4, 6), (4, 2), (6, 0), (6, 4), (8, 2)]

codes_1 = [1, 2, 1, 2, 1, 2, 1, 2]
codes_2 = [1, 2, 1, 2, 1, 2, 1, 2]

path_1 = Path(vertices_1, codes_1)
path_2 = Path(vertices_2, codes_2)

path_patch_1 = PathPatch(path_1, color="blue", lw=3)
path_patch_2 = PathPatch(path_2, color="pink", lw=3)

ax.add_patch(path_patch_1)
ax.add_patch(path_patch_2)

ax.axes.set_axis_off()
plt.show()