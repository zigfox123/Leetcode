#Solution for Leetcode Problem 1: Two Sum

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Output = []
        left = 0
        right = len(nums) -1
        while left < right:
            current_sum = nums[left] +nums[right]
            if current_sum == target:
                Output.append(left)
                Output.append(right)
                return Output
            else:
                right -= 1
                if right == left:
                    left += 1
                    right = len(nums) -1

#Accepted Solution