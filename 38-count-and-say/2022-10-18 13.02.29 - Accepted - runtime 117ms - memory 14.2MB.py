class Solution:
    def countAndSay(self, n: int) -> str:
        found = {1: '1'}
        for i in range(2, n + 1):
            found[i] = self.say(found[i - 1])
        return found[n]
        
    def say(self, s):
        i = 0
        result = []
        while i < len(s):
            char_i = s[i]
            j = i + 1
            while j < len(s) and s[j] == char_i:
                j += 1
            result.append(str(j - i))
            result.append(char_i)
            i = j
        return ''.join(result)
        
        