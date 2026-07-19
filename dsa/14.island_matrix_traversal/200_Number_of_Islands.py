from collections import deque
import typing as t

class Solution:
    def numIslands(self, grid: t.List[t.List[str]]) -> int:
        queue: deque = deque()
        result: int = 0
        num_row: int = len(grid)
        num_col: int = len(grid[0])
        adj_offset: t.List[t.Tuple[int]] = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]
        for row_ind in range(0, num_row, 1):
            for col_ind in range(0, num_col, 1):
                if grid[row_ind][col_ind] == "0":
                    continue
                queue.append((row_ind, col_ind))
                # grid[row_ind][col_ind] = "0"

                while queue:
                    (cur_row, cur_col) = queue.popleft()
                    grid[cur_row][cur_col] = "0"
                    for offset in adj_offset:
                        adj_row: int = cur_row + offset[0]
                        adj_col: int = cur_col + offset[1]
                        if (
                            adj_row >= 0 and adj_row < num_row
                            and adj_col >= 0 and adj_col < num_col
                            and grid[adj_row][adj_col] == "1"
                        ):
                            queue.append((adj_row, adj_col))
                            grid[adj_row][adj_col] = "0"
                
                result += 1

        return result
        