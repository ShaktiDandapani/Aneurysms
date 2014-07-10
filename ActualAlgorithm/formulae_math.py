import math
from sympy.geometry import polygon as poly


# sorts a dictionary in ascending order for keys.
def minimum_distance_sort(distance_dict):
    #make this return two lists -> line1 and line2

    final_set = sorted(distance_dict.iteritems())

    # print 'checking ->', final_set[0][1]
    return final_set


# The function is used to find the common point amongst the four points.
def cp_finder(temp_list):
    d = {}

    for point in temp_list:
        if point[0] in d:
            d[point[0]] += point[1]
            result = [point[0], point[1]]
        else:
            d[point[0]] = point[1]
        ## Get the common points list

    p_set = set(map(tuple, temp_list))
    q_points = map(list, p_set)

    return result, q_points


# takes in the lines and provides the distance dictionaries for all planes
# -> {eu_dist: [line1, line2] }  --> line1 = [x1, y1], line2 = [x2, y2]

def get_dist_dict_xy(line1, line2):
    distance_dict_xy_plane = {}
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

    return distance_dict_xy_plane


def get_dist_dict_yz(line1, line2):
    distance_dict_yz_plane = {}
    for point1 in line1:
        for point2 in line2:
            within_sqrt = (pow((point1.y - point2.y), 2) + pow((point1.z - point2.z), 2))
            euclidean_distance = round(math.sqrt(within_sqrt), 3)
            line1_points = [point1.y, point1.z]
            line2_points = [point2.y, point2.z]
            line_points = [line1_points, line2_points]
            if euclidean_distance > 0:
                distance_dict_yz_plane[euclidean_distance] = line_points

    return distance_dict_yz_plane


def get_dist_dict_zx(line1, line2):
    distance_dict_zx_plane = {}
    for point1 in line1:
        for point2 in line2:
            within_sqrt = (pow((point1.z - point2.z), 2) + pow((point1.x - point2.x), 2))
            euclidean_distance = round(math.sqrt(within_sqrt), 3)
            line1_points = [point1.z, point1.x]
            line2_points = [point2.z, point2.x]
            line_points = [line1_points, line2_points]
            if euclidean_distance > 0:
                distance_dict_zx_plane[euclidean_distance] = line_points

    return distance_dict_zx_plane


################################################################################################################

#                            CURRENTLY WORK ON PART BELOW                                                      #

################################################################################################################
def get_fourth_point_xy_plane(line1, line2, set_of_final_points, common_point, cp_dist_dict_line1, cp_dist_dict_line2):

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
                        print 'quad with cp2 is concave'

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