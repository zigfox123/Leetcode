class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest_substring = ""

        for i in range(len(s)):
            for j in range(i, len(s)):

                test_substring = s[i:j+1]

                reversed_string = test_substring[::-1]

                if test_substring == reversed_string:
                    if len(test_substring) > len(longest_substring):
                        longest_substring = test_substring

        return longest_substring
    
#Accepted answer