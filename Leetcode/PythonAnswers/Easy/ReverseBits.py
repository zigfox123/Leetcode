class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:].zfill(32)
        answer = binary[::-1]
        answer = int(answer,2)


        return answer
