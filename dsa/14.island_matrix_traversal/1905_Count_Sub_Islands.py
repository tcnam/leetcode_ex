import typing as t
from collections import deque

class Solution:
    def countSubIslands(self, grid1: t.List[t.List[int]], grid2: t.List[t.List[int]]) -> int:
        result: int = 0
        queue: deque = deque()
        num_row: int = len(grid2)
        num_col: int = len(grid2[0])
        adj_offset: t.List[t.Tuple[int]] = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]

        for row_ind in range(0, num_row, 1):
            for col_ind in range(0, num_col, 1):
                if grid2[row_ind][col_ind] == 0:
                    continue
                
                queue.append((row_ind, col_ind))
                grid2[row_ind][col_ind] = 0
                is_sub_island: bool = True

                while queue:
                    (cur_row, cur_col) = queue.popleft()
                    if grid1[cur_row][cur_col] == 0:
                        is_sub_island = False
                    for offset in adj_offset:
                        adj_row: int = cur_row + offset[0]
                        adj_col: int = cur_col + offset[1]
                        if (
                            adj_row >= 0 and adj_row < num_row
                            and adj_col >= 0 and adj_col < num_col
                            and grid2[adj_row][adj_col] == 1
                        ):
                            queue.append((adj_row, adj_col))
                            grid2[adj_row][adj_col] = 0
                
                if is_sub_island:
                    result += 1
        return result

        