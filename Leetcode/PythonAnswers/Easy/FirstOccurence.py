class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)

        for i in range(h - n +1):
            j = 0
            while j < n and haystack[i+j] == needle[j]:
                j+=1
            
            if j == n:
                return i
        return -1

#Accepted answer using naive pattern matching