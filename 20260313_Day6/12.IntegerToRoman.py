class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {
            "I":1,
            "IV":4,
            "V":5,
            "IX":9,
            "X":10,
            "XL":40,
            "L":50,
            "XC":90,
            "C":100,
            "CD":400,
            "D":500,
            "CM":900,
            "M":1000
        }
        res = ""
        for i in reversed(dic.keys()):
            if num // dic[i]:
                res += i * (num // dic[i])
                num %= dic[i]
        return res
        