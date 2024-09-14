import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout


if __name__ == '__main__':
    # Create an application object
    app = QApplication(sys.argv)

    # Create a window (widget)
    window = QWidget()
    window.setWindowTitle('PyQt6 App on macOS')

    # Create a vertical layout
    layout = QVBoxLayout()

    # Add a label widget
    label = QLabel('Hello, PyQt6!')
    layout.addWidget(label)

    # Set the layout for the main window
    window.setLayout(layout)

    # Show the window
    window.show()

    # Execute the application's event loop
    sys.exit(app.exec())
