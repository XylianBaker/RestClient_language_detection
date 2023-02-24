from PyQt6.QtCore import Qt, QStringListModel
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt6.QtWidgets import *
from PyQt6 import uic
from src.controller.controller import Controller


class View(QMainWindow):
    input: QTextEdit
    output: QTextBrowser

    def __init__(self, controller: Controller):
        super().__init__()
        uic.loadUi("../../data/gui.ui", self)
        self.button_check.clicked.connect(controller.execute)
        self.button_reset.clicked.connect(controller.reset)
        self.output.setReadOnly(True)

    def reset(self):
        self.input.setText("")
        self.output.setText("")

    def set_text_statusbar(self, text: str):
        self.statusbar.showMessage(text)

    def set_text_output(self, text: str):
        self.output.setText(text)

    def get_text_input(self):
        return self.input.toPlainText()


if __name__ == '__main__':
    app = QApplication([])
    view = View()
    view.show()
    app.exec()
