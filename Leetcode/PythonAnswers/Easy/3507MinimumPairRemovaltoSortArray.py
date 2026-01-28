#Accepted answer for Leetcode problem 3507 "Minimum Pair Removal to Sort Array"

from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        output = 0
        if (nums == []):
            return 0
        if (nums == sorted(nums)):
            return 0
        
        while(nums != sorted(nums)):
            sum = 0
            for i in range(len(nums) - 1):
                if i == 0:
                    sum = nums[i] + nums[i+1]
                    index = i
                elif (sum > (nums[i]+ nums[i+1])):
                    sum = nums[i] + nums[i+1]
                    index = i
            nums[index] = nums[index] +nums[index + 1]
            nums.pop(index + 1)
            output += 1
        
        return output

test = Solution()
print(test.minimumPairRemoval([5,2,3,1]))