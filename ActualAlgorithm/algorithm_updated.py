from sympy.geometry import polygon as poly
import sympy as sp
import geomstruct as gs
import formulae_math as fmath
import plot_overlap as diagrams


def main():

    line1 = [gs.Point3D(2, 3, 1), gs.Point3D(3, 4, 2), gs.Point3D(5, 4, 3), gs.Point3D(7, 4, 4)]
    # line1 = [p3D.Point3D(1, 3, 1), p3D.Point3D(3, 4, 2), p3D.Point3D(5, 4, 3), p3D.Point3D(6, 5, 4)]
    line2 = [gs.Point3D(1, 5, 4), gs.Point3D(2, 4, 3), gs.Point3D(4, 3, 2), gs.Point3D(5, 3, 1)]

    distance_list_xy_plane = fmath.get_dist_dict_xy(line1, line2)
    distance_dict_yz_plane = fmath.get_dist_dict_yz(line1, line2)
    distance_dict_zx_plane = fmath.get_dist_dict_zx(line1, line2)

    point_of_int__xy_plane_flag = False
    point_of_int__yz_plane_flag = False
    point_of_int__zx_plane_flag = False


    incr_entry = 1
    while not point_of_int__xy_plane_flag:

        #function to obtain 2 shortest lines
        # make it return the entire list and select the distances based on need.
        all_distances_set_xy_plane = fmath.minimum_distance_sort(distance_list_xy_plane)

        """
        put a check for length of the incr_entry to be less than the length of the all_distances_set_xy_plane
        """

        # print type(all_distances_set_xy_plane)
        print '+' * 30
        print all_distances_set_xy_plane
        print '+' * 30
        short_line_1_xy_plane = all_distances_set_xy_plane[0][1]
        short_line_2_xy_plane = all_distances_set_xy_plane[incr_entry][1]

        print short_line_1_xy_plane
        print short_line_2_xy_plane

        #Set of points after common point or with no common point
        #points_set = set(short_line_1_xy_plane)
        temp_list_xy_plane = short_line_1_xy_plane + short_line_2_xy_plane

        print 'Points for two shortest distance>> xy plane: ', temp_list_xy_plane

        # if common point check presence in line sets --> and then do the distance finding to get the next point
        # which forms the convex quadrilateral
        [common_point_xy_plane, final_points_xy_plane] = fmath.cp_finder(temp_list_xy_plane)

        print 'common_point_xy_plane', common_point_xy_plane
        print 'final points xy plane', final_points_xy_plane

        # This is for 3 points --> make another loop for 4 points
        cp_dist_dict_line1_xy_plane = {}
        cp_dist_dict_line2_xy_plane = {}

        # the for loops are for both lines to check for near point of the cp if they belong to either of the 2 lines
        # Again for the x-y plane
        if len(final_points_xy_plane) == 3:
            print 'enter'
            [close_point_1, close_point_2] = fmath.get_fourth_point_xy_plane(line1, line2, common_point_xy_plane,
                                                                             cp_dist_dict_line1_xy_plane,
                                                                             cp_dist_dict_line2_xy_plane)

            # supply closest points and final set points to a function which returns whether
            # it is convex, triangle etc and then find the point of intersection and make the further
            # calculations

            ## Below make a function to return the convex points
            print 'closest points to (', common_point_xy_plane[0], common_point_xy_plane[1], ') :'
            print close_point_1, ' & ', close_point_2

            new_quad_points_cp1 = final_points_xy_plane + [close_point_1]
            new_quad_points_cp2 = final_points_xy_plane + [close_point_2]

            print 'new lists are'
            print 'list 1:', new_quad_points_cp1
            print 'list 2:', new_quad_points_cp2

        else:
            # four points directly
            print 'points without commmon points', final_points_xy_plane
            # do convex checks etc..
            print 'for four points'



        ######################################## END OF XY PLANE CODE ##################################################

        #The line below should be after we find a point of intersection

        # put line below in if loop
        point_of_int__xy_plane_flag = True
        #
        # else:
        #     print 'no intersection for current points'
        #     incr_entry += 1

    ## Plots below
    #Plot the figures
    # dummy below till code is checkd
    # point_of_intersection_xy = sp.Point(2, 3)
    # diagrams.original_lines(line1, line2, point_of_intersection_xy)


main()
