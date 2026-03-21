class Solution:
    def getLucky(self, s: str, k: int) -> int:
        total = 0
        snew = ""
        for i in s:
            snew += str(ord(i) - 96)
        
        while k != 0:
            total = sum(list(int(snew[i]) for i in range(len(snew))))
            snew = str(total)
            k-= 1
        return total