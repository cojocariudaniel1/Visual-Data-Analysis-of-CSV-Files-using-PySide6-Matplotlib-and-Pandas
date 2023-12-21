import sys

import matplotlib
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import QRect, Qt, QPoint
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QRadioButton, QLineEdit, QCheckBox, QFileDialog
from matplotlib import rcParams

from design.style1.Canvas import MplCanvas
from design.style1.QLabelAnimation import QLabelAnimation
from design.style1.QLabelXButton import QLabelXButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from design.style1.QLaberClassic import QLabelClassic
from design.style1.QRadioButtonClassic import RadioButtonClassic
from design.style1.QTButtonCustom import Button
from design.style1.QTComboBox import QTComboBox
from design.style1.QTLabel_center import QLabelCenter
from functions.form1_methods import export_evidentiere_comenzi_oras
from functions.form2_methods import export_frecventa_categorii_pe_subcategorie
from functions.form3_methods import export_least_profitable_products
from functions.form4_methods import export_top_products_profit
from functions.form5_methods import export_profit_evolution
from functions.form6_methods import export_bottom_profit_products
from functions.form7_methods import export_profit_loss_by_state_category
from functions.form8_methods import export_order_processing_duration_graph
from functions.form9_methods import export_product_profitability

rcParams.update({'figure.autolayout': True})
matplotlib.use('Qt5Agg')


