__author__ = 'Shakti'
import geomstruct as gs
import geomoperations as gops


def convex_check(polygon_points):

            # Arrange points in order so as to get extrem right and extreme left points and join with other 2
            # to get the sides to check for convexity
            sorted_polygon_points = sorted(polygon_points, key=lambda x: (x[0], x[1]), reverse=False)
            sorted_polygon_points = gops.correct_order(sorted_polygon_points)

            ## Just set the lines to opposite sets of points
            ## Line 1
            fline1 = gs.Line((sorted_polygon_points[0], sorted_polygon_points[1]))
            fline1_slope = fline1.slope()
            fline1_const = fline1.intercept_constant(fline1_slope)
            fline1_point_cc_wp_2 = fline1.convex_criteria(sorted_polygon_points[2][0], sorted_polygon_points[2][1], fline1_slope, fline1_const)
            fline1_point_cc_wp_3 = fline1.convex_criteria(sorted_polygon_points[3][0], sorted_polygon_points[3][1], fline1_slope, fline1_const)

            ## Line 2
            fline2 = gs.Line((sorted_polygon_points[0], sorted_polygon_points[2]))
            fline2_slope = fline2.slope()
            fline2_const = fline2.intercept_constant(fline2_slope)
            fline2_point_cc_wp_1 = fline2.convex_criteria(sorted_polygon_points[1][0], sorted_polygon_points[1][1], fline2_slope, fline2_const)
            fline2_point_cc_wp_3 =  fline2.convex_criteria(sorted_polygon_points[3][0], sorted_polygon_points[3][1], fline2_slope, fline2_const)

            ## Line 3
            fline3 = gs.Line((sorted_polygon_points[1], sorted_polygon_points[3]))
            fline3_slope = fline3.slope()
            fline3_const = fline3.intercept_constant(fline3_slope)
            fline3_point_cc_wp_0 = fline3.convex_criteria(sorted_polygon_points[0][0], sorted_polygon_points[0][1], fline3_slope, fline3_const)
            fline3_point_cc_wp_2 = fline3.convex_criteria(sorted_polygon_points[2][0], sorted_polygon_points[2][1], fline3_slope, fline3_const)

            ## Line 4
            fline4 = gs.Line((sorted_polygon_points[2], sorted_polygon_points[3]))
            fline4_slope = fline4.slope()
            fline4_const = fline4.intercept_constant(fline4_slope)
            fline4_point_cc_wp_0 = fline4.convex_criteria(sorted_polygon_points[0][0], sorted_polygon_points[0][1], fline4_slope, fline4_const)
            fline4_point_cc_wp_1 = fline4.convex_criteria(sorted_polygon_points[1][0], sorted_polygon_points[1][1], fline4_slope, fline4_const)

            if fline1_point_cc_wp_2 > 0 and fline1_point_cc_wp_3 > 0 or fline1_point_cc_wp_2 < 0 and fline1_point_cc_wp_3 < 0:
                print 'checked convex for first side'
            else:
                print 'first line not part of convex set'

            if fline2_point_cc_wp_1 > 0 and fline2_point_cc_wp_3 > 0 or fline2_point_cc_wp_1 < 0 and fline2_point_cc_wp_3 < 0:
                print 'checked convex for second side'
            else:
                print 'second line not part of convex set'

            if fline3_point_cc_wp_0 > 0 and fline3_point_cc_wp_2 > 0 or fline3_point_cc_wp_0 < 0 and fline3_point_cc_wp_2 < 0:
                print 'checked convex for third side'
            else:
                print 'third line not part of convex set'

            if fline4_point_cc_wp_0 > 0 and fline4_point_cc_wp_1 > 0 or fline4_point_cc_wp_0 < 0 and fline4_point_cc_wp_1 < 0:
                print 'checked convex for fourth side'
            else:
                print 'fourth point not part of convex set'


def main():

        points_1 = [[3, 4], [2, 3], [2, 4], [1, 5]]
        points_2 = [[3, 4], [2, 3], [2, 4], [4, 3]]

        xpoint = [[2, 6], [3, 1], [3, 2], [4, 6]]
        more_poits = [[2, 1], [3, 3], [4, 3], [4, 2]]

        convex_check(points_2)


main()