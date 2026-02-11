from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        result = []
        
        for i in range(len(digits)):
            num += digits[i] * (10**(len(digits)-1-i))
        num += 1
        num = str(num)
        for i in range(len(str(num))):
            result.append(int(num[i]))
            
        return result

    
test = Solution()
test.plusOne([1,2,3])

#Accepted answer