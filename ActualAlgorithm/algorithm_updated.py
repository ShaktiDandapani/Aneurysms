import math
import point3D as p3D
import formulae_math as fmath
import plot_overlap as diagrams


def main():

    line1 = [p3D.Point3D(1, 3, 1), p3D.Point3D(3, 4, 2), p3D.Point3D(5, 4, 3), p3D.Point3D(6, 4, 4)]
    line2 = [p3D.Point3D(1, 5, 4), p3D.Point3D(2, 4, 3), p3D.Point3D(4, 3, 2), p3D.Point3D(5, 3, 1)]

    distance_dict = {}
    # for now X and Y co ordinates --> make a separate function which takes in Point3D
    for point1 in line1:
        for point2 in line2:
            within_sqrt = (pow((point1.x - point2.x), 2) + pow((point1.y - point2.y), 2))
            euclidean_distance = round(math.sqrt(within_sqrt), 3)
            line1_points = [point1.x, point1.y]
            line2_points = [point2.x, point2.y]
            line_points = [line1_points, line2_points]
            if euclidean_distance > 0:
                distance_dict[euclidean_distance] = line_points

    #function to obtain 2 shortest lines
    [short_line_1, short_line_2] = fmath.minimum_distance_sort(distance_dict)

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
        print 'true'
        for point_a in line1:
            if point_a.x == common_point[0] and point_a.y == common_point[1]:
                print 'cp present in 2nd line'
                for point in line1:
                    in_root = (pow((point.x - common_point[0]), 2) + pow((point.y - common_point[1]), 2))
                    distance = round(math.sqrt(in_root), 3)
                    line_point = [point.x, point.y]
                    cp_point = [common_point[0], common_point[1]]
                    if distance > 0.0:
                        cp_dist_dict_line1[distance] = [line_point, cp_point]

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

        # insert the point in the final point --> will get 2 lists for 2 points on either sidem then do convex
        # testing and insert the one forming the convex
    else:
        print 'no common point'

    print 'distances with common_point'
    print cp_dist_dict_line2
    print cp_dist_dict_line1
    ## Plots below
    #Plot the figures
    diagrams.original_lines(line1, line2)


main()