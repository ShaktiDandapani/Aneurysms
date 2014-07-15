import math
import sympy as sp
from operator import itemgetter


def minimum_distance_sort(simple_distances):
    """
    # # sorts a dictionary in ascending order for keys.
    # distance dict should be of the form
    #
    # --> { 'distance':
    #             [ point1_line1, point2_line1, point1_line2, point2_line2]
    #     }
    #     each point is of the form [x,y]

    :param distance_dict:
    :return sorted distance_dict:
    """
    #
    # final_set = sorted(distance_dict.iteritems())
    # print 'dicationary of distances >> ', final_set

    final_set = sorted(simple_distances, key=itemgetter(0))
    # print '>>', final_set

    return final_set


def cp_finder(temp_list):
    """
    checks if there is a common point.
    1. if there is returns a common point and the list of points with it
    2. if no common point returns the original list back

    :param temp_list:
    :return common_point, set_list_of_points:
    """
    print 'wo set', temp_list
    p_set = set(map(tuple, temp_list))
    unique_points = map(list, p_set)
    print 'with set', temp_list,'<>', unique_points
    intermediary_dict = {}

    for point in temp_list:
        if tuple(point) in intermediary_dict:
            intermediary_dict[tuple(point)] += 1
        else:
            intermediary_dict[tuple(point)] = 1

    print 'common_point dictionary', intermediary_dict

    common_point = ''

    # if v == 1 what then -->
    for k, v in intermediary_dict.iteritems():
        if v == 2:
            common_point = k

    if common_point != '':
        unique_points.remove(list(common_point))
        print '>>>', unique_points + [list(common_point)]

        set_list_of_points = unique_points + [list(common_point)]
    else:
        set_list_of_points = temp_list

    return common_point, set_list_of_points


def cp_point_of_intersection(four_possible_points):
    """
    finds the point of intersection

    :param four_possible_points:
    :return:
    """

    line1_p1 = sp.Point(four_possible_points[0])
    line1_p2 = sp.Point(four_possible_points[1])

    line2_p1 = sp.Point(four_possible_points[2])
    line2_p2 = sp.Point(four_possible_points[3])

    l1 = sp.Line(line1_p1, line1_p2)
    l2 = sp.Line(line2_p1, line2_p2)

    ## Below make a loop if point found set flag to true else incr_entry += 1
    #print 'point of intersection', sp.intersection(l1, l2)
    point_of_intersection_xy_list = sp.intersection(l1, l2)
    point_of_intersection_xy = point_of_intersection_xy_list[0]
    print 'xy plane point of intersection', point_of_intersection_xy

    # point_one = sp.Point(four_possible_points[0])
    # point_two = sp.Point(four_possible_points[1])
    # point_three = sp.Point(four_possible_points[2])
    # point_four = sp.Point(four_possible_points[3])
    #
    # area_original_polygon = sp.Polygon(point_one, point_two, point_three, point_four).area
    #
    # triangle_one = sp.Triangle(point_one, point_two, point_of_intersection_xy)
    # triangle_two = sp.Triangle(point_two, point_three, point_of_intersection_xy)


def get_dist_dict_xy(line1, line2):
    """
    # takes in the lines and provides the distance dictionaries for all planes
    # -> { eu_dist:
            [line1, line2]
        }  --> line1 = [x1, y1], line2 = [x2, y2]

    :param line1:
    :param line2:
    :return:
    """
    simple_distances = []
    # distance_dict_xy_plane = {}
    for point1 in line1:
        for point2 in line2:
            within_sqrt = (pow((point1.x - point2.x), 2) + pow((point1.y - point2.y), 2))
            euclidean_distance = round(math.sqrt(within_sqrt), 3)
            # print 'distance: ', euclidean_distance
            line1_points = [point1.x, point1.y]
            line2_points = [point2.x, point2.y]
            line_points = [line1_points, line2_points]

            #print line1_points, line2_points
            if euclidean_distance > 0:
                simple_distances.append([euclidean_distance, line_points])
                # distance_dict_xy_plane[euclidean_distance] = line_points

    print 'yaha', simple_distances
    return simple_distances


def get_dist_dict_yz(line1, line2):
    """

    :param line1:
    :param line2:
    :return:
    """
    simple_distances = []
    # distance_dict_yz_plane = {}
    for point1 in line1:
        for point2 in line2:
            within_sqrt = (pow((point1.y - point2.y), 2) + pow((point1.z - point2.z), 2))
            euclidean_distance = round(math.sqrt(within_sqrt), 3)
            line1_points = [point1.y, point1.z]
            line2_points = [point2.y, point2.z]
            line_points = [line1_points, line2_points]
            if euclidean_distance > 0:
                simple_distances.append([euclidean_distance, line_points])
                # distance_dict_yz_plane[euclidean_distance] = line_points

    return simple_distances


def get_dist_dict_zx(line1, line2):
    """

    :param line1:
    :param line2:
    :return:
    """
    simple_distances = []
    # distance_dict_zx_plane = {}
    for point1 in line1:
        for point2 in line2:
            within_sqrt = (pow((point1.z - point2.z), 2) + pow((point1.x - point2.x), 2))
            euclidean_distance = round(math.sqrt(within_sqrt), 3)
            line1_points = [point1.z, point1.x]
            line2_points = [point2.z, point2.x]
            line_points = [line1_points, line2_points]
            if euclidean_distance > 0:
                simple_distances.append([euclidean_distance, line_points])
                # distance_dict_zx_plane[euclidean_distance] = line_points

    return simple_distances


################################################################################################################

#                            CURRENTLY WORK ON PART BELOW                                                      #

################################################################################################################
def get_fourth_point_xy_plane(line1, line2, common_point, cp_dist_dict_line1, cp_dist_dict_line2):
    """
    :param line1:
    :param line2:
    :param set_of_final_points:
    :param common_point:
    :param cp_dist_dict_line1:
    :param cp_dist_dict_line2:
    :return:
    """
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
                    # print sort_stuff
                    cp_closest_point_1 = sort_stuff[0][1][0]
                    cp_closest_point_2 = sort_stuff[1][1][0]

                    return cp_closest_point_1, cp_closest_point_2

    for point_b in line2:
                if point_b.x == common_point[0] and point_b.y == common_point[1]:
                    # print 'cp present in 2nd line'
                    for point in line2:
                        in_root = (pow((point.x - common_point[0]), 2) + pow((point.y - common_point[1]), 2))
                        distance = round(math.sqrt(in_root), 3)
                        line_point = [point.x, point.y]
                        cp_point = [common_point[0], common_point[1]]
                        if distance > 0.0:
                            cp_dist_dict_line2[distance] = [line_point, cp_point]

                    # set_of_final_points <-- add the point which forms the convex set to this
                    sort_stuff = sorted(cp_dist_dict_line2.iteritems(), reverse=False)
                    # print sort_stuff
                    cp_closest_point_1 = sort_stuff[0][1][0]
                    cp_closest_point_2 = sort_stuff[1][1][0]

                    return cp_closest_point_1, cp_closest_point_2

    # if polygon_cp1.is_convex():
    #
    #     print polygon_cp1.is_convex()
    #     return new_quad_points_cp1
    #
    # else:
    #     print 'quad with closest point 1 is concave'
    #
    # if polygon_cp2.is_convex():
    #
    #     print polygon_cp2.is_convex()
    #     return new_quad_points_cp2
    #
    # else:
    #     print'quad with closest point 2 is concave'
    # # insert the point in the final point --> will get 2 lists for 2 points on either sidem then do convex
    # # testing and insert the one forming the convex