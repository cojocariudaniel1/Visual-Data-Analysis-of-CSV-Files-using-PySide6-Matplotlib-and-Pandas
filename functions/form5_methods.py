import logging

import xlsxwriter
import os
import logging

from functions.basic_functions import get_data
from functions.form3_methods import chart_trendline


def get_profit_evolution_by_subcategory_with_dates(sub_category, date_min=None, date_max=None):
    dataframe = get_data()

    try:
        if not date_min and not date_max:
            # Se selecteaza coloana order date product name si profit din DataBase
            df = dataframe[["Order Date", "Sub-Category", "Profit"]]
            # Se filtreaza coloana product name in functie de product name si se ordoneaza.
            df2 = df[df["Sub-Category"] == sub_category].sort_values(by="Order Date")

            order_date = df2["Order Date"].tolist()
            profit = df2["Profit"]
            date_min = df2["Order Date"].min()
            date_max = df2["Order Date"].max()
            print(date_min)
            print(date_max)
            obj = [order_date, profit, date_min, date_max]

            # calculate equation for trendline
            return obj
        else:
            print(date_min)
            print(date_max)

            df = dataframe[["Order Date", "Sub-Category", "Profit"]]
            df2 = df[df["Sub-Category"] == sub_category].sort_values(by="Order Date")
            df_date = df2[df2["Order Date"] >= date_min]
            df_date1 = df_date[df_date["Order Date"] <= date_max]

            print(df_date1["Order Date"].min())
            order_date = df_date1["Order Date"].tolist()
            profit = df_date1["Profit"]
            obj = [order_date, profit, date_min, date_max]
            return obj

    except BaseException as e:
        logging.exception(e)


import xlsxwriter
import os
import logging

def export_profit_evolution(sub_category, date_min, date_max, x_values, y_values,trendLineAttrs=None, patch="profit_evolution.xlsx"):
    try:
        workbook = xlsxwriter.Workbook(patch[0])
        worksheet = workbook.add_worksheet()

        # Adaugă datele în fișierul Excel
        worksheet.write_row('A1', ["Order Date", "Profit"])
        worksheet.write_column('A2', x_values)
        worksheet.write_column('B2', y_values)


        # Adaugă graficul în fișierul Excel
        chart = workbook.add_chart({'type': 'line'})
        if trendLineAttrs:
            chart.add_series({
                'name': 'Profit',
                'categories': f'=Sheet1!$A$2:$A${len(x_values) + 1}',
                'values': f'=Sheet1!$B$2:$B${len(y_values) + 1}',
                'trendline': chart_trendline(trendLineAttrs)

            })
        else:
            chart.add_series({
                'name': 'Profit',
                'categories': f'=Sheet1!$A$2:$A${len(x_values) + 1}',
                'values': f'=Sheet1!$B$2:$B${len(y_values) + 1}',
            })

        worksheet.insert_chart('E2', chart)

        workbook.close()
        full_path_to_file = str(patch[0])
        os.startfile(full_path_to_file)

    except BaseException as e:
        logging.exception(e)
