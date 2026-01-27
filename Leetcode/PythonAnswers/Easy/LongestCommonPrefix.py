class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        for s in strs[1:]:
            while not s.startswith(first_word):
                first_word =first_word[:-1]
                if not first_word:
                    return ""
                

        return first_word

#Take the first word and compare it to the rest checking first letter against first 
# second against second and so on until not a match

#Accept python answer