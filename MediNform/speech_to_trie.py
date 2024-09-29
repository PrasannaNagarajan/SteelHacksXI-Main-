import speech_recognition as sr
import gemini_access as gem
import re
import trie as t


class SearchSpeech:
    # initialization function
    def __init__(self, age):
        self.ret_val = ""
        self.working_string = ""
        
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
        
        self.gemini = None
        
        #setup complete
        print("Begin Speaking")
    
    # cleaning word function
    def clean_word(self,word):
        cleaned_word = re.sub(r'[^a-zA-Z\s]', '', word)
        cleaned_word = cleaned_word.lower()

        # Remove spaces to concatenate words
        concatenated_word = ''.join(cleaned_word.split())
        return concatenated_word
    
    #cleanup function
    def cleanup(self):
        self.stop_listening(wait_for_stop=False)
        