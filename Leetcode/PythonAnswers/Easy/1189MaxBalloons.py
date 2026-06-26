class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ballon_count = {"b": 0, "a":0, "l": 0 , "o": 0 , "n": 0}
        text = text.lower()
        for char in text:
            if char in ballon_count:
                ballon_count[char] += 1
        ballon_count["l"] //=2
        ballon_count["o"] //=2
        return min(ballon_count.values())

        #accepted answer.