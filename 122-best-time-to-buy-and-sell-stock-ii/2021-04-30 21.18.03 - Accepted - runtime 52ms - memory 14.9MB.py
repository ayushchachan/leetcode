class Solution:
    def maxProfit(self, prices):
        profit = 0
        count = 0
        buy = prices[0]
        for i in range(len(prices)-1):            
                if buy <= prices[i + 1]:
                    profit += prices[i + 1] - buy
                    buy = prices[i + 1]
                elif buy > prices[i + 1]:
                    buy = prices[i + 1]
        return profit