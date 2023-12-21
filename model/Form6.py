from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

from ExportTemplate import ExportTemplate
from design.style1.QLabelXButton import QLabelXButton
from design.style1.QTComboBox import QTComboBox
from design.style1.WindowTemplate import WindowTemplate
from functions.basic_functions import get_subCategory
from functions.form6_methods import get_bottom_profit_products, export_bottom_profit_products


class Form6(WindowTemplate):
    def __init__(self, title_text):
        super().__init__(title_text)

        self.setObjectName("Form6")

        pixmap = QPixmap("imgs/x_ button.png")
        pixmap = pixmap.scaled(25, 25, Qt.KeepAspectRatio)
        self.x_button = QLabelXButton(parent=self)
        self.x_button.setGeometry(QRect(self.APP_RES[0] - 45, 15, 25, 25))
        self.x_button.setPixmap(pixmap)

        self.alegere_sub_categorie_label = QLabel("Selecteaza sub-categoria: ", self)
        self.alegere_sub_categorie_label.setGeometry(QRect(50, 125, 200, 50))
        self.alegere_sub_categorie_label.setStyleSheet(
            "border: 1px solid gray; border-radius: 10px; background-color: white; "
            "color: black;}")
        self.alegere_sub_categorie_label.setFont(QtGui.QFont("Helvetica", 13))

        self.sub_category_cb = QTComboBox(self)
        self.sub_category_cb.setGeometry(QRect(230, self.alegere_sub_categorie_label.y(), 170, 50))
        self.populare_combobox_sub_categorii()
        self.button.func = self.generate_graph
        self.export.func = self.export_graph

    def populare_combobox_sub_categorii(self):
        data = get_subCategory()

        for item in data:
            self.sub_category_cb.addItem(item)

    def generate_graph(self):
        obj = get_bottom_profit_products(self.sub_category_cb.currentText())
        self.sc.axes.clear()
        print('aaa')
        x1 = obj[0]
        y1 = obj[1]

        self.sc.axes.barh(x1, y1, color='royalblue')

        self.sc.axes.set_xlabel('Produse')
        self.sc.axes.set_ylabel('Profit')

        self.sc.axes.tick_params(axis="x", labelrotation=90)

        self.sc.draw()
        self.show()


    def export_graph(self):
        subcategory = self.sub_category_cb.currentText()
        x_values, y_values = get_bottom_profit_products(subcategory)

        self.new_window = ExportTemplate("Export", "Form6", [subcategory, x_values, y_values])
        self.new_window.show()

