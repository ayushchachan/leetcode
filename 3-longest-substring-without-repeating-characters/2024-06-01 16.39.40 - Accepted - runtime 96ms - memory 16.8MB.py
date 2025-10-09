class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0;j = 0
        d = set()
        minL = 0
        while(j < len(s)):
            c = s[j]
            if(c not in d):
                d.add(c)
                if(j >= len(s)):
                    return minL
            else:
                while(s[i] != s[j] and i < j):
                    print(i,j,d)
                    d.remove(s[i])
                    i += 1
                    if(i >= len(s)):
                        return minL
                i += 1
                if(i >= len(s)):
                    return minL
            
            minL = max(minL,j - i + 1)
            j += 1
        return minL


        