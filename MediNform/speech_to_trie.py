import speech_recognition as sr
import re
import trie as t
from google.generativeai.types import HarmCategory, HarmBlockThreshold


# initialization function
def __init__(self):
    #getting microphone
    self.r = sr.Recognizer()
    self.m = sr.Microphone()
    self.stop_listening = self.r.listen_in_background(m, callback, phrase_time_limit = 2)
    self.working_string = ""


# listening for input
def callback(recognizer, audio):
    # received audio data
    try:
        # recognize data using Google Speech Recognition, storing in string
        output = recognizer.recognize_google(audio)
        
        #splitting text into array
        output_arr = output.split(" ")

        #searching in trie
        for txt in output_arr:
            #removing special characters
            txt = clean_word(txt)

            #checking if txt is prefix
            if t.search_prefix(txt):
                working_string += txt
                
            #checking if txt is word
            elif t.search_prefix(txt):
                #call function through gemini
                print("Is a word!")
                working_string = ""

            #neither
            else:
                working_string = ""

    except sr.UnknownValueError:
        text = ""
    except sr.RequestError as e:
        text = ""

#cleanup function
def cleanup():
    stop_listening(wait_for_stop=False)

def clean_word(word):
    cleaned_word = re.sub(r'[^a-zA-Z\s]', '', line)
    cleaned_word = cleaned_word.lower()
    
    # Remove spaces to concatenate words
    concatenated_word = ''.join(cleaned_word.split())