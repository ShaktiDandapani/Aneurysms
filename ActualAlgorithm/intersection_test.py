from __future__ import division

p1 = (0, 1)
p2 = (1, 2)

p3 = (2, 4)
p4 = (1, 2)

x1 = p1[0]
y1 = p1[1]

x2 = p2[0]
y2 = p2[1]

x3 = p3[0]
y3 = p3[1]

x4 = p4[0]
y4 = p4[1]

x_num = float(((x1*y2 - y1*x2) * (x3 - x4) - (x1 - x2) * (x3*y4 - y3*x4)))
x_den = float(((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)))

y_num = float(((x1*y2 - y1*x2) * (y3 - y4) - (y1 - y2) * (x3*y4 - y3*x4)))
y_den = float(((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)))

poi_x = float(x_num / x_den)
poi_y = float(y_num/ y_den)

print poi_x, poi_y