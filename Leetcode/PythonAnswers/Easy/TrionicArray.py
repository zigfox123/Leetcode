from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        if n < 4:
            return False
        
        # Find the peak (p) - end of first increasing section
        p = 0
        while p < n - 1 and nums[p] < nums[p + 1]:
            p += 1
        
        if p == 0 or p >= n - 1:
            return False
        
        # Find the valley (q) - end of decreasing section
        q = p
        while q < n - 1 and nums[q] > nums[q + 1]:
            q += 1
        
        if q == p or q >= n - 1:
            return False
        
        # Verify final section is strictly increasing
        for i in range(q, n - 1):
            if nums[i] >= nums[i + 1]:
                return False
        
        return True
#Accepted answer.