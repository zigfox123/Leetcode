#Accepted answer for Leetcode problem 20 "Valid Parentheses"

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            #print(char)
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
                
                
        return True
    
test = Solution()
print(test.isValid("(()[]{})"))

#All parentheses must be closed and in the correct order.
#Loop through the string and use a stack to keep track of opening parentheses.
#When a closing parenthesis is found, check if it matches the last opening parenthesis in the stack.
#If it matches, pop the last opening parenthesis from the stack.
#If it doesn't match or the stack is empty, return False.
#At the end of the loop, if the stack is empty, return True. Otherwise, return False.