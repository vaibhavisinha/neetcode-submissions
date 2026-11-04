class TreeNode:
    def __init__(self):
        self.characters = dict() #[None]*26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            # print(curr.characters)
            if not curr.characters.get(c,False):
                curr.characters[c] = TreeNode()
            # idx = ord(c)-ord('a')
            # if curr.children[idx] is None:
            #     curr.children[idx] = TreeNode()
            curr = curr.characters[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            idx = ord(c)-ord('a')
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
        # curr = self.root
        # for c in prefix:
        #     idx = ord(c)-ord('a')
        #     if curr.children is None:
        #         return False
        #     curr = curr.children[idx]
        # return True
        