import logging

from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel
from matplotlib import pyplot as plt

from design.style1.QLabelXButton import QLabelXButton
from design.style1.QTComboBox import QTComboBox
from design.style1.QTRadioButton import RadioButton
from design.style1.WindowTemplate import WindowTemplate
from functions.form6_methods import get_bottom_profit_products
from functions.form8_methods import order_processing_duration_by_subcategory, order_processing_duration_by_category, \
    export_order_processing_duration_graph


class Form8(WindowTemplate):
    def __init__(self, titlu_text):
        super().__init__(titlu_text)

        self.setObjectName("Form8")

        pixmap = QPixmap("imgs/x_ button.png")
        pixmap = pixmap.scaled(25, 25, Qt.KeepAspectRatio)
        self.x_button = QLabelXButton(parent=self)
        self.x_button.setGeometry(QRect(self.APP_RES[0] - 45, 15, 25, 25))
        self.x_button.setPixmap(pixmap)

        self.sub_categorie_rb = RadioButton("Sub-categorie", "subcategorie_rb", self)
        self.sub_categorie_rb.setGeometry(QRect(450,105, 150, 35))

        self.categorie_rb = RadioButton("Categorie", "categorie_rb", self)
        self.categorie_rb.setGeometry(QRect(450, 150, 150, 35))

        self.alegere_grafic = QLabel("Tip grafic: ", self)
        self.alegere_grafic.setGeometry(QRect(50, 125, 200, 50))
        self.alegere_grafic.setStyleSheet(
            "border: 1px solid gray; border-radius: 10px; background-color: white; "
            "color: black;}")
        self.alegere_grafic.setFont(QtGui.QFont("Helvetica", 13))

        self.alegere_grafic_cb = QTComboBox(self)
        self.alegere_grafic_cb.setGeometry(QRect(230, self.alegere_grafic.y(), 170, 50))
        self.button.func = self.generate_graph
        self.populare_combobox_aleger_grafic()
        self.export.func = self.export_graph
    def populare_combobox_aleger_grafic(self):
        data = ["Pie", "Bar", "Barh"]
        for item in data:
            self.alegere_grafic_cb.addItem(item)

    def generate_graph(self):
        self.sc.axes.clear()
        self.sc.axes.clear()

        if self.sub_categorie_rb.isChecked():
            obj = order_processing_duration_by_subcategory()
            self.sc.axes.clear()
            self.sc.axes.set_xlabel('Categorii')
            self.sc.axes.set_ylabel('Durata de procesare')
        else:
            self.sc.axes.clear()
            obj = order_processing_duration_by_category()
            self.sc.axes.set_xlabel('Sub-categorii')
            self.sc.axes.set_ylabel('Durata de procesare')
        x_data = obj[0]
        y_data = obj[1]
        if self.alegere_grafic_cb.currentText() == "Pie":

            self.sc.axes.pie(y_data, labels=x_data, autopct='%1.1f%%', startangle=140)

            self.sc.draw()
            self.show()

        elif self.alegere_grafic_cb.currentText() == "Bar":
            self.sc.axes.bar(x_data, y_data, color='royalblue')
            self.sc.draw()
            self.show()
        elif self.alegere_grafic_cb.currentText() == "Barh":
            self.sc.axes.barh(x_data, y_data, color='royalblue')
            self.sc.draw()
            self.show()

    def export_graph(self):
        try:

            if self.sub_categorie_rb.isChecked():
                obj = order_processing_duration_by_subcategory()
                bool = False
            else:
                obj = order_processing_duration_by_category()
                bool = True

            x_data = obj[0]
            y_data = obj[1]

            chart_type = "pie" if self.alegere_grafic_cb.currentText() == "Pie" else "bar" if self.alegere_grafic_cb.currentText() == "Bar" else "barh"

            export_order_processing_duration_graph(x_data, y_data, bool, chart_type)

        except BaseException as e:
            logging.exception(e)