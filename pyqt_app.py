import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLineEdit

from main import main


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Layout setup
        self.layout = QVBoxLayout()

        # Create a text input field
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Enter some text here")

        # Create a button to select a directory
        self.select_dir_button = QPushButton("Select Directory")
        self.select_dir_button.clicked.connect(self.select_directory)

        # Create a label to show the selected directory
        self.selected_dir_label = QLabel("No directory selected")

        # Create a label to show the convertion status
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

        self.setLayout(self.layout)

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

        # Display the convertion status
        self.convertion_status.setVisible(True)

        # Clear input box
        self.text_input.clear()


if __name__ == '__main__':
    # Create an application object
    app = QApplication(sys.argv)

    # Create a window
    window = MainWindow()
    window.setWindowTitle('Download PDF from Google Drive and Merge It')

    # Show the window
    window.show()

    # Execute the application's event loop
    sys.exit(app.exec())
