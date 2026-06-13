import typing as t
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: t.List[t.List[int]]) -> int:
        num_row: int = len(grid)
        num_col: int = len(grid)

        if grid[num_row - 1][num_col - 1] == 1:
            return -1

        queue: deque = deque([(0, 0)])
        result: int = 0

        while queue:
            queue_length: int = len(queue)
            ind: int = 0
            
            while ind < queue_length:
                ind += 1

                cur_vertex: t.Set[int] = queue.popleft()
                row_ind: int = cur_vertex[0]
                col_ind: int = cur_vertex[1]

                if grid[row_ind][col_ind] == 1:
                    continue
                
                if row_ind == num_row - 1 and col_ind == num_col - 1:
                    return result + 1
                
                grid[row_ind][col_ind] = 1
                
                for row_offset in [-1, 0, 1]:
                    for col_offset in [-1, 0, 1]:
                        adj_row_ind: int = row_ind + row_offset
                        adj_col_ind: int = col_ind + col_offset
                        if (
                            self.isValidAdj(adj_row_ind, adj_col_ind, num_row, num_col)
                            and grid[adj_row_ind][adj_col_ind] == 0
                        ):
                            adj_tuple: t.Tuple[int] = (adj_row_ind, adj_col_ind)
                            queue.append(adj_tuple)

            result += 1
        
        return -1
    
    def isValidAdj(self, row_ind: int, col_ind: int, num_row: int, num_col: int) -> bool:
        return (
            0 <= row_ind < num_row
            and 0 <= col_ind < num_col
        )
    