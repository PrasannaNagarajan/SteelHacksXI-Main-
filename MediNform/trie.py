class Trie:
    #initialize trie function
    def __init__(self, file_name):
        self.root = None

    #add function
    def add(self, word):
        #root is null
        if self.root == None:
            self.root = word[0]
            self.root = add_rec(word, self.root.down, 1)

    #add recursive funtion    
    def add_rec(self, word, cur_node, index):
        #end of key,
        if(index >= word.len()):
            cur_node.down = Node('^')
            return cur_node
        


    

    #private node class
    class Node:
        #initialize node function
        def __init__(self, letter):
            self.letter = letter
            self.down = None
            self.right = None
