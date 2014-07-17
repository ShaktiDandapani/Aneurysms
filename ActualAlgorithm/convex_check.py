__author__ = 'Shakti'
import geomstruct as gs
import geomoperations as gops

def convex_check(polygon_points_1):

            # Arrange points in order so as to get extrem right and extreme left points and join with other 2
            # to get the sides to check for convexity
            arranged_quads_1 = sorted(polygon_points_1, key=lambda x: (x[0], x[1]), reverse=False)

            arranged_quads_1 = gops.correct_order(arranged_quads_1)
            for p in arranged_quads_1:
                print p

            """
            For first set of polygon points
            """
            #arrange the quad points in ascendig order and get the lines for 0, 1 & 0, 2 ; 3, 1 & 3, 2
            ## Just set the lines to opposite sets of points
            ## Line 1
            fline1 = gs.Line((arranged_quads_1[0], arranged_quads_1[1]))
            fline1_slope = fline1.slope()
            fline1_const = fline1.intercept_constant(fline1_slope)

            # print fline1_slope
            # print fline1_const
            print '*' * 30
            print fline1.convex_criteria(arranged_quads_1[2][0], arranged_quads_1[2][1], fline1_slope, fline1_const)
            print fline1.convex_criteria(arranged_quads_1[3][0], arranged_quads_1[3][1], fline1_slope, fline1_const)

            ## Line 2
            fline2 = gs.Line((arranged_quads_1[0], arranged_quads_1[2]))
            # print type(fline1)
            fline2_slope = fline2.slope()
            fline2_const = fline2.intercept_constant(fline2_slope)
            #
            # print fline2_slope
            # pint fline2_const
            print '*' * 30
            print fline2.convex_criteria(arranged_quads_1[1][0], arranged_quads_1[1][1], fline2_slope, fline2_const)
            print fline2.convex_criteria(arranged_quads_1[3][0], arranged_quads_1[3][1], fline2_slope, fline2_const)

            ## Line 3
            fline3 = gs.Line((arranged_quads_1[3], arranged_quads_1[1]))
            fline3_slope = fline3.slope()
            fline3_const = fline3.intercept_constant(fline3_slope)
            print '*' * 30
            print fline3.point_1, fline3.point_2
            print fline3.convex_criteria(arranged_quads_1[0][0], arranged_quads_1[0][1], fline3_slope, fline3_const)
            print fline3.convex_criteria(arranged_quads_1[2][0], arranged_quads_1[2][1], fline3_slope, fline3_const)

            ## Line 4
            fline4 = gs.Line((arranged_quads_1[3], arranged_quads_1[2]))
            fline4_slope = fline4.slope()
            fline4_const = fline4.intercept_constant(fline4_slope)
            print '*' * 30
            print fline4.convex_criteria(arranged_quads_1[0][0], arranged_quads_1[0][1], fline4_slope, fline4_const)
            print fline4.convex_criteria(arranged_quads_1[1][0], arranged_quads_1[1][1], fline4_slope, fline4_const)

def main():

        points_1 = [[3, 4], [2, 3], [2, 4], [1, 5]]
        points_2 = [[3, 4], [2, 3], [2, 4], [4, 3]]

        xpoint = [[2, 6], [3, 1], [3, 2], [4, 6]]
        more_poits = [[2, 1], [3, 3], [4, 3], [4, 2]]

        convex_check(points_2)


main()