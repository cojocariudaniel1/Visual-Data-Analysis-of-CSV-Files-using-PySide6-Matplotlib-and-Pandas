from PySide6 import QtWidgets as qt, QtGui, QtWidgets, QtCore
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt, QTimer
from PySide6.QtWidgets import QGraphicsDropShadowEffect

from design.style1.QLabelAnimation import QLabelAnimation

string_default_style = "{border: 1px solid gray; border-radius: 10px; background-color: rgba(255,255, 255, 0); color: black;}"
string_clicked_style = "{border: 1px solid #c634eb; border-radius: 10px; background-color: rgba(255,255, 255, 0); color: black;}"
string_hover_style = "{border: 1px solid brown; border-radius: 10px; background-color: rgba(255,255, 255, 0); color: black;}"


class RadioButtonClassic(qt.QRadioButton):
    def __init__(self, text, objectname: str, background, obj, parent=None, geometry=None, ):
        super().__init__(parent)

        # Basic settings
        self.setText(text)
        self.setObjectName(objectname)
        if geometry:
            self.setGeometry(geometry)

        self.setFont(QtGui.QFont("Helvetica", 13))

        self.background = background
        # Setting Shadow Animation
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(5)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(5)
        self.shadow.setXOffset(2)
        self.shadow.setYOffset(2)
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

        self.background_objectName = self.background.objectName()
        self.background.setObjectName(self.background_objectName)

        self.default_style = f"#{self.background_objectName} {string_default_style}"
        self.clicked_style = f"#{self.background_objectName} {string_clicked_style}"
        self.hover_style = f"#{self.background_objectName} {string_hover_style}"
        self.background.setStyleSheet(self.default_style)
        self.enterEvent = self.on_button_enter
        self.leaveEvent = self.on_button_leave

        self.bg_obj = obj
        ##

    def on_button_enter(self, event):
        if not self.isChecked():
            self.shadow_animation.setDirection(QPropertyAnimation.Forward)
            self.shadow_animation2.setDirection(QPropertyAnimation.Forward)
            self.background.setStyleSheet(self.hover_style)
            self.shadow_animation.start()
            self.shadow_animation2.start()


        event.accept()

    def on_button_leave(self, event):
        if not self.isChecked():
            self.shadow_animation.setDirection(QPropertyAnimation.Backward)
            self.shadow_animation2.setDirection(QPropertyAnimation.Backward)
            self.background.setStyleSheet(self.default_style)
            self.shadow_animation.start()
            self.shadow_animation2.start()

        event.accept()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.isChecked():
                self.background.setStyleSheet(self.clicked_style)
                self.setChecked(False)
            else:
                self.background.setStyleSheet(self.default_style)
                self.setChecked(True)
            self.background.setStyleSheet(self.clicked_style)
            QTimer.singleShot(350, self.restore_style)
            for i in self.bg_obj:
                if i.objectName() != self.background.objectName():
                    self.d = f"#{i.objectName()}{string_default_style}"
                    i.setStyleSheet(self.d)
    def restore_style(self):
        self.setStyleSheet(self.default_style)
