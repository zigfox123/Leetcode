#https://leetcode.com/problems/set-mismatch/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            if (i+1) not in nums:
                missing = i+1
        #Look for a duplicate
        for i in range(len(nums)):
            if nums.count(nums[i]) > 1:
                duplicate = nums[i]
                break
        output.append(duplicate)
        output.append(missing)
        return output

test = Solution().findErrorNums([1,2,2,4])

print(test)

#Accepted answer