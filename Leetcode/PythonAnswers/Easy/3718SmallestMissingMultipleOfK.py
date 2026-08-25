class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        ans_found = False
        multiple = 1
        ans = 0
        while(ans_found == False):
            found = False
            ans = k*multiple
            for i in nums:
                if i == ans:
                    found = True
                    break

            if found == False:
                return ans
            multiple += 1
#Accepted solution