class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        Output = 0
        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
                Output += 1
                j = 1
                while i - j >= 0 and i + 1 + j < len(s) and s[i - j] == s[i] and s[i + 1 + j] == s[i + 1]:
                    Output += 1
                    j += 1
        return Output

#Accepted Answer 