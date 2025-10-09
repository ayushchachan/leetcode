class Solution {
    

    public int rob(int[] nums) {

        if (nums.length == 1) {
            return nums[0];
        } else if (nums.length == 2) {
            return Math.max(nums[0], nums[1]);
        }

        int n = nums.length;

        int[][] robbery = new int[n][n];

        for (int i = 0; i < nums.length; i++) {
            robbery[i][0] = nums[i];
            
            robbery[i][1] = Math.max(nums[i], nums[(i + 1) % n]);
            
        }

        for (int i = 0; i < nums.length; i++) {
            for (int j = 2; j < nums.length - 1; j++) {
                robbery[i][j] = Math.max(robbery[i][j - 2] + nums[(i + j) % n], robbery[i][j - 1]);
            }

        }

        int maxVal = robbery[0][n - 2];

        for (int i = 1; i < nums.length; i++) {
            if (robbery[i][n - 2] > maxVal) {
                maxVal = robbery[i][n - 2];
            }
            
        }

        return maxVal;
    }



}