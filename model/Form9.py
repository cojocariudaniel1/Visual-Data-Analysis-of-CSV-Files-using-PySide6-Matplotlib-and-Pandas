from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

from design.style1.QLabelXButton import QLabelXButton
from design.style1.QTComboBox import QTComboBox
from design.style1.WindowTemplate import WindowTemplate
from functions.basic_functions import get_ShipMode
from functions.form9_methods import product_profitability_by_state, export_product_profitability


class Form9(WindowTemplate):
    def __init__(self,title_text):
        super().__init__(title_text)

        self.setObjectName("Form1")

        self.setObjectName("Form8")

        pixmap = QPixmap("imgs/x_ button.png")
        pixmap = pixmap.scaled(25, 25, Qt.KeepAspectRatio)
        self.x_button = QLabelXButton(parent=self)
        self.x_button.setGeometry(QRect(self.APP_RES[0] - 45, 15, 25, 25))
        self.x_button.setPixmap(pixmap)

        self.alegere_shipmode_label = QLabel("Segment:  ", self)
        self.alegere_shipmode_label.setGeometry(QRect(50, 125, 200, 50))
        self.alegere_shipmode_label.setStyleSheet(
            "border: 1px solid gray; border-radius: 10px; background-color: white; "
            "color: black;}")
        self.alegere_shipmode_label.setFont(QtGui.QFont("Helvetica", 13))

        self.shipmode_cb = QTComboBox(self)
        self.shipmode_cb.setGeometry(QRect(230, self.alegere_shipmode_label.y(), 170, 50))
        self.populate_shipmode_cb()
        self.button.func = self.generate_graph
        self.export.func = self.export_graph
    def populate_shipmode_cb(self):
        data = get_ShipMode()

        for item in data:
            self.shipmode_cb.addItem(item)

    def generate_graph(self):
        obj = product_profitability_by_state(self.shipmode_cb.currentText())
        self.sc.axes.clear()
        x1 = obj[0]
        y1 = obj[1]

        self.sc.axes.bar(x1, y1, color='royalblue')

        self.sc.axes.set_xlabel('Produse')
        self.sc.axes.set_ylabel('Profit')

        self.sc.axes.tick_params(axis="x", labelrotation=90)

        self.sc.draw()
        self.show()

    def export_graph(self):
        obj = product_profitability_by_state(self.shipmode_cb.currentText())
        x_values = obj[0]
        y_values = obj[1]
        ship_mode = self.shipmode_cb.currentText()

        export_product_profitability(x_values, y_values, ship_mode)