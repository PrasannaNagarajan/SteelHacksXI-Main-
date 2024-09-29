import sys
from list_choose import *

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QLabel, QLineEdit,\
    QVBoxLayout, QWidget, QHBoxLayout, QTextEdit


#also can import from QTWidgets, QtGui, and QtCore

#create instance of application that allows for command line args - needed

#create instance of widget
#window = QWidget()
#window = QPushButton("Push me")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Initialize Recording")
        self.setFixedSize(QSize(720,360))
        #main group for all widgets
        self.window =  QWidget(self)
        self.setCentralWidget(self.window)
        self.main_layout = QVBoxLayout(self.window)

        #horizontal box to align patient info next to one another
        self.patient_info = QHBoxLayout()

        #patient name text box
        self.name_label = QLabel("Patient Name") #QlineEdit short, qtextedit long - notes(can be exported to txt)
        #self.name_label.setContentsMargins(60,0,0,0)
        self.name_input = QLineEdit()
        self.name_input.setFixedWidth(200)
        self.name_input.setStyleSheet("QLineEdit { border: 2px solid #000000; padding: 5px; }")
        #self.name_input.setContentsMargins(0,0,0,0)

        #patient age text box
        self.age_label = QLabel("Patient Age")
        #self.age_label.setStyleSheet("QLineEdit{margin-left: 500px; }") #not shifting how we want
        self.age_label.setContentsMargins(0,0,0,0)
        self.age_input = QLineEdit()
        self.age_input.setFixedWidth(50)
        self.age_input.setStyleSheet("QLineEdit { border: 2px solid #000000; padding: 5px; }")
        #self.age_input.setContentsMargins(0,0,0,0)

        #align patient info in horizontal box
        self.patient_info.addWidget(self.name_label)
        self.patient_info.addWidget(self.name_input)
        self.patient_info.addWidget(self.age_label)
        self.patient_info.addWidget(self.age_input)
        #self.patient_info.setContentsMargins(20,0,20,0)

        #Doc's notes box
        self.notes = QHBoxLayout()

        self.notes_label = QLabel("Patient Notes")
        self.notes_input = QTextEdit()
        self.notes_input.setFixedWidth(480)
        self.notes_input.setFixedHeight(150)
        self.notes_input.setStyleSheet("QTextEdit { border: 2px solid #000000}")

        self.notes.addWidget(self.notes_label)
        self.notes.addWidget(self.notes_input)

        #stop and start recording button structures
        self.buttons = QHBoxLayout()
        self.start_button = QPushButton("Start Recording Transcript ▶")
        self.start_button.setFixedHeight(30)
        self.start_button.setFixedWidth(300)
        self.start_button.clicked.connect(self.start_clicked)
        self.stop_button = QPushButton("Stop Recording Transcript ■")
        self.stop_button.setFixedHeight(30)
        self.stop_button.setFixedWidth(300)
        self.stop_button.clicked.connect(self.stop_clicked)


        self.buttons.addWidget(self.start_button)
        self.buttons.addWidget(self.stop_button)


        #add widgets info to main window
        self.main_layout.addLayout(self.patient_info)
        self.main_layout.addLayout(self.notes)
        self.main_layout.addLayout(self.buttons)

        #initialize main window
        self.setLayout(self.main_layout)

    def start_clicked(self):
        #button = QPushButton("Start Recording")
        #layout.addWidget(button)
        if self.age_input.text() != "":
            age_value = self.age_input.text()
            print("Patient's age is " + age_value)
            print("recording...")
            self.patient_window = ComboBoxExample()
            self.patient_window.show()
        else:
            print("Input patient age")

    def stop_clicked(self):
        #button = QPushButton("Stop Recording")
        print("stopped recording...")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())