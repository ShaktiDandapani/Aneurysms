import xlrd
import os


def read_excel(filename):
    """
    It takes an excel file with three columns named x, y and z
    and the rows have the respective values and returns them as 3 lists,
    with the x's, y's and z's.

    :param filename:
    :return x_values, y_values, z_values:
    """
    filename = os.path.abspath(filename)
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
    return tuple(x_values), tuple(y_values), tuple(z_values)

