from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        target_set = set(target)
        
        for i in range(1, target[-1] + 1):
            output.append("Push")
            if i not in target_set:
                output.append("Pop")
        
        return output
    
#Accepted answer