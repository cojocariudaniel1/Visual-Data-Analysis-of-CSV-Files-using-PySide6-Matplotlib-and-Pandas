import logging
import os

import numpy as np
import pandas as pd
import xlsxwriter
from matplotlib import pyplot as plt

from functions.basic_functions import get_data
from functions.form3_methods import chart_trendline


def evidențiere_comenzi_oras(oras):
    dataframe = get_data()

    comenzile_orasului = dataframe[dataframe['City'] == oras]

    comenzi_pe_client = comenzile_orasului.groupby('Customer Name')['Order ID'].count().reset_index()

    comenzi_pe_client = comenzi_pe_client.sort_values(by='Order ID', ascending=False)
    obj = [comenzi_pe_client["Customer Name"].tolist(), comenzi_pe_client["Order ID"].tolist()]
    return obj


def export_evidentiere_comenzi_oras(oras, trendLineAttrs=None, patch="comenzi_oras.xlsx"):
    try:
        obj = evidențiere_comenzi_oras(oras)
        workbook = xlsxwriter.Workbook(patch[0])
        worksheet = workbook.add_worksheet()

        worksheet.write_row('A1', ["Customer Name", "Numar de comenzi"])
        worksheet.write_column('A2', obj[0])
        worksheet.write_column('B2', obj[1])

        chart = workbook.add_chart({'type': 'column'})
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