import matplotlib.pyplot as plt


class Line(object):
    def __init__(self, data):
        point_1, point_2 = data
        self.point_1 = point_1
        self.point_2 = point_2
        # print point_1, point_2

    def slope(self):
        """
        Get slope of a line segment
        :return:
        """

        (x1, y1), (x2, y2) = self.point_1, self.point_2

        try:
            return float(y2 - y1) / float(x2 - x1)
        except ZeroDivisionError:
            # Vertical Line
            return None

    def intercept_constant(self, slope):
        """
        obtain the y intercept of the line segment
        :param slope:
        :return:
        """

        if slope is not None:
            (x, y) = self.point_1
            return y - slope * x
        else:
            return None

    def convex_criteria(self, x, y, slope, intercept_c):
        """
        solve the equation for an arbitary point with the slope and intercept of another line
        and return positive or negative depending on which side of the line they lie
        :param x:
        :param y:
        :param slope:
        :param intercept_c:
        :return y - mx - c:
        """
        if slope is not None and intercept_c is not None:
            return y - slope * x - intercept_c
        else:
            return None


## testing for polygon convexity
def main():
    # polygon_1 = [[3, 4], [2, 3], [2, 4], [1, 5]]
    # polygon_2 = [[3, 4], [2, 3], [2, 4], [4, 3]]

    data = ((4, 6), (9, 1))     # can even use polygon[0] etc to get points from list.
    new_line = Line(data)
    n_slope = new_line.slope()
    n_const = new_line.intercept_constant(n_slope)

    print new_line.convex_criteria(7, 5, n_slope, n_const)
    print new_line.convex_criteria(6, 5, n_slope, n_const)

    print new_line.convex_criteria(5, 4, n_slope, n_const)
    print new_line.convex_criteria(3, 2, n_slope, n_const)

    fig = plt.figure()
    ax = fig.gca()
    ax.plot(data[0], data[1])
    ax.plot(7, 5, 'r.')
    ax.plot(6, 5, 'r.')
    ax.plot(5, 4, 'r.')
    ax.plot(3, 2, 'r.')
    plt.show()


main()





