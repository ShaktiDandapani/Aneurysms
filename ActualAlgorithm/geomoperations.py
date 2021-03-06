from __future__ import division
import math
import sympy as sp
from operator import itemgetter


def correct_order(x):
    """

    :param x:
    :return:
    """
    if x[0][0] == x[1][0]:
        if x[0][1] < x[1][1]:
            temp = x[0]
            x[0] = x[1]
            x[1] = temp

    if x[2][0] == x[3][0]:
        if x[2][1] < x[3][1]:
            x_temp = x[2]
            x[2] = x[3]
            x[3] = x_temp

    return x


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
    final_set = sorted(simple_distances, key=itemgetter(0))

    return final_set


def check_triangle(x):
    """

    :param x:
    :return:
    """
    triangle = sp.Polygon(*x)

    if type(triangle) == sp.Triangle:
        return True


def intersection(line1, line2):
    """

    :param line1:
    :param line2:
    :return:
    """


    p1 = line1.point_1
    p2 = line1.point_2

    p3 = line2.point_1
    p4 = line2.point_2

    x1 = p1[0]
    y1 = p1[1]

    x2 = p2[0]
    y2 = p2[1]

    x3 = p3[0]
    y3 = p3[1]

    x4 = p4[0]
    y4 = p4[1]

    x_num = round(float(((x1*y2 - y1*x2) * (x3 - x4) - (x1 - x2) * (x3*y4 - y3*x4))), 3)
    x_den = round(float(((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))), 3)

    y_num = round(float(((x1*y2 - y1*x2) * (y3 - y4) - (y1 - y2) * (x3*y4 - y3*x4))), 3)
    y_den = round(float(((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))), 3)
    try:
        poi_x = round(float(x_num / x_den), 3)
        poi_y = round(float(y_num / y_den), 3)
    except ZeroDivisionError:
        return None

    if (poi_x != 0.0) and (poi_y != 0.0):
        return tuple((round(float(poi_x), 3), round(float(poi_y), 3)))
    else:
        return None


