class Solution:
    def findErrorNums(self, nums):
        n = len(nums)

        duplicate = sum(nums) - sum(set(nums))
        missing = n*(n+1)//2 - sum(set(nums))

        return [duplicate, missing]