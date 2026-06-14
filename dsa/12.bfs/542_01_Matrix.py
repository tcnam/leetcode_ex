from collections import deque
import typing as t

class Solution:
    def updateMatrix(self, mat: t.List[t.List[int]]) -> t.List[t.List[int]]:
        queue: deque = deque()
        num_row: int = len(mat)
        num_col: int = len(mat[0])
        result: t.List[t.List[int]] = [[-1] * num_col for _ in range(num_row)]
        adj_offset: t.List[t.Tuple[int]] = [
            (-1, 0)
            ,(1, 0)
            ,(0, -1)
            ,(0, 1)
        ]

        for row_ind in range(0, num_row, 1):
            for col_ind in range(0, num_col, 1):
                if mat[row_ind][col_ind] == 0:
                    cur_vertex: t.Tuple[int] = (row_ind, col_ind)
                    queue.append(cur_vertex)
                    result[row_ind][col_ind] = 0
        
        while queue:
            cur_queue_size: int = len(queue)
            ind: int = 0
            while ind < cur_queue_size:
                ind += 1
                cur_vertex: int = queue.popleft()
                row_ind: int = cur_vertex[0]
                col_ind: int = cur_vertex[1]
                
                for offset in adj_offset:
                    adj_row_ind: int = row_ind + offset[0]
                    adj_col_ind: int = col_ind + offset[1]
                    if (
                        0 <= adj_row_ind < num_row
                        and 0 <= adj_col_ind < num_col
                        and result[adj_row_ind][adj_col_ind] == -1
                    ):
                        
                        result[adj_row_ind][adj_col_ind] = result[row_ind][col_ind] + 1
                        adj_vertex: t.Tuple[int] = (adj_row_ind, adj_col_ind)
                        queue.append(adj_vertex)
        
        return result
