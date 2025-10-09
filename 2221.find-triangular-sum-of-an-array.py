#
# @lc app=leetcode id=2221 lang=python3
#
# [2221] Find Triangular Sum of an Array
#

import math
# @lc code=start
class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        N = len(nums)
        if (N == 1):
            return nums[0]
        answer = 0
        for i in range(N):
            answer = answer + (math.comb(N - 1, i) * nums[i]) % 10
        return answer % 10
        
# @lc code=end

