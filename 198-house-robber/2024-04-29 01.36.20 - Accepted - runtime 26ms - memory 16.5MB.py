class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.robService(nums,0,{})

    def robService(self, nums, i, memo={}):
        if i >= len(nums):
            return 0
        if i in memo:
            return memo[i]
        res = max(
            self.robService(nums, i + 1, memo),
            nums[i] + self.robService(nums, i + 2, memo),
        )
        memo[i] = res
        return res

