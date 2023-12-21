import logging

from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QRect, Qt, QPoint
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

from design.style1.CustomTable import CustomTableWidget
from design.style1.QLabelXButton import QLabelXButton
from design.style1.QTLabel_center import QLabelCenter
from design.style1.QTButtonCustom import Button
from design.style1.QTRadioButton import RadioButton
from model.Form1 import Form1
from model.Form11 import Form11
from model.Form2 import Form2
from model.Form3 import Form3
from model.Form4 import Form4
from model.Form5 import Form5
from model.Form6 import Form6
from model.Form7 import Form7
from model.Form8 import Form8
from model.Form9 import Form9
from model.GeoMap import GeoMap

RES = 1920, 1080
APP_RES = 940, 810


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Basic Settings
        self.new_window = None
        self.setObjectName("mainWindow")
        self.setGeometry(QRect(int(RES[0] / 2 - APP_RES[0] / 2), 75, APP_RES[0], APP_RES[1]))
        self.setStyleSheet("#mainWindow {background-color:#e6fcff}")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.dragging = False
        self.offset = QPoint()
        background_image = QLabel(self)
        pixmap = QPixmap("imgs/background_main_window.jpg")  # Setează calea către imagine
        scaled_pixmap = pixmap.scaled(APP_RES[0], APP_RES[1])

        background_image.setPixmap(scaled_pixmap)
        background_image.setGeometry(0, 0, APP_RES[0], APP_RES[1])


        self.title = QLabel("SAD Project", self)
        self.title.setGeometry(QRect(int(APP_RES[0] / 2 - self.title.width() + 45), -15, 150, 100))
        self.title.setFont(QtGui.QFont("Helvetica", 16))

        # Create main button
        self.buton = Button("Open Form", self.open_forms, self)
        self.buton.setGeometry(QRect(320, 740, 280, 50))
        self.buton.setObjectName("QButtonCustom")

        pixmap = QPixmap("imgs/x_ button.png")
        pixmap = pixmap.scaled(25,25, Qt.KeepAspectRatio)
        self.x_button = QLabelXButton(parent=self)
        self.x_button.setGeometry(QRect(APP_RES[0] - 45,15,25,25))
        self.x_button.setPixmap(pixmap)
        # Settup the radio buttons

        self.radio_button_form1 = RadioButton(" Evidențierea comenzilor plasate de clienți dintr-o anumit oras.", "Form1", self)
        self.radio_button_form1.setGeometry(QRect(60, 70, 505, 50))

        self.radio_button_form2 = RadioButton("Frecvența categoriilor, în funcție de vânzările și profitul realizate "
                                              "pe subcategorii, grupându-se pe categorii.", "Form2", self)
        self.radio_button_form2.setGeometry(QRect(60, 130, 830, 50))

        self.radio_button_form3 = RadioButton(" Cele mai neprofitabile produse existente în catalog în funcție de stat.", "Form3", self)
        self.radio_button_form3.setGeometry(QRect(60, 190, 550, 50))

        self.radio_button_form4 = RadioButton(" Profitul realizat după aplicarea discount-ului ale produselor pe categorii.", "Form4", self)
        self.radio_button_form4.setGeometry(QRect(60, 250, 570, 50))

        self.radio_button_form5 = RadioButton(" Evidențierea celor mai des cumpărate produse din fiecare subcategorie.", "Form5", self)
        self.radio_button_form5.setGeometry(QRect(60, 310, 574, 50))

        self.radio_button_form6 = RadioButton(" Top 10 produse care generează cel mai mic profit dintr-o subcategorie.", "Form6", self)
        self.radio_button_form6.setGeometry(QRect(60, 370, 574, 50))

        self.radio_button_form7 = RadioButton(" Compararea profitului și a pierderii pentru fiecare stat, în funcție de categoria.", "Form7", self)
        self.radio_button_form7.setGeometry(QRect(60, 430, 590, 50))

        self.radio_button_form8 = RadioButton(" Raportul perioadei, pe fiecare categorie, de la data plasării."
                                              "comenzii, până la data expediției acesteia.", "Form8", self)
        self.radio_button_form8.setGeometry(QRect(60, 490, 784, 50))

        self.radio_button_form9 = RadioButton(" Profitabilitatea produselor în funcție de statul în care locuiesc clienții în funcție de ship mod.", "Form9", self)
        self.radio_button_form9.setGeometry(QRect(60, 550, 720, 50))

        self.radio_button_form10 = RadioButton("Vanzari pe categorii in functie de regiune din USA", "Form10", self)
        self.radio_button_form10.setGeometry(QRect(60, 610, 720, 50))

        self.radio_button_form11 = RadioButton("Choropleth Map", "Form11", self)
        self.radio_button_form11.setGeometry(QRect(60, 670, 720, 50))



        self.forms_list = [
            self.radio_button_form1,
            self.radio_button_form2,
            self.radio_button_form3,
            self.radio_button_form4,
            self.radio_button_form5,
            self.radio_button_form6,
            self.radio_button_form7,
            self.radio_button_form8,
            self.radio_button_form9,
            self.radio_button_form10,
            self.radio_button_form11,
        ]

    def open_forms(self):
        for i in self.forms_list:
            if i.isChecked():
                if i.objectName() == "Form1":
                    self.new_window = Form1("Evidențierea comenzilor plasate de clienți.")
                    self.new_window.show()
                if i.objectName() == "Form2":
                    self.new_window = Form2("Frecvența categoriilor, în funcție de vânzările și profitul realizate pe subcategorii, grupându-se pe categorii")
                    self.new_window.show()
                if i.objectName() == "Form3":
                    self.new_window = Form3("Cele mai neprofitabile produse existente în catalog în funcție de stat")
                    self.new_window.show()
                if i.objectName() == "Form4":
                    self.new_window = Form4("Profitul realizat după aplicarea discount-ului ale produselor pe categorii")
                    self.new_window.show()
                if i.objectName() == "Form5":
                    self.new_window = Form5("Evidențierea celor mai des cumpărate produse din fiecare subcategorie.")
                    self.new_window.show()
                if i.objectName() == "Form6":
                    self.new_window = Form6("Top 10 produse care generează cel mai mic profit dintr-o subcategorie")
                    self.new_window.show()
                if i.objectName() == "Form7":
                    self.new_window = Form7("Compararea profitului și a pierderii pentru fiecare stat, în funcție de categoria.")
                    self.new_window.show()
                if i.objectName() == "Form8":
                    self.new_window = Form8("Raportul perioadei, pe fiecare categorie si sub-categorie, de la data plasării."
                                              "comenzii, până la data expediției acesteia")
                    self.new_window.show()
                if i.objectName() == "Form9":
                    self.new_window = Form9("Profitabilitatea produselor în funcție de statul în care locuiesc clienții în funcție de ship mod")
                    self.new_window.show()

                if i.objectName() == "Form10":
                    self.new_window = GeoMap()
                    self.new_window.show()

                if i.objectName() == "Form11":
                    self.new_window = Form11()
                    self.new_window.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()
            self.dragging = True

    def mouseMoveEvent(self, event):
        if self.dragging:
            new_pos = event.globalPos() - self.offset
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False