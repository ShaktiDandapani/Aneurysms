import numpy as np
from sympy.geometry import polygon as poly
import matplotlib.pyplot as plt


def convex_check(quad_points):
    c_polygon = poly.Polygon(*quad_points)

    print c_polygon.is_convex()
    #plt.plot(c_polygon)
    #plt.show()


def main():
    quad_points = [[1, 2], [3, 5], [5, 5], [4, 2]]
    convex_check(quad_points)

main()