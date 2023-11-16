from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLineEdit, QLabel

from design.style1.QLabelXButton import QLabelXButton
from design.style1.QTComboBox import QTComboBox
from design.style1.WindowTemplate import WindowTemplate
from functions.basic_functions import get_Category
from functions.form4_methods import calculate_top_products_profit, export_top_products_profit


class Form4(WindowTemplate):
    def __init__(self, title_text):
        super().__init__(title_text)

        self.setObjectName("Form4")

        pixmap = QPixmap("imgs/x_ button.png")
        pixmap = pixmap.scaled(25, 25, Qt.KeepAspectRatio)
        self.x_button = QLabelXButton(parent=self)
        self.x_button.setGeometry(QRect(self.APP_RES[0] - 45, 15, 25, 25))
        self.x_button.setPixmap(pixmap)

        self.alegere_categorie_label = QLabel("Selecteaza categoria: ", self)
        self.alegere_categorie_label.setGeometry(QRect(50, 125, 200, 50))
        self.alegere_categorie_label.setStyleSheet(
            "border: 1px solid gray; border-radius: 10px; background-color: white; "
            "color: black;}")
        self.alegere_categorie_label.setFont(QtGui.QFont("Helvetica", 13))

        self.category_cb = QTComboBox(self)
        self.category_cb.setGeometry(QRect(230, self.alegere_categorie_label.y(), 170, 50))
        self.populare_combobox_categorii()

        self.discount_label = QLabel("Discount:  ", self)
        self.discount_label.setGeometry(QRect(500, 125, 145, 50))
        self.discount_label.setStyleSheet(
            "border: 1px solid gray; border-radius: 10px; background-color: white; "
            "color: black;}")
        self.discount_label.setFont(QtGui.QFont("Helvetica", 13))

        self.input = QLineEdit(self)
        self.input.setGeometry(QRect(580, 132, 50, 35))
        self.input.setStyleSheet("border: none;, border-down: 1px solid gray;")
        self.input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input.setFont(QtGui.QFont("Helvetica", 13))
        self.input.setText("2")
        self.export.func = self.export_graph
        self.button.func = self.generate_graph

    def populare_combobox_categorii(self):
        data = get_Category()

        for item in data:
            self.category_cb.addItem(item)

    def generate_graph(self):
        print('a')
        category = self.category_cb.currentText()
        discount = float(self.input.text())

        top_10_before_discount, top_10_after_discount = calculate_top_products_profit(category, discount)

        self.sc.axes.clear()

        # Set the width of the bars
        bar_width = 0.4  # Ajustați lățimea barelor după necesitate

        x1 = range(len(top_10_before_discount))
        y1 = top_10_before_discount["Profit"]

        x2 = range(len(top_10_after_discount))
        y2 = top_10_after_discount["Profit After Discount"]

        # Convertim etichetele axelor x la valori de tip float pentru a putea efectua adunarea
        x2 = [x + bar_width for x in x2]

        self.sc.axes.bar(x1, y1, width=bar_width, color='skyblue', label="Profit după discount")
        self.sc.axes.bar(x2, y2, width=bar_width, color='lightcoral',
                         label="Profit înainte de discount")

        # Setăm etichetele axelor x cu nume de produse sau puteți folosi orice altă etichetă corespunzătoare
        product_labels = top_10_before_discount["Product ID"].tolist()
        self.sc.axes.set_xticks([x + bar_width / 2 for x in x1])
        self.sc.axes.set_xticklabels(product_labels, rotation=45)
        self.sc.axes.legend(["Profit înainte de discount", "Profit după discount" ])
        self.sc.axes.set_xlabel("Product ID")
        self.sc.axes.set_ylabel("Profit")
        self.sc.axes.set_title(f"Top 10 Products - Profit Before and After {discount}% Discount")
        self.sc.draw()
        self.show()



    def export_graph(self):
        category = self.category_cb.currentText()
        discount = float(self.input.text())

        top_10_before_discount, top_10_after_discount = calculate_top_products_profit(category, discount)

        export_top_products_profit(category, discount, top_10_before_discount, top_10_after_discount)