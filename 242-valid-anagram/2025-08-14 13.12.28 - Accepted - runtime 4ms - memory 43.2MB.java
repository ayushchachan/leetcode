class Solution {
    public boolean isAnagram(String s, String t) {
        int[] freq1 = new int[26];
        int[] freq2 = new int[26];

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            freq1[c - 'a'] += 1;
        }

        for (int j = 0; j < t.length(); j++) {
            char c = t.charAt(j);
            freq2[c - 'a'] += 1;
        }

        for (int k = 0; k < 26; k++) {
            if (freq1[k] != freq2[k]) {
                return false;
            }
            
        }
        return true;

    }
}