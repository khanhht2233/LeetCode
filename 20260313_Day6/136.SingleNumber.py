class Solution:
    def singleNumber(self, nums: List[int]) -> int:   #Cach1 : su dung dic -> HashMap -> (O(n))
        dic = dict({})
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        for i in dic.keys():
            if dic[i] == 1:
                return i
        

class Solution:                                        #Su dung ham co san -> O(n^2)
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i