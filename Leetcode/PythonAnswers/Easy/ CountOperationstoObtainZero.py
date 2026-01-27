class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        counter = 0
        while (num1 != 0) and (num2 != 0):
            if num2 > num1:
                num2 = num2 - num1
            else:
                num1 = num1 - num2
            counter += 1
        
        return(counter)
#Accepted Solution
''' You get two non-negative numbers num1 and num2
    In one operation, if num1 >= num2, you must subtract num2 from num1,
    otherwise subtract num1 from num2. 
    Return the number of operations required to make either num1 = 0 or num2 = 0
    if they are the same num2 - num1'''

'''Example
    num1 = 2, num2 = 3
    num2-num1
    num1 = 2 num2 =1
    num1-num2
    num1 = 1 num2 = 1
    num2 - num1
    num2 = 0 hence return
    '''
