import sys

import matplotlib
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import QRect, Qt, QPoint
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel
from matplotlib import rcParams

from design.style1.Canvas import MplCanvas
from design.style1.QLabelXButton import QLabelXButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from design.style1.QTButtonCustom import Button

rcParams.update({'figure.autolayout': True})
matplotlib.use('Qt5Agg')


class ExportTemplate(QtWidgets.QMainWindow):
    def __init__(self, title_text):
        super().__init__()
        print("ExportTemplate __init__ called")
        self.APP_RES = (550, 700)
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

        self.title_text = title_text
        self.title = QLabel(self.title_text, self)
        self.title.setGeometry(QRect(100, 15, self.APP_RES[0] - 180, 60))
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setFont(QtGui.QFont("Helvetica", 16))
        self.title.setWordWrap(True)

        pixmap = QPixmap("imgs/x_ button.png")
        pixmap = pixmap.scaled(25, 25, Qt.KeepAspectRatio)
        self.x_button = QLabelXButton(parent=self)
        self.x_button.setGeometry(QRect(self.APP_RES[0] - 45, 15, 25, 25))
        self.x_button.setPixmap(pixmap)




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
    mainWindow = ExportTemplate("Export")
    mainWindow.show()
    sys.exit(app.exec())
