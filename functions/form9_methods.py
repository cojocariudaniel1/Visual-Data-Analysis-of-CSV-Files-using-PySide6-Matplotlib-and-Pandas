import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functions.basic_functions import get_data

import xlsxwriter
import os
import logging


def product_profitability_by_state(ship_mode):
    dataframe = get_data()
    dataframe2 = dataframe[dataframe["Ship Mode"] == ship_mode]

    state_product_profit = dataframe2.groupby(['State', 'Product Name'])['Profit'].sum().reset_index()

    top_products = state_product_profit.groupby('State')['Profit'].idxmax()

    most_profitable_products = state_product_profit.loc[top_products]

    x_values = most_profitable_products['Product Name'].tolist()
    y_values = most_profitable_products['State'].tolist()

    return x_values, y_values


import xlsxwriter
import os
import logging

import xlsxwriter
import os
import logging

def export_product_profitability(x_values, y_values, ship_mode, filename="product_profitability_by_state.xlsx"):
    try:
        workbook = xlsxwriter.Workbook(filename[0])
        worksheet = workbook.add_worksheet()

        worksheet.write_row('A1', ["Product Name", "State"])
        worksheet.write_column('A2', x_values)
        worksheet.write_column('B2', y_values)


        worksheet.write('D1', 'Ship Mode:')
        worksheet.write('D2', ship_mode)


        chart = workbook.add_chart({'type': 'bar'})
        data_len = len(x_values) + 1
        chart.add_series({
            'name': 'Profit',
            'categories': f'=Sheet1!$A$2:$A${data_len}',
            'values': f'=Sheet1!$B$2:$B${data_len}',
            'data_labels': {'value': True},
        })
        chart.set_x_axis({'name': 'Product Name'})
        chart.set_y_axis({'name': 'State'})
        chart.set_title({'name': 'Product Profitability by State'})

        worksheet.insert_chart('D5', chart)

        workbook.close()
        full_path_to_file = os.path.abspath(filename[0])
        os.startfile(full_path_to_file)

    except BaseException as e:
        logging.exception(e)
