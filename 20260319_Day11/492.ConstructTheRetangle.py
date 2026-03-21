class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        i = int(area**0.5)
        if float(i) < area**0.5:
            i += 1 
        ok = True
        while ok:
            if area % i == 0:
                return [i, area//i]
                ok = False
            else:
                i += 1

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        i = int(area**0.5)
        ok = True
        while ok:
            if area % i == 0:
                return [area//i, i]
                ok = False
            else:
                i -= 1