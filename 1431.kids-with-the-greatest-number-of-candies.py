#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> List[bool]:
        largest = max(candies)
        result = []
        for c in candies:
            if c + extraCandies >= largest:
                result.append(True)
            else:
                result.append(False)
        return result
# @lc code=end

