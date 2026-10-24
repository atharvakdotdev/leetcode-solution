class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for r in matrix:
            l= 0 
            h= len(r)-1
            while l<=h:
                m = l + (h-l) // 2 
                if target == r[m]:
                    return True
                if target < r[m]:
                    h = m -1

                if target > r[m]:
                    l = m+1
        return False