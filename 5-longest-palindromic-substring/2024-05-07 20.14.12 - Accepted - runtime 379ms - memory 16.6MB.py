def checkpalindrome(text, i, j):
    while i > -1 and j < len(text):
        if text[i] != text[j]:
            return (i,j)
        i -= 1
        j += 1

    return (i, j)


def LPS(text):
    maxLength = 0
    pStr = ""
    for i in range(len(text)):
        ## Case - 1
        res = checkpalindrome(text, i - 1, i + 1)
        if res[1] - res[0] - 1 > maxLength:
            maxLength = res[1] - res[0] - 1
            pStr = res

        ## Case - 2
        res = checkpalindrome(text, i, i + 1)
        if res[1] - res[0] - 1 > maxLength:
            maxLength = res[1] - res[0] - 1
            pStr = res

        ## Case - 3
        res = checkpalindrome(text, i - 1, i)
        if res[1] - res[0] - 1 > maxLength:
            maxLength = res[1] - res[0] - 1
            pStr = res

    return text[pStr[0] + 1:pStr[1]]



class Solution:
    def longestPalindrome(self, s: str) -> str:
        return LPS(s)
        