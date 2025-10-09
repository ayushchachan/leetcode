class Solution:
    def reverseWords(self, s: str) -> str:
        wordlist = s.split(" ")
        for i in range(len(wordlist)):
            wordlist[i] = wordlist[i][-1 :: -1]
        return " ".join(wordlist)
        