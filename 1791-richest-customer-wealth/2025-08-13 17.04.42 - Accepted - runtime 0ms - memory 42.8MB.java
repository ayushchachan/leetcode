class Solution {
    public int maximumWealth(int[][] accounts) {
        int m = accounts.length;
        int n = accounts[0].length;
        int maxWealth = 0;

        for (int i = 0; i < m; i++) {
            int wealthi = 0;
            for (int j = 0; j < n; j++) {
                wealthi += accounts[i][j];
            }

            if (wealthi > maxWealth) {
                maxWealth = wealthi;
            }
        }
        return maxWealth;

    }
}