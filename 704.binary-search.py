#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#


# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i = 0
        j = len(nums)

        while i < j:
            mid = (i + j) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                j = mid
            else:
                i = mid + 1
        return -1


# @lc code=end
