import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QComboBox, QSpacerItem, QSizePolicy, \
    QVBoxLayout, QPushButton

class ComboBoxExample(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout for the main page
        self.layout = QHBoxLayout()  # Change to QHBoxLayout for horizontal alignment

        # Create a label
        self.label = QLabel("Select an option:")
        self.layout.addWidget(self.label)

        # Create a spacer to push the combo box to the right
        self.layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        # Create a combo box
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Select an option", "Option 1", "Option 2", "Option 3", "Option 4"])
        self.combo_box.currentIndexChanged.connect(self.on_combobox_changed)
        self.layout.addWidget(self.combo_box)

        # Set the layout for the main window
        self.setLayout(self.layout)

        # Set the window title
        self.setWindowTitle("Combo Box Example")
        self.showFullScreen()  # Full screen

    def on_combobox_changed(self, index):
        if index > 0:  # Skip the first option (default)
            self.navigate_to_new_page(index)

    def navigate_to_new_page(self, index):
        # Create and show the new page
        self.new_page = NewPage(index)
        self.new_page.show()
        self.close()  # Close the current window


class NewPage(QWidget):
    def __init__(self, option_index):
        super().__init__()

        # Set up the layout for the new page
        self.layout = QVBoxLayout()

        # Create a label to display the selected option
        self.label = QLabel(f"You selected Option {option_index}!")
        self.layout.addWidget(self.label)

        # Create a button to go back to the main page
        self.back_button = QPushButton("Back to Main Page")
        self.back_button.clicked.connect(self.go_back)
        self.layout.addWidget(self.back_button)

        # Set the layout for the new page
        self.setLayout(self.layout)

        # Set the window title
        self.setWindowTitle("New Page")

    def go_back(self):
        # Go back to the main page
        self.main_page = ComboBoxExample()
        self.main_page.show()
        self.close()  # Close the current window


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ComboBoxExample()
    window.show()
    sys.exit(app.exec())


