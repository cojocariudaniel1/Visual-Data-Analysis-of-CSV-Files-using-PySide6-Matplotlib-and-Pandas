from PySide6 import QtGui
from PySide6.QtWidgets import QComboBox


class QTComboBox(QComboBox):
    def __init__(self, parent=None, ):
        super().__init__(parent)
        self.setObjectName("QComboBox")
        self.setStyleSheet(
            "#QComboBox {background-color: white; color: black; border: 1px solid gray; border-radius: 0px; "
            "border-top-left-radius: 10px; border-bottom-left-radius: 10px;}")

        self.setFont(QtGui.QFont("Helvetica", 13))
