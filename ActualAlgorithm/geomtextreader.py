import xlrd
import geomstruct as gs
import algorithm_updated as alg

def read_excel(filename):
    # data_file = "Book1.xlsx"
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)
    x_values = []
    y_values = []
    z_values = []

    for row in range(sheet.nrows):
        # print sheet.cell_value(row, 0), '  ',  sheet.cell_value(row, 1), '  ', sheet.cell_value(row, 2)
        x_values.append(sheet.cell_value(row, 0))
        y_values.append(sheet.cell_value(row, 1))
        z_values.append(sheet.cell_value(row, 2))

    del x_values[0]
    del y_values[0]
    del z_values[0]
    return x_values, y_values, z_values


def main():
    filename_line1 = 'line1.xlsx'
    filename_line2 = 'line2.xlsx'

    [xs1, ys1, zs1] = read_excel(filename_line1)
    [xs2, ys2, zs2] = read_excel(filename_line2)

    line1 = []
    line2 = []
    for i in range(len(xs1)):
        line1.append(gs.Point3D(xs1[i], ys1[i], zs1[i]))

    for j in range(len(xs2)):
        line2.append(gs.Point3D(xs2[j], ys2[j], zs2[j]))

    [poi_xy, poi_yz, poi_zx] = alg.find_overlap(line1, line2)

    print 'ok'
    print ' -------------------------------------|'
    print '|xy plane intersection: ', poi_xy, '|'
    print '|yz plane intersection: ', poi_yz, '|'
    print '|zx plane intersection: ', poi_zx, '|'
    print ' -------------------------------------|'


main()