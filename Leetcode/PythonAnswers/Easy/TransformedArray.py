#Leetcode Problem 3379 Transformed Array
from typing import List

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        #Itereate through the list and append the new value to the result list.
        result = []
        for i in range(len(nums)):
            n= nums[i]
            if i + n < len(nums) and i + n >= 0:
                result.append(nums[i + n])
            elif i + n >= len(nums):
                overflow = (i + n) // len(nums)
                overflow_result = (i+n) - (overflow * len(nums))
                result.append(nums[overflow_result])
            else:
                underflow = (i + n) // len(nums)
                underflow_result = (i+n) - (underflow * len(nums))
                result.append(nums[underflow_result])
        return result

#Accepted answer.