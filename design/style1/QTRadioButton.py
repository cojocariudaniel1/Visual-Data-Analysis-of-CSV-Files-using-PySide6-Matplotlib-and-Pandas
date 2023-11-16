from PySide6 import QtWidgets as qt, QtGui, QtWidgets, QtCore
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt, QTimer
from PySide6.QtWidgets import QGraphicsDropShadowEffect

string_default_style = "{border: 1px solid gray; border-radius: 10px; background-color: white; ""color: black;}"
string_clicked_style = "{border: 2px solid #c634eb; border-radius: 10px; background-color: ""white; color: black;}"
string_hover_style = "{border: 1px solid #95a1d6; border-radius: 10px; background-color: ""white; color: black;}"
class RadioButton(qt.QRadioButton):
    def __init__(self, text, objectname: str, parent=None, ):
        super().__init__(parent)

        # Basic settings
        self.setText(text)
        self.setObjectName(objectname)

        self.default_style = f"#{self.objectName()} {string_default_style}"
        self.clicked_style = f"#{self.objectName()} {string_clicked_style}"
        self.hover_style = f"#{self.objectName()} {string_hover_style}"

        self.setStyleSheet(self.default_style)
        self.setFont(QtGui.QFont("Helvetica", 13))

        # Setting Shadow Animation
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
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

    def on_button_enter(self, event):
        self.shadow_animation.setDirection(QPropertyAnimation.Forward)

        self.shadow_animation2.setDirection(QPropertyAnimation.Forward)
        self.setStyleSheet(self.hover_style)
        self.shadow_animation.start()
        self.shadow_animation2.start()

        event.accept()

    def on_button_leave(self, event):
        self.shadow_animation.setDirection(QPropertyAnimation.Backward)
        self.shadow_animation2.setDirection(QPropertyAnimation.Backward)
        self.setStyleSheet(self.default_style)
        self.shadow_animation.start()
        self.shadow_animation2.start()

        event.accept()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.isChecked():
                self.setStyleSheet(self.clicked_style)
                self.setChecked(False)
            else:
                self.setStyleSheet(self.default_style)
                self.setChecked(True)
            self.setStyleSheet(self.clicked_style)
            QTimer.singleShot(350, self.restore_style)

    def restore_style(self):
        self.setStyleSheet(self.default_style)