def convex_check(polygon_points):
    """
    Checks whether four points form a convex polygon,
    using the theory that for every point angle formed with the others
    added with their sum is less than 360 degrees or pi radians.

    :param polygon_points:
    :return True/ False:
    """
    polygon_points = sorted(polygon_points, key=lambda x: (x[0], x[1]))
    # print 'it is these points', polygon_points
    a = polygon_points[0]
    b = polygon_points[1]
    c = polygon_points[2]
    d = polygon_points[3]
    # Vectors are in the form  AB = [ bx - ax, by - ay]
    # 0 1 2 3 --> a b c d

    ab = (b[0] - a[0], b[1] - a[1])
    ac = (c[0] - a[0], c[1] - a[1])
    ad = (d[0] - a[0], d[1] - a[1])
    # print 'a: ', a, 'b: ', b, 'd: ', d
    ba = (a[0] - b[0], a[1] - b[1])
    bc = (c[0] - b[0], c[1] - b[1])
    bd = (d[0] - b[0], d[1] - b[1])

    ca = (a[0] - c[0], a[1] - c[1])
    cb = (b[0] - c[0], b[1] - c[1])
    cd = (d[0] - c[0], d[1] - c[1])

    da = (a[0] - d[0], a[1] - d[1])
    db = (b[0] - d[0], b[1] - d[1])
    dc = (c[0] - d[0], c[1] - d[1])

    ## The _mod means the magnitude which is \sqrt(x^2 + y^2)
    ab_mod = round(math.sqrt((pow(ab[0], 2) + pow(ab[1], 2))), 1)
    ac_mod = round(math.sqrt((pow(ac[0], 2) + pow(ac[1], 2))), 1)
    ad_mod = round(math.sqrt((pow(ad[0], 2) + pow(ad[1], 2))), 1)

    ba_mod = round(math.sqrt((pow(ba[0], 2) + pow(ba[1], 2))), 1)
    bc_mod = round(math.sqrt((pow(bc[0], 2) + pow(bc[1], 2))), 1)
    bd_mod = round(math.sqrt((pow(bd[0], 2) + pow(bd[1], 2))), 1)

    ca_mod = round(math.sqrt((pow(ca[0], 2) + pow(ca[1], 2))), 1)
    cb_mod = round(math.sqrt((pow(cb[0], 2) + pow(cb[1], 2))), 1)
    cd_mod = round(math.sqrt((pow(cd[0], 2) + pow(cd[1], 2))), 1)
    # print cd[0], cd[1]
    # print 'here it is ', ca_mod, cb_mod, cd_mod
    da_mod = round(math.sqrt((pow(da[0], 2) + pow(da[1], 2))), 1)
    db_mod = round(math.sqrt((pow(db[0], 2) + pow(db[1], 2))), 1)
    dc_mod = round(math.sqrt((pow(dc[0], 2) + pow(dc[1], 2))), 1)

    ## Finally Calculating the dot product
    (theta_ab_ac_deg, theta_ab_ac_rad) = dp_vectors_angle(ab, ac, ab_mod, ac_mod)
    (theta_ab_ad_deg, theta_ab_ad_rad) = dp_vectors_angle(ab, ad, ab_mod, ad_mod)
    (theta_ac_ad_deg, theta_ac_ad_rad) = dp_vectors_angle(ac, ad, ac_mod, ad_mod)

    (theta_ba_bc_deg, theta_ba_bc_rad) = dp_vectors_angle(ba, bc, ba_mod, bc_mod)
    (theta_ba_bd_deg, theta_ba_bd_rad) = dp_vectors_angle(ba, bd, ba_mod, bd_mod)
    (theta_bc_bd_deg, theta_bc_bd_rad) = dp_vectors_angle(bc, bd, bc_mod, bd_mod)
    # print 'prob: ', ca_mod, cd_mod
    (theta_ca_cb_deg, theta_ca_cb_rad) = dp_vectors_angle(ca, cb, ca_mod, cb_mod)
    (theta_ca_cd_deg, theta_ca_cd_rad) = dp_vectors_angle(ca, cd, ca_mod, cd_mod)
    (theta_cb_cd_deg, theta_cb_cb_rad) = dp_vectors_angle(cb, cd, cb_mod, cd_mod)

    (theta_da_db_deg, theta_da_db_rad) = dp_vectors_angle(da, db, da_mod, db_mod)
    (theta_da_dc_deg, theta_da_dc_rad) = dp_vectors_angle(da, dc, da_mod, dc_mod)
    (theta_db_dc_deg, theta_db_dc_rad) = dp_vectors_angle(db, dc, dc_mod, db_mod)

    resultant_angle_a = theta_ab_ac_deg + theta_ab_ad_deg + theta_ac_ad_deg
    resultant_angle_b = theta_ba_bc_deg + theta_ba_bd_deg + theta_bc_bd_deg
    resultant_angle_c = theta_ca_cb_deg + theta_ca_cd_deg + theta_cb_cd_deg
    resultant_angle_d = theta_da_db_deg + theta_da_dc_deg + theta_db_dc_deg

    convex_angle_a = False
    convex_angle_b = False
    convex_angle_c = False
    convex_angle_d = False

    final_angle = False

    if resultant_angle_a < 360:
        convex_angle_a = True
    if resultant_angle_b < 360:
        convex_angle_b = True
    if resultant_angle_c < 360:
        convex_angle_c = True
    if resultant_angle_d < 360:
        convex_angle_d = True

    if (convex_angle_a is True) and (convex_angle_b is True) and (convex_angle_c is True) and (convex_angle_d is True):
        final_angle = True

    return final_angle


