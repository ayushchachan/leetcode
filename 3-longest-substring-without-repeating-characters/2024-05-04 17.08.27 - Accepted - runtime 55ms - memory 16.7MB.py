class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0;j = 0
        d = {}
        maxLength = 0
        for j in range(len(s)):
            if(s[j] not in d):
                d[s[j]] = j
            else:
                index = d[s[j]]
                while(i <= index):
                    del d[s[i]]
                    i += 1
                d[s[j]] = j
            maxLength = max(maxLength,j - i + 1)
        return maxLength 



        