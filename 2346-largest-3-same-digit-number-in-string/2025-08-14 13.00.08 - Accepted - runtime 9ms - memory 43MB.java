class Solution {
    public String largestGoodInteger(String num) {
        String answer = "";
        char highestVal = 0;

        for (int i = 0; i < num.length() - 3 + 1; i++) {
            char a = num.charAt(i);
            char b = num.charAt(i + 1);
            if (a != b) continue;
            char c = num.charAt(i + 2);

            if (b == c) {
                if (a >= highestVal) {
                    highestVal = a;
                    answer = "" + a + b + c;
                }
            }
        }
        return answer;

    }
}