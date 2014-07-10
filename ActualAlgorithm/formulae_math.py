# sorts a dictionary in ascending order for keys.
def minimum_distance_sort(distance_dict):
    #make this return two lists -> line1 and line2

    final_set = sorted(distance_dict.iteritems())

    minimum_line_1 = final_set[0][1]
    minimum_line_2 = final_set[1][1]

    return minimum_line_1, minimum_line_2


# The function is used to find the common point amongst the four points.
def cp_finder(temp_list):
    d = {}

    for point in temp_list:
        if point[0] in d:
            #print point[0], point[1]
            d[point[0]] += point[1]
            result = [point[0], point[1]]
        else:
            #print 'else', point[0], point[1]
            d[point[0]] = point[1]
        ## Get the common points list

    p_set = set(map(tuple, temp_list))
    q_points = map(list, p_set)

    return result, q_points
