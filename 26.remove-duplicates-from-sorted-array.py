#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 0
        val = nums[0]
        i = 0
        N = len(nums)

        while (i < N):
            while (i < N and nums[i] == val):
                i += 1
            nums[index] = val
            index += 1
            if (i < N):
                val = nums[i]
        return index

# @lc code=end

