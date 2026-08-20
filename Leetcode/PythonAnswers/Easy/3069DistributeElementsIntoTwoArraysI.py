class Solution(object):
    def resultArray(self, nums):
        arr1 = []
        arr2 = []
        result = []
        for i in range(len(nums)):
            if i == 0:
                arr1.append(nums[i])
            elif i == 1:
                arr2.append(nums[i])
            elif arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        for i in range(len(arr1)):
            result.append(arr1[i])
        for i in range(len(arr2)):
            result.append(arr2[i])
        return result
#Accepted solution