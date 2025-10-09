#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#


# @lc code=start
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if k == 0:
            return
        k = k % N
        temp = []
        for i in range(N - k, N):
            temp.append(nums[i])

        j = N - 1
        for i in range(N - k - 1, -1, -1):
            nums[j] = nums[i]
            j -= 1

        for j in range(k):
            nums[j] = temp[j]


# @lc code=end
