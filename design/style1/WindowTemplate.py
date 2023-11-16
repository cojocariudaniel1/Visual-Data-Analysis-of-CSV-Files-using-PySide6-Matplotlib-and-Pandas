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


class WindowTemplate(QtWidgets.QMainWindow):
    def __init__(self, title_text):
        super().__init__()

        self.APP_RES = (900, 800)
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
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Create the layout widget for the chart
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 230, 840, 550))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        # Create the chart layout
        self.chart_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.chart_layout.setContentsMargins(0, 0, 0, 0)
        self.chart_layout.setObjectName("chart_layout")

        # Create and add the chart and toolbar to the chart layout
        self.sc = MplCanvas(self, width=5, height=3, dpi=85)
        self.toolbar = NavigationToolbar(self.sc, self)
        self.chart_layout.addWidget(self.sc, 0, 0)  # Add the chart
        self.chart_layout.addWidget(self.toolbar, 1, 0)  # Add the toolbar





        # Show the central widget to make the layout visible
        self.setCentralWidget(self.centralwidget)

        self.button = Button("Genereaza grafic", None, self)
        self.button.setGeometry(QRect(665, 170, 175, 40))

        self.export = Button("Export", None, self)
        self.export.setGeometry(QRect(665, 750, 175, 40))

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
