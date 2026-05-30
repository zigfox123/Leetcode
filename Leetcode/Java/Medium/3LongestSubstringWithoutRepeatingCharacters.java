class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) return 0;

        int current_start_pos = 0;
        int current_end_pos = 1;
        int longest_substring = 1;

        while (current_end_pos < s.length()) {

            for (int i = current_start_pos; i < current_end_pos; i++) {

                if (s.charAt(i) == s.charAt(current_end_pos)) {

                    int length_of_substring =
                        current_end_pos - current_start_pos;

                    longest_substring =
                        Math.max(longest_substring, length_of_substring);

                    current_start_pos = i + 1;
                    break;
                }
            }

            current_end_pos++;
        }

        longest_substring = Math.max(
            longest_substring,
            current_end_pos - current_start_pos
        );

        return longest_substring;
    }
}

//Accepted answer