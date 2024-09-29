import re

class TrieNode:
    # Initialize TrieNode
    def __init__(self):
        self.child = [None] * 26  
        self.wordend = False  

class Trie:
    def __init__(self):
        self.root = TrieNode()  
        
    # Add a word to the Trie
    def add(self, key):
        curr = self.root

        for c in key:
            
            if 'a' <= c <= 'z':  
                index = ord(c) - ord('a')  # Map character to index (0-25)

                if curr.child[index] is None:
                    curr.child[index] = TrieNode()  # Create a new node if necessary

                curr = curr.child[index]

        curr.wordend = True

    # Search for a word in the Trie
    def search_key(self, key):
        curr = self.root

        for c in key:
            index = ord(c) - ord('a')
            if curr.child[index] is None:
                return False  

            curr = curr.child[index]

        return curr.wordend 
    
    def search_prefix(self, prefix):
        curr = self.root

    # Traverse through each character in the prefix
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.child[index] is None:  # If the child doesn't exist, the prefix is not present
                return False
            curr = curr.child[index]  # Move to the next child node
    
    
        return True

def clean_and_concatenate_words(line):
    # Remove special characters (except spaces) and convert to lowercase
    cleaned_line = re.sub(r'[^a-zA-Z\s]', '', line)
    cleaned_line = cleaned_line.lower()
    
    # Remove spaces to concatenate words
    concatenated_word = ''.join(cleaned_line.split())
    
    return concatenated_word


def process_input_file(input_file):
 
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Clean and concatenate each line
    cleaned_words = [clean_and_concatenate_words(line) for line in lines]
    
    return cleaned_words


input_file = "medical_wordlist.txt"
trie = Trie()

# Get the list of cleaned and concatenated words
cleaned_words = process_input_file(input_file)


for word in cleaned_words:
    trie.add(word)


word_to_search = "prostate".lower()  # Ensure word is lowercase
is_prefix = trie.search_prefix(word_to_search)
print(is_prefix)
# is_found = trie.search_key(word_to_search)
# print(f"Word '{word_to_search}' found in Trie:", is_found)