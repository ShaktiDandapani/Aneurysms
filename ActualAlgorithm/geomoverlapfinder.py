import geomstruct as gs
import geomoperations as gops
import geomplot as diagrams
import time

def find_overlap(line1, line2):
    """
    Calculates the overlap between two lines in 3D space.
    This is equivalent to finding the point of intersection in 2D space between two lines but
    in 3D space.

    :param line1:
    :param line2:
    :return poi_xy, poi_yz, poi_zx:
    """
    final_xy_intersection_point = None
    final_yz_intersection_point = None
    final_zx_intersection_point = None

    distance_list_xy_plane = gops.get_dist_dict_xy(line1, line2)
    distance_list_yz_plane = gops.get_dist_dict_yz(line1, line2)
    distance_list_zx_plane = gops.get_dist_dict_zx(line1, line2)

    '''
    Sorting the distances in ascending order so as to get the shortest lines easily
    '''
    all_distances_set_xy_plane = gops.minimum_distance_sort(distance_list_xy_plane)
    all_distances_set_yz_plane = gops.minimum_distance_sort(distance_list_yz_plane)
    all_distances_set_zx_plane = gops.minimum_distance_sort(distance_list_zx_plane)
    '''
    If distance is zero just take that point as the intersection.
    '''

    if all_distances_set_xy_plane[0][0] == 0.0:
        final_xy_intersection_point = all_distances_set_xy_plane[0][1][0]

    if all_distances_set_xy_plane[0][0] == 0.0:
        final_yz_intersection_point = all_distances_set_yz_plane[0][1][0]

    if all_distances_set_zx_plane[0][0] == 0.0:
        final_zx_intersection_point = all_distances_set_zx_plane[0][1][0]

    '''
    If we do not have zero distance points we move into the loops and search for intersections
    '''
    # print len(all_distances_set_xy_plane)

    incr_entry = 1
    while final_xy_intersection_point is None and incr_entry < len(all_distances_set_xy_plane):
        # print 'here', len(all_distances_set_xy_plane)

        short_line_1_xy_plane = all_distances_set_xy_plane[0][1]
        short_line_2_xy_plane = all_distances_set_xy_plane[incr_entry][1]

        temp_list_xy_plane = short_line_1_xy_plane + short_line_2_xy_plane

        (common_point_xy_plane, final_points_xy_plane) = gops.cp_finder(temp_list_xy_plane)

        if len(final_points_xy_plane) == 3:

            (close_point_1, close_point_2) = gops.get_fourth_point_xy_plane(line1, line2, common_point_xy_plane)

            new_quad_points_cp1 = final_points_xy_plane + [close_point_1]
            new_quad_points_cp2 = final_points_xy_plane + [close_point_2]
            # Slowing things is this triangle check

            polygon_1_convex_truth = gops.convex_check(new_quad_points_cp1)

            polygon_2_convex_truth = gops.convex_check(new_quad_points_cp2)

            if polygon_1_convex_truth:
                within_poly_1 = False

                p1_first_final_line = gs.Line((new_quad_points_cp1[0], new_quad_points_cp1[1]))
                p1_second_final_line = gs.Line((new_quad_points_cp1[2], new_quad_points_cp1[3]))

                p1_point_of_int_xy_plane = gops.intersection(p1_first_final_line, p1_second_final_line)

                if p1_point_of_int_xy_plane is not None:
                    within_poly_1 = gops.inside_polygon_test(new_quad_points_cp1, p1_point_of_int_xy_plane)
                if within_poly_1:
                    final_xy_intersection_point = p1_point_of_int_xy_plane

            if polygon_2_convex_truth:
                within_poly_2 = False
                p2_first_final_line = gs.Line((new_quad_points_cp2[0], new_quad_points_cp2[1]))
                p2_second_final_line = gs.Line((new_quad_points_cp2[2], new_quad_points_cp2[3]))

                p2_point_of_int_xy_plane = gops.intersection(p2_first_final_line, p2_second_final_line)

                if p2_point_of_int_xy_plane is not None:
                    within_poly_2 = gops.inside_polygon_test(new_quad_points_cp2, p2_point_of_int_xy_plane)

                if within_poly_2:
                    final_xy_intersection_point = p2_point_of_int_xy_plane

        elif len(final_points_xy_plane) == 4:
                # four points directly

                within_polygon = False

                polygon_is_convex = gops.convex_check(final_points_xy_plane)

                if polygon_is_convex:
                    first_final_line = gs.Line((final_points_xy_plane[0], final_points_xy_plane[2]))
                    second_final_line = gs.Line((final_points_xy_plane[1], final_points_xy_plane[3]))

                    point_of_intersection_xy = gops.intersection(first_final_line, second_final_line)

                    if point_of_intersection_xy is not None:
                        within_polygon = gops.inside_polygon_test(final_points_xy_plane, point_of_intersection_xy)

                    if within_polygon:
                        final_xy_intersection_point = point_of_intersection_xy

        else:
            print 'not enough data to compute xy plane co ordinates'
            final_xy_intersection_point = False

        incr_entry += 1

    # print 'xy calculations done'
    ######################################## END OF XY PLANE CODE ##################################################

    incr_entry = 1
    while final_yz_intersection_point is None and incr_entry < len(all_distances_set_yz_plane):
        # print 'here'
        short_line_1_yz_plane = all_distances_set_yz_plane[0][1]
        short_line_2_yz_plane = all_distances_set_yz_plane[incr_entry][1]

        temp_list_yz_plane = short_line_1_yz_plane + short_line_2_yz_plane
        (common_point_yz_plane, final_points_yz_plane) = gops.cp_finder(temp_list_yz_plane)

        if len(final_points_yz_plane) == 3:
            (close_point_1, close_point_2) = gops.get_fourth_point_yz_plane(line1, line2, common_point_yz_plane)

            new_quad_points_cp1 = final_points_yz_plane + [close_point_1]
            new_quad_points_cp2 = final_points_yz_plane + [close_point_2]

            polygon_1_convex_truth = gops.convex_check(new_quad_points_cp1)
            polygon_2_convex_truth = gops.convex_check(new_quad_points_cp2)

            if polygon_1_convex_truth:
                within_poly_1 = False

                p1_first_final_line = gs.Line((new_quad_points_cp1[0], new_quad_points_cp1[1]))
                p1_second_final_line = gs.Line((new_quad_points_cp1[2], new_quad_points_cp1[3]))

                p1_point_of_int_yz_plane = gops.intersection(p1_first_final_line, p1_second_final_line)

                if p1_point_of_int_yz_plane is not None:
                    within_poly_1 = gops.inside_polygon_test(new_quad_points_cp1, p1_point_of_int_yz_plane)

                if within_poly_1:
                    final_yz_intersection_point = p1_point_of_int_yz_plane

            if polygon_2_convex_truth:
                within_poly_2 = False
                p2_first_final_line = gs.Line((new_quad_points_cp2[0], new_quad_points_cp2[1]))
                p2_second_final_line = gs.Line((new_quad_points_cp2[2], new_quad_points_cp2[3]))

                p2_point_of_int_yz_plane = gops.intersection(p2_first_final_line, p2_second_final_line)

                if p2_point_of_int_yz_plane is not None:
                    within_poly_2 = gops.inside_polygon_test(new_quad_points_cp2, p2_point_of_int_yz_plane)

                if within_poly_2:
                    final_yz_intersection_point = p2_point_of_int_yz_plane
        elif len(final_points_yz_plane) == 4:
                # four points directly
                # print 'Enter Hilarity'
                # print final_points_yz_plane
                within_polygon = False

                polygon_is_convex = gops.convex_check(final_points_yz_plane)

                if polygon_is_convex:
                    first_final_line = gs.Line((final_points_yz_plane[0], final_points_yz_plane[2]))
                    second_final_line = gs.Line((final_points_yz_plane[1], final_points_yz_plane[3]))

                    point_of_intersection_yz = gops.intersection(first_final_line, second_final_line)

                    if point_of_intersection_yz is not None:
                        within_polygon = gops.inside_polygon_test(final_points_yz_plane, point_of_intersection_yz)

                    if within_polygon:
                        final_yz_intersection_point = point_of_intersection_yz
        else:
            print 'not enough data to compute yz plane co ordinates'
            final_yz_intersection_point = False

        incr_entry += 1

    # print 'yz calculations done'
    ######################################## END OF YZ PLANE CODE ##################################################

    incr_entry = 1
    while final_zx_intersection_point is None and incr_entry < len(all_distances_set_zx_plane):

        short_line_1_zx_plane = all_distances_set_zx_plane[0][1]
        short_line_2_zx_plane = all_distances_set_zx_plane[incr_entry][1]

        temp_list_zx_plane = short_line_1_zx_plane + short_line_2_zx_plane
        (common_point_zx_plane, final_points_zx_plane) = gops.cp_finder(temp_list_zx_plane)
        if len(final_points_zx_plane) == 3:
            (close_point_1, close_point_2) = gops.get_fourth_point_zx_plane(line1, line2, common_point_zx_plane)

            new_quad_points_cp1 = final_points_zx_plane + [close_point_1]
            new_quad_points_cp2 = final_points_zx_plane + [close_point_2]

            polygon_1_convex_truth = gops.convex_check(new_quad_points_cp1)
            polygon_2_convex_truth = gops.convex_check(new_quad_points_cp2)

            if polygon_1_convex_truth:
                within_poly_1 = False

                p1_first_final_line = gs.Line((new_quad_points_cp1[0], new_quad_points_cp1[1]))
                p1_second_final_line = gs.Line((new_quad_points_cp1[2], new_quad_points_cp1[3]))

                p1_point_of_int_zx_plane = gops.intersection(p1_first_final_line, p1_second_final_line)

                if p1_point_of_int_zx_plane is not None:
                    within_poly_1 = gops.inside_polygon_test(new_quad_points_cp1, p1_point_of_int_zx_plane)

                if within_poly_1:
                    final_zx_intersection_point = p1_point_of_int_zx_plane

            if polygon_2_convex_truth:
                within_poly_2 = False
                p2_first_final_line = gs.Line((new_quad_points_cp2[0], new_quad_points_cp2[1]))
                p2_second_final_line = gs.Line((new_quad_points_cp2[2], new_quad_points_cp2[3]))

                p2_point_of_int_zx_plane = gops.intersection(p2_first_final_line, p2_second_final_line)

                if p2_point_of_int_zx_plane is not None:
                    within_poly_2 = gops.inside_polygon_test(new_quad_points_cp2, p2_point_of_int_zx_plane)

                if within_poly_2:
                    final_zx_intersection_point = p2_point_of_int_zx_plane

        elif len(final_points_zx_plane) == 4:
                within_polygon = False

                polygon_is_convex = gops.convex_check(final_points_zx_plane)

                if polygon_is_convex:
                    first_final_line = gs.Line((final_points_zx_plane[0], final_points_zx_plane[2]))
                    second_final_line = gs.Line((final_points_zx_plane[1], final_points_zx_plane[3]))

                    point_of_intersection_zx = gops.intersection(first_final_line, second_final_line)

                    if point_of_intersection_zx is not None:
                        within_polygon = gops.inside_polygon_test(final_points_zx_plane, point_of_intersection_zx)

                    if within_polygon:
                        final_zx_intersection_point = point_of_intersection_zx

        else:
            print 'not enough data to compute zx plane co ordinates'
            final_zx_intersection_point = False
        incr_entry += 1

    # print 'zx calculations done'
    ######################################## END OF ZX PLANE CODE ##################################################
    final_points = [final_xy_intersection_point, final_yz_intersection_point, final_zx_intersection_point]
    return final_points
