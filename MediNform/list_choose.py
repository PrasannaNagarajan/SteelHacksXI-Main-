import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QComboBox, QSpacerItem, QSizePolicy, \
    QVBoxLayout, QPushButton, QTextEdit
from PyQt6.QtCore import QThread, pyqtSignal
import speech_to_trie as stt

class Worker(QThread):
    output_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
    
    def run(self):
        #iterating over generator
        for output in speech_rec.get_ret_val():
            print(output)
            self.output_signal.emit(output)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #setting up speech to trie
        global  speech_rec
        speech_rec = stt.SearchSpeech(19)

        # Set up the layout for the main page
        self.layout = QHBoxLayout()  # Change to QHBoxLayout for horizontal alignment
        self.setFixedSize(QSize(720,360))
        self.setWindowTitle("Medical Terms")

        # Set up the layout
        self.layout = QVBoxLayout()
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)  # Make text edit read-only

        self.layout.addWidget(self.text_edit)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        
        #automatically starting background process
        self.start_process()
        
    #starts the bacground process
    def start_process(self):
        self.text_edit.clear()
        self.worker = Worker()
        self.worker.output_signal.connect(self.update_text_edit)
        self.worker.start()
        
    def update_text_edit(self, output):
        self.text_edit.append(output)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


