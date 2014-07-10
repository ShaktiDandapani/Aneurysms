import math
from sympy.geometry import polygon as poly
import point3D as p3D
import formulae_math as fmath
import plot_overlap as diagrams


def main():

    line2 = [p3D.Point3D(1, 3, 1), p3D.Point3D(3, 4, 2), p3D.Point3D(5, 4, 3), p3D.Point3D(6, 4, 4)]
    line1 = [p3D.Point3D(1, 5, 4), p3D.Point3D(2, 4, 3), p3D.Point3D(4, 3, 2), p3D.Point3D(5, 3, 1)]

    distance_dict_xy_plane = fmath.get_dist_dict_xy(line1, line2)
    distance_dict_yz_plane = fmath.get_dist_dict_yz(line1, line2)
    distance_dict_zx_plane = fmath.get_dist_dict_zx(line1, line2)

    # print distance_dict_xy_plane
    # print distance_dict_yz_plane
    # print distance_dict_zx_plane

    point_of_int_flag = False

    while not point_of_int_flag:
        incr_entry = 1
        #function to obtain 2 shortest lines
        # make it return the entire list and select the distances based on need.
        all_distances_set_xy_plane = fmath.minimum_distance_sort(distance_dict_xy_plane)
        all_distances_set_yz_plane = fmath.minimum_distance_sort(distance_dict_yz_plane)
        all_distances_set_zx_plane = fmath.minimum_distance_sort(distance_dict_zx_plane)
        # print all_distances_set_xy_plane
        # print all_distances_set_yz_plane
        # print all_distances_set_zx_plane

        short_line_1_xy_plane = all_distances_set_xy_plane[0][1]
        short_line_2_xy_plane = all_distances_set_xy_plane[incr_entry][1]

        short_line_1_yz_plane = all_distances_set_yz_plane[0][1]
        short_line_2_yz_plane = all_distances_set_yz_plane[incr_entry][1]

        short_line_1_zx_plane = all_distances_set_zx_plane[0][1]
        short_line_2_zx_plane = all_distances_set_zx_plane[incr_entry][1]

        #Set of points after common point or with no common point
        #points_set = set(short_line_1_xy_plane)
        temp_list_xy_plane = short_line_1_xy_plane + short_line_2_xy_plane
        temp_list_yz_plane = short_line_1_yz_plane + short_line_2_yz_plane
        temp_list_zx_plane = short_line_1_zx_plane + short_line_2_zx_plane

        # temp_list_xy_plane = []
        # temp_list_xy_plane.extend(short_line_1_xy_plane)
        # temp_list_xy_plane.extend(short_line_2_xy_plane)
        print 'Points for two shortest distance>> xy plane: ', temp_list_xy_plane
        print 'Points for two shortest distance>> yz plane: ', temp_list_yz_plane
        print 'Points for two shortest distance>> zx plane: ', temp_list_zx_plane

        # if common point check presence in line sets --> and then do the distance finding to get the next point
        # which forms the convex quadrilateral
        [common_point_xy_plane, final_points_xy_plane] = fmath.cp_finder(temp_list_xy_plane)
        [common_point_yz_plane, final_points_yz_plane] = fmath.cp_finder(temp_list_yz_plane)
        [common_point_zx_plane, final_points_zx_plane] = fmath.cp_finder(temp_list_zx_plane)

        print 'common_point_xy_plane', common_point_xy_plane
        print 'common_point_yz_plane', common_point_yz_plane
        print 'common_point_zx_plane', common_point_zx_plane

        print 'final points xy plane', final_points_xy_plane
        print 'final points yz plane', final_points_yz_plane
        print 'final points zx plane', final_points_zx_plane

        ################################################################################################################

        #                            CURRENTLY WORK ON PART BELOW                                                      #

        ################################################################################################################

        # This is for 3 poiints --> make another loop for 4 points
        cp_dist_dict_line1_xy_plane = {}
        cp_dist_dict_line2_xy_plane = {}

        # the for loops are for both lines to check for near point of the cp if they belong to either of the 2 lines
        # Again for the x-y plane
        if len(final_points_xy_plane) == 3:
            fmath.get_fourth_point_xy_plane(line1, line2, final_points_xy_plane, common_point_xy_plane,
                                            cp_dist_dict_line1_xy_plane, cp_dist_dict_line2_xy_plane)
        # if len(final_points_yz_plane) == 3:
        #     fmath.get_fourth_point_yz_plane(line1, line2, final_points_yz_plane, common_point_yz_plane,
        #                                   cp_dist_dict_line1_yz_plane, cp_dist_dict_line2_yz_plane)
        # if len(final_points_zx_plane) == 3:
        #     fmath.get_fourth_point_zx_plane(line1, line2, final_points_xy_plane, common_point_xy_plane,
        #                                   cp_dist_dict_line1_xy_plane, cp_dist_dict_line2_xy_plane)
        else:
            # four points directly
            quad_points = final_points_xy_plane
            # do convex checks etc..
            print 'for four points'

        #The line below should be after we find a point of intersection
        incr_entry += 1
        point_of_int_flag = True

        #here Increment the dictionary for the next side discarding the larger line from the two short_lines


    ## Plots below
    #Plot the figures

    diagrams.original_lines(line1, line2)


main()