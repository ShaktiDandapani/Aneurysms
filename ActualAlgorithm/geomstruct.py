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
    def __init__(self, data):
        point_1, point_2 = data
        self.point_1 = point_1
        self.point_2 = point_2
        (self.x1, self.y1), (self.x2, self.y2) = self.point_1, self.point_2
        # print point_1, point_2

    # works for both zero -> None and div by zero -> None
    def slope(self):
        """
        Get slope of a line segment
        :return:
        """

        try:
            m = float(self.y2 - self.y1) / float(self.x2 - self.x1)
            return m
        except ZeroDivisionError:
            # Vertical Line
            return None

    def intercept_constant(self, slope):
        """
        obtain the y intercept of the line segment
        :param slope:
        :return:
        """

        if self.x2 - self.x1 == 0 and slope is None:
            return self.x1

        elif self.y2 - self.y1 == 0 and slope is not None:
            return self.y1

        if slope is not None:
            return self.y1 - slope * self.x1

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
        # print self.x1, self.y1
        # print self.x2, self.y2
        if self.x1 - self.x2 == 0:
            return x - self.x1

        if self.y1 - self.y2 == 0:
            # print y, 'subtracting ->', self.y1
            return y - self.y1

        if slope is not None and intercept_c is not None:
            return y - slope * x - intercept_c
