import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from functions.basic_functions import get_data

import xlsxwriter
import os
import logging


def profit_loss_by_state_category(category):
    dataframe = get_data()  #

    category_data = dataframe[dataframe['Category'] == category]

    state_category_profit = category_data.groupby(['State', 'Category'])['Profit'].sum().reset_index()

    unique_states = state_category_profit['State'].unique()

    profits = []
    losses = []
    for state in unique_states:
        state_data = state_category_profit[state_category_profit['State'] == state]
        total_profit = state_data[state_data['Category'] == category]['Profit'].sum()
        profits.append(total_profit if total_profit >= 0 else 0)
        losses.append(-total_profit if total_profit < 0 else 0)

    return unique_states, profits, losses


def export_profit_loss_by_state_category(category, states, profits, losses, patch="profit_loss_by_state_category.xlsx"):
    try:
        workbook = xlsxwriter.Workbook(patch)
        worksheet = workbook.add_worksheet()

        worksheet.write_row('A1', ["State", "Profit", "Loss"])
        worksheet.write_column('A2', states)
        worksheet.write_column('B2', profits)
        worksheet.write_column('C2', losses)

        chart = workbook.add_chart({'type': 'column'})
        chart.add_series({
            'name': 'Profit',
            'categories': f'=Sheet1!$A$2:$A${len(states) + 1}',
            'values': f'=Sheet1!$B$2:$B${len(profits) + 1}',
        })
        chart.add_series({
            'name': 'Loss',
            'categories': f'=Sheet1!$A$2:$A${len(states) + 1}',
            'values': f'=Sheet1!$C$2:$C${len(losses) + 1}',
        })
        worksheet.insert_chart('E2', chart)

        workbook.close()
        full_path_to_file = str(patch)
        os.startfile(full_path_to_file)

    except BaseException as e:
        logging.exception(e)
