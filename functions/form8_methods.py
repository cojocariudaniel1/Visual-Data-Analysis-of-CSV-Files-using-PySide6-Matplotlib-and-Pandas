import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from functions.basic_functions import get_data
import xlsxwriter
import os
import logging


def order_processing_duration_by_category():
    dataframe = get_data()  # Asigurați-vă că aveți DataFrame-ul dvs.

    # Convertim coloanele de dată la tip de dată
    dataframe['Order Date'] = pd.to_datetime(dataframe['Order Date'])
    dataframe['Ship Date'] = pd.to_datetime(dataframe['Ship Date'])

    # Calculăm durata de procesare a comenzilor pentru fiecare comandă
    dataframe['Order Processing Duration'] = (dataframe['Ship Date'] - dataframe['Order Date']).dt.days

    # Grupăm comenzile după categorie și calculăm suma totală a duratei de procesare pentru fiecare categorie
    category_processing_duration = dataframe.groupby('Category')['Order Processing Duration'].sum().reset_index()

    # Extragere date pentru a genera grafic
    x = category_processing_duration['Category']
    y = category_processing_duration['Order Processing Duration']

    return x, y


def order_processing_duration_by_subcategory():
    dataframe = get_data()

    dataframe['Order Date'] = pd.to_datetime(dataframe['Order Date'])
    dataframe['Ship Date'] = pd.to_datetime(dataframe['Ship Date'])

    dataframe['Order Processing Duration'] = (dataframe['Ship Date'] - dataframe['Order Date']).dt.days

    subcategory_processing_duration = dataframe.groupby('Sub-Category')['Order Processing Duration'].sum().reset_index()

    x = subcategory_processing_duration['Sub-Category']
    y = subcategory_processing_duration['Order Processing Duration']

    return x, y




def export_order_processing_duration_graph(x_data, y_data, bool_category, chart_type, filename="order_processing_duration_graph.xlsx"):
    try:
        workbook = xlsxwriter.Workbook(filename[0])
        worksheet = workbook.add_worksheet()


        worksheet.write_row('A1', ["Category" if bool_category else "Subcategory", "Processing Duration"])
        worksheet.write_column('A2', x_data)
        worksheet.write_column('B2', y_data)


        chart = workbook.add_chart({'type': chart_type})
        data_len = len(x_data) + 1
        chart.add_series({
            'name': f'=Sheet1!$B$1',
            'categories': f'=Sheet1!$A$2:$A${data_len}',
            'values': f'=Sheet1!$B$2:$B${data_len}',
        })
        worksheet.insert_chart('D2', chart)

        workbook.close()
        full_path_to_file = os.path.abspath(filename[0])
        os.startfile(full_path_to_file)

    except BaseException as e:
        logging.exception(e)
