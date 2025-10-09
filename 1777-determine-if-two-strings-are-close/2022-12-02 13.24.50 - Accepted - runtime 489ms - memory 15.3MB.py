class Solution:
    def closeStrings(self, word1, word2):
        n1 = len(word1)
        n2 = len(word2)

        if n1 != n2:
            return False
        
        w1 = [0 for j in range(26)]
        w2 = [0 for j in range(26)]
        
        for i in range(n1):
            w1[ord('a') - ord(word1[i])] += 1
            w2[ord('a') - ord(word2[i])] += 1
        
        for j in range(26):
            if w1[j] == 0 and w2[j] != 0:
                return False

        freq1 = {}
        freq2 = {}
        
        return sorted(w1) == sorted(w2)
        
        
        
            