from typing import List, Dict, Set
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict: Dict[int, Set[int]] = {i: set() for i in range(0, 9, 1)}
        colDict: Dict[int, Set[int]] = {i: set() for i in range(0, 9, 1)}
        squareDict: Dict[int, Set[int]] = {i: set() for i in range(0, 9, 1)}
        for rowInd in range(0, len(board), 1):
            for colInd in range(0, len(board[0]) ,1):
                if board[rowInd][colInd] != '.':
                    squareInd: int = rowInd//3*3 + colInd//3
                    if (board[rowInd][colInd] not in rowDict[rowInd]
                        and board[rowInd][colInd] not in colDict[colInd]
                        and board[rowInd][colInd] not in squareDict[squareInd]):
                        rowDict[rowInd].add(board[rowInd][colInd])
                        colDict[colInd].add(board[rowInd][colInd])
                        squareDict[squareInd].add(board[rowInd][colInd])
                    else:
                        return False
        return True
