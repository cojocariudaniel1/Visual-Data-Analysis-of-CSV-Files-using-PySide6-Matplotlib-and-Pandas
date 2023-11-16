from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor, QPen, QFont


class QLabelCenter(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("QLabelCenter")

        self.setStyleSheet("#QLabelCenter {border: 1px solid gray; border-radius: 10px; background-color: white; "
                           "color: black;}")
        self.setAlignment(Qt.AlignCenter)

        font = QFont()
        font.setPointSize(12)
        self.setFont(font)

