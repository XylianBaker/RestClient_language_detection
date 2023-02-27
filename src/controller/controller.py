from PyQt6.QtWidgets import QApplication

from src.view import view
from src.model import model


class Controller:
    def __init__(self):
        """
        Initializes an instance of the Controller class, which controls the behavior of a GUI for language detection.
        It creates a View instance, shows the GUI, and sets the status bar message to "Ready".
        """
        self.view = view.View(self)
        self.view.show()
        self.view.set_text_statusbar("Ready")

    def execute(self):
        """
        Executes language detection when the "Check" button is clicked in the GUI.
        It gets the text input from the View instance, and calls the language_detection function of the model to
        perform language detection.
        It then sets the output text in the View instance, and sets the status bar message to "Ready".
        """
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
        """
        Resets the GUI when the "Reset" button is clicked.
        It calls the reset function of the View instance to clear the input and output fields of the GUI,
        and sets the status bar message to "Ready".
        """
        self.view.set_text_statusbar("Resetting...")
        self.view.reset()
        self.view.set_text_statusbar("Ready")


if __name__ == '__main__':
    app = QApplication([])
    controller = Controller()
    app.exec()
