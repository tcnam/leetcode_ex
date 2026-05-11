from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result: List[List[int]] = []
        for row_ind in range(0, numRows, 1):
            result.append([])
            for col_ind in range(0, row_ind + 1, 1):
                if col_ind == 0 or col_ind == row_ind:
                    result[row_ind].append(1)
                else:
                    left_val: int = result[row_ind - 1][col_ind - 1]
                    right_val: int = result[row_ind - 1][col_ind]
                    result[row_ind].append(left_val + right_val)
        return result