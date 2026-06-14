import typing as t
from collections import deque

class Solution:
    def shortestPath(self, grid: t.List[t.List[int]], k: int) -> int:
        num_row: int = len(grid)
        num_col: int = len(grid[0])
        queue: deque = deque([(0, 0, k)])
        adj_offset: t.List[t.Tuple[int]] = [
            (-1, 0)
            ,(1, 0)
            ,(0, -1)
            ,(0, 1)
        ]
        result: int = 0
        visited: t.Set[t.Tuple[int]] = set()

        while queue:
            len_queue: int = len(queue)
            ind: int = 0
            while ind < len_queue:
                ind += 1
                cur_vertex: t.Tuple[int] = queue.popleft()
                if cur_vertex in visited:
                    continue

                row_ind: int = cur_vertex[0]
                col_ind: int = cur_vertex[1]
                remain_k: int = cur_vertex[2]

                visited.add(cur_vertex)

                if (row_ind == num_row - 1 
                    and col_ind == num_col - 1
                    and (
                        grid[row_ind][col_ind] == 0
                        or (grid[row_ind][col_ind] == 1
                            and remain_k >= 1)
                    )
                ):
                    return result
                
                for offset in adj_offset:
                    adj_row_ind: int = row_ind + offset[0]
                    adj_col_ind: int = col_ind + offset[1]
                    if (0 <= adj_row_ind < num_row
                        and 0 <= adj_col_ind < num_col
                    ):
                        if (grid[adj_row_ind][adj_col_ind] == 0 
                            and (adj_row_ind, adj_col_ind, remain_k) not in visited
                        ):
                            queue.append((adj_row_ind, adj_col_ind, remain_k))
                            continue
                        
                        if (grid[adj_row_ind][adj_col_ind] == 1
                            and remain_k >= 1
                            and (adj_row_ind, adj_col_ind, remain_k - 1) not in visited  
                        ):
                            queue.append((adj_row_ind, adj_col_ind, remain_k - 1))
                            continue

            result += 1

        return -1 
                


        