class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int result = 0;

        int i = 0;

        while (i < nums.length) {
            if (nums[i] == 1) {
                int j = i + 1;
                int count = 1;

                while (j < nums.length && nums[j] == 1) {
                    count++;
                    j++;
                }
                if (count > result) result = count;
                i = j;

            }
            i++;
        }
        return result;
        
    }
}