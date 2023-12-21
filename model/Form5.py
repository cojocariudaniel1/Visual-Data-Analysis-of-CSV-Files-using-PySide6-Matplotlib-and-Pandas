import numpy as np
import pandas as pd
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt, QRect, QDate
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QSlider, QLineEdit

from ExportTemplate import ExportTemplate
from design.style1.QLabelXButton import QLabelXButton
from design.style1.QLineEdit import QLineEditX
from design.style1.QTComboBox import QTComboBox
from design.style1.WindowTemplate import WindowTemplate
from functions.basic_functions import get_Segment, get_subCategory
from functions.form5_methods import get_profit_evolution_by_subcategory_with_dates, export_profit_evolution


def calculate_month_difference(start_date, end_date):
    start_str = start_date.strftime('%Y-%m-%d')
    end_str = end_date.strftime('%Y-%m-%d')

    start_qdate = QDate.fromString(start_str, "yyyy-MM-dd")
    end_qdate = QDate.fromString(end_str, "yyyy-MM-dd")

    year_difference = end_qdate.year() - start_qdate.year()
    month_difference = end_qdate.month() - start_qdate.month() + year_difference * 12
    return month_difference


class Form5(WindowTemplate):
    def __init__(self, title_text):
        super().__init__(title_text)

        self.setObjectName("Form4")

        pixmap = QPixmap("imgs/x_ button.png")
        pixmap = pixmap.scaled(25, 25, Qt.KeepAspectRatio)
        self.x_button = QLabelXButton(parent=self)
        self.x_button.setGeometry(QRect(self.APP_RES[0] - 45, 15, 25, 25))
        self.x_button.setPixmap(pixmap)
        self.alegere_segment_label = QLabel("Sub-Category:  ", self)
        self.alegere_segment_label.setGeometry(QRect(50, 125, 200, 50))
        self.alegere_segment_label.setStyleSheet(
            "border: 1px solid gray; border-radius: 10px; background-color: white; "
            "color: black;}")
        self.alegere_segment_label.setFont(QtGui.QFont("Helvetica", 13))

        self.segment_cb = QTComboBox(self)
        self.segment_cb.setGeometry(QRect(230, self.alegere_segment_label.y(), 170, 50))
        self.populare_combobox_segment()

        self.horizontalSlider = QSlider(self)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setGeometry(QRect(250, 185, 400, 30))
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(120)  # Asumăm că avem 12 luni înainte
        self.horizontalSlider.valueChanged.connect(self.update_label)
        self.horizontalSlider.setValue(0)
        self.button.func = self.generate_graph
        self.button.setGeometry(QRect(665, 140, 175, 40))
        self.current_date = None
        self.selected_date = None
        self.initial_min_date = None
        self.initial_max_date = None
        self.export.func = self.export_graph

        self.mindate_label = QLabel("Min Date", self)
        self.mindate_label.setGeometry(QRect(50, 170, 100, 50))
        self.mindate_lineEdit = QLineEditX("", self)
        self.mindate_lineEdit.setGeometry(QRect(115, 180, 100, 30))

        self.mindate_lineEdit.enterPressed.connect(self.update_min_form)

        self.maxdate_label = QLabel("Max Date", self)
        self.maxdate_label.setGeometry(QRect(670, 170, 100, 50))
        self.maxdate_lineEdit = QLineEditX("", self)
        self.maxdate_lineEdit.setGeometry(QRect(730, 180, 100, 30))

        self.maxdate_lineEdit.enterPressed.connect(self.update_max_form)

        self.get_initial_date()

    def populare_combobox_segment(self):
        data = get_subCategory()

        for item in data:
            self.segment_cb.addItem(item)

    def update_label(self):
        selected_month = self.horizontalSlider.value()
        self.mindate_lineEdit.setText(self.get_date_string(selected_month))

    def update_min_form(self):
        end_date = pd.to_datetime(self.mindate_lineEdit.text())
        value = calculate_month_difference(self.initial_min_date, end_date)
        self.horizontalSlider.setValue(value)

    def update_max_form(self):
        max_date = pd.to_datetime(self.maxdate_lineEdit.text())
        min_date = pd.to_datetime(self.mindate_lineEdit.text())

        month_difference = calculate_month_difference(min_date, max_date)
        self.horizontalSlider.setMaximum(int(month_difference))

    def get_initial_date(self):
        obj = get_profit_evolution_by_subcategory_with_dates("Tables")
        start_date = obj[2]
        end_date = obj[3]
        start_str = start_date.strftime('%Y-%m-%d')
        end_str = end_date.strftime('%Y-%m-%d')

        start_qdate = QDate.fromString(start_str, "yyyy-MM-dd")
        end_qdate = QDate.fromString(end_str, "yyyy-MM-dd")
        self.selected_date = end_qdate.toString('yyyy-MM-dd')
        self.current_date = start_qdate
        self.initial_min_date = start_date
        self.initial_max_date = end_date
        month_difference = calculate_month_difference(start_date, end_date)
        self.mindate_lineEdit.setText(f"{start_qdate.toString('yyyy-MM-dd')}")
        self.maxdate_lineEdit.setText(f"{end_qdate.toString('yyyy-MM-dd')}")
        self.horizontalSlider.setMaximum(int(month_difference))

    def get_date(self):
        obj = get_profit_evolution_by_subcategory_with_dates("Tables")
        start_date = obj[2]
        end_date = obj[3]
        start_str = start_date.strftime('%Y-%m-%d')
        end_str = end_date.strftime('%Y-%m-%d')

        start_qdate = QDate.fromString(start_str, "yyyy-MM-dd")
        end_qdate = QDate.fromString(end_str, "yyyy-MM-dd")
        self.selected_date = end_qdate.toString('yyyy-MM-dd')
        self.current_date = start_qdate
        month_difference = calculate_month_difference(start_date, end_date)
        self.mindate_lineEdit.setText(f"{start_qdate.toString('yyyy-MM-dd')}")
        self.horizontalSlider.setMaximum(int(month_difference))
        print('cccc')

    def get_date_string(self, selected_month):
        print(self.current_date)
        future_date = self.current_date.addMonths(selected_month)
        self.selected_date = future_date.toString('yyyy-MM-dd')
        print(future_date)
        return f"{future_date.toString('yyyy-MM-dd')}"

    def generate_graph(self):
        self.sc.axes.clear()
        list1 = []
        min_date = self.mindate_lineEdit.text()
        max_date = self.maxdate_lineEdit.text()

        obj = get_profit_evolution_by_subcategory_with_dates(self.segment_cb.currentText(),
                                                             min_date, max_date
                                                             )
        x, y = obj[0], obj[1]

        for idx, i in enumerate(x):
            list1.append(idx)

        self.sc.axes.plot(x, y, color='royalblue')
        print(x)
        self.sc.axes.set_xlabel('Produse')
        self.sc.axes.set_ylabel('Profit')

        self.sc.axes.tick_params(axis="x", labelrotation=90)
        self.sc.draw()
        self.show()

    def export_graph(self):
        obj = get_profit_evolution_by_subcategory_with_dates(self.segment_cb.currentText(),
                                                             self.mindate_lineEdit.text(),
                                                             self.maxdate_lineEdit.text()
                                                             )
        x, y, date_min, date_max = obj[0], obj[1], obj[2], obj[3]

        self.new_window = ExportTemplate("Export", "Form5", [self.segment_cb.currentText(), pd.to_datetime(self.mindate_lineEdit.text()), pd.to_datetime(self.maxdate_lineEdit.text()), x, y])
        self.new_window.show()
