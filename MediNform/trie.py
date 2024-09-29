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
            
        if curr.wordend == True:
            curr.wordend = False
            return True
        
        return False
    
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