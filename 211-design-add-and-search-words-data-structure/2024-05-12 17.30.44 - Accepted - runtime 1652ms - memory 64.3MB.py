#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#


# @lc code=start
class trieNode:
    def __init__(self) -> None:
        self.isEnd = False
        self.map = {}

    def insert(self, c):
        if c not in self.map:
            self.map[c] = trieNode()
        return self.map[c]


class WordDictionary:

    def __init__(self):
        self.root = trieNode()

    def addWord(self, word: str) -> None:
        currNode = self.root
        i = 0
        while i < len(word):
            c = word[i]
            currNode = currNode.insert(c)
            i += 1
            if i == len(word):
                currNode.isEnd = True

    def search(self, word: str) -> bool:
        def search(word, i, node):
            currNode = node
            index = i
            while index < len(word):
                c = word[index]
                if c == ".":
                    for key in currNode.map.keys():
                        if search(word, index + 1, currNode.map[key]):
                            return True
                    return False
                if c not in currNode.map:
                    return False
                currNode = currNode.map[c]
                index += 1
            return currNode.isEnd
        return search(word,0,self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)