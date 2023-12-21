from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt, QRect, QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QSlider

from ExportTemplate import ExportTemplate
from design.style1.QLabelXButton import QLabelXButton
from design.style1.QTComboBox import QTComboBox
from design.style1.WindowTemplate import WindowTemplate
from functions.basic_functions import get_State
from functions.form3_methods import find_least_profitable_products, export_least_profitable_products


class Form3(WindowTemplate):
    def __init__(self, title_text):
        super().__init__(title_text)

        self.setObjectName("Form2")
        self.new_window = None

        pixmap = QPixmap("imgs/x_ button.png")
        pixmap = pixmap.scaled(25, 25, Qt.KeepAspectRatio)
        self.x_button = QLabelXButton(parent=self)
        self.x_button.setGeometry(QRect(self.APP_RES[0] - 45, 15, 25, 25))
        self.x_button.setPixmap(pixmap)
        self.setObjectName("Form1")

        self.alegere_state_label = QLabel("Selecteaza statul: ", self)
        self.alegere_state_label.setGeometry(QRect(50, 125, 200, 50))
        self.alegere_state_label.setStyleSheet(
            "border: 1px solid gray; border-radius: 10px; background-color: white; "
            "color: black;}")
        self.alegere_state_label.setFont(QtGui.QFont("Helvetica", 13))

        self.state_cb = QTComboBox(self)
        self.state_cb.setGeometry(QRect(230, self.alegere_state_label.y(), 170, 50))
        self.populare_combobox_state_cb()

        self.horizontalSlider = QSlider(self)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setGeometry(QRect(100,185, 500, 30))
        self.horizontalSlider.valueChanged.connect(self.update_label)
        self.slider_label_text = QLabel(f"{str(self.horizontalSlider.value())}",self)
        self.slider_label_text.setGeometry(QRect(620, 185, 50, 30))
        self.horizontalSlider.setValue(30)
        self.export.func = self.export_graph
        self.button.func = self.generate_graph
    def populare_combobox_state_cb(self):
        data = get_State()

        for item in data:
            self.state_cb.addItem(item)


    def update_label(self, value):
        self.slider_label_text.setText(str(value))



    def generate_graph(self):
        obj = find_least_profitable_products(self.state_cb.currentText(), int(self.horizontalSlider.value()))
        self.sc.axes.clear()
        x = obj[0]
        y = obj[1]
        self.sc.axes.plot(x, y)
        self.sc.axes.tick_params(axis="x", labelrotation=90)
        self.sc.axes.legend(["Profit", "Product"])
        self.sc.draw()
        self.show()

    def export_graph(self):
        self.new_window = ExportTemplate("Export", "Form3", [self.state_cb.currentText(), int(self.horizontalSlider.value())] )
        self.new_window.show()