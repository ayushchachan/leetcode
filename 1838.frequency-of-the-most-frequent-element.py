#
# @lc app=leetcode id=1838 lang=python3
#
# [1838] Frequency of the Most Frequent Element
#

from collections import Counter


# @lc code=start
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        freq = Counter(nums)

        nums.sort()
        highest_val = nums[-1]

        ## now we have highest_value and freq table
        for j in range(len(nums) - 2, -1, -1):
            y = nums[j]
            while y in freq and k >= (highest_val - y):
                freq[y] = freq[y] - 1
                if freq[y] == 0:
                    freq.pop(y)
                freq[highest_val] += 1
                k = k - highest_val + y

            if y not in freq:
                continue

        return freq[highest_val]


k = 7925
nums = [
    9930,
    9923,
    9983,
    9997,
    9934,
    9952,
    9945,
    9914,
    9985,
    9982,
    9970,
    9932,
    9985,
    9902,
    9975,
    9990,
    9922,
    9990,
    9994,
    9937,
    9996,
    9964,
    9943,
    9963,
    9911,
    9925,
    9935,
    9945,
    9933,
    9916,
    9930,
    9938,
    10000,
    9916,
    9911,
    9959,
    9957,
    9907,
    9913,
    9916,
    9993,
    9930,
    9975,
    9924,
    9988,
    9923,
    9910,
    9925,
    9977,
    9981,
    9927,
    9930,
    9927,
    9925,
    9923,
    9904,
    9928,
    9928,
    9986,
    9903,
    9985,
    9954,
    9938,
    9911,
    9952,
    9974,
    9926,
    9920,
    9972,
    9983,
    9973,
    9917,
    9995,
    9973,
    9977,
    9947,
    9936,
    9975,
    9954,
    9932,
    9964,
    9972,
    9935,
    9946,
    9966,
]


S = Solution()
print(S.maxFrequency(nums, k))

# @lc code=end
