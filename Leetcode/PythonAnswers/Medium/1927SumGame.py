class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        Lsum = Rsum = 0
        Lq = Rq = 0

        for i in range(half):
            if num[i] == '?':
                Lq += 1
            else:
                Lsum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                Rq += 1
            else:
                Rsum += int(num[i])

        if (Lq + Rq) % 2 == 1:
            return True

        return (Lsum - Rsum) != (Rq - Lq) * 9 // 2
#Accepted solution