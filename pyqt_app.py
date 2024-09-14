import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QFileDialog


# Define a function to open the directory selection dialog
def select_directory():
    # Open a dialog to select a directory
    directory = QFileDialog.getExistingDirectory(window, 'Select Directory')
    if directory:
        label.setText(f'Selected Directory: {directory}')
    else:
        label.setText('No directory selected.')


if __name__ == '__main__':
    # Create an application object
    app = QApplication(sys.argv)

    # Create a window (widget)
    window = QWidget()
    window.setWindowTitle('Download PDF from Google Drive and Merge It')

    # Create a vertical layout
    layout = QVBoxLayout()

    # Add a label to display the selected path
    label = QLabel('Please select an output directory...')
    layout.addWidget(label)

    # Add a button to open the selection dialog
    button = QPushButton('Select Directory')
    button.clicked.connect(select_directory)  # Connect the button to the directory selection function
    layout.addWidget(button)

    # Set the layout for the main window
    window.setLayout(layout)

    # Show the window
    window.show()

    # Execute the application's event loop
    sys.exit(app.exec())
