class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = set()
        for n in nums:
            if n in S:
                S.remove(n)
            else:
                S.add(n)
        return S.pop()
        
