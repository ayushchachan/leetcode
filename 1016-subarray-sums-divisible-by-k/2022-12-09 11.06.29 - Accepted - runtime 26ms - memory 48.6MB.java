
class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int n = nums.length;
        int divisibleByK = 0;

        int[] remCount = new int[k];    // remainder count map

        int[] mod = new int[n];
        mod[0] = Math.floorMod(nums[0], k);
        if (mod[0] == 0) divisibleByK++;

        remCount[mod[0]] = 1;

        for (int i = 1; i < n; i++) {
            int newRem = Math.floorMod(mod[i - 1] + nums[i], k);
            if (newRem == 0) divisibleByK++;

            remCount[newRem] += 1;
            mod[i] = newRem;

        }

        System.out.println("mod[] = " + Arrays.toString(mod));
        System.out.println("remCount[] = " + Arrays.toString(remCount));

        // divisibleByK += remCount[0];

        for (int i = 0; i < k; i++) {
            divisibleByK += remCount[i]*(remCount[i] - 1)/2;
        }


        return divisibleByK;

    }
}