import io
import logging

from PySide6 import QtWidgets, QtGui

from PySide6.QtWebEngineWidgets import QWebEngineView
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from functions.geo_map_functions import map_create, get_info, mean_sales, zona
from views.map_form import Ui_MainWindow


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=300):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)
        self.fig.tight_layout()


class GeoMap(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.ui.chart_layout.addWidget(self.sc)


        try:
            # Adaugare harta in interfata
            data = io.BytesIO()
            geo_map = map_create()
            geo_map.save(data, close_file=False)
            self.webview = QWebEngineView()
            self.webview.setHtml(data.getvalue().decode())
            self.ui.map_layout.addWidget(self.webview)

            self.gen_auto_graph()

            self.ui.checkBox.clicked.connect(self.check_button)
            self.ui.genereazaGraph_Button.clicked.connect(self.vizualizeaza)

        except BaseException as e:
            logging.exception(e)

    def vizualizeaza(self):
        if self.ui.checkBox.isChecked():
            self.get_map_html(self.ui.combobox.currentText())
            self.generate_graph()
        else:
            self.get_map_html()
            self.gen_auto_graph()

    def get_map_html(self, regiune=None):
        try:
            data = io.BytesIO()
            geo_map = None
            if not regiune:
                for i in reversed(range(self.ui.map_layout.count())):
                    self.ui.map_layout.itemAt(i).widget().setParent(None)
                geo_map = map_create()
                geo_map.save(data, close_file=False)

                self.webview = QWebEngineView()
                self.webview.setHtml(data.getvalue().decode())
                self.ui.map_layout.addWidget(self.webview)
            else:
                for i in reversed(range(self.ui.map_layout.count())):
                    self.ui.map_layout.itemAt(i).widget().setParent(None)
                geo_map = zona(regiune)
                print('try regiune')
                geo_map.save(data, close_file=False)

                self.webview = QWebEngineView()
                self.webview.setHtml(data.getvalue().decode())
                self.ui.map_layout.addWidget(self.webview)
        except BaseException as e:
            logging.exception(e)

    def check_button(self):
        if self.ui.checkBox.isChecked():
            self.ui.combobox.setEnabled(True)
        else:
            self.ui.combobox.setEnabled(False)

    def gen_auto_graph(self):
        data = mean_sales()
        index = []
        values = []
        for i in data:
            index.append(i[0])
            values.append(i[1])

        self.sc.axes.clear()
        x1 = values
        labels = index
        explode = []
        for i in range(len(x1)):
            explode.append(0.1)
        self.sc.axes.pie(x1, explode=explode, labels=labels, autopct='%1.1f%%',
                         shadow=True, startangle=90)

        # self.sc.axes.tick_params(axis="x", labelrotation=90)
        self.sc.draw()
        self.show()

    def generate_graph(self):
        data = get_info(self.ui.combobox.currentText())
        index = []
        values = []
        for i in data:
            index.append(i[0])
            values.append(i[1])
        self.sc.axes.clear()
        x1 = values
        labels = index
        explode = []
        for i in range(len(x1)):
            explode.append(0.1)

        self.sc.axes.pie(x1, explode=explode, labels=labels, autopct='%1.1f%%',
                         shadow=True, startangle=90)

        # self.sc.axes.tick_params(axis="x", labelrotation=90)
        self.sc.draw()
        self.show()
