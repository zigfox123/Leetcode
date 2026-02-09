from typing import List
#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii
#Find how many numbers are smaller than the current number
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        Output = []
        for i in range(len(nums)):
            smaller_num = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    smaller_num += 1
            Output.append(smaller_num)
        return Output
    
test = Solution()
print(test.smallerNumbersThanCurrent([8,1,2,2,3]))

#Accepted answer