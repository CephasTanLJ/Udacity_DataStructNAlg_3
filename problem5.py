class TrieNode:
    def __init__(self, value):
        '''
        value       - Parent character
        children    - A dictionary of Nodes that are children to this node instant
        us_word     - Boolean type indicating if this Node.value is the last char of a word.
        :param value:
        '''
        self.value = str(value)
        self.children = dict()
        self.is_word = False

    def insert(self, char):
        '''Insert Child node'''
        if char in self.children:
            return
        else:
            self.children[char] = TrieNode(char)


    def suffixes(self, suffix = ''):
        '''
        Return a list of suffixes given the current node as the prefix node.
        Suffixes traverse down the trie recursively, Each character is added to the suffix during the traversal,
        suffix are only added to the suffix_list if the TrieNodes are tagged as True for is_word attribute.
        '''
        suffix_list = list()

        if self.is_word:
            suffix_list.append(suffix)
        for child_char, child_node in self.children.items():
            suffix += child_char
            suffix_list.extend(child_node.suffixes(suffix))
        return suffix_list


    def __repr__(self):
        '''Node(parent, child(ren))'''
        return f'Node({self.value}, {list(self.children.keys())}, {self.is_word})'

class Trie:
    def __init__(self):
        self.root = TrieNode('root')

    def insert(self, word):
        node_tracer = self.root
        for char in str(word):
            if char not in node_tracer.children:
                node_tracer.children[char] = TrieNode(char)
                node_tracer = node_tracer.children[char]
            else:
                node_tracer = node_tracer.children[char]

        node_tracer.is_word = True

    def find(self, prefix):
        '''Given a prefix, return the last char node of the prefix'''
        node_tracer = self.root
        for char in str(prefix):
            if char in node_tracer.children:
                node_tracer = node_tracer.children[char]
            else:
                return None
        return node_tracer



MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)




print(MyTrie.find('ant').suffixes())
print(MyTrie.find('tri').suffixes())
print(MyTrie.find('tri').suffixes())


