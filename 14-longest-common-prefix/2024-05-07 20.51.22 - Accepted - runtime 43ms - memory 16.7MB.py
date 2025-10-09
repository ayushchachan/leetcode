class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        p = ""
        while True:
            c = None
            for string in strs:
                if(i >= len(string)):
                    return p
                if c == None:
                    c = string[i]
                else:
                    if c != string[i]:
                        return p
            p += c
            i += 1
                    
            
        

