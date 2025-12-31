#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # ways = dict()
        # ways[1] = 1
        # ways[2] = 2
        # for i in range(3, n + 1):
        #     ways[i] = ways[i - 1] + ways[i - 2]
        # return ways[n]

        ## 2nd solution
        if n == 1:
            return 1
        x = 1
        y = 2
        for i in range(3, n + 1):
            y, x = x + y, y
        return y


# @lc code=end
