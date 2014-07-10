import math
from sympy.geometry import polygon as poly
import point3D as p3D
import formulae_math as fmath
import plot_overlap as diagrams


def main():

    line1 = [p3D.Point3D(1, 3, 1), p3D.Point3D(3, 4, 2), p3D.Point3D(5, 4, 3), p3D.Point3D(6, 4, 4), p3D.Point3D(7 ,2, 5)]
    line2 = [p3D.Point3D(1, 5, 4), p3D.Point3D(2, 4, 3), p3D.Point3D(4, 3, 2), p3D.Point3D(5, 3, 1)]

    distance_dict_xy_plane = {}
    distance_dict_yz_plane = {}
    distance_dict_zx_plane = {}

    # for now X and Y co ordinates --> make a separate function which takes in Point3D
    for point1 in line1:
        for point2 in line2:
            within_sqrt = (pow((point1.x - point2.x), 2) + pow((point1.y - point2.y), 2))
            euclidean_distance = round(math.sqrt(within_sqrt), 3)
            line1_points = [point1.x, point1.y]
            line2_points = [point2.x, point2.y]
            line_points = [line1_points, line2_points]
            #print line1_points, line2_points
            if euclidean_distance > 0:
                distance_dict_xy_plane[euclidean_distance] = line_points

    print distance_dict_xy_plane
    #print distance_dict_xy_plane
    ## For yz plane
    for point1 in line1:
        for point2 in line2:
            within_sqrt = (pow((point1.y - point2.y), 2) + pow((point1.z - point2.z), 2))
            euclidean_distance = round(math.sqrt(within_sqrt), 3)
            line1_points = [point1.y, point1.z]
            line2_points = [point2.y, point2.z]
            line_points = [line1_points, line2_points]
            if euclidean_distance > 0:
                distance_dict_yz_plane[euclidean_distance] = line_points

    ## For zx plane
    for point1 in line1:
        for point2 in line2:
            within_sqrt = (pow((point1.z - point2.z), 2) + pow((point1.x - point2.x), 2))
            euclidean_distance = round(math.sqrt(within_sqrt), 3)
            line1_points = [point1.z, point1.x]
            line2_points = [point2.z, point2.x]
            line_points = [line1_points, line2_points]
            if euclidean_distance > 0:
                distance_dict_zx_plane[euclidean_distance] = line_points

    point_of_int_flag = False

    while not point_of_int_flag :
        #function to obtain 2 shortest lines
        # make it return the entire list and select the distances based on need.
        [all_distances_set, short_line_1, short_line_2] = fmath.minimum_distance_sort(distance_dict_xy_plane)

        for x in all_distances_set:
            print '>>>', x
        #Set of points after common point or with no common point
        #points_set = set(short_line_1)
        temp_list = []
        temp_list.extend(short_line_1)
        temp_list.extend(short_line_2)
        print 'Points from shortest distance>>', temp_list

        # if common point check presence in line sets --> and then do the distance finding to get the next point
        # which forms the convex quadrilateral
        [common_point, set_of_final_points] = fmath.cp_finder(temp_list)
        print 'common_point', common_point

        print 'final points', set_of_final_points

        # This is for 3 poiints --> make another loop for 4 points
        cp_dist_dict_line1 = {}
        cp_dist_dict_line2 = {}

        # Again for the x-y plane
        if len(set_of_final_points) == 3:
            for point_a in line1:
                if point_a.x == common_point[0] and point_a.y == common_point[1]:
                    print 'cp present in 1st line'
                    for point in line1:
                        in_root = (pow((point.x - common_point[0]), 2) + pow((point.y - common_point[1]), 2))
                        distance = round(math.sqrt(in_root), 3)
                        line_point = [point.x, point.y]
                        cp_point = [common_point[0], common_point[1]]
                        if distance > 0.0:
                            cp_dist_dict_line1[distance] = [line_point, cp_point]

                    # set_of_final_points <-- add the point which forms the convex set to this
                    sort_stuff = sorted(cp_dist_dict_line1.iteritems(), reverse=False)
                    print sort_stuff
                    cp_closest_point_1 = sort_stuff[0][1][0]
                    cp_closest_point_2 = sort_stuff[1][1][0]

                    print 'closest points to (', common_point[0], common_point[1], ') :'
                    print cp_closest_point_1, ' & ', cp_closest_point_2

            for point_b in line2:
                if point_b.x == common_point[0] and point_b.y == common_point[1]:
                    print 'cp present in 2nd line'
                    for point in line2:
                        in_root = (pow((point.x - common_point[0]), 2) + pow((point.y - common_point[1]), 2))
                        distance = round(math.sqrt(in_root), 3)
                        line_point = [point.x, point.y]
                        cp_point = [common_point[0], common_point[1]]
                        if distance > 0.0:
                            cp_dist_dict_line2[distance] = [line_point, cp_point]

                    # set_of_final_points <-- add the point which forms the convex set to this
                    sort_stuff = sorted(cp_dist_dict_line2.iteritems(), reverse=False)
                    print sort_stuff
                    cp_closest_point_1 = sort_stuff[0][1][0]
                    cp_closest_point_2 = sort_stuff[1][1][0]

                    print 'closest points to (', common_point[0], common_point[1], ') :'
                    print cp_closest_point_1, ' & ', cp_closest_point_2


                    new_quad_points_cp1 = set_of_final_points + [cp_closest_point_1]
                    new_quad_points_cp2 = set_of_final_points + [cp_closest_point_2]

                    print 'new lists are'
                    print 'list 1:', new_quad_points_cp1
                    print 'list 2:', new_quad_points_cp2

                    polygon_cp1 = poly.Polygon(*new_quad_points_cp1)
                    polygon_cp2 = poly.Polygon(*new_quad_points_cp2)

                    # convex check
                    # try plotting it out
                    if polygon_cp1.is_convex():
                        print polygon_cp1.is_convex()
                    else:
                        print 'quad with cp1 is concave'

                    if polygon_cp2.is_convex():
                        print polygon_cp2.is_convex()
                    else:
                        print'quad with cp2 is concave'

            # insert the point in the final point --> will get 2 lists for 2 points on either sidem then do convex
            # testing and insert the one forming the convex
        else:
            # four points directly
            quad_points = set_of_final_points
            # do convex checks etc..
            print 'no common point'

        #The line below should be after we find a point of intersection
        point_of_int_flag = True

        #here Increment the dictionary for the next side discarding the larger line from the two short_lines

    ## Plots below
    #Plot the figures

    diagrams.original_lines(line1, line2)


main()