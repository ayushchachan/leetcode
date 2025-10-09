import java.util.HashSet;

class Solution {
   public int countPrimes(int n) {
        if (n <= 2) return 0;
        int primeCount = 0;

        boolean[] notPrime = new boolean[n - 1];

        for (int i = 2; i < n; i++) {
            if (!notPrime[i - 1]) {
                primeCount++;
                int j = 2;
                int z;
                while ((z = i*j) < n) {

                    notPrime[z - 1] = true;
                    j++;

                }
            }

        }


        return primeCount;
    }



}