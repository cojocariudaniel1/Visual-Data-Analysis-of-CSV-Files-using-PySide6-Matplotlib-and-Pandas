from PySide6 import QtGui
from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

from design.style1.QLabelXButton import QLabelXButton
from design.style1.QTComboBox import QTComboBox
from design.style1.WindowTemplate import WindowTemplate
from functions.basic_functions import get_City

from functions.form1_methods import evidențiere_comenzi_oras, export_evidentiere_comenzi_oras


class Form1(WindowTemplate):
    def __init__(self, title_text):
        super().__init__(title_text)

        self.setObjectName("Form1")
        pixmap = QPixmap("imgs/x_ button.png")
        pixmap = pixmap.scaled(25, 25, Qt.KeepAspectRatio)
        self.x_button = QLabelXButton(parent=self)
        self.x_button.setGeometry(QRect(self.APP_RES[0] - 45, 15, 25, 25))
        self.x_button.setPixmap(pixmap)

        self.selecteaza_produs_label = QLabel("Selecteaza Oras: ", self)
        self.selecteaza_produs_label.setGeometry(QRect(50, 125, 200, 50))
        self.selecteaza_produs_label.setStyleSheet("border: 1px solid gray; border-radius: 10px; background-color: white; "
                                  "color: black;}")
        self.selecteaza_produs_label.setFont(QtGui.QFont("Helvetica", 13))
        self.cities_cb = QTComboBox(self)
        self.cities_cb.setGeometry(QRect(230, self.selecteaza_produs_label.y(), 125, 50))

        self.button.func = self.generate_graph
        self.export.func = self.export_graph
        self.populate_combobox()

    def populate_combobox(self):
        cities = get_City()
        for j in cities:
            self.cities_cb.addItem(str(j))

    def generate_graph(self):
        obj = evidențiere_comenzi_oras(self.cities_cb.currentText())
        self.sc.axes.clear()
        x = obj[0]
        y = obj[1]
        new_list_x = []
        new_list_y = []
        if len(x) > 30:
            num_clients = len(x)
            min_ticks = 30
            step = max(num_clients // min_ticks, 1)

            for i in range(0, len(x), step):
                new_list_x.append(x[i])
                new_list_y.append(y[i])
        if len(new_list_x) > 29:
            x = new_list_x
            y = new_list_y
        self.sc.axes.bar(x, y)
        self.sc.axes.tick_params(axis="x", labelrotation=90)
        self.sc.axes.legend(["Numar de comenzi", "Clienți"])
        self.sc.axes.set_title(f"Evidențierea comenzilor plasate de clienții în orașul {self.cities_cb.currentText()}")
        self.sc.draw()
        self.show()

    def export_graph(self):
        export_evidentiere_comenzi_oras(self.cities_cb.currentText())