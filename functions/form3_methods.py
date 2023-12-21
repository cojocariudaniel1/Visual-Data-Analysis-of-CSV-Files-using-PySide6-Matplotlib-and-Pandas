import matplotlib.pyplot as plt

from functions.basic_functions import get_data

import xlsxwriter
import os
import logging


def find_least_profitable_products(state=None, nr_product=10):
    dataframe = get_data()
    if state:
        dataframe_filter = dataframe[dataframe["State"] == state]
    else:
        dataframe_filter = dataframe
    df = dataframe_filter[["Product ID", "Profit", "Category", "Sub-Category"]]

    if nr_product == 0:
        return [[], []]
    result = df.groupby("Product ID").sum(numeric_only=True). \
        sort_values(by="Profit", ascending=False).head(nr_product)

    values = []

    for k in result.values:
        values.append(k[0])

    index = result.index
    obj = [index, values]
    return obj


def export_least_profitable_products(state, nr_products, trendLineAttrs=None, patch="least_profitable_products.xlsx"):
    try:
        obj = find_least_profitable_products(state, nr_products)
        workbook = xlsxwriter.Workbook(patch[0])
        worksheet = workbook.add_worksheet()

        worksheet.write_row('A1', ["Product ID", "Profit"])
        worksheet.write_column('A2', obj[0])
        worksheet.write_column('B2', obj[1])

        chart = workbook.add_chart({'type': 'line'})
        data_len = len(obj[0]) + 1

        if trendLineAttrs:
            chart.add_series({
                'name': '=Sheet1!$B$1',
                'categories': f'=Sheet1!$A$2:$A${data_len}',
                'values': f'=Sheet1!$B$2:$B${data_len}',
                'trendline': chart_trendline(trendLineAttrs)
            })
        else:
            chart.add_series({
                'name': '=Sheet1!$B$1',
                'categories': f'=Sheet1!$A$2:$A${data_len}',
                'values': f'=Sheet1!$B$2:$B${data_len}',
            })

        worksheet.insert_chart('D2', chart)
        worksheet.conditional_format(f'B2:B{data_len}', {'type': '3_color_scale'})

        workbook.close()
        full_path_to_file = str(patch[0])
        os.startfile(full_path_to_file)

    except BaseException as e:
        logging.exception(e)


def chart_trendline(trend_line_attrs):
    if trend_line_attrs["type"] == "polynomial":
        return {

            'type': trend_line_attrs['type'],
            'name': trend_line_attrs['name'],
            'order': trend_line_attrs['order'],
            'forward': trend_line_attrs['forward'],
            'backward': trend_line_attrs['backward'],
            'display_r_squared': trend_line_attrs['r_square'],
            'display_equation': trend_line_attrs['equation'],
            'line': {
                'color': trend_line_attrs['line_color'],
                'width': trend_line_attrs['line_width'],
            },
        }
    elif trend_line_attrs["type"] == "moving_average":
        return {
            'type': trend_line_attrs["type"],
            'name': trend_line_attrs['name'],
            'period': trend_line_attrs["period"],
            'line': {
                'color': trend_line_attrs['line_color'],
                'width': trend_line_attrs['line_width'],
            },
        }
    elif trend_line_attrs["type"] == "linear" or trend_line_attrs["type"] == "exponential":
        return {
            'type': trend_line_attrs["type"],
            'name': trend_line_attrs['name'],
            'intercept': trend_line_attrs["intercept"],
            'display_r_squared': trend_line_attrs['r_square'],
            'display_equation': trend_line_attrs['equation'],
            'forward': trend_line_attrs['forward'],
            'backward': trend_line_attrs['backward'],
            'line': {
                'color': trend_line_attrs['line_color'],
                'width': trend_line_attrs['line_width'],

            },
        }
    elif trend_line_attrs["type"] == "power":
        return {
            "type": trend_line_attrs["type"],
            "name": trend_line_attrs["name"],
            'line': {
                'color': trend_line_attrs['line_color'],
                'width': trend_line_attrs['line_width'],

            },
        }
    elif trend_line_attrs["type"] == "log":
        return {
            "type": trend_line_attrs["type"],
            "name": trend_line_attrs["name"],
            'line': {
                'color': trend_line_attrs['line_color'],
                'width': trend_line_attrs['line_width'],

            },
        }
