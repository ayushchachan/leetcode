class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)

        j = n - 1

        for i in range(n - 1, -1, -1):
            ## if we can reach j from i
            if nums[i] > 0 and (i + nums[i] >= j):
                j = i
        
        return j == 0