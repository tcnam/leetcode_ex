from collections import deque
import typing as t

class Solution:
    def solve(self, board: t.List[t.List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue: deque = deque()
        num_row: int = len(board)
        num_col: int = len(board[0])
        visited: t.Set[t.Tuple[int]] = set()
        adj_offset: t.List[t.Tuple[int]] = [
            (-1, 0)
            ,(1, 0)
            ,(0, -1)
            ,(0, 1)
        ]

        for row_ind in range(0, num_row, 1):
            for col_ind in range(0, num_col, 1):
                if (
                    board[row_ind][col_ind] == "O"
                    and (
                        row_ind == 0
                        or col_ind == 0
                        or row_ind == num_row - 1
                        or col_ind == num_col - 1
                    )
                ):
                    queue.append((row_ind, col_ind))
        
        while queue:
            cur_vertex: t.Tuple[int] = queue.popleft()
            row_ind: int = cur_vertex[0]
            col_ind: int = cur_vertex[1]

            if cur_vertex in visited:
                continue

            visited.add(cur_vertex)
            
            for offset in adj_offset:
                adj_row_ind: int = row_ind + offset[0]
                adj_col_ind: int = col_ind + offset[1]
                if (0 <= adj_row_ind < num_row
                    and 0 <= adj_col_ind < num_col
                    and board[adj_row_ind][adj_col_ind] == "O"
                    and (adj_row_ind, adj_col_ind) not in visited
                ):
                    queue.append((adj_row_ind, adj_col_ind))
        
        for row_ind in range(0, num_row, 1):
            for col_ind in range(0, num_col, 1):
                if (board[row_ind][col_ind] == "O"
                    and (row_ind, col_ind) not in visited
                ):
                    board[row_ind][col_ind] = "X"
            
        
        

        