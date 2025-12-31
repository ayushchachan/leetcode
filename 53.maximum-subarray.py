#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        prefixSum = nums[0]
        minVal = nums[0]
        n = len(nums)
        for i in range(1, n):
            prefixSum += nums[i]

            if prefixSum - minVal > maxSum:
                maxSum = prefixSum - minVal
            maxSum = max(maxSum, prefixSum)
            minVal = min(minVal, prefixSum)
        return maxSum


S = Solution()
nums = [1, 1, -2]
print(S.maxSubArray(nums))
# @lc code=end
