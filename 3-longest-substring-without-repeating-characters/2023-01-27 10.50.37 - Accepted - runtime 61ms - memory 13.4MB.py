class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = dict()
        max_len = 0
        i = 0
        j = 0
        while i < len(s):
            if s[i] not in substring:
                substring[s[i]] = [i]
                i += 1
                continue
            max_len = max(max_len, len(substring))
            ## s[i] in substring
            while s[i] in substring and j < i:
                substring.pop(s[j])
                j += 1
        max_len = max(max_len, len(substring))
        return max_len



        
