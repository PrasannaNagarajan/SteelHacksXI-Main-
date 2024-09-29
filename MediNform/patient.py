#ChatGPT used for enhancment of this file to increase efficiency
#and give a more desireable output

import time
import threading
import speech_to_trie as sst
import gemini_access as gem
import file_parsing as fp
import speech_recognition as sr
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QTextEdit, QWidget, QListWidget
from PyQt6.QtCore import QSize

class AudioProcessor(threading.Thread):
    def __init__(self, update_function):
        super().__init__()
        self.update_function = update_function
        self.running = True
        self.audio = None

    def run(self):
        while self.running:
            if self.audio is not None:
                self.process_audio(self.audio)
                self.audio = None  # Clear the audio after processing

    def process_audio(self, audio):
        try:
            recognizer = sr.Recognizer()
            output = recognizer.recognize_google(audio)

            # Splitting array of the output into individual words
            output_arr = output.split(" ")
            out = ""

            for txt in output_arr:
                txt = search_rec.clean_word(txt)

                # Processing trie search
                if search_rec.trie.search_prefix(search_rec.working_string + txt):
                    search_rec.working_string += txt
                elif search_rec.trie.search_key(search_rec.working_string):
                    out = search_rec.gemini.prompt_gemini(search_rec.working_string)
                    search_rec.working_string = ""
                else:
                    search_rec.working_string = ""

            # Updating window
            if out:
                self.update_function(out)

        except sr.UnknownValueError:
            print("Could not understand audio.")
            time.sleep(1)
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    def set_audio(self, audio):
        self.audio = audio

    def stop(self):
        self.running = False

class PatientWindow(QMainWindow):
    def __init__(self, age):
        super().__init__()
        global search_rec

        # Setting up search in trie
        search_rec = sst.SearchSpeech(age)
        
        #setting list
        self.terms_list = []

        # Setting window information
        self.setWindowTitle("User Device")
        self.setFixedSize(QSize(720, 500))

        # Creating central widget
        central_widget = QWidget()
        layout = QHBoxLayout(central_widget)
        
        # setting font
        font1 = QFont("Neue Helvetica", 14)
        font2 = QFont("Neue Helvetica", 16)
        font2.setBold(True)
        
        # Text display
        self.text_edit = QTextEdit(self)
        self.text_edit.setFont(font1)
        self.text_edit.setReadOnly(True)
        self.text_edit.setMinimumSize(500, 340)
        layout.addWidget(self.text_edit)
        
        # List widget
        self.list_widget = QListWidget()
        self.list_widget.setFont(font2)
        layout.addWidget(self.list_widget)

        # Set the central widget
        self.setCentralWidget(central_widget)

        self.audio_processor = AudioProcessor(self.add_to_list)
        self.audio_processor.start()  # Start the audio processing thread

        # Build gemini instance
        search_rec.gemini = gem.Gemini(age)

        # Initialize microphone
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

        # Adjust for ambient noise
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

        #looking for item list click
        self.list_widget.itemClicked.connect(self.on_item_click)
        
        # Start listening in background
        self.r.listen_in_background(self.m, self.callback_function) #phrase_time_limit = 3)
        
        print("Begin speaking")

    def on_item_click(self, item):
        index = self.list_widget.row(item)
        self.text_edit.setText(self.terms_list[index])
    
    def callback_function(self, recognizer, audio):
        self.audio_processor.set_audio(audio)  # Pass the audio to the processing thread

    def add_to_list(self, value):    
        if value != None:
            #parsing the info
            term_info = fp.parse_input(value)
            print(value)
            
            try:
                #adding formatted string to list of info
                if term_info[0] == "Disease" or term_info[0] == "Injury":
                    to_add = "\t\t" + term_info[1] + "\n\nSymptoms:\n\n"
                    
                    for sym in term_info[2].split(":"):
                        to_add += "➼" + sym + "\n\n"
                    
                    to_add += "\n\nCauses:\n\n"
                    for cs in term_info[3].split(":"):
                        to_add += "➼" + cs + "\n\n"
                        
                    to_add +="\nTreatments:\n\n"
                    for trt in term_info[4].split(":"):
                        to_add += "➼" + trt + "\n\n"
                        
                    self.terms_list.append(to_add)
                elif term_info[0] == "Operation":
                    to_add = "\t\t" + term_info[1] + "\n\nPre-op:\n\n" + term_info[2] + "\n\nOperation:\n\n" + term_info[3] + "\n\nPost-op:\n\n" + term_info[4] + "\n\nRecovery Time: " + term_info[5]
                    self.terms_list.append(to_add)
                elif term_info[0] == "Treatment":
                    to_add = "\t\t" + term_info[1] + "\n\nTreatment Information:\n\n" + term_info[2] + "\n\nTreatment Duration:\n\n" + term_info[3]
                    self.terms_list.append(to_add)
                elif term_info[0] == "Drug":
                    to_add = "Generic Name:\n" + term_info[1] + "\n\nTrade Name:\n" + term_info[2] + "\n\nUses:\n\n" + term_info[3]
                    to_add += "\n\nSide Effects:\n\n"
                    
                    for se in term_info[4].split(":"):
                        to_add += "➼" + trt + "\n\n"
                    
                    self.terms_list.append(to_add)
                elif term_info[0] == "Anatomical Term":
                    to_add = "\t\t" + term_info[1] + "\n\nLocation on Body:\n\n" + term_info[2] + "\n\nUse:\n\n" + term_info[3]
                    self.terms_list.append(to_add)
                
                #adding to the list of items
                self.list_widget.addItem(term_info[1])
            except:
                #gemini output error
                print("Gemini made an oopsie")

    def closeEvent(self, event):
        self.audio_processor.stop()  # Stop the audio processing thread
        event.accept()
