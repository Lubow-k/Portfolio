from matplotlib.patches import Wedge, Arc
import matplotlib.pyplot as plt

plt.xlim(0, 6)
plt.ylim(0, 5)

ax = plt.gca()

# нарисовать сектор
figure_w = Wedge((3, 1), 2, 45, 135)
ax.add_patch(figure_w)

# нарисовать дугу
figure_a = Arc((3, 1), 6, 6, 0, 45, 135, lw=3)
ax.add_patch(figure_a)
plt.grid()
plt.show()