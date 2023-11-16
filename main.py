import sys

from PySide6 import QtWidgets

from model.mainwindow import MainWindow

app = QtWidgets.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec())

