import typing as t
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: t.List[t.List[int]]) -> t.List[t.List[int]]:
        visited_pacific: t.Set[t.Tuple[int]] = set()
        visited_atlantic: t.Set[t.Tuple[int]] = set()
        queue_pacific: deque = deque()
        queue_atlantic: deque = deque()

        result: t.List[t.List[int]] = []
        num_row: int = len(heights)
        num_col: int = len(heights[0])
        adj_offset: t.List[t.Tuple[int]] = [
            (-1, 0)
            ,(1, 0)
            ,(0, -1)
            ,(0, 1)
        ]

        for row_ind in range(0, num_row, 1):
            for col_ind in range(0, num_col, 1):

                if row_ind == 0 or col_ind == 0:
                    queue_pacific.append((row_ind, col_ind))
                
                if row_ind == num_row - 1 or col_ind == num_col - 1:
                    queue_atlantic.append((row_ind, col_ind))
        
        while queue_pacific:
            cur_vertex: t.Tuple[int] = queue_pacific.popleft()
            row_ind: int = cur_vertex[0]
            col_ind: int = cur_vertex[1]
            
            if cur_vertex in visited_pacific:
                continue
            
            visited_pacific.add(cur_vertex)

            for offset in adj_offset:
                adj_row_ind: int = row_ind + offset[0]
                adj_col_ind: int = col_ind + offset[1]

                if (0 <= adj_row_ind < num_row
                    and 0 <= adj_col_ind < num_col
                    and heights[adj_row_ind][adj_col_ind] >= heights[row_ind][col_ind]
                    and (adj_row_ind, adj_col_ind) not in visited_pacific
                ):
                    queue_pacific.append((adj_row_ind, adj_col_ind))
        
        while queue_atlantic:
            cur_vertex: t.Tuple[int] = queue_atlantic.popleft()
            row_ind: int = cur_vertex[0]
            col_ind: int = cur_vertex[1]
            
            if cur_vertex in visited_atlantic:
                continue
            
            visited_atlantic.add(cur_vertex)

            for offset in adj_offset:
                adj_row_ind: int = row_ind + offset[0]
                adj_col_ind: int = col_ind + offset[1]

                if (0 <= adj_row_ind < num_row
                    and 0 <= adj_col_ind < num_col
                    and heights[adj_row_ind][adj_col_ind] >= heights[row_ind][col_ind]
                    and (adj_row_ind, adj_col_ind) not in visited_atlantic
                ):
                    queue_atlantic.append((adj_row_ind, adj_col_ind))

        for cur_vertex in visited_pacific:
            if cur_vertex in visited_atlantic:
                result.append([cur_vertex[0], cur_vertex[1]])
        
        return result

