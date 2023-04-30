class TrieNode:

    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        if word is None:
            return None
        curr = self.root

        for char in word:
            # if not exist, create a node
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            # if exists, move to that node
            curr = curr.children[char]

        curr.endOfWord = True

        return None

    def search(self, word: str) -> bool:
        if word is None:
            return False

        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        # if exists, check it is denoted as end of word
        return curr.endOfWord

    def startsWith(self, word: str) -> bool:
        if word is None:
            return False

        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True
