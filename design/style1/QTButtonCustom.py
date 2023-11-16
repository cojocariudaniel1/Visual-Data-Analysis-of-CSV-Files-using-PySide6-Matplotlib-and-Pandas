from PySide6 import QtGui
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt, QTimer
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QPushButton


class Button(QPushButton):
    def __init__(self, text, func, parent=None, ):
        super().__init__(parent)
        self.setObjectName("QButtonCustom")
        # Default Style of the object
        self.default_style = ("#QButtonCustom {border: 1px solid gray; border-radius: 10px; background-color: white; "
                              "color: black;}")
        ##
        # Different Style when is clicked.
        self.hover_style = ("#QButtonCustom {border: 1px solid #95a1d6; border-radius: 10px; background-color: "
                              "white; color: black;}")
        ##
        self.clicked_style = ("#QButtonCustom {border: 1px solid #c634eb; border-radius: 10px; background-color: "
                              "white; color: black;}")
        # Basic settings
        self.setText(text)
        self.setStyleSheet(self.default_style)
        self.setFont(QtGui.QFont("Helvetica", 13))
        ##

        # Setting Shadow Animation
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(3)
        self.shadow.setYOffset(3)
        self.setGraphicsEffect(self.shadow)

        self.shadow_animation = QPropertyAnimation(self.shadow, b"yOffset")
        self.shadow_animation.setDuration(100)
        self.shadow_animation.setStartValue(3)
        self.shadow_animation.setEndValue(3)
        self.shadow_animation.setEasingCurve(QEasingCurve.OutCubic)

        self.shadow_animation2 = QPropertyAnimation(self.shadow, b"xOffset")
        self.shadow_animation.setDuration(250)
        self.shadow_animation2.setStartValue(3)
        self.shadow_animation2.setEndValue(8)
        self.shadow_animation2.setEasingCurve(QEasingCurve.OutCubic)

        self.enterEvent = self.on_button_enter
        self.leaveEvent = self.on_button_leave
        ##
        self.func = func


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setStyleSheet(self.clicked_style)
            QTimer.singleShot(350, self.restore_style)
        if self.func is not None:
            self.func()

    def restore_style(self):
        self.setStyleSheet(self.default_style)

    def on_button_enter(self, event):
        self.shadow_animation.setDirection(QPropertyAnimation.Forward)
        self.setStyleSheet(self.hover_style)
        self.shadow_animation2.setDirection(QPropertyAnimation.Forward)

        self.shadow_animation.start()
        self.shadow_animation2.start()

        event.accept()

    def on_button_leave(self, event):
        self.shadow_animation.setDirection(QPropertyAnimation.Backward)
        self.shadow_animation2.setDirection(QPropertyAnimation.Backward)

        self.shadow_animation.start()
        self.shadow_animation2.start()
        self.setStyleSheet(self.default_style)
        event.accept()
