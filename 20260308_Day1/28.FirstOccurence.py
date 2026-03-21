class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                result = i
                break
        return result