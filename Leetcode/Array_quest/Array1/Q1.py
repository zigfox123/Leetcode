#https://leetcode.com/problems/concatenation-of-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = []
        ans = nums
        for i in range(len(nums)):
            ans.append(nums[i])
        print(ans)
        return ans

#Valid Solution(Slow)(Above)

#Optimized Solution(Faster)

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        return nums + nums