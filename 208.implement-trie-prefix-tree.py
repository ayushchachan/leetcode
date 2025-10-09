#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#


# @lc code=start
class Trie:

    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        return None

    def search(self, word: str) -> bool:
        return True

    def startsWith(self, prefix: str) -> bool:
        return True


class TrieNode:
    def __init__(self, c):
        self.children = []
        for i in range(26):
            self.children.append(None)

        self.value = c
        self.isEnd = False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
