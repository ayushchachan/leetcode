class TrieNode:
    def __init__(self, key) -> None:
        self.map = {}
        self.key = key
        self.isEnd = False

    def insert(self, c):
        if c not in self.map:
            self.map[c] = TrieNode(c)
        return self.map[c]


class Trie:

    def __init__(self):
        self.root = TrieNode("R")

    def insert(self, word: str) -> None:
        i = 0
        currNode = self.root
        while i < len(word):
            ch = word[i]
            currNode = currNode.insert(ch)
            i += 1
            if i == len(word):
                currNode.isEnd = True
        return currNode

    def search(self, word: str) -> bool:
        currNode = self.root
        i = 0
        while i < len(word):
            ch = word[i]
            if ch not in currNode.map:
                return False
            currNode = currNode.map[ch]
            i += 1
            if i == len(word):
                return currNode.isEnd
        return False

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        i = 0
        while i < len(prefix):
            ch = prefix[i]
            if ch not in currNode.map:
                return False
            currNode = currNode.map[ch]
            i += 1
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)