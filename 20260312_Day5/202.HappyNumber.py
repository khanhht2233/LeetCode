class Solution:
    def isHappy(self, n: int) -> bool:
        data = set()
        tmp = 0
        while n != 1 and n not in data:
            data.add(n)
            tmp = 0
            while n != 0:
                tmp += (n % 10) ** 2
                n //= 10
            n = tmp
        return n == 1