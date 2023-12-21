from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit


class QLineEditX(QLineEdit):
    enterPressed = Signal()
    def __init__(self, text, parent=None, geometry = None):
        super().__init__(parent=parent)

        self.returnPressed.connect(self.handle_enter_pressed)
    def handle_enter_pressed(self):
        # Funcția care va fi apelată atunci când este apăsat Enter
        self.enterPressed.emit()
        text = self.text()
        print(f"Enter apăsat! Text introdus: {text}")