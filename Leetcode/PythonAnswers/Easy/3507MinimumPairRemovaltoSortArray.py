class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        output = 0
        if (nums == sorted(nums)):
            return 0
        while(nums != sorted(nums)):
            sum = 0
            for i in range((len(nums)-1)):
                if (nums[i] + nums[i+1] > sum):
                    sum = nums[i] + nums[i+1]
                    index = i
            nums[index] = sum
            nums.pop(index+1)
            output += 1
        return (output-1)  

#Not done yet