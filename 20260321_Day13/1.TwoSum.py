class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = dict({})
        for i in range(len(numbers)):
            need = target - numbers[i]
            if need in dic:
                return [dic[need], i]
            else:
                dic[numbers[i]] = i
