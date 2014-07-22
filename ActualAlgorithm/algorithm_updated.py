import sympy as sp
import geomstruct as gs
import geomoperations as gops
import geomplot as diagrams
from operator import itemgetter
import math


def main():

    line1 = [gs.Point3D(2, 3, 5), gs.Point3D(3, 4, 2), gs.Point3D(5, 4, 3), gs.Point3D(7, 4, 4), gs.Point3D(6, 5, 5)]
    # line2 = [gs.Point3D(1, 5, 3), gs.Point3D(2, 4, 3), gs.Point3D(4, 3, 3), gs.Point3D(5, 3, 6)]
    line2 = [gs.Point3D(5, 5, 3), gs.Point3D(2, 4, 3), gs.Point3D(4, 3, 3), gs.Point3D(5, 3, 6)]
    # line1 = [gs.Point3D(0, 0, 0), gs.Point3D((math.pi / 2), 1, 0), gs.Point3D(math.pi, 0, 0),
    #          gs.Point3D((3 / 2 * math.pi), -1, 0), gs.Point3D(2 * math.pi, 0, 0), gs.Point3D((5 * math.pi) / 2, 1, 0)]
    #
    # line2 = [gs.Point3D(0, -math.pi**2, 0), gs.Point3D((math.pi / 2), -(3 / 4) * (math.pi**2), 0),
    #          gs.Point3D(math.pi, 0, 0), gs.Point3D((3 / 2) * math.pi, (5 / 4) * (math.pi**2), 0),
    #          gs.Point3D(2 * math.pi, 3 * (math.pi**2), 0)]

    distance_list_xy_plane = gops.get_dist_dict_xy(line1, line2)
    distance_list_yz_plane = gops.get_dist_dict_yz(line1, line2)
    distance_list_zx_plane = gops.get_dist_dict_zx(line1, line2)

    point_of_int__xy_plane_flag = False
    point_of_int__yz_plane_flag = False
    point_of_int__zx_plane_flag = False

    incr_entry = 1
    while not point_of_int__xy_plane_flag:

        #function to obtain 2 shortest lines
        # make it return the entire list and select the distances based on need.
        all_distances_set_xy_plane = gops.minimum_distance_sort(distance_list_xy_plane)

        short_line_1_xy_plane = all_distances_set_xy_plane[0][1]
        short_line_2_xy_plane = all_distances_set_xy_plane[incr_entry][1]

        temp_list_xy_plane = short_line_1_xy_plane + short_line_2_xy_plane
        [common_point_xy_plane, final_points_xy_plane] = gops.cp_finder(temp_list_xy_plane)

        if len(final_points_xy_plane) == 3:
            [close_point_1, close_point_2] = gops.get_fourth_point_xy_plane(line1, line2, common_point_xy_plane)

            new_quad_points_cp1 = final_points_xy_plane + [close_point_1]
            new_quad_points_cp2 = final_points_xy_plane + [close_point_2]

            polygon_1_triangle_truth = gops.check_triangle(new_quad_points_cp1)
            polygon_2_triangle_truth = gops.check_triangle(new_quad_points_cp2)

            if polygon_1_triangle_truth:
                polygon_1_convex_truth = True
            else:
                polygon_1_convex_truth = gops.convex_check(new_quad_points_cp1)

            if polygon_2_triangle_truth:
                polygon_2_convex_truth = True
            else:
                polygon_2_convex_truth = gops.convex_check(new_quad_points_cp2)

            if polygon_1_convex_truth:
                within_poly_1 = False

                p1_first_final_line = gs.Line((new_quad_points_cp1[0], new_quad_points_cp1[1]))
                p1_second_final_line = gs.Line((new_quad_points_cp1[2], new_quad_points_cp1[3]))

                p1_point_of_int_xy_plane = gops.intersection(p1_first_final_line, p1_second_final_line)

                if p1_point_of_int_xy_plane is not None:
                    within_poly_1 = gops.inside_polygon_test(new_quad_points_cp1, p1_point_of_int_xy_plane)
                else:
                    incr_entry += 1
                if within_poly_1:
                    final_xy_intersection_point = p1_point_of_int_xy_plane
                    point_of_int__xy_plane_flag = True
                else:
                    incr_entry += 1

            if polygon_2_convex_truth:
                within_poly_2 = False
                p2_first_final_line = gs.Line((new_quad_points_cp2[0], new_quad_points_cp2[1]))
                p2_second_final_line = gs.Line((new_quad_points_cp2[2], new_quad_points_cp2[3]))

                p2_point_of_int_xy_plane = gops.intersection(p2_first_final_line, p2_second_final_line)

                if p2_point_of_int_xy_plane is not None:
                    within_poly_2 = gops.inside_polygon_test(new_quad_points_cp2, p2_point_of_int_xy_plane)
                else:
                    incr_entry += 1

                if within_poly_2:
                    final_xy_intersection_point = p2_point_of_int_xy_plane
                    point_of_int__xy_plane_flag = True
                else:
                    incr_entry += 1

        else:
            # four points directly
            if len(final_points_xy_plane) == 4:
                within_polygon = False

                polygon_is_triangle = gops.check_triangle(final_points_xy_plane)

                if polygon_is_triangle:
                    polygon_is_convex = True
                else:
                    polygon_is_convex = gops.convex_check(final_points_xy_plane)

                if polygon_is_convex:
                    first_final_line = gs.Line((final_points_xy_plane[0], final_points_xy_plane[1]))
                    second_final_line = gs.Line((final_points_xy_plane[2], final_points_xy_plane[3]))

                    point_of_intersection_xy = gops.intersection(first_final_line, second_final_line)

                    if point_of_intersection_xy is not None:
                        within_polygon = gops.inside_polygon_test(final_points_xy_plane, point_of_intersection_xy)
                    else:
                        incr_entry += 1

                if within_polygon:
                    final_xy_intersection_point = point_of_intersection_xy
                    point_of_int__xy_plane_flag = True
                else:
                    incr_entry += 1
            else:
                print 'not enough data to solve for a polygon in xy plane'
                point_of_int__xy_plane_flag = True

    ######################################## END OF XY PLANE CODE ##################################################

    incr_entry = 1
    while not point_of_int__yz_plane_flag:

        all_distances_set_yz_plane = gops.minimum_distance_sort(distance_list_yz_plane)

        short_line_1_yz_plane = all_distances_set_yz_plane[0][1]
        short_line_2_yz_plane = all_distances_set_yz_plane[incr_entry][1]

        temp_list_yz_plane = short_line_1_yz_plane + short_line_2_yz_plane

        [common_point_yz_plane, final_points_yz_plane] = gops.cp_finder(temp_list_yz_plane)

        if len(final_points_yz_plane) == 3:
            [close_point_1, close_point_2] = gops.get_fourth_point_xy_plane(line1, line2, common_point_yz_plane)

            new_quad_points_cp1 = final_points_yz_plane + [close_point_1]
            new_quad_points_cp2 = final_points_yz_plane + [close_point_2]

            polygon_1_triangle_truth = gops.check_triangle(new_quad_points_cp1)
            polygon_2_triangle_truth = gops.check_triangle(new_quad_points_cp2)

            if polygon_1_triangle_truth:
                polygon_1_convex_truth = True
            else:
                polygon_1_convex_truth = gops.convex_check(new_quad_points_cp1)

            if polygon_2_triangle_truth:
                polygon_2_convex_truth = True
            else:
                polygon_2_convex_truth = gops.convex_check(new_quad_points_cp2)

            if polygon_1_convex_truth:
                within_poly_1 = False

                p1_first_final_line = gs.Line((new_quad_points_cp1[0], new_quad_points_cp1[1]))
                p1_second_final_line = gs.Line((new_quad_points_cp1[2], new_quad_points_cp1[3]))

                p1_point_of_int_yz_plane = gops.intersection(p1_first_final_line, p1_second_final_line)

                if p1_point_of_int_yz_plane is not None:
                    within_poly_1 = gops.inside_polygon_test(new_quad_points_cp1, p1_point_of_int_yz_plane)
                else:
                    incr_entry += 1
                if within_poly_1:
                    final_yz_intersection_point = p1_point_of_int_yz_plane
                    point_of_int__yz_plane_flag = True
                else:
                    incr_entry += 1

            # Check if second polygon has the point
            if polygon_2_convex_truth:
                within_poly_2 = False
                p2_first_final_line = gs.Line((new_quad_points_cp2[0], new_quad_points_cp2[1]))
                p2_second_final_line = gs.Line((new_quad_points_cp2[2], new_quad_points_cp2[3]))

                p2_point_of_int_yz_plane = gops.intersection(p2_first_final_line, p2_second_final_line)

                if p2_point_of_int_yz_plane is not None:
                    within_poly_2 = gops.inside_polygon_test(new_quad_points_cp2, p2_point_of_int_yz_plane)
                else:
                    incr_entry += 1

                if within_poly_2:
                    final_yz_intersection_point = p2_point_of_int_yz_plane
                    point_of_int__yz_plane_flag = True
                else:
                    incr_entry += 1

        else:
            if len(final_points_yz_plane) == 4:
                # four points directly
                within_polygon = False
                polygon_is_triangle = gops.check_triangle(final_points_yz_plane)

                if polygon_is_triangle:
                    polygon_is_convex = True
                else:
                    polygon_is_convex = gops.convex_check(final_points_yz_plane)

                if polygon_is_convex:
                    first_final_line = gs.Line((final_points_yz_plane[0], final_points_yz_plane[1]))
                    second_final_line = gs.Line((final_points_yz_plane[2], final_points_yz_plane[3]))

                    point_of_intersection_yz = gops.intersection(first_final_line, second_final_line)

                    if point_of_intersection_yz is not None:
                        within_polygon = gops.inside_polygon_test(final_points_yz_plane, point_of_intersection_yz)
                    else:
                        incr_entry += 1

                if within_polygon:
                    final_yz_intersection_point = point_of_intersection_yz
                    point_of_int__yz_plane_flag = True
                else:
                    incr_entry += 1
            else:
                print 'not enough data for a polygon in yz plane'
                point_of_int__yz_plane_flag = True
    ######################################## END OF YZ PLANE CODE ##################################################

    incr_entry = 1
    while not point_of_int__zx_plane_flag:

        all_distances_set_zx_plane = gops.minimum_distance_sort(distance_list_zx_plane)

        short_line_1_zx_plane = all_distances_set_zx_plane[0][1]
        short_line_2_zx_plane = all_distances_set_zx_plane[incr_entry][1]

        temp_list_zx_plane = short_line_1_zx_plane + short_line_2_zx_plane
        [common_point_zx_plane, final_points_zx_plane] = gops.cp_finder(temp_list_zx_plane)

        if len(final_points_zx_plane) == 3:
            [close_point_1, close_point_2] = gops.get_fourth_point_zx_plane(line1, line2, common_point_zx_plane)

            new_quad_points_cp1 = final_points_zx_plane + [close_point_1]
            new_quad_points_cp2 = final_points_zx_plane + [close_point_2]

            polygon_1_triangle_truth = gops.check_triangle(new_quad_points_cp1)
            polygon_2_triangle_truth = gops.check_triangle(new_quad_points_cp2)

            if polygon_1_triangle_truth:
                polygon_1_convex_truth = True
            else:
                polygon_1_convex_truth = gops.convex_check(new_quad_points_cp1)

            if polygon_2_triangle_truth:
                polygon_2_convex_truth = True
            else:
                polygon_2_convex_truth = gops.convex_check(new_quad_points_cp2)

            if polygon_1_convex_truth:
                within_poly_1 = False

                p1_first_final_line = gs.Line((new_quad_points_cp1[0], new_quad_points_cp1[1]))
                p1_second_final_line = gs.Line((new_quad_points_cp1[2], new_quad_points_cp1[3]))

                p1_point_of_int_zx_plane = gops.intersection(p1_first_final_line, p1_second_final_line)

                if p1_point_of_int_zx_plane is not None:
                    within_poly_1 = gops.inside_polygon_test(new_quad_points_cp1, p1_point_of_int_zx_plane)
                else:
                    incr_entry += 1
                if within_poly_1:
                    final_zx_intersection_point = p1_point_of_int_zx_plane
                    point_of_int__zx_plane_flag = True
                else:
                    incr_entry += 1

            if polygon_2_convex_truth:
                within_poly_2 = False
                p2_first_final_line  = gs.Line((new_quad_points_cp2[0], new_quad_points_cp2[1]))
                p2_second_final_line = gs.Line((new_quad_points_cp2[2], new_quad_points_cp2[3]))

                p2_point_of_int_zx_plane = gops.intersection(p2_first_final_line, p2_second_final_line)

                if p2_point_of_int_zx_plane is not None:
                    within_poly_2 = gops.inside_polygon_test(new_quad_points_cp2, p2_point_of_int_zx_plane)
                else:
                    incr_entry += 1

                if within_poly_2:
                    final_zx_intersection_point = p2_point_of_int_zx_plane
                    point_of_int__zx_plane_flag = True
                else:
                    incr_entry += 1

        else:
            if len(final_points_zx_plane) == 4:
                # four points directly
                within_polygon = False
                polygon_is_triangle = gops.check_triangle(final_points_zx_plane)

                if polygon_is_triangle:
                    polygon_is_convex = True
                else:
                    polygon_is_convex = gops.convex_check(final_points_zx_plane)

                if polygon_is_convex:
                    first_final_line = gs.Line((final_points_zx_plane[0], final_points_zx_plane[1]))
                    second_final_line = gs.Line((final_points_zx_plane[2], final_points_zx_plane[3]))

                    point_of_intersection_zx = gops.intersection(first_final_line, second_final_line)

                    if point_of_intersection_zx is not None:
                        within_polygon = gops.inside_polygon_test(final_points_zx_plane, point_of_intersection_zx)
                    else:
                        incr_entry += 1

                if within_polygon:
                    final_zx_intersection_point = point_of_intersection_zx
                    point_of_int__zx_plane_flag = True
                else:
                    incr_entry += 1
            else:
                print 'not enough data for a polygon in zx plane'
                point_of_int__zx_plane_flag = True
    ######################################## END OF ZX PLANE CODE ##################################################

    # Plots below
    # Plot the figures
    if len(final_xy_intersection_point) == 2 and len(final_yz_intersection_point) == 2 \
            and len(final_zx_intersection_point) == 2:
        print 'ok'
        print ' -------------------------------------|'
        print '|xy plane intersection: ', final_xy_intersection_point, '|'
        print '|yz plane intersection: ', final_yz_intersection_point, '|'
        print '|zx plane intersection: ', final_zx_intersection_point, '|'
        print ' -------------------------------------|'
        diagrams.original_lines(line1, line2, final_xy_intersection_point, final_yz_intersection_point,
                                final_zx_intersection_point)
    else:
        print 'no sufficient data to display'


main()
