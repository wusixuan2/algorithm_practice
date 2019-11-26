class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.is_word = True

    """
    return the node in the trie if exists
    """
    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        node = self.find(word)
        return node is not None and node.is_word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        return self.find(prefix) is not None

class TrieService:

    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        # Return root of trie root, and
        # lintcode will print the tree struct.
        return self.root

    # @param {str} word a string
    # @param {int} frequency an integer
    # @return nothing
    def insert(self, word, frequency):
        node = self.root
        for letter in word:
            child = node.children.get(letter, None)

            if child is None:
                child = TrieNode()

            node.children[letter] = child
            self.add_frequency(child.top10, frequency)

            node = child

    def add_frequency(self, top10, frequency):
        top10.append(frequency)
        index = len(top10) - 1
        while index > 0:
            if top10[index] > top10[index - 1]:
                top10[index], top10[index - 1] = top10[index - 1], top10[index]
                index -= 1
            else:
                break
        if len(top10) > 10:
            top10.pop()

class Solution:

    '''
    @param root: An object of TrieNode, denote the root of the trie.
    This method will be invoked first, you should design your own algorithm
    to serialize a trie which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        if root is None:
            return ""

        data = ""
        for key, value in root.children.items():
            data += key + self.serialize(value)

        return "<%s>" % data


    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    '''
    def deserialize(self, data):
        if data is None or len(data) == 0:
            return None

        root = TrieNode()
        current = root
        path =[]
        for c in data:
            if c == '<':
                path.append(current)
            elif c == '>':
                path.pop()
            else:
                current = TrieNode()
                if len(path) == 0:
                    print c, path
                path[-1].children[c] = current

        return root

class Typeahead:

    # @param dict: A dictionary of words dict
    def __init__(self, dict):
        # do initialize if necessary
        self.mp = {}
        for s in dict:
            l = len(s)
            for i in xrange(l):
                for j in xrange(i + 1, l + 1):
                    tmp = s[i:j]
                    if tmp not in self.mp:
                        self.mp[tmp] = [s]
                    elif self.mp[tmp][-1] != s:
                        self.mp[tmp].append(s)

    # @param word: a string
    # @return a list of words
    def search(self, word):
        if word not in self.mp:
            return []
        else:
            return self.mp[word]
