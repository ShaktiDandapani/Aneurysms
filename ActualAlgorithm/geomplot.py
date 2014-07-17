import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def original_lines(line1, line2, poi_xy_plane):

    x_data = []
    y_data = []
    z_data = []

    p_data = []
    q_data = []
    r_data = []

    for p in line1:
        x_data.append(p.x)
        y_data.append(p.y)
        z_data.append(p.z)

    for t in line2:
        p_data.append(t.x)
        q_data.append(t.y)
        r_data.append(t.z)

    #xy plane point of intersection (remember lists)
    poi_x = [poi_xy_plane.x]
    poi_y = [poi_xy_plane.y]
    poi_z = [0]

    print poi_x, poi_y
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x_data, y_data, z_data, 'b.')
    ax.plot(p_data, q_data, r_data, 'r.')
    ax.plot(poi_x, poi_y, poi_z, 'g.')
    xlabel = ax.set_xlabel('x-axis')
    ylabel = ax.set_ylabel('y-axis')
    zlabel = ax.set_zlabel('z-axis')
    plt.show()
    print 'DONE'
