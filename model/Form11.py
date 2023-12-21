from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QRect, Qt, QPoint
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

from ExportTemplate import ExportTemplate
from design.style1.QLabelXButton import QLabelXButton
from design.style1.QTButtonCustom import Button
from design.style1.QTComboBox import QTComboBox
from design.style1.WindowTemplate import WindowTemplate
from functions.basic_functions import get_ShipMode
from functions.ccc import grafic_bar_vanzari_pe_an, harta_vanzari_pe_luna, grafic_bar_pe_profit, \
    grafic_bar_vanzari_pe_luna
from functions.form9_methods import product_profitability_by_state, export_product_profitability
from functions.geodata import harta_vanzari_pe_an


class Form11(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("Form11")
        self.APP_RES = (600, 300)
        self.setGeometry(QRect(int(1920 / 2 - self.APP_RES[0] / 2), 75, self.APP_RES[0], self.APP_RES[1]))
        self.setStyleSheet("#mainWindow {background-color:#e6fcff}")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.dragging = False
        self.offset = QPoint()
        background_image = QLabel(self)
        pixmap = QPixmap("imgs/background_image.jpg")  # Setează calea către imagine
        scaled_pixmap = pixmap.scaled(self.APP_RES[0], self.APP_RES[1])

        background_image.setPixmap(scaled_pixmap)
        background_image.setGeometry(0, 0, self.APP_RES[0], self.APP_RES[1])

        self.title_text = "Choropleth Map"
        self.title = QLabel(self.title_text, self)
        self.title.setGeometry(QRect(100, 15, self.APP_RES[0] - 180, 60))
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setFont(QtGui.QFont("Helvetica", 16))
        self.title.setWordWrap(True)
        self.setWindowTitle("Choropleth Map")

        pixmap = QPixmap("imgs/x_ button.png")
        pixmap = pixmap.scaled(25, 25, Qt.KeepAspectRatio)
        self.x_button = QLabelXButton(parent=self)
        self.x_button.setGeometry(QRect(self.APP_RES[0] - 45, 15, 25, 25))
        self.x_button.setPixmap(pixmap)

        self.button = Button("Afiseaza Choropleth Map Vanzari pe an in functie de state", harta_vanzari_pe_an, self)
        self.button.setGeometry(QRect(25, 70, 500, 40))

        self.button1 = Button("Afiseaza Choropleth Map Vanzari pe luna in functie de state", harta_vanzari_pe_luna, self)
        self.button1.setGeometry(QRect(25, 140, 500, 40))

        self.button1 = Button("Afiseaza Grafic Bar Map Vanzari pe luna in functie de state", grafic_bar_vanzari_pe_luna, self)
        self.button1.setGeometry(QRect(25, 210, 500, 40))
        #grafic_bar_pe_profit
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Salvăm poziția inițială a cursorului în raport cu fereastra
            self.offset = event.pos()
            self.dragging = True

    def mouseMoveEvent(self, event):
        if self.dragging:
            # Calculăm poziția nouă a fereastrei bazată pe mutarea cursorului
            new_pos = event.globalPos() - self.offset
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
