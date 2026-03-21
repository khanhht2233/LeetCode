class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ""
        for i in digits:
            res += str(i)
        tmp = str(int(res) + 1)
        return [int(i) for i in tmp]