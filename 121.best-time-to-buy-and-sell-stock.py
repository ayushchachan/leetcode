#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # first find min value index
        high_i = len(prices) - 1  ## index for higher value
        low_i = 0  ## index for lower value
        max_profit = max(prices[high_i] - prices[low_i], 0)

        for j in range(len(prices) - 2, -1, -1):
            if prices[j] > prices[high_i]:
                high_i = j
                if prices[high_i] - prices[low_i] > max_profit:
                    max_profit = prices[high_i] - prices[low_i]

            else:
                if (prices[high_i] - prices[j]) > max_profit:
                    max_profit = prices[high_i] - prices[j]

        return max_profit


# prices = [7, 1, 5, 3, 6, 4]
# S = Solution()
# print(S.maxProfit(prices))
# @lc code=end
