class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        result = (-1, -1)
        maxLen = 0
        n = len(s)
        palindrome = [[-1 for i in range(n)] for i in range(n)]
        # print(palindrome)
        for i in range(n):
            palindrome[i][i] = 1
        # print(palindrome)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] != s[j]:
                    palindrome[i][j] = -1
                else:
                    if j == i + 1:
                        palindrome[i][j] = 2
                    elif palindrome[i + 1][j - 1] == -1:
                        palindrome[i][j] = -1
                    else:
                        palindrome[i][j] = palindrome[i + 1][j - 1] + 2
                if palindrome[i][j] > maxLen:
                    maxLen = palindrome[i][j]
                    result = (i, j)


        # print(palindrome)
        if result[0] != -1:
            i, j = result
            return s[i:j + 1]
        else:
            return s[0]



        
