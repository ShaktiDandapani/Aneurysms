import os
import matplotlib.pyplot as plt
import geomstruct as gs
import geom2intersectionsfinder as g2f
import geomtextreader as gt

def main():
    left_list = os.listdir('LeftSideBf')
    right_list = os.listdir('RightSideBf')
    front_list = os.listdir('FrontSideBf')
    back_list = os.listdir('BackSideBf')

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    xlabel = ax.set_xlabel('x-axis')
    ylabel = ax.set_ylabel('y-axis')
    zlabel = ax.set_zlabel('z-axis')

    (front_mount_x, front_mount_y, front_mount_z) = gt.read_excel("FrontSideBf//"+front_list[4])
    (back_mount_x, back_mount_y, back_mount_z) = gt.read_excel("BackSideBf//"+back_list[0])

    '''
    Right side data
    '''
    (front_right_side_spline_x, front_right_side_spline_y, front_right_side_spline_z) = \
        gt.read_excel("RightSideBf//"+right_list[0])
    (back_right_side_spline_x, back_right_side_spline_y, back_right_side_spline_z) = \
        gt.read_excel("RightSideBf//"+right_list[1])
    '''
    Left Side data
    '''
    (front_left_side_spline_x, front_left_side_spline_y, front_left_side_spline_z) = \
        gt.read_excel("LeftSideBf//"+left_list[0])
    (back_left_side_spline_x, back_left_side_spline_y, back_left_side_spline_z) = \
        gt.read_excel("LeftSidebf//"+left_list[1])

    front_mount_tuple = (front_mount_x, front_mount_y, front_mount_z)
    back_mount_tuple = (back_mount_x, back_mount_y, back_mount_z)

    front_left_tuple = (front_left_side_spline_x, front_left_side_spline_y, front_left_side_spline_z)
    back_left_tuple = (back_left_side_spline_x, back_left_side_spline_y, back_right_side_spline_z)

    front_right_tuple = (front_right_side_spline_x, front_right_side_spline_y, front_right_side_spline_z)
    back_right_tuple = (back_right_side_spline_x, back_right_side_spline_y, back_right_side_spline_z)
    '''
    Find intersections
    '''
    print front_mount_tuple
    (intersection_1_fmfr, intersection_2_fmfr) = g2f.findinterpoints(front_mount_tuple, front_right_tuple)
    (intersection_1_fmfl, intersection_2_fmfl) = g2f.findinterpoints(front_mount_tuple, front_left_tuple)
    (intersection_1_bmbr, intersection_2_bmbr) = g2f.findinterpoints(back_mount_tuple, back_right_tuple)
    (intersection_1_bmbl, intersection_2_bmbl) = g2f.findinterpoints(back_mount_tuple, back_left_tuple)

    ax.plot(front_right_side_spline_x, front_right_side_spline_y, front_right_side_spline_z, 'r.')
    ax.plot(front_left_side_spline_x, front_left_side_spline_y, front_left_side_spline_z, 'r.')
    ax.plot(back_right_side_spline_x, back_right_side_spline_y, back_right_side_spline_z, 'r.')
    ax.plot(back_left_side_spline_x, back_left_side_spline_y, back_left_side_spline_z, 'r.')
    ax.plot(front_mount_x, front_mount_y, front_mount_z, 'b.')
    ax.plot(back_mount_x, back_mount_y, back_mount_z, 'g.')

    ax.plot([intersection_1_fmfr[0]], [intersection_1_fmfr[1]], [intersection_1_fmfr[2]], 'k.', label='first_point')
    ax.plot([intersection_1_fmfl[0]], [intersection_1_fmfl[1]], [intersection_1_fmfl[2]], 'k.', label='first_point')
    ax.plot([intersection_2_fmfr[0]], [intersection_2_fmfr[1]], [intersection_2_fmfr[2]], 'c.', label='second_point')
    ax.plot([intersection_2_fmfl[0]], [intersection_2_fmfl[1]], [intersection_2_fmfl[2]], 'c.', label='second_point')

    ax.plot([intersection_1_bmbr[0]], [intersection_1_bmbr[1]], [intersection_1_bmbr[2]], 'k.')
    ax.plot([intersection_1_bmbl[0]], [intersection_1_bmbl[1]], [intersection_1_bmbl[2]], 'k.')
    ax.plot([intersection_2_bmbr[0]], [intersection_2_bmbr[1]], [intersection_2_bmbr[2]], 'm.')
    ax.plot([intersection_2_bmbl[0]], [intersection_2_bmbl[1]], [intersection_2_bmbl[2]], 'm.')


    ax.legend(loc='upper right')
    plt.show()

if __name__ == '__main__':
    main()