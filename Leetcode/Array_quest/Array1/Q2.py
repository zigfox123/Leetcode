#https://leetcode.com/problems/shuffle-the-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        output = []
        for i in range(len(nums)//2):
            output.append(nums[i])
            output.append(nums[i+n])
        return output

test = Solution().shuffle([2,5,1,3,4,7], 3)
print(test)

#acceppted answer