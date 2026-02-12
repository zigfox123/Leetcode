from math import sqrt
class Solution:
    def mySqrt(self, x: int) -> int:
        ans = sqrt(x)
        ans = int(ans)
        return ans

test = Solution()
print(test.mySqrt(8))
#No idea why you wouldn't use anything but sqrt function

class Solution:
    def mySqrt(self, x: int) ->int:
        if x < 2:
            return x
        
        i = 2
        while i * i <= x:
            i += 1
        
        return i - 1
#Brute force solution

#Both are accepted