def dp_vectors_angle(a, b, mod_a, mod_b):
    """
    Returns the angle between two vectors in both degrees and
    radians.

    :param a:
    :param b:
    :param mod_a:
    :param mod_b:
    :return angle_degrees, angle_rads:
    """
    vec_mult = round(a[0] * b[0] + a[1] * b[1], 2)
    mod_mult = round(mod_a * mod_b, 2)

    try:
        division_calc = round(float(vec_mult / mod_mult), 2)
        # print '>>', division_calc
        if (division_calc <= 1.0) and (division_calc >= -1.0):
            theta_a_rad = round(math.acos(division_calc), 2)
        else:
            # theta_a_rad = 3.14
            theta_a_rad = 0.0
    except ZeroDivisionError:
        theta_a_rad = round(math.pi / 2, 2)

    theta_a_deg = round((theta_a_rad * 180) / math.pi, 2)

    return round(theta_a_deg, 3), round(theta_a_rad, 2)


def cp_finder(temp_list):
    """
    checks if there is a common point.
    1. if there is returns a common point and the list of points with it
    2. if no common point returns the original list back

    :param temp_list:
    :return common_point, set_list_of_points:
    """
    p_set = set(map(tuple, temp_list))
    unique_points = map(list, p_set)
    intermediary_dict = {}

    for point in temp_list:
        if tuple(point) in intermediary_dict:
            intermediary_dict[tuple(point)] += 1
        else:
            intermediary_dict[tuple(point)] = 1

    common_point = ''

    for k, v in intermediary_dict.iteritems():
        if v == 2:
            common_point = k

    if common_point != '':
        unique_points.remove(list(common_point))

        set_list_of_points = unique_points + [list(common_point)]
    else:
        set_list_of_points = temp_list
    # print 'check errors', set_list_of_points
    return common_point, set_list_of_points


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
            line1_points = (point1.x, point1.y)
            line2_points = (point2.x, point2.y)
            line_points = (line1_points, line2_points)

            #print line1_points, line2_points
            # if euclidean_distance > 0:
            simple_distances.append((euclidean_distance, line_points))
            # distance_dict_xy_plane[euclidean_distance] = line_points

    return tuple(simple_distances)


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
            line1_points = (point1.y, point1.z)
            line2_points = (point2.y, point2.z)
            line_points = (line1_points, line2_points)
            if euclidean_distance > 0:
                simple_distances.append((euclidean_distance, line_points))

    return tuple(simple_distances)


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
            line1_points = (point1.z, point1.x)
            line2_points = (point2.z, point2.x)
            line_points = (line1_points, line2_points)
            if euclidean_distance > 0:
                simple_distances.append((euclidean_distance, line_points))

    return tuple(simple_distances)


def get_fourth_point_xy_plane(line1, line2, common_point):
    """
    :param line1:
    :param line2:
    :param set_of_final_points:
    :param common_point:
    :param cp_dist_dict_line1:
    :param cp_dist_dict_line2:
    :return:
    """
    cp_dist_dict_line1 = {}
    cp_dist_dict_line2 = {}
    for point_a in line1:
        if point_a.x == common_point[0] and point_a.y == common_point[1]:
            for point in line1:
                in_root = (pow((point.x - common_point[0]), 2) + pow((point.y - common_point[1]), 2))
                distance = round(math.sqrt(in_root), 3)
                line_point = (point.x, point.y)
                cp_point = (common_point[0], common_point[1])
                if distance > 0.0:
                    cp_dist_dict_line1[distance] = (line_point, cp_point)

            sort_stuff = sorted(cp_dist_dict_line1.iteritems(), reverse=False)
            cp_closest_point_1 = sort_stuff[0][1][0]
            cp_closest_point_2 = sort_stuff[1][1][0]

            return cp_closest_point_1, cp_closest_point_2

    for point_b in line2:
        if point_b.x == common_point[0] and point_b.y == common_point[1]:
            for point in line2:
                in_root = (pow((point.x - common_point[0]), 2) + pow((point.y - common_point[1]), 2))
                distance = round(math.sqrt(in_root), 3)
                line_point = (point.x, point.y)
                cp_point = (common_point[0], common_point[1])
                if distance > 0.0:
                    cp_dist_dict_line2[distance] = (line_point, cp_point)

            sort_stuff = sorted(cp_dist_dict_line2.iteritems(), reverse=False)
            cp_closest_point_1 = sort_stuff[0][1][0]
            cp_closest_point_2 = sort_stuff[1][1][0]

            return cp_closest_point_1, cp_closest_point_2


def get_fourth_point_yz_plane(line1, line2, common_point):
    """

    remember common_point = [y, z]
    :param line1:
    :param line2:
    :param set_of_final_points:
    :param common_point:
    :param cp_dist_dict_line1:
    :param cp_dist_dict_line2:
    :return:
    """
    cp_dist_dict_line1 = {}
    cp_dist_dict_line2 = {}
    for point_a in line1:
        if point_a.y == common_point[0] and point_a.z == common_point[1]:
            for point in line1:
                in_root = (pow((point.y - common_point[0]), 2) + pow((point.z - common_point[1]), 2))
                distance = round(math.sqrt(in_root), 3)
                line_point = (point.y, point.z)
                cp_point = (common_point[0], common_point[1])
                if distance > 0.0:
                    cp_dist_dict_line1[distance] = (line_point, cp_point)

            sort_stuff = sorted(cp_dist_dict_line1.iteritems(), reverse=False)
            cp_closest_point_1 = sort_stuff[0][1][0]
            cp_closest_point_2 = sort_stuff[1][1][0]

            return cp_closest_point_1, cp_closest_point_2

    for point_b in line2:
        if point_b.y == common_point[0] and point_b.z == common_point[1]:
            for point in line2:
                in_root = (pow((point.y - common_point[0]), 2) + pow((point.z - common_point[1]), 2))
                distance = round(math.sqrt(in_root), 3)
                line_point = (point.y, point.z)
                cp_point = (common_point[0], common_point[1])
                if distance > 0.0:
                    cp_dist_dict_line2[distance] = (line_point, cp_point)

            sort_stuff = sorted(cp_dist_dict_line2.iteritems(), reverse=False)
            cp_closest_point_1 = sort_stuff[0][1][0]
            cp_closest_point_2 = sort_stuff[1][1][0]

            return cp_closest_point_1, cp_closest_point_2


def get_fourth_point_zx_plane(line1, line2, common_point):
    """

    remember common_point = [z, x]
    :param line1:
    :param line2:
    :param set_of_final_points:
    :param common_point:
    :param cp_dist_dict_line1:
    :param cp_dist_dict_line2:
    :return:
    """
    cp_dist_dict_line1 = {}
    cp_dist_dict_line2 = {}

    # print 'cp: ', common_point
    for point_a in line1:
        # print point_a.z, point_a.x, 'vs ', common_point
        if point_a.z == common_point[0] and point_a.x == common_point[1]:
            for point in line1:
                in_root = (pow((point.z - common_point[0]), 2) + pow((point.x - common_point[1]), 2))
                distance = round(math.sqrt(in_root), 3)
                line_point = (point.z, point.x)
                cp_point = (common_point[0], common_point[1])
                if distance > 0.0:
                    cp_dist_dict_line1[distance] = (line_point, cp_point)

            sort_stuff = sorted(cp_dist_dict_line1.iteritems(), reverse=False)
            cp_closest_point_1 = sort_stuff[0][1][0]
            cp_closest_point_2 = sort_stuff[1][1][0]

            return cp_closest_point_1, cp_closest_point_2
        # print 'not found'

    for point_b in line2:
        if point_b.z == common_point[0] and point_b.x == common_point[1]:
            for point in line2:
                in_root = (pow((point.z - common_point[0]), 2) + pow((point.x - common_point[1]), 2))
                distance = round(math.sqrt(in_root), 3)
                line_point = (point.z, point.x)
                cp_point = (common_point[0], common_point[1])
                if distance > 0.0:
                    cp_dist_dict_line2[distance] = (line_point, cp_point)

            sort_stuff = sorted(cp_dist_dict_line2.iteritems(), reverse=False)
            cp_closest_point_1 = sort_stuff[0][1][0]
            cp_closest_point_2 = sort_stuff[1][1][0]

            return cp_closest_point_1, cp_closest_point_2

"""
below are functions for inside outside pollygon and tirangle area etc
"""


def inside_polygon_test(poly_points, ext_point):
    """
    Checks whether a point is within or without four points on a co-ordinate plane.
    Uses the theory of area of the triangles formed with every point by the external point is greater than
    the area of the convex polygon for an external point.

    :param poly_points:
    :param ext_point:
    :return True/ False: for inside a polygon
    """
    #  Area_ext > Area_poly --> outside
    #  Area_ext < Area_poly --> inside
    #  Area_ext = Area_poly --> on the poly

    triangle_1_pts = [ext_point, poly_points[0], poly_points[1]]
    triangle_2_pts = [ext_point, poly_points[1], poly_points[2]]
    triangle_3_pts = [ext_point, poly_points[2], poly_points[3]]
    triangle_4_pts = [ext_point, poly_points[0], poly_points[3]]

    (at1, bt1, ct1) = sides_of_a_triangle(triangle_1_pts)
    (at2, bt2, ct2) = sides_of_a_triangle(triangle_2_pts)
    (at3, bt3, ct3) = sides_of_a_triangle(triangle_3_pts)
    (at4, bt4, ct4) = sides_of_a_triangle(triangle_4_pts)

    area_triangle_1 = round(area_triangle(at1, bt1, ct1), 2)
    area_triangle_2 = round(area_triangle(at2, bt2, ct2), 2)
    area_triangle_3 = round(area_triangle(at3, bt3, ct3), 2)
    area_triangle_4 = round(area_triangle(at4, bt4, ct4), 2)

    area_of_triangles_ext = area_triangle_1 + area_triangle_2 + area_triangle_3 + area_triangle_4

    poly_triangle_1 = (poly_points[0], poly_points[1], poly_points[3])
    poly_triangle_2 = (poly_points[1], poly_points[2], poly_points[3])

    (pt1, qt1, rt1) = sides_of_a_triangle(poly_triangle_1)
    (pt2, qt2, rt2) = sides_of_a_triangle(poly_triangle_2)

    area_polytri_1 = area_triangle(pt1, qt1, rt1)
    area_polytri_2 = area_triangle(pt2, qt2, rt2)

    area_of_polygon = area_polytri_1 + area_polytri_2

    if area_of_triangles_ext > area_of_polygon:
        inside_truth_value = False
    else:
        inside_truth_value = True
    return inside_truth_value


def sides_of_a_triangle(tri_points):
    """
    obtain the sides of the triangle from three points to be used in
    calculations such as area, perimeter etc.

    :param tri_points:
    :return:
    """
    x = tri_points[0]
    y = tri_points[1]
    z = tri_points[2]
    # print x, y, z
    side_xy = round(math.sqrt(pow(y[0] - x[0], 2) + pow(y[1] - x[1], 2)), 2)
    side_yz = round(math.sqrt(pow(z[0] - y[0], 2) + pow(z[1] - y[1], 2)), 2)
    side_zx = round(math.sqrt(pow(x[0] - z[0], 2) + pow(x[1] - z[1], 2)), 2)

    return side_xy, side_yz, side_zx


def area_triangle(a, b, c):
    """
    a, b, c are lengths of the sides

    :param a:
    :param b:
    :param c:
    :return:
    """

    # s = round(float((a + b + c) / 2), 3)
    s = round(float((a + b + c) / 2), 3)
    under_root = s * (s - a) * (s - b) * (s - c)

    if under_root > 0.0:
        area = round(math.sqrt(under_root), 3)
    else:
        area = 0

    return area

