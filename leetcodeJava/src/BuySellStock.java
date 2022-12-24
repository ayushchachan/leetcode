public class BuySellStock {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] prices = {1, 2, 3, 0, 2};
        System.out.println(s.maxProfit(prices));

    }

}

class Solution {
    public int maxProfit(int[] prices) {
        boolean isBought = false;       // is there any stock to sell
        int profit = 0;
        int i = 0;

        int lastBought = -1;
        int N = prices.length;

        while (i < N) {
            if (isBought) {
                int j = i + 1;
                if (j == N || prices[j] < prices[i]) {
                    profit += prices[i] - prices[lastBought];
                    isBought = false;
                    i++;        // cooldown
                }
                i++;
                continue;

            } else {
                int j = i + 1;
                if (j == N || prices[j] <= prices[i]) {
                    i++;
                    continue;
                }
                isBought = true;
                lastBought = i;
            }
            i++;
        }
        return profit;
    }
}
