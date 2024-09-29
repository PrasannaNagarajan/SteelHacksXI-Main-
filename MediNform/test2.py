#ChatGPT used for enhancment of this file to increase efficiency
#and give a more desireable output

import sys
import threading
import speech_to_trie as sst
import gemini_access as gem
import speech_recognition as sr
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QWidget, QListWidget
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
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    def set_audio(self, audio):
        self.audio = audio

    def stop(self):
        self.running = False

class MainWindow(QMainWindow):
    def __init__(self, age):
        super().__init__()
        global search_rec

        # Setting up search in trie
        search_rec = sst.SearchSpeech(age)

        # Setting window information
        self.setWindowTitle("Medical Terminology")
        self.setFixedSize(QSize(720, 360))

        # Creating central widget
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # List widget
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)
        
        # 

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

        # Start listening in background
        self.r.listen_in_background(self.m, self.callback_function, phrase_time_limit = 2)

    def callback_function(self, recognizer, audio):
        self.audio_processor.set_audio(audio)  # Pass the audio to the processing thread

    def add_to_list(self, value):
        if value:
            self.list_widget.addItem(value)

    def closeEvent(self, event):
        self.audio_processor.stop()  # Stop the audio processing thread
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(19)
    window.show()
    sys.exit(app.exec())
