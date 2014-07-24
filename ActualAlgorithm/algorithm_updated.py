import geomstruct as gs
import geomoperations as gops
import geomplot as diagrams


def main():
    final_xy_intersection_point = None
    final_yz_intersection_point = None
    final_zx_intersection_point = None

    # line1 = [gs.Point3D(2, 3, 5), gs.Point3D(3, 4, 6), gs.Point3D(5, 4, 3), gs.Point3D(7, 4, 1), gs.Point3D(2, 5, 5)]
    # line2 = [gs.Point3D(1, 5, 3), gs.Point3D(2, 4, 3), gs.Point3D(4, 3, 3), gs.Point3D(5, 3, 6)]
    # line2 = [gs.Point3D(7, 5, 3), gs.Point3D(3, 4, 5), gs.Point3D(4, 3, 3), gs.Point3D(5, 3, 6)]
    #
    '''
    xy calculations -> done good result
    '''
    # line1 = [gs.Point3D(0, 0, 0), gs.Point3D(0.79, 0.71, 0), gs.Point3D(1.57, 1, 0),
    #          gs.Point3D(2.35, 0.71, 0), gs.Point3D(3.14, 0, 0), gs.Point3D(3.93, -0.71, 0)]
    #
    # line2 = [gs.Point3D(0, -9.86, 0), gs.Point3D(0.5, -9.61, 0), gs.Point3D(1, -8.82, 0), gs.Point3D(2, -5.82, 0),
    #          gs.Point3D(3, -0.82, 0), gs.Point3D(4, 6.18, 0)]

    '''
    zx calculations -> done good result
    '''
    line1 = [gs.Point3D(1, 0, 0), gs.Point3D(1.5, 0, 0.18), gs.Point3D(2.0, 0, 0.3), gs.Point3D(2.5, 0, 0.40),
             gs.Point3D(3.0, 0, 0.48), gs.Point3D(3.5, 0, 0.54), gs.Point3D(4, 0, 0.60), gs.Point3D(4.5, 0, 0.65)]

    line2 = [gs.Point3D(1, 0, 2), gs.Point3D(1.5, 0, 1.3), gs.Point3D(2.0, 0, 1.0), gs.Point3D(2.5, 0, 0.8),
             gs.Point3D(3.0, 0, 0.66), gs.Point3D(3.5, 0, 0.57), gs.Point3D(4, 0, 0.5), gs.Point3D(4.5, 0, 0.44)]

    '''
    yz calculations -> errors for xy plane ....
    '''
    # line1 = [gs.Point3D(1, 0, 0), gs.Point3D(1.5, 0.18, 0), gs.Point3D(2.0, 0.3, 0), gs.Point3D(2.5, 0.4, 0),
    #          gs.Point3D(3.0, 0.47, 0), gs.Point3D(3.5, 0.54, 0), gs.Point3D(4, 0.6, 0), gs.Point3D(4.5, 0.65, 0)]
    #
    # line2 = [gs.Point3D(1, 2, 0), gs.Point3D(1.5, 1.3, 0), gs.Point3D(2.0, 1.0, 0), gs.Point3D(2.5, 0.8, 0),
    #          gs.Point3D(3.0, 0.66, 0), gs.Point3D(3.5, 0.57, 0), gs.Point3D(4, 0.5, 0), gs.Point3D(4.5, 0.44, 0)]

    distance_list_xy_plane = gops.get_dist_dict_xy(line1, line2)
    distance_list_yz_plane = gops.get_dist_dict_yz(line1, line2)
    distance_list_zx_plane = gops.get_dist_dict_zx(line1, line2)
    #
    # print distance_list_xy_plane
    # print distance_list_yz_plane
    # print distance_list_zx_plane
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
        # print 'this', final_xy_intersection_point

    if all_distances_set_xy_plane[0][0] == 0.0:
        final_yz_intersection_point = all_distances_set_yz_plane[0][1][0]
        # print 'this', final_yz_intersection_point

    if all_distances_set_zx_plane[0][0] == 0.0:
        final_zx_intersection_point = all_distances_set_zx_plane[0][1][0]
        # print 'this', final_zx_intersection_point

    incr_entry = 1
    while final_xy_intersection_point is None and incr_entry < len(all_distances_set_xy_plane):

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

                    if within_polygon:
                        final_xy_intersection_point = point_of_intersection_xy
        else:
            print 'not enough data to compute xy plane co ordinates'
            final_xy_intersection_point = False

        incr_entry += 1

    print 'xy calculations done'
    ######################################## END OF XY PLANE CODE ##################################################

    incr_entry = 1
    while final_yz_intersection_point is None and incr_entry < len(all_distances_set_yz_plane):

        short_line_1_yz_plane = all_distances_set_yz_plane[0][1]
        short_line_2_yz_plane = all_distances_set_yz_plane[incr_entry][1]

        temp_list_yz_plane = short_line_1_yz_plane + short_line_2_yz_plane
        [common_point_yz_plane, final_points_yz_plane] = gops.cp_finder(temp_list_yz_plane)

        if len(final_points_yz_plane) == 3:
            [close_point_1, close_point_2] = gops.get_fourth_point_yz_plane(line1, line2, common_point_yz_plane)

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

                    if within_polygon:
                        final_yz_intersection_point = point_of_intersection_yz
        else:
            print 'not enough data to compute yz plane co ordinates'
            final_yz_intersection_point = False

        incr_entry += 1

    print 'yz calculations done'
    ######################################## END OF YZ PLANE CODE ##################################################

    incr_entry = 1
    # print all_distances_set_zx_plane
    while final_zx_intersection_point is None and incr_entry < len(all_distances_set_zx_plane):

        short_line_1_zx_plane = all_distances_set_zx_plane[0][1]
        short_line_2_zx_plane = all_distances_set_zx_plane[incr_entry][1]

        temp_list_zx_plane = short_line_1_zx_plane + short_line_2_zx_plane
        [common_point_zx_plane, final_points_zx_plane] = gops.cp_finder(temp_list_zx_plane)
        # print temp_list_zx_plane
        if len(final_points_zx_plane) == 3:
            # print 'here', final_points_zx_plane
            [close_point_1, close_point_2] = gops.get_fourth_point_zx_plane(line1, line2, common_point_zx_plane)

            # print 'zx commom points,', common_point_zx_plane, ',  closest pts:  ', close_point_1, close_point_2
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
                # print '1: ', new_quad_points_cp1
                # print '2: ', new_quad_points_cp2
                p1_first_final_line = gs.Line((new_quad_points_cp1[0], new_quad_points_cp1[1]))
                p1_second_final_line = gs.Line((new_quad_points_cp1[2], new_quad_points_cp1[3]))
                #
                # print p1_first_final_line.point_1, p1_first_final_line.point_2
                # print p1_second_final_line.point_1, p1_second_final_line.point_2

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

                    if within_polygon:
                        final_zx_intersection_point = point_of_intersection_zx

        else:
            print 'not enough data to compute zx plane co ordinates'
            final_zx_intersection_point = False
        incr_entry += 1

    print 'zx calculations done'
    ######################################## END OF ZX PLANE CODE ##################################################

    # Plots below
    # Plot the figures
    print 'ok'
    print ' -------------------------------------|'
    print '|xy plane intersection: ', final_xy_intersection_point, '|'
    print '|yz plane intersection: ', final_yz_intersection_point, '|'
    print '|zx plane intersection: ', final_zx_intersection_point, '|'
    print ' -------------------------------------|'
    try:
        diagrams.original_lines(line1, line2, final_zx_intersection_point)\
            # , final_yz_intersection_point,
            #                     final_zx_intersection_point)
    except TypeError:
        print 'Need three points to plot'

main()
