#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxAmount = [0 for _ in range(len(nums))]
        maxAmount[-1] = nums[-1]
        maxAmount[-2] = max(nums[-1], nums[-2])
        for i in range(len(nums) - 3, -1, -1):
            maxAmount[i] = max(nums[i] + maxAmount[i + 2], maxAmount[i + 1])
        return maxAmount[0]


# @lc code=end
