import geomtextreader as gt
import geomstruct as gs
import geomoverlapfindermod as gof
import matplotlib.pyplot as plt
import geomplot as gp
import time


def main():
    start_time = time.time()
    filename_line1 = 'line1.xlsx'
    filename_line2 = 'line2_std.xlsx'

    (xs1, ys1, zs1) = gt.read_excel(filename_line1)
    (xs2, ys2, zs2) = gt.read_excel(filename_line2)

    line1 = []
    line2 = []

    for i in range(len(xs1)):
        line1.append(gs.Point3D(round(xs1[i], 2), round(ys1[i], 2), round(zs1[i], 2)))

    for j in range(len(xs2)):
        line2.append(gs.Point3D(round(xs2[j], 2), round(ys2[j], 2), round(zs2[j], 2)))

    (poi_xy, poi_yz, poi_zx) = gof.find_overlap(line1, line2)

    if (poi_xy is not None or False) & (poi_yz is not None or False) & (poi_zx is not None or False):

        (fp_x, fp_y, fp_z) = return_3d_point(poi_xy, poi_yz, poi_zx)

        print 'final intersection: (', fp_x, ', ', fp_y, ', ', fp_z, ') '

    print ' -------------------------------------|'
    print '|xy plane intersection: ', poi_xy, '|'
    print '|yz plane intersection: ', poi_yz, '|'
    print '|zx plane intersection: ', poi_zx, '|'
    print ' -------------------------------------|'

    f_2d, ax_2d = plt.subplots(1, 3)

    if (poi_xy is None) or (poi_xy is False):
        print 'No xy plane intersection'
    else:
        ax_2d[0].plot(xs1, ys1, 'y.')
        ax_2d[0].plot(xs2, ys2, 'c.')
        ax_2d[0].plot(poi_xy[0], poi_xy[1], 'r.')
        ax_2d[0].set_title('XY plane')
        ax_2d[0].set_xlabel('x axis')
        ax_2d[0].set_axis_bgcolor('black')

    if (poi_yz is None) or (poi_yz is False):
        print 'No yz plane intersection'
    else:
        ax_2d[1].plot(ys1, zs1, 'y.')
        ax_2d[1].plot(ys2, zs2, 'c.')
        ax_2d[1].plot(poi_yz[0], poi_yz[1], 'r.')
        ax_2d[1].set_title('YZ plane')
        ax_2d[1].set_xlabel('y axis')
        ax_2d[1].set_ylabel('z axis')
        ax_2d[1].set_axis_bgcolor('black')

    if (poi_zx is None) or (poi_zx is False):
        print 'No zx plane intersection'
    else:
        ax_2d[2].plot(zs1, xs1, 'y.')
        ax_2d[2].plot(zs2, xs2, 'c.')
        ax_2d[2].plot(poi_zx[0], poi_zx[1], 'r.')
        ax_2d[2].set_title('ZX plane')
        ax_2d[2].set_xlabel('z axis')
        ax_2d[2].set_ylabel('x axis')
        ax_2d[2].set_axis_bgcolor('black')

    print "---- %s seconds ---" % (time.time() - start_time)

    if (poi_xy is None or poi_xy is False) or (poi_yz is None or poi_yz is False) \
            or (poi_zx is None or poi_zx is False):
        print 'Less than 3 intersections for 3D plot'
    else:
        print '3 intersections found'
        gp.plot_3d_points(line1, line2, poi_xy, poi_yz, poi_zx)
    plt.show()


def return_3d_point(poi_xy_plane, poi_yz_plane, poi_zx_plane):
    poi_x_xy = [poi_xy_plane[0]]
    poi_y_xy = [poi_xy_plane[1]]
    poi_z_xy = [0]

    poi_x_yz = [0]
    poi_y_yz = [poi_yz_plane[0]]
    poi_z_yz = [poi_yz_plane[1]]
    #
    poi_x_zx = [poi_zx_plane[1]]
    poi_y_zx = [0]
    poi_z_zx = [poi_zx_plane[0]]

    final_x_point = round(float(poi_x_xy[0] + poi_x_yz[0] + poi_x_zx[0]) / 2.0, 2)
    final_y_point = round(float(poi_y_xy[0] + poi_y_yz[0] + poi_y_zx[0]) / 2.0, 2)
    final_z_point = round(float(poi_z_xy[0] + poi_z_yz[0] + poi_z_zx[0]) / 2.0, 2)

    point_of_overlap_x = [final_x_point]
    point_of_overlap_y = [final_y_point]
    point_of_overlap_z = [final_z_point]

    return tuple((point_of_overlap_x, point_of_overlap_y, point_of_overlap_z))

if __name__ == "__main__":

    main()
