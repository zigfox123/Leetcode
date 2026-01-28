from typing import List
#First Solution which brute forces through all combinations
#Works but execeeds time limits on larger inputs
class Solution:
    def maxArea(self, height: List[int]) -> int:
        largest_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = min(height[i], height[j]) * (j - i)
                if area > largest_area:
                    largest_area = area


        return largest_area 
    


test = Solution().maxArea([1,8,6,2,5,4,8,3,7])
print(test)

#Solution takes too long Is big O(n^2) time complexity

#Second Solution with O(n) time complexity

class SecondSolution:
    def maxArea(self, height: List[int]) -> int:
        largest_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            #Calculate the area using pointers
            area = min(height[left], height[right]) * (right - left)
            largest_area = max(largest_area, area)
            
            #Move the pointer pointing to shorter height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return largest_area


test = SecondSolution().maxArea([1,8,6,2,5,4,8,3,7])
print(test)