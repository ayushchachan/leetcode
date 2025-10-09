class Solution:
    def maxProfit(self, prices):
        A = prices;
        n = len(A)
        lastBought = None;
        
        profit = 0;
        i = 0;
        while (i < n - 1):
            
            if (lastBought is None):
                if (A[i + 1] > A[i]):
                    lastBought = i;
                i = i + 1
            else:
                if A[i + 1] >= A[i]:
                    i = i + 1;
                else:
                    profit += (A[i] - A[lastBought]);
                    lastBought = None;
                    i = i + 1;
        
        if (lastBought is not None):
            profit += (A[i] - A[lastBought]);
        return profit;