class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        se = set(nums)
        dic = dict({})
        res = []
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        for i in dic.keys():
            if dic[i] == 2:
                res.append(i)
                break
        seg = set()
        for i in range(len(nums)):
            seg.add(i + 1)
        tmp = seg.difference(se)
        res.append(next(iter(tmp)))
        return res

