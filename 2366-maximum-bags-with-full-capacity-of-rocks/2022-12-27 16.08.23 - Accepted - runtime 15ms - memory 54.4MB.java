class Solution {
    

    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        int[] availability = new int[capacity.length];

        for (int i = 0; i < capacity.length; i++) {
            availability[i] = capacity[i] - rocks[i];
        }

        Arrays.sort(availability);

        int j = 0;
        int count = 0;

        while (additionalRocks > 0 && j < availability.length) {
            if (availability[j] == 0) {
                count++;
                j++;
                continue;
            }
            if (additionalRocks >= availability[j]) {
                additionalRocks -= availability[j];
                count++;
                j++;
            } else {
                break;
            }

        }

        return count;
    }


}