class Point3D(object):
    """
    define a point object and its methods.
    """
    def __init__(self, x, y, z):
        """

        :param x:
        :param y:
        :param z:
        :return:
        """
        #try making each point object as list to hold
        #multiple points.
        self.x = x
        self.y = y
        self.z = z


class Line(object):
    """
    define a line and a few methods to calculate various attributes
    """
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
