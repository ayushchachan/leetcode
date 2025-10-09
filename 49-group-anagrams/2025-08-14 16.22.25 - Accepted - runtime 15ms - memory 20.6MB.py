class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = dict()
        
        for s in strs:
            s1 = "".join(sorted(s))
            
            if s1 in groups:
                groups[s1].append(s)
            else:
                groups[s1] = [s]
        
        return list(groups.values())
                
                
            
# def isAnagram(S1, S2):
#     alphaCount = [0] * 26
    
#     if (len(S1) != len(S2)):
#         return False
    
#     for i in range(len(S1)):
#         alphaCount[ord(S1[i]) - ord('a')] += 1
#         alphaCount[ord(S2[i]) - ord('a')] -= 1
    
#     for n in alphaCount:
#         if n is not 0:
#             return False
#     return True
                    
        