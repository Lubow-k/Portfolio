from matplotlib.patches import Circle, Wedge, Polygon, Ellipse, Arc, Path, PathPatch
import matplotlib.pyplot as plt

def draw_cat(ax):
 # туловище
    poly = [(3,1),(4,14),(5,11),(8,11),(9,14),(10,1)]
    polygon = Polygon(poly, fc="grey", ec="black", lw=4)
    ax.add_patch (polygon)

    # глаза
    circle = Circle((5.3, 8.5), 1.2, fc="white", ec="black", lw=4)
    ax.add_patch (circle)

    circle = Circle((7.7, 8.5), 1.2, fc="white", ec="black", lw=4)
    ax.add_patch (circle)

    # зрачки
    circle = Circle((5.6, 8.3), 0.1, fc="black", ec="black", lw=4)
    ax.add_patch (circle)

    circle = Circle((7.4, 8.3), 0.1, fc="black", ec="black", lw=4)
    ax.add_patch (circle)

    # нос
    circle = Circle((6.5, 7.5), 0.3, fc="black", ec="black", lw=4)
    ax.add_patch (circle)

    # задние лапы
    wedge = Wedge((3, 1), 2, 86, 180, fc="grey", ec="black", lw=4)
    ax.add_patch (wedge)
    
    wedge = Wedge((10, 1), 2, 0, 94, fc="grey", ec="black", lw=4)
    ax.add_patch (wedge)

    # передние лапы
    ellipse = Ellipse((5.5,1.2), 2, 1.5, fc="grey", ec="black", lw=4)
    ax.add_patch (ellipse)

    ellipse = Ellipse((7.5,1.2), 2, 1.5, fc = "grey", ec="black", lw=4)
    ax.add_patch (ellipse)

    # улыбка
    arc =  Arc((6.5, 6.5), 5, 3, 0, 200, 340, lw=4, fill=False)
    ax.add_patch(arc)

    # линия между носом и улыбкой, усы
    vertices = [(6.5, 5), (6.5, 7.5), (10, 6), (6.5, 7.5), (10, 6.5), (6.5, 7.5), (10, 7),
                (6.5, 7.5), (3, 6), (6.5, 7.5), (3, 6.5), (6.5, 7.5), (3, 7)]
    
    # число 1 соответствует команде matplotlib.path.Path.MOVETO
    # число 2 соответствует команде matplotlib.path.Path.LINETO
    codes = [1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

    path = Path(vertices, codes)
    path_patch = PathPatch(path, fill=False, lw=1)
    ax.add_patch(path_patch)
    
n = 13

m  = 15

plt.xlim(0, n)

plt.ylim(0, m)

ax = plt.gca()

draw_cat(ax)



plt.show()
