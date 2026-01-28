#Accepted answer for Leetcode problem 17 "Letter Combinations of a Phone Number"

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        Output = []
        holder = 0
        while holder < len(digits):
            current_digit = digits[holder]
            letters = dict.get(current_digit, [])
            if holder == 0:
                for letter in letters:
                    Output.append(letter)
            else:
                temp = []
                for combo in Output:
                    for letter in letters:
                        temp.append(combo + letter)
                Output = temp
            holder += 1

        return Output
    
test = Solution()
print(test.letterCombinations("233"))

