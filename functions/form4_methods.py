import numpy as np
from matplotlib import pyplot as plt

from functions.basic_functions import get_data

import xlsxwriter
import os
import logging

from functions.form3_methods import chart_trendline


def calculate_top_products_profit(category, discount):
    df = get_data()
    df = df[df["Category"] == category]

    df['Profit After Discount'] = df['Profit'] * (1 - discount)

    profit_before_discount = df.groupby("Product ID")["Profit"].sum().reset_index()
    profit_after_discount = df.groupby("Product ID")["Profit After Discount"].sum().reset_index()

    top_10_before_discount = profit_before_discount.sort_values(by="Profit", ascending=False).head(10)
    top_10_after_discount = profit_after_discount.sort_values(by="Profit After Discount", ascending=False).head(10)

    return top_10_before_discount, top_10_after_discount


def export_top_products_profit(category, discount, top_10_before_discount, top_10_after_discount,  trendLineAttrs=None, patch="top_products_profit.xlsx"):
    try:
        workbook = xlsxwriter.Workbook(patch)
        worksheet = workbook.add_worksheet()

        worksheet.write_row('A1', ["Product ID", "Profit Before Discount", "Profit After Discount"])
        worksheet.write_column('A2', top_10_before_discount["Product ID"])
        worksheet.write_column('B2', top_10_before_discount["Profit"])
        worksheet.write_column('C2', top_10_after_discount["Profit After Discount"])

        chart = workbook.add_chart({'type': 'column'})
        data_len = len(top_10_before_discount) + 1
        chart.add_series({
            'name': '=Sheet1!$B$1',
            'categories': f'=Sheet1!$A$2:$A${data_len}',
            'values': f'=Sheet1!$B$2:$B${data_len}',
        })
        if trendLineAttrs:
            chart.add_series({
                'name': '=Sheet1!$C$1',
                'categories': f'=Sheet1!$A$2:$A${data_len}',
                'values': f'=Sheet1!$C$2:$C${data_len}',
                'trendline': chart_trendline(trendLineAttrs)

            })
        else:
            chart.add_series({
                'name': '=Sheet1!$C$1',
                'categories': f'=Sheet1!$A$2:$A${data_len}',
                'values': f'=Sheet1!$C$2:$C${data_len}',
            })
        worksheet.insert_chart('E2', chart)
        worksheet.conditional_format(f'B2:B{data_len}', {'type': '3_color_scale'})
        worksheet.conditional_format(f'C2:C{data_len}', {'type': '3_color_scale'})

        workbook.close()
        full_path_to_file = str(patch)
        os.startfile(full_path_to_file)

    except BaseException as e:
        logging.exception(e)
