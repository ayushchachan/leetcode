#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i = i - 1
            else:
                nums1[i + j + 1] = nums2[j]
                j = j - 1
        
        while i >= 0:
            nums1[i + j + 1] = nums1[i]
            i = i - 1
        
        while j >= 0:
            nums1[i + j + 1] = nums2[j]
            j = j - 1
# @lc code=end

