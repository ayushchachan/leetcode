class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set()
        for num in nums:
            if num not in d:
                d.add(num)

        memo = {}

        def count(num):
            if num in memo:
                return memo[num]
            if num + 1 in d:
                memo[num] = count(num + 1) + 1
            else:
                memo[num] = 1
            return memo[num]

        maxCount = 0

        for num in nums:
            maxCount = max(maxCount, count(num))
        
        return maxCount

