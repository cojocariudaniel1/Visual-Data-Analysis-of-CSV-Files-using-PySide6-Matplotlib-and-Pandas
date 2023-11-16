import logging

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from PySide6.QtCore import Qt

from design.style1.QTLabel_center import QLabelCenter


class TableHeader:
    columns = []  # List of dict columns with name and width.
    columns_widget = ()

    def __init__(self, max_width, data: list, parent=None):
        self.max_width = max_width  # Set max width of the header (Max width is from parent tabel max width)
        self.calculate_column_width(data)  # Calculate width for column
        self.parent = parent
        self.create_column_widget()

    def set_column_width(self, width, column_name=None, column_id=None, ):
        if column_name:
            for dict_element in self.columns:
                if dict_element["name"] == column_name:
                    dict_element["width"] = width

    def calculate_column_width(self, data):
        base_spacing = 20
        for column in data:
            word_lenght = len(column)
            width = base_spacing * 2 + word_lenght * 10
            self.columns.append({"name": column, "width": width})

    def create_column_widget(self):
        try:
            label = None
            for idx, element in enumerate(self.columns):
                print(element["name"])
                label = QLabel("test", self.parent)
                self.columns_widget.append(label)

        except Exception as e:
            logging.exception(e)



class CustomTableWidget(QFrame):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.colums_data = ["Produse", "Pret", "Depozit"]

        self.setObjectName("QLabelTabel")
        # Setarea colțurilor rotunjite și culoare de contur
        self.setStyleSheet("#QLabelTabel {border: 1px solid gray; border-radius: 10px; background-color: white; "
                           "color: black;}")
        self.k = TableHeader(300,["ID", "Product", "Price"], self)

