#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#


# @lc code=start
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        reachable = 0
        i = 0
        while i < len(nums) and reachable < len(nums) - 1:
            if reachable < i:
                return False
            reachable = max(reachable, i + nums[i])
            i += 1

        if reachable >= len(nums) - 1:
            return True
        return False


# nums = [3, 2, 1, 0, 4]
# S = Solution()
# S.canJump(nums)
# @lc code=end