class ExportTemplate(QtWidgets.QMainWindow):
    def __init__(self, title_text, form, data = None):
        super().__init__()
        print("ExportTemplate __init__ calleddddd")
        self.APP_RES = (800, 600)
        self.setGeometry(QRect(int(1920 / 2 - self.APP_RES[0] / 2), 75, self.APP_RES[0], self.APP_RES[1]))
        self.setStyleSheet("#mainWindow {background-color:#e6fcff}")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.dragging = False
        self.offset = QPoint()
        background_image = QLabel(self)
        background_image_pixmap = QPixmap("imgs/background_image.jpg")  # Setează calea către imagine
        scaled_pixmap = background_image_pixmap.scaled(self.APP_RES[0], self.APP_RES[1])

        background_image.setPixmap(scaled_pixmap)
        background_image.setGeometry(0, 0, self.APP_RES[0], self.APP_RES[1])

        self.title_text = title_text
        self.title = QLabel(self.title_text, self)
        self.title.setGeometry(QRect(100, 15, self.APP_RES[0] - 180, 60))
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setFont(QtGui.QFont("Helvetica", 16))
        self.title.setWordWrap(True)

        pixmap1 = QPixmap("imgs/x_ button.png")
        pixmap1 = pixmap1.scaled(25, 25, Qt.KeepAspectRatio)
        self.x_button = QLabelXButton(parent=self)
        self.x_button.setGeometry(QRect(self.APP_RES[0] - 45, 15, 25, 25))
        self.x_button.setPixmap(pixmap1)

        self.bg_obj = []
        self.exponential_background = QLabelAnimation("exponential", self)
        self.liniar_background = QLabelAnimation("liniar", self)
        self.logarithmic_background = QLabelAnimation("logarithmic", self)
        self.poly_background = QLabelAnimation("poly", self)
        self.power_background = QLabelAnimation("power", self)
        self.moving_avarage_background = QLabelAnimation("moving_avarage", self)

        self.bg_obj.append(self.exponential_background)
        self.bg_obj.append(self.liniar_background)
        self.bg_obj.append(self.logarithmic_background)
        self.bg_obj.append(self.poly_background)
        self.bg_obj.append(self.power_background)
        self.bg_obj.append(self.moving_avarage_background)

        self.exponential_image_QP = QPixmap("imgs/exponential_img.png")
        self.exponential_image_QP = self.exponential_image_QP.scaled(50, 50, Qt.KeepAspectRatio)
        self.exponential_image = QLabel(self)
        self.exponential_image.setPixmap(self.exponential_image_QP)
        self.exponential_image.setGeometry(QRect(50, 100, 50, 60))

        self.liniar_image_QP = QPixmap("imgs/linear_img.png")
        self.liniar_image_QP = self.liniar_image_QP.scaled(50, 50, Qt.KeepAspectRatio)
        self.liniar_image = QLabel(self)
        self.liniar_image.setPixmap(self.liniar_image_QP)
        self.liniar_image.setGeometry(QRect(50, 180, 50, 60))

        self.logarithmic_image_QP = QPixmap("imgs/logarithmic_img.png")
        self.logarithmic_image_QP = self.logarithmic_image_QP.scaled(50, 50, Qt.KeepAspectRatio)
        self.logarithmic_image = QLabel(self)
        self.logarithmic_image.setPixmap(self.logarithmic_image_QP)
        self.logarithmic_image.setGeometry(QRect(50, 260, 50, 60))

        self.poly_image_QP = QPixmap("imgs/polynomial_img.png")
        self.poly_image_QP = self.poly_image_QP.scaled(50, 50, Qt.KeepAspectRatio)
        self.poly_image = QLabel(self)
        self.poly_image.setPixmap(self.poly_image_QP)
        self.poly_image.setGeometry(QRect(50, 340, 50, 60))

        self.power_image_QP = QPixmap("imgs/exponential_img.png")
        self.power_image_QP = self.power_image_QP.scaled(50, 50, Qt.KeepAspectRatio)
        self.power_image = QLabel(self)
        self.power_image.setPixmap(self.power_image_QP)
        self.power_image.setGeometry(QRect(50, 420, 50, 60))

        self.moving_avarage_image_QP = QPixmap("imgs/moving_avarage_img.png")
        self.moving_avarage_image_QP = self.moving_avarage_image_QP.scaled(50, 50, Qt.KeepAspectRatio)
        self.moving_avarage_image = QLabel(self)
        self.moving_avarage_image.setPixmap(self.moving_avarage_image_QP)
        self.moving_avarage_image.setGeometry(QRect(50, 500, 50, 60))

        self.exponential_background.setGeometry(40, 100, 220, 65)
        self.exponential_radioButton = RadioButtonClassic("Exponential", "Exp", self.exponential_background,
                                                          self.bg_obj, self, QRect(125, 95, 130, 75))

        self.liniar_background.setGeometry(40, 180, 220, 65)
        self.liniar_rb = RadioButtonClassic("Linear", "Lin", self.liniar_background, self.bg_obj, self,
                                            QRect(125, 175, 130, 75))

        self.logarithmic_background.setGeometry(40, 260, 220, 65)
        self.logarithmic_rb = RadioButtonClassic("Log", "Log", self.logarithmic_background, self.bg_obj, self,
                                                 QRect(125, 255, 130, 75))

        self.poly_background.setGeometry(40, 340, 220, 65)
        self.poly_rb = RadioButtonClassic("Polynomial", "Log", self.poly_background, self.bg_obj, self,
                                          QRect(125, 335, 130, 75))

        self.power_background.setGeometry(40, 420, 220, 65)
        self.power_rb = RadioButtonClassic("Power", "Log", self.power_background, self.bg_obj, self,
                                           QRect(125, 415, 130, 75))

        self.moving_avarage_background.setGeometry(40, 500, 220, 65)
        self.moving_avarage_rb = RadioButtonClassic("Moving_Avarage", "Log", self.moving_avarage_background,
                                                    self.bg_obj, self, QRect(125, 495, 130, 75))

        self.border_label = QLabel(self)
        self.border_label.setGeometry(290, 100, 285, 380)
        self.border_label.setStyleSheet("border: 1px solid gray; border-radius: 10px; ""color: black;")


        self.label_order = QLabelClassic("Order:", self, QRect(300, 100, 100, 50))
        self.order_lineEdit = QLineEdit(self)
        self.order_lineEdit.setGeometry(QRect(410, 115, 25 ,25))
        self.order_lineEdit.setText('1')

        self.period_label = QLabelClassic("Period:", self, QRect(300, 160, 100, 50))
        self.period_lineEdit = QLineEdit(self)
        self.period_lineEdit.setGeometry(QRect(410, 175, 25 ,25))
        self.period_lineEdit.setText('1')

        self.intercept_label = QLabelClassic("Intercept:", self, QRect(300, 210, 100, 50))
        self.intercept_lineEdit = QLineEdit(self)
        self.intercept_lineEdit.setGeometry(QRect(410, 225, 25 ,25))
        self.intercept_lineEdit.setText('0.1')

        self.forward_label = QLabelClassic("Forward:", self, QRect(300, 260, 100, 50))
        self.forward_lineEdit = QLineEdit(self)
        self.forward_lineEdit.setGeometry(QRect(410, 275, 25 ,25))
        self.forward_lineEdit.setText('0.1')

        self.backward_label = QLabelClassic("Backward:", self, QRect(300, 310, 100, 50))
        self.backward_lineEdit = QLineEdit(self)
        self.backward_lineEdit.setGeometry(QRect(410, 325, 25 ,25))
        self.backward_lineEdit.setText('0.1')


        self.equation_label = QLabelClassic("Display equation:", self, QRect(300, 360, 150, 50))
        self.equation_checkbox = QCheckBox(self)
        self.equation_checkbox.setGeometry(QRect(455, 375, 25 ,25))

        self.trendline_color_label = QLabelClassic("Trend Line color:", self, QRect(300, 410, 150, 50))
        self.trendlinecolor_combobox = QTComboBox(self)
        self.trendlinecolor_combobox.setGeometry(QRect(460, 410, 100, 50))
        self.populate_trendlineColorCB()

        self.button_export = Button("Export", self.export, self)
        self.button_export.setGeometry(QRect(340, 510, 150, 50))

        self.form = form
        self.data = data

    def export(self):
        trendLine_attrs = self.getTrendLineDict()

        if self.form == "Form3":
            folderpath = QFileDialog.getSaveFileName(self, 'Select Folder')
            if folderpath:
                export_least_profitable_products(self.data[0], self.data[1], trendLine_attrs, folderpath)
        elif self.form == "Form4":
            folderpath = QFileDialog.getSaveFileName(self, 'Select Folder')
            if folderpath:
                export_top_products_profit(self.data[0], self.data[1], self.data[2], self.data[3], trendLine_attrs)
        elif self.form == "Form1":
            folderpath = QFileDialog.getSaveFileName(self, 'Select Folder')
            if folderpath:
                export_evidentiere_comenzi_oras(self.data[0], trendLine_attrs, folderpath)
        elif self.form == "Form2":
            folderpath = QFileDialog.getSaveFileName(self, 'Select Folder')
            if folderpath:
                export_frecventa_categorii_pe_subcategorie(self.data[0], self.data[1], trendLine_attrs, folderpath)
        elif self.form == "Form5":
            folderpath = QFileDialog.getSaveFileName(self, 'Select Folder')
            if folderpath:
                export_profit_evolution(self.data[0], self.data[1], self.data[2], self.data[3], self.data[4],trendLine_attrs, folderpath)
        elif self.form == "Form6":
            folderpath = QFileDialog.getSaveFileName(self, 'Select Folder')
            if folderpath:
                export_bottom_profit_products(self.data[0], self.data[1], self.data[2],trendLine_attrs, folderpath)
        elif self.form == "Form7":
            folderpath = QFileDialog.getSaveFileName(self, 'Select Folder')
            if folderpath:
                export_profit_loss_by_state_category(self.data[0], self.data[1], self.data[2],self.data[3], folderpath)
        elif self.form == "Form8":
            folderpath = QFileDialog.getSaveFileName(self, 'Select Folder')
            if folderpath:
                export_order_processing_duration_graph(self.data[0], self.data[1], self.data[2],self.data[3], folderpath)
        elif self.form == "Form9":
            folderpath = QFileDialog.getSaveFileName(self, 'Select Folder')
            if folderpath:
                export_product_profitability(self.data[0], self.data[1], self.data[2], folderpath)


    def getTrendLineDict(self):
        trendLineType = None
        rb_list = [self.liniar_rb, self.exponential_radioButton, self.logarithmic_rb, self.poly_rb, self.power_rb, self.moving_avarage_rb]
        for a in rb_list:
            if a.isChecked():
                trendLineType = a.text().lower()

        trendLine_attrs = {            "equation": self.equation_checkbox.isChecked(),

            "type": trendLineType,
            "order": int(self.order_lineEdit.text()),
            "period": int(self.period_lineEdit.text()),
            "intercept": float(self.intercept_lineEdit.text()),
            "name": "Trend Line",
            "forward": float(self.forward_lineEdit.text()),
            "backward": float(self.backward_lineEdit.text()),
            "line_color": self.trendlinecolor_combobox.currentText(),
            "line_width": 1
        }

        return trendLine_attrs


    def populate_trendlineColorCB(self):
        colors = ["red", "green", "black", "brown", "blue", "pink", "purple"]
        for i in colors:
            self.trendlinecolor_combobox.addItem(i)

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = ExportTemplate("Export", "Form3")
    mainWindow.show()
    sys.exit(app.exec())
