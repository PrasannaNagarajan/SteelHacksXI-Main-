import speech_recognition as sr
import gemini_access as gem
import re
import trie as t


class SearchSpeech:
    # initialization function
    def __init__(self, age):
        #building trie
        input_file = "medical_wordlist.txt"
        self.trie = t.Trie()

        file = open(input_file, encoding="utf8")    
    
        while True:
            line = file.readline()

            if line == "":
                break

            word = t.clean_and_concatenate_words(line)
            self.trie.add(word)
        
        #building gemini
        self.gemini = gem.Gemini(age)
        
        #getting microphone
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        
        #adjusting for ambient noise
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
            
        #starting listening
        self.stop_listening = self.r.listen_in_background(self.m, self.callback, phrase_time_limit = 2)
        self.working_string = ""
        
        #setup complete
        print("Begin Speaking")
    
    # cleaning word function
    def clean_word(self,word):
        cleaned_word = re.sub(r'[^a-zA-Z\s]', '', word)
        cleaned_word = cleaned_word.lower()

        # Remove spaces to concatenate words
        concatenated_word = ''.join(cleaned_word.split())
        return concatenated_word
    
    # listening for input
    def callback(self, recognizer, audio):
        # received audio data
        try:
            # recognize data using Google Speech Recognition, storing in string
            output = recognizer.recognize_google(audio)

            #splitting text into array
            output_arr = output.split(" ")

            #searching in trie
            for txt in output_arr:
                #removing special characters
                txt = self.clean_word(txt)
            
                #checking if txt is prefix
                if self.trie.search_prefix(self.working_string+txt):
                    self.working_string += txt

                #checking if txt is word
                elif self.trie.search_key(self.working_string):
                    #call function through gemini
                    print(self.gemini.prompt_gemini(self.working_string))
                    self.working_string = ""

                #neither
                else:
                    self.working_string = ""

        except sr.UnknownValueError:
            if self.trie.search_key(self.working_string):
                    #call function through gemini
                    print(self.gemini.prompt_gemini(self.working_string))
                    self.working_string = ""
            text = ""
        except sr.RequestError as e:
            text = ""

    
    #cleanup function
    def cleanup(self):
        self.stop_listening(wait_for_stop=False)