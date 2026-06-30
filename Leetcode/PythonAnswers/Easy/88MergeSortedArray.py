class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new_nums = []
        for i in range(m):
            new_nums.append(nums1[i])
        for i in range(len(nums2)):
            new_nums.append(nums2[i])
        
        new_nums.sort()
        nums1[:] = new_nums

        

