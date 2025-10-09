class Solution {
    public int searchInsert(int[] nums, int target) {
        int p = 0;
        int r = nums.length;

        while (p < r) {
            int q = (p + r)/2;

            if (nums[q] == target) return q;
            else if (target < nums[q]) {
                r = q;
            } else {
                p = q + 1;
            }
        }
        return p;


    }
}