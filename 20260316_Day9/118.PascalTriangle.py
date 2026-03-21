class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        else:
            ls = []
            for i in range(numRows):
                subLs = [0]
                ls.append(subLs * (i + 1))
            ls[0][0] = 1
            for i in range(1, numRows):
                for j in range(i + 1):
                    if (j - 1) < 0:
                        ls[i][j] = ls[i-1][j]
                    elif j >= i:
                        ls[i][j] = ls[i - 1][j - 1]
                    else:
                        ls[i][j] = ls[i-1][j] + ls[i - 1][j - 1]
            return ls