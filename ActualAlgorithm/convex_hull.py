from scipy.spatial import qhull as ch
import matplotlib.pyplot as plt
from numpy import array


def main():
    quad_points = array([[1, 2], [3, 5], [5, 5], [4, 2]])
    print quad_points

    hull = ch.ConvexHull(quad_points)

    plt.plot(quad_points[hull.vertices, 0], quad_points[hull.vertices, 1], 'r--')
    plt.show()

    #print hull.vertices


main()