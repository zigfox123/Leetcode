

class Solution {
    public int numberOfSubstrings(String s) {
        int ans = 0;
        int left = 0;
        Map<Character, Integer> count= new HashMap<>();
        count.put('a',0);
        count.put('b',0);
        count.put('c',0);

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            count.put(c, count.get(c) + 1);

            while (count.get('a') > 0 && count.get('b') > 0 && count.get('c') > 0) {
                ans += s.length() - right;
                char leftChar = s.charAt(left);
                count.put(leftChar, count.get(leftChar) - 1);
                left++;
            }
        }
        return ans;


    }
}
//Solution accepted runs in O(n) time using a sliding window approach.