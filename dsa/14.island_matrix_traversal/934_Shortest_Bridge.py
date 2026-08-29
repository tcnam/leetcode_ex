import typing as t 
from collections import deque

class Solution:
    def shortestBridge(self, grid: t.List[t.List[int]]) -> int:
        num_row: int = len(grid)
        num_col: int = len(grid[0])
        result: int = -1
        visited: t.List[t.List[bool]] = [[False] * num_col for _ in range(num_row)]
        queue: deque = deque()
        adj_offset: t.List[t.Tuple[int]] = [
            (-1, 0)
            ,(1, 0)
            ,(0, -1)
            ,(0, 1)
        ]
        first_island: t.List[t.List[int]] = []
        second_island: t.List[t.List[int]] = []

        for i in range(0, num_row, 1):
            for j in range(0, num_col, 1):
                if grid[i][j] == 0:
                    visited[i][j] = True
                    continue
                
                if visited[i][j]:
                    continue

                queue.append((i, j))
                temp_island: t.List[t.List[int]] = []
                while queue:
                    (row_ind, col_ind) = queue.popleft()
                    if visited[row_ind][col_ind]:
                        continue
                    
                    visited[row_ind][col_ind] = True
                    temp_island.append((row_ind, col_ind))

                    for offset in adj_offset:
                        adj_row_ind: int = row_ind + offset[0]
                        adj_col_ind: int = col_ind + offset[1]
                        if (0 <= adj_row_ind < num_row
                            and 0 <= adj_col_ind < num_col
                            and grid[adj_row_ind][adj_col_ind] == 1
                            and not visited[adj_row_ind][adj_col_ind]
                        ):
                            queue.append((adj_row_ind, adj_col_ind))
                if temp_island:
                    if not first_island:
                        first_island = temp_island.copy()
                    else:
                        second_island = temp_island.copy()
        
        for first_island_vertex in first_island:
            for second_island_vertex in second_island:
                bridge_val: int = abs(first_island_vertex[0] - second_island_vertex[0]) + abs(first_island_vertex[1] - second_island_vertex[1]) - 1
                if result < 0:
                    result = bridge_val
                
                if bridge_val < result:
                    result = bridge_val
            
        return result
