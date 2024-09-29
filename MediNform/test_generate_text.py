import re
import random
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QListWidget
from PyQt6.QtCore import Qt
from doctor_frontend import MainWindow
import sys

from Gemini_Access import Gemini

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.setFixedSize(720, 360) #fixed size
        self.layout = QVBoxLayout() #wrap words
        self.setLayout(self.layout)

        # Create a QLabel for the text
        self.text_label = QLabel("")
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignLeft)  # Align text to the left
        self.text_label.setStyleSheet("font-size: 16px;")  # Set font size
        self.layout.addWidget(self.text_label)

        # Create a button to regenerate the text TESTING ONLY DO NOT IMPLEMENT IN FINAL CODE
        self.regenerate_button = QPushButton("Regenerate")
        self.regenerate_button.clicked.connect(self.regenerate_text)  # Connect button click to method
        self.layout.addWidget(self.regenerate_button)

        # Keep track of looked-up words
        self.word_list_widget = QListWidget()
        self.word_list_widget.itemClicked.connect(self.display_word_info)  # Connect item click to method
        self.layout.addWidget(self.word_list_widget)

        # Dictionary to store the information about medical terms
        self.medical_info = {}

        # Initial text generation
        self.regenerate_text()

    # FOR TESTING PURPOSES ONLY
    def regenerate_text(self):
        response_text, med_term = self.test_prompt_gemini()
        self.text_label.setText(response_text)  # Update the QLabel with new text

        # Add the medical term to the list if it's not already there
        if med_term and med_term not in [self.word_list_widget.item(i).text() for i in range(self.word_list_widget.count())]:
            self.word_list_widget.addItem(med_term)
            self.medical_info[med_term] = response_text  # Store the information for the term

    def test_prompt_gemini(self):
        age = MainWindow(age_value)
        gemini_instance = Gemini(age)

        # Read medical terms from the text file
        file_path = 'medical_wordlist.txt'  # Change to your file path
        try:
            with open(file_path, 'r') as file:
                med_terms = file.read().splitlines()  # Read lines into a list

            if med_terms:
                # RANDOMIZE MEDICAL TERM
                med_term = random.choice(med_terms)
                response_text = gemini_instance.prompt_gemini(med_term)
                labeled_response_text = self.label_text(response_text)
                return labeled_response_text, med_term
            else:
                return "The medical terms file is empty.", None
        except Exception as e:
            return f"Error reading medical terms file: {e}", None

    def label_text(self, text):
        # Mapping to help label
        tag_mapping = {
            '<T>': 'Type: ',
            '<NM>': 'Name: ',
            '<SY>': 'Symptoms list: ',
            '<CS>': 'Causes list: ',
            '<TR>': 'Treatments: ',
            '<PRE>': 'Pre Op information: ',
            '<OP>': 'Operation information: ',
            '<POS>': 'Post Op information: ',
            '<RT>': 'Recovery time: ',
            '<TRI>': 'Treatment information: ',
            '<TRD>': 'Treatment Duration: ',
            '<GNM>': 'Generic Drug Name: ',
            '<TNM>': 'Trade Drug Name: ',
            '<US>': 'Drug uses: ',
            '<SDE>': 'Drug side effects: ',
            '<BP>': 'Part of body: ',
            '<UBP>': 'Use of body part: ',
        }

        # Replace each opening tag with its corresponding label
        for tag, label in tag_mapping.items():
            text = text.replace(tag, label)

        # Add newlines for closing tags and remove them
        for tag in tag_mapping.keys():
            closing_tag = f"</{tag[1:]}"  # Create the closing tag
            text = text.replace(closing_tag, '\n')  # Replace closing tag with a newline

        # Clean up any self-closing tags
        text = re.sub(r'</[^>]*>', '', text)

        return text

    def display_word_info(self, item):
        # Display info
        selected_word = item.text()
        if selected_word in self.medical_info:
            self.text_label.setText(self.medical_info[selected_word]) #Set label that allows you to RETURN to that word
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
