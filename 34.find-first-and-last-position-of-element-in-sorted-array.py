#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        start_i = -1
        end_i = -1

        i = 0
        j = len(nums)
        ## finding start index
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                start_i = mid
                j = mid
            elif target < nums[mid]:
                j = mid
            else:
                i = mid + 1

        i = 0
        j = len(nums)
        ## finding start index
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                end_i = mid
                i = mid + 1
            elif target < nums[mid]:
                j = mid
            else:
                i = mid + 1

        return [start_i, end_i]


# @lc code=end
