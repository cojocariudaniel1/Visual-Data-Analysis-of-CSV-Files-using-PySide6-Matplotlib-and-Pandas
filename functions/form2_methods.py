from matplotlib import pyplot as plt

from functions.basic_functions import get_data
import xlsxwriter
import os
import logging

from functions.form3_methods import chart_trendline


def frecventa_categorii_pe_subcategorie(categorie):
    dataframe = get_data()
    filtered_data = dataframe[dataframe['Category'] == categorie]

    grouped_data = filtered_data.groupby('Sub-Category')[['Sales', 'Profit']].sum()

    subcategories = grouped_data.index.tolist()
    sales = grouped_data['Sales'].tolist()
    profit = grouped_data['Profit'].tolist()

    return subcategories, sales, profit


def export_frecventa_categorii_pe_subcategorie(categorie, tip_date, trendLineAttrs=None, patch="frecventa_categorii_pe_subcategorie.xlsx"):
    try:
        obj = frecventa_categorii_pe_subcategorie(categorie)
        workbook = xlsxwriter.Workbook(patch[0])
        worksheet = workbook.add_worksheet()

        if tip_date == 'vanzari':
            worksheet.write_row('A1', ["Sub-Categorie", "Vânzări"])
            worksheet.write_column('A2', obj[0])
            worksheet.write_column('B2', obj[1])
        elif tip_date == 'profit':
            worksheet.write_row('A1', ["Sub-Categorie", "Profit"])
            worksheet.write_column('A2', obj[0])
            worksheet.write_column('B2', obj[2])

        chart = workbook.add_chart({'type': 'column'})
        data_len = len(obj[0]) + 1
        if trendLineAttrs:
            chart.add_series({
                'name': f'=Sheet1${"B" if tip_date == "vanzari" else "C"}$1',
                'categories': f'=Sheet1!$A$2:$A${data_len}',
                'values': f'=Sheet1!${"B" if tip_date == "vanzari" else "C"}$2:${"B" if tip_date == "vanzari" else "C"}${data_len}',
                'trendline': chart_trendline(trendLineAttrs)

            })
        else:
            chart.add_series({
                'name': f'=Sheet1${"B" if tip_date == "vanzari" else "C"}$1',
                'categories': f'=Sheet1!$A$2:$A${data_len}',
                'values': f'=Sheet1!${"B" if tip_date == "vanzari" else "C"}$2:${"B" if tip_date == "vanzari" else "C"}${data_len}',
            })
        worksheet.insert_chart('D2', chart)
        worksheet.conditional_format(f'B2:B{data_len}' if tip_date == 'vanzari' else f'C2:C{data_len}', {'type': '3_color_scale'})

        workbook.close()
        full_path_to_file = str(patch[0])
        os.startfile(full_path_to_file)

    except BaseException as e:
        logging.exception(e)

if __name__ == "__main__":
    frecventa_categorii_pe_subcategorie("Bookcases")
