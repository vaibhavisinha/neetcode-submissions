class TreeNode:
    def __init__(self):
        self.characters = dict()
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not curr.characters.get(c,False):
                curr.characters[c] = TreeNode()
            curr = curr.characters[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if not curr.characters.get(c, False):
                return False
            curr = curr.characters.get(c)
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            idx = ord(c)-ord('a')
            if not curr.characters.get(c, False):
                return False
            curr = curr.characters.get(c)
        return True