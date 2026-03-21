class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        val1, val2 = 0, 0
        for i in range(len(a)):
            val1 += int(a[i]) * (2**i)
        for j in range(len(b)):
            val2 += int(b[j]) * (2**j)
        total = val1 + val2
        if total == 0:
            return "0"
        s = ""
        while total != 0:
            s += str(total % 2)
            total //= 2
        return s[::-1]