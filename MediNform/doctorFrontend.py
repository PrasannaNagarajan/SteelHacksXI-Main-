import sys

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
        self.name_input = QLineEdit()
        self.name_input.setFixedWidth(200)
        self.name_input.setStyleSheet("QLineEdit { border: 2px solid #000000; padding: 5px; }")
        #patient age text box
        self.age_lable = self.age_label = QLabel("Patient Age")
        self.age_input = QLineEdit()
        self.age_input.setFixedWidth(50)
        self.age_input.setStyleSheet("QLineEdit { border: 2px solid #000000; padding: 5px; }")
        #align patient info in horizontal box
        self.patient_info.addWidget(self.name_label)
        self.patient_info.addWidget(self.name_input)
        self.patient_info.addWidget(self.age_label)
        self.patient_info.addWidget(self.age_input)

        #Doc's notes box
        self.notes = QHBoxLayout()

        self.notes_label = QLabel("Patient Notes")
        self.notes_input = QTextEdit()
        self.notes_input.setFixedWidth(400)
        self.notes_input.setFixedHeight(150)
        self.notes_input.setStyleSheet("QTextEdit { border: 2px solid #000000}")

        self.notes.addWidget(self.notes_label)
        self.notes.addWidget(self.notes_input)
        #add patient info to main window
        self.main_layout.addLayout(self.patient_info)
        self.main_layout.addLayout(self.notes)


        #self.notes_box(layout)
        self.setLayout(self.main_layout)


    def notes_box(self,layout):

        self.text_box = QLineEdit()
        layout.addWidget(self.text_box)

    def start_recording(self,layout):
        button = QPushButton("Start Recording")
        layout.addWidget(button)

    def stop_recording(self):
        button = QPushButton("Stop Recording")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
'''class doctorFrontend:
    x = st.slider("select a value")
    st.write(x, "squared is", x*x)'''