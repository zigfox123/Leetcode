class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        word = ""
        words = []
        if len(s) == 1:
            return 1
        
        for i in range(len(s)):

            if i == len(s)-1:
                if s[i] != " ":
                    word+= s[i]
                    words.append(word)
                    word = ""
                
            if s[i] == " ":
                if word != "":
                    words.append(word)
                    word = ""
            else:
                word += s[i]

        print(words)
            
        return len(words[-1])
        

test = Solution()
print(test.lengthOfLastWord("luffy is still joyboy"))

#Accepted answer