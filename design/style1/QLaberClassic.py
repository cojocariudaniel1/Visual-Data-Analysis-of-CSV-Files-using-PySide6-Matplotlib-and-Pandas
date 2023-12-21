from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QColor, QPen, QFont


class QLabelClassic(QLabel):
    def __init__(self, text, parent=None, geometry = None):
        super().__init__(parent=parent)
        self.setObjectName("QLabelCenter")
        self.setGeometry(geometry)
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)

        font = QFont()
        font.setPointSize(14)
        self.setFont(font)

