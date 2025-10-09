class Solution {
    public boolean check(int[] nums) {

        int x = -1;

        // first find x
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                x = i;
                break;
            }

        }
        System.out.println("x = " + x);
        if (x != -1) {
            for (int i = x + 1; i < x + nums.length; i++) {
                System.out.println("i = " + i);
                if (nums[i % nums.length] > nums[(i + 1) % nums.length]) {
                return false;
            }

            }

        }
        return true;
        
    }
}