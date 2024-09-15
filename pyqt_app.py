import sys

from PyQt6.QtCore import QSharedMemory
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QPushButton,
                             QFileDialog, QLineEdit, QMainWindow)

from main import main


class SingleInstance:
    def __init__(self, key):
        self.shared_memory = QSharedMemory(key)
        if not self.shared_memory.create(1):  # Try to create the shared memory
            sys.exit('Another instance is already running.')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a central widget and set the layout for the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)

        # Create a text input field
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Enter some text here")

        # Create a button to select a directory
        self.select_dir_button = QPushButton("Select Directory")
        self.select_dir_button.clicked.connect(self.select_directory)

        # Create a label to show the selected directory
        self.selected_dir_label = QLabel("No directory selected")

        # Create a label to show the conversion status
        self.convertion_status = QLabel("PDF has been converted")
        self.convertion_status.setVisible(False)

        # Create a button to submit the data
        self.submit_button = QPushButton("Convert")
        self.submit_button.clicked.connect(self.submit_data)

        # Add widgets to layout
        self.layout.addWidget(self.text_input)
        self.layout.addWidget(self.select_dir_button)
        self.layout.addWidget(self.selected_dir_label)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.convertion_status)

        # Variable to store selected directory
        self.selected_directory = ""

    def select_directory(self):
        # Open a directory selection dialog
        dir = QFileDialog.getExistingDirectory(self, "Select Directory")

        if dir:
            self.selected_directory = dir
            self.selected_dir_label.setText(f"Selected Directory: {dir}")

    def submit_data(self):
        # Get text from the input box
        input_text = self.text_input.text()

        # Call the function to handle the data
        self.handle_data(self.selected_directory, input_text)

    def handle_data(self, directory, text):
        main(text, directory)

        # Display the conversion status
        self.convertion_status.setVisible(True)

        # Clear input box
        self.text_input.clear()


if __name__ == '__main__':
    # Create an application object
    app = QApplication(sys.argv)

    # Create a SingleInstance object with a unique key
    single_instance = SingleInstance("my_unique_app_key_pyqt6")

    # Create a window
    window = MainWindow()
    window.setWindowTitle('Download PDF from Google Drive and Merge It')
    window.show()

    # Execute the application's event loop
    sys.exit(app.exec())
