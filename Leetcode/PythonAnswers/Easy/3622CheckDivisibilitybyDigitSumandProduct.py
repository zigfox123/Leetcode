class Solution:
    def checkDivisibility(self, n: int) -> bool:
        if n == 0:
            return False
        sum = 0
        product = 1
        string_n = str(n)
        for i in string_n:
            sum += int(i)
            product *= int(i)
        total = product + sum
        if(n % total == 0):
            return True
        else:
            return False
#Accepted solution