from functions.basic_functions import get_data

import pandas as pd
import xlsxwriter
import os
import logging


def get_bottom_profit_products(subcategory):
    dataframe = get_data()

    subcategory_data = dataframe[dataframe['Sub-Category'] == subcategory]

    product_profit = subcategory_data.groupby('Product Name')['Profit'].sum().reset_index()

    sorted_products = product_profit.sort_values(by='Profit', ascending=True)

    bottom_10_products = sorted_products.head(10)

    x_values = bottom_10_products['Product Name'].tolist()
    y_values = bottom_10_products['Profit'].tolist()

    return x_values, y_values


def export_bottom_profit_products(subcategory, x_values, y_values, trendLineAttrs=None, patch="bottom_profit_products.xlsx"):
    try:
        workbook = xlsxwriter.Workbook(patch[0])
        worksheet = workbook.add_worksheet()

        worksheet.write_row('A1', ["Product Name", "Profit"])
        worksheet.write_column('A2', x_values)
        worksheet.write_column('B2', y_values)

        chart = workbook.add_chart({'type': 'bar'})
        if trendLineAttrs:
            chart.add_series({
                'name': 'Profit',
                'categories': f'=Sheet1!$A$2:$A${len(x_values) + 1}',
                'values': f'=Sheet1!$B$2:$B${len(y_values) + 1}',
                'data_labels': {'value': True},
            })
        else:
            chart.add_series({
                'name': 'Profit',
                'categories': f'=Sheet1!$A$2:$A${len(x_values) + 1}',
                'values': f'=Sheet1!$B$2:$B${len(y_values) + 1}',
                'data_labels': {'value': True},
            })
        worksheet.insert_chart('D2', chart)

        workbook.close()
        full_path_to_file = str(patch[0])
        os.startfile(full_path_to_file)

    except BaseException as e:
        logging.exception(e)
