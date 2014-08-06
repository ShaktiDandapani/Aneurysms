import os
import geomtextreader as gt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import geomstruct as gs
import geomoverlapfindermod as gop2


def findinterpoints(mount_tuple, side_tuple):

    (front_mount_x, front_mount_y, front_mount_z) = mount_tuple
    (front_side_spline_x, front_side_spline_y, front_side_spline_z) = side_tuple
    """
    make below code separate to obtain 2 pts of int between 2 curves.
    """
    '''
    List for front and back mountain splines
    '''
    mountain_spline = []

    '''
    List for left and right divided splines/
    '''
    upper_side_spline = []
    lower_side_spline = []

    '''
    make the code below a separate function returning 2 3D points of intersection of two given splines.
    '''
    for i in range(len(front_mount_x)):
        mountain_spline.append(gs.Point3D(round(front_mount_x[i], 3), round(front_mount_y[i], 3),
                                          round(front_mount_z[i], 3)))

    for j in range(0, len(front_side_spline_x) / 2):
        upper_side_spline.append(gs.Point3D(round(front_side_spline_x[j], 3), round(front_side_spline_y[j], 3),
                                            round(front_side_spline_z[j], 3)))

    for k in range(len(front_side_spline_x)/2, len(front_side_spline_x)):
        lower_side_spline.append(gs.Point3D(round(front_side_spline_x[k], 3), round(front_side_spline_y[k], 3),
                                            round(front_side_spline_z[k], 3)))

    sideuppertofrontmount_int = gop2.find_overlap(mountain_spline, upper_side_spline)
    sidetlowertofrontmount_int = gop2.find_overlap(mountain_spline, lower_side_spline)

    lower_intersection_xy = sidetlowertofrontmount_int[0]
    lower_intersection_yz = sidetlowertofrontmount_int[1]
    lower_intersection_zx = sidetlowertofrontmount_int[2]
    #
    upper_intersection_xy = sideuppertofrontmount_int[0]
    upper_intersection_yz = sideuppertofrontmount_int[1]
    upper_intersection_zx = sideuppertofrontmount_int[2]

    x_lower = float(lower_intersection_xy[0] + lower_intersection_zx[1]) / 2.0
    y_lower = float(lower_intersection_xy[1] + lower_intersection_yz[0]) / 2.0
    z_lower = float(lower_intersection_yz[1] + lower_intersection_zx[0]) / 2.0

    x_upper = float(upper_intersection_xy[0] + upper_intersection_zx[1]) / 2.0
    y_upper = float(upper_intersection_xy[1] + upper_intersection_yz[0]) / 2.0
    z_upper = float(upper_intersection_yz[1] + upper_intersection_zx[0]) / 2.0

    intersection_point_lower = (x_lower, y_lower, z_lower)
    intersection_point_upper = (x_upper, y_upper, z_upper)

    print 'planar intersection lower :'
    print 'xy: ', lower_intersection_xy
    print 'yz: ', lower_intersection_yz
    print 'zx: ', lower_intersection_zx

    print 'planar intersection upper :'
    print 'xy: ', upper_intersection_xy
    print 'yz: ', upper_intersection_yz
    print 'zx: ', upper_intersection_zx

    return intersection_point_lower, intersection_point_upper
