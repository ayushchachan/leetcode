#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#


# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)

        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                j = mid
            else:
                i = mid + 1
        return i


# @lc code=end
