from PyQt6.QtWidgets import QApplication

from src.view import view
from src.model import model


class Controller:
    def __init__(self):
        self.view = view.View(self)
        self.view.show()
        self.view.set_text_statusbar("Ready")

    def execute(self):
        self.view.set_text_statusbar("Checking...")
        text = self.view.get_text_input()
        # only execute if there is text in the input field (otherwise the webservice will crash)
        if text:
            result = model.language_detection(text)
            self.view.set_text_output(result)
            self.view.set_text_statusbar("Ready")
        else:
            self.view.set_text_statusbar("No text to check.")

    def reset(self):
        self.view.set_text_statusbar("Resetting...")
        self.view.reset()
        self.view.set_text_statusbar("Ready")


if __name__ == '__main__':
    app = QApplication([])
    controller = Controller()
    app.exec()
