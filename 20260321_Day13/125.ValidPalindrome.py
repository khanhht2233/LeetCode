class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if "a" <= i <= "z" or "A" <= i <= "Z" or "0" <= i <= "9"]
        return s == s[::-1]