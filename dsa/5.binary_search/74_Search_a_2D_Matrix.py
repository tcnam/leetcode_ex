import typing as t

class Solution:
    def searchMatrix(self, matrix: t.List[t.List[int]], target: int) -> bool:
        num_row: int = len(matrix)
        num_col: int = len(matrix[0])

        left: int = 0
        right: int = num_row * num_col - 1

        while left <= right:
            mid: int = int((right - left) / 2) + left
            (row_ind, col_ind) = self.convert1DIndTo2DInd(mid, num_col)
            if matrix[row_ind][col_ind] == target:
                return True
            elif matrix[row_ind][col_ind] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
    
    def convert1DIndTo2DInd(self, ind: int, num_col: int) -> t.Tuple[int]:
        row_ind: int = int(ind / num_col)
        col_ind: int = ind % num_col
        return (row_ind, col_ind)
