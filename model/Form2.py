from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

from design.style1.QLabelXButton import QLabelXButton
from design.style1.QTComboBox import QTComboBox
from design.style1.QTRadioButton import RadioButton
from design.style1.WindowTemplate import WindowTemplate
from functions.basic_functions import get_Category
from functions.form2_methods import frecventa_categorii_pe_subcategorie, export_frecventa_categorii_pe_subcategorie


class Form2(WindowTemplate):
    def __init__(self, title_text):
        super().__init__(title_text = title_text)

        self.setObjectName("Form2")

        pixmap = QPixmap("imgs/x_ button.png")
        pixmap = pixmap.scaled(25, 25, Qt.KeepAspectRatio)
        self.x_button = QLabelXButton(parent=self)
        self.x_button.setGeometry(QRect(self.APP_RES[0] - 45, 15, 25, 25))
        self.x_button.setPixmap(pixmap)

        self.alegere_categorie_label = QLabel("Selecteaza categorie: ", self)
        self.alegere_categorie_label.setGeometry(QRect(50, 125, 200, 50))
        self.alegere_categorie_label.setStyleSheet(
            "border: 1px solid gray; border-radius: 10px; background-color: white; "
            "color: black;}")
        self.alegere_categorie_label.setFont(QtGui.QFont("Helvetica", 13))

        self.category_cb = QTComboBox(self)
        self.category_cb.setGeometry(QRect(230, self.alegere_categorie_label.y(), 170, 50))

        self.profit_rb = RadioButton("Profit", "profit_rb", self)
        self.profit_rb.setGeometry(QRect(450,105, 150, 35))

        self.vanzari_rb = RadioButton("Vânzări", "vanzari_rb", self)
        self.vanzari_rb.setGeometry(QRect(450, 150, 150, 35))

        self.populare_combobox_categorii()
        self.button.func = self.generate_graph
        self.export.func = self.export_graph




    def populare_combobox_categorii(self):
        data = get_Category()

        for item in data:
            self.category_cb.addItem(item)

    def generate_graph(self):
        obj = frecventa_categorii_pe_subcategorie(self.category_cb.currentText())
        self.sc.axes.clear()

        subcategories = obj[0]
        sales = obj[1]
        profit = obj[2]
        if self.vanzari_rb.isChecked():
            self.sc.axes.bar(subcategories, sales)
            self.sc.axes.set_title(f"Frecventa sub-categoriilor din: {self.category_cb.currentText()} pe vânzări")
            self.sc.axes.legend(["Sub categories", "Vanzari"])

        else:
            self.sc.axes.set_title(f"Frecventa sub-categoriilor din: {self.category_cb.currentText()} pe profit")
            self.sc.axes.legend(["Sub categories", "Profit"])

            self.sc.axes.bar(subcategories, profit)

        self.sc.axes.tick_params(axis="x", labelrotation=45)

        self.sc.draw()
        self.show()

    def export_graph(self):
        tip_date = 'vanzari' if self.vanzari_rb.isChecked() else 'profit'
        export_frecventa_categorii_pe_subcategorie(self.category_cb.currentText(), tip_date)