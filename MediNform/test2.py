import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

def load_phrases_from_file(filename):
    """Load phrases from a given file and return them as a list."""
    try:
        with open(filename, 'r') as file:
            phrases = [line.strip() for line in file.readlines() if line.strip()]  # Read lines and strip whitespace
        return phrases
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return []

class MedicalTermsApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Terms Detector")
        self.layout = QVBoxLayout()

        # Load medical terms and speech text
        medical_terms = load_phrases_from_file('medical-wordlist-main/medical_wordlist.txt')  # List of medical terms
        speech_text = self.load_speech_text('hunter-test-file/test-speech-to-text-file.txt')  # Load speech text

        # Find common phrases
        common_phrases = self.find_common_phrases(medical_terms, speech_text)
        if common_phrases:
            print("Medical terms detected:", ', '.join(common_phrases))
        else:
            print("No medical terms detected.")

        # Create label for displaying results
        self.label = QLabel("Detected Medical Terms:")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def load_speech_text(self, filename):
        """Load speech text from a file."""
        try:
            with open(filename, 'r') as file:
                return file.read()  # Read entire file content as a single string
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            return ""
        except Exception as e:
            print(f"Error reading file '{filename}': {e}")
            return ""

    def find_common_phrases(self, medical_terms, speech_text):
        """Find and return medical terms that exist in the speech text."""
        common_phrases = [term for term in medical_terms if term.lower() in speech_text.lower()]
        return common_phrases

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MedicalTermsApp()
    window.show()
    sys.exit(app.exec())