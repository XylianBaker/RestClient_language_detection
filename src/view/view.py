from PyQt6.QtCore import Qt, QStringListModel
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt6.QtWidgets import *
from PyQt6 import uic
from src.controller.controller import Controller


class View(QMainWindow):
    """
    The View component of the GUI, responsible for displaying the GUI elements and handling user input.

    Attributes:
    -----------
    input : QTextEdit
        The input text box where the user can input text to be analyzed.
    output : QTextBrowser
        The output text box where the results of the analysis are displayed.

    Methods:
    --------
    __init__(self, controller: Controller):
        Initializes the View component of the GUI, loading the GUI elements from the UI file and connecting the buttons to the controller.
    reset(self):
        Resets the input and output text boxes.
    set_text_statusbar(self, text: str):
        Sets the text of the status bar.
    set_text_output(self, text: str):
        Sets the text of the output text box.
    get_text_input(self):
        Gets the text of the input text box.
    """

    input: QTextEdit
    output: QTextBrowser

    def __init__(self, controller: Controller):
        """
        Initializes the View component of the GUI, loading the GUI elements from the UI file and connecting the buttons to the controller.

        Parameters:
        -----------
        controller : Controller
            The Controller component of the GUI.
        """
        super().__init__()
        uic.loadUi("../../data/gui.ui", self)  # Load the GUI elements from the UI file
        self.button_check.clicked.connect(
            controller.execute)  # Connect the "Check" button to the controller's execute method
        self.button_reset.clicked.connect(
            controller.reset)  # Connect the "Reset" button to the controller's reset method
        self.output.setReadOnly(True)  # Make the output text box read-only

    def reset(self):
        """
        Resets the input and output text boxes.
        """
        self.input.setText("")  # Clear the input text box
        self.output.setText("")  # Clear the output text box

    def set_text_statusbar(self, text: str):
        """
        Sets the text of the status bar.

        Parameters:
        -----------
        text : str
            The text to set the status bar to.
        """
        self.statusbar.showMessage(text)  # Set the text of the status bar

    def set_text_output(self, text: str):
        """
        Sets the text of the output text box.

        Parameters:
        -----------
        text : str
            The text to set the output text box to.
        """
        self.output.setText(text)  # Set the text of the output text box

    def get_text_input(self):
        """
        Gets the text of the input text box.

        Returns:
        --------
        str
            The text in the input text box.
        """
        return self.input.toPlainText()  # Get the text in the input text box


if __name__ == '__main__':
    app = QApplication([])
    view = View()
    view.show()
    app.exec()
