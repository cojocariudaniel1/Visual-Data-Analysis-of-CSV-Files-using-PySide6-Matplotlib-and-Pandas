import matplotlib.pyplot as plt

from functions.basic_functions import get_data

import xlsxwriter
import os
import logging

def find_least_profitable_products(state=None, nr_product = 10):
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



def export_least_profitable_products(state, nr_products, patch="least_profitable_products.xlsx"):
    try:
        obj = find_least_profitable_products(state, nr_products)
        workbook = xlsxwriter.Workbook(patch)
        worksheet = workbook.add_worksheet()

        worksheet.write_row('A1', ["Product ID", "Profit"])
        worksheet.write_column('A2', obj[0])
        worksheet.write_column('B2', obj[1])

        chart = workbook.add_chart({'type': 'line'})
        data_len = len(obj[0]) + 1
        chart.add_series({
            'name': '=Sheet1!$B$1',
            'categories': f'=Sheet1!$A$2:$A${data_len}',
            'values': f'=Sheet1!$B$2:$B${data_len}',
        })
        worksheet.insert_chart('D2', chart)
        worksheet.conditional_format(f'B2:B{data_len}', {'type': '3_color_scale'})

        workbook.close()
        full_path_to_file = str(patch)
        os.startfile(full_path_to_file)

    except BaseException as e:
        logging.exception(e)
