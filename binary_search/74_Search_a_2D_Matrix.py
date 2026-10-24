class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        low_row= 0
        low_column =0

        high_row= len(matrix) - 1
        high_column= len(matrix[0])- 1

        mid_c = low_column + (high_column - low_column) // 2
        mid_r = low_row + (high_row - low_row) // 2

        while low_row <= high_row :
            mid_r = low_row + (high_row - low_row) // 2

            if target == matrix[mid_r][mid_c]:
                return True
            if matrix[mid_r][0] <= target <= matrix[mid_r][-1]:
                while low_column <= high_column:
                    mid_c = low_column + (high_column - low_column) // 2

                    if target == matrix[mid_r][mid_c]:
                        return True
                    
                    if target < matrix[mid_r][mid_c]:
                        high_column= mid_c - 1

                    if target > matrix[mid_r][mid_c]:
                        low_column= mid_c + 1

            if target < matrix[mid_r][mid_c]:
                high_row = mid_r - 1 

            if target > matrix[mid_r][mid_c]:
                low_row= mid_r + 1
        
        return False
        

