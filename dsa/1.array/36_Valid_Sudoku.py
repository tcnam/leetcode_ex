from typing import List, Dict, Set
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map: Dict[Set[str]] = {i: set() for i in range(0, 9, 1)}
        col_map: Dict[Set[str]] = {i: set() for i in range(0, 9, 1)}
        grid_map: Dict[Set[str]] = {i: set() for i in range(0, 9, 1)}
        row: int = len(board)
        col: int = len(board[0])
        
        for row_ind in range (0, row, 1):
            for col_ind in range (0, col, 1):
                grid_ind: int = self._find_grid_ind(row_ind, col_ind)
                val: int = board[row_ind][col_ind]
                if val == '.':
                    continue

                if val in grid_map[grid_ind] or val in row_map[row_ind] or val in col_map[col_ind]:
                    return False
                else:
                    grid_map[grid_ind].add(val)
                    row_map[row_ind].add(val)
                    col_map[col_ind].add(val)
        
        return True

    
    def _find_grid_ind(self, row: int, col: int) -> int:
        return int(row/3) * 3 + int(col/3)
