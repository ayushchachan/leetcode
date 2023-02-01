public class Duplicates {
    public static void main(String[] args) {
        int[] nums = {0,0,1,1,1,2,2,3,3,4};
        Duplicates S = new Duplicates();
        System.out.println(S.removeDuplicates(nums));
    }

    public int removeDuplicates(int[] nums) {
        int i = 1;
        int j = 2;
        int largest = nums[nums.length - 1];
        while (j < nums.length) {
            if (nums[i] == largest) return i + 1;
            if (nums[i] == nums[i - 1]) {
                while (j < nums.length && nums[j] == nums[i]) {
                    j++;
                }
                nums[i] = nums[j];
                while (j < nums.length && nums[j] == nums[i]) {
                    j++;
                }
            }
            i++;

        }
        return i;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
