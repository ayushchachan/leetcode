class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;

        int rev = 0;
        int temp = x;

        while (temp != 0) {
            rev = rev * 10 + (temp % 10);
            // System.out.println("rev = " + rev);
            temp = temp / 10;
            // System.out.println("temp = " + temp);

        }
        return rev == x;
        
    }
}