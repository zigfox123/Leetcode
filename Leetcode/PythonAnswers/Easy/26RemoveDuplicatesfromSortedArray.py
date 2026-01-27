class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_nums = []
        for i in nums:
            if i not in unique_nums:
                unique_nums.append(i)
        for i in range(len(unique_nums)):
            nums[i] = unique_nums[i]
        
        return(len(unique_nums))
        
            
#Accepted answer