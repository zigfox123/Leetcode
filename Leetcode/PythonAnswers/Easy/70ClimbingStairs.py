class Solution:
    def climbStairs(self, n: int) -> int:
        answer = 0
        base1 = 1
        
        #Fibonnaci sequence
        for i in range(n+1):
            print(answer)
            newanswer = answer +base1
            answer = base1
            base1 = newanswer

        return answer

#Accepted answer
                     
            



        
        

