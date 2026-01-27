class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return(True)
        for i in range(len(nums)):
            if nums[i] == 1:
                for j in range(len(nums)):
                    if nums[j] == 1 and j > i and ((j-i)<=k):
                        return False
        return(True)
                        
#Accepted answer