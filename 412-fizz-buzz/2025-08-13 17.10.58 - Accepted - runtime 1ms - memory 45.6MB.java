class Solution {
    public List<String> fizzBuzz(int n) {

        ArrayList<String> answer = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int j = i + 1;
            if (j % 15 == 0) {
                answer.add("FizzBuzz");
            } else if (j % 3 == 0) {
                answer.add("Fizz");
            } else if (j % 5 == 0) {
                answer.add("Buzz");

            } else {
                answer.add("" + j);
            }
        }
        return answer;

    }
}