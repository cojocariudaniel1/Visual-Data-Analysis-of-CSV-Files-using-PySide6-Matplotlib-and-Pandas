import numpy as np
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

from ExportTemplate import ExportTemplate
from design.style1.QLabelXButton import QLabelXButton
from design.style1.QTComboBox import QTComboBox
from design.style1.WindowTemplate import WindowTemplate
from functions.basic_functions import get_State, get_Category
from functions.form7_methods import profit_loss_by_state_category, export_profit_loss_by_state_category


class Form7(WindowTemplate):
    def __init__(self,title_text):
        super().__init__(title_text)

        self.setObjectName("Form7")

        pixmap = QPixmap("imgs/x_ button.png")
        pixmap = pixmap.scaled(25, 25, Qt.KeepAspectRatio)
        self.x_button = QLabelXButton(parent=self)
        self.x_button.setGeometry(QRect(self.APP_RES[0] - 45, 15, 25, 25))
        self.x_button.setPixmap(pixmap)
        self.setObjectName("Form1")

        self.alegere_categorie_label = QLabel("Selecteaza categoria: ", self)
        self.alegere_categorie_label.setGeometry(QRect(50, 125, 200, 50))
        self.alegere_categorie_label.setStyleSheet(
            "border: 1px solid gray; border-radius: 10px; background-color: white; "
            "color: black;}")
        self.alegere_categorie_label.setFont(QtGui.QFont("Helvetica", 13))

        self.category_cb = QTComboBox(self)
        self.category_cb.setGeometry(QRect(230, self.alegere_categorie_label.y(), 170, 50))
        self.populare_combobox_categorii()
        self.export.func = self.export_graph
        self.button.func = self.generate_graph

    def populare_combobox_categorii(self):
        data = get_Category()

        for item in data:
            self.category_cb.addItem(item)

    def generate_graph(self):
        obj = profit_loss_by_state_category(self.category_cb.currentText())
        self.sc.axes.clear()
        states = obj[0]
        values = obj[1]  # Profits
        losses = obj[2]  # Losses
        print(states)
        print(values)
        print(losses)
        x = np.arange(len(states))
        width = 0.35

        self.sc.axes.bar(x, values, width, label='Profit', color='royalblue')
        self.sc.axes.bar(x, losses, width, label='Pierdere', color='tomato')

        self.sc.axes.set_xlabel('Stat')
        self.sc.axes.set_ylabel('Valoare')
        self.sc.axes.set_title(
            f'Compararea Profitului și Pierderii pe Categoria {self.category_cb.currentText()} (după State)')
        self.sc.axes.set_xticks(x)
        self.sc.axes.set_xticklabels(states, rotation=45, ha='right')
        self.sc.axes.legend()

        self.sc.draw()
        self.show()

    def export_graph(self):
        category = self.category_cb.currentText()
        states, profits, losses = profit_loss_by_state_category(category)


        self.new_window = ExportTemplate("Export", "Form7", [category, states, profits, losses])
        self.new_window.show()