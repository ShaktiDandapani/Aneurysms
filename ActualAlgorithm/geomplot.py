import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_3d_points(line1, line2, poi_xy_plane, poi_yz_plane, poi_zx_plane):

    x_data = []
    y_data = []
    z_data = []

    p_data = []
    q_data = []
    r_data = []
    # line1 = sorted(line1, key=lambda x: (x[0], x[1]))
    # line2 = sorted(line2, key=lambda x: (x[0], x[1]))

    for p in line1:
        x_data.append(p.x)
        y_data.append(p.y)
        z_data.append(p.z)

    for t in line2:
        p_data.append(t.x)
        q_data.append(t.y)
        r_data.append(t.z)

    #xy plane point of intersection (remember lists)
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

    # print poi_x_xy, poi_y_xy
    #
    # print 'final point: (', final_x_point, ',', final_y_point, ',', final_z_point, ')'
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x_data, y_data, z_data, 'y.', label='curve_1')
    ax.plot(p_data, q_data, r_data, 'c.', label='curve_2')
    ax.plot(point_of_overlap_x, point_of_overlap_y, point_of_overlap_z, 'r.', label='3d Overlap Point')

    xlabel = ax.set_xlabel('x-axis')
    ylabel = ax.set_ylabel('y-axis')
    zlabel = ax.set_zlabel('z-axis')
    ax.legend(loc='upper right')

    print 'DONE'
