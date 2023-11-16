from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor, QPen, QFont, QPixmap


class QLabelXButton(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("QLabelXButton")
        self.parent1 = parent
        pixmap = QPixmap("../../imgs/x_ button.png")
        pixmap = pixmap.scaled(100,100, Qt.KeepAspectRatio)
        self.setPixmap(pixmap)


    def mousePressEvent(self, event):
        print('teast')
        self.parent1.close()
        self.close()