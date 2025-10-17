package bfs;
import java.util.*;

class Solution {
    public void solve(char[][] board) {
        int numRows = board.length;
        int numCols = board[0].length;
        Queue<int[]> queue = new LinkedList<int[]>();
        int[][] adjDelta = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
        for (int i = 0; i < numRows; i++){
            for (int j = 0; j < numCols; j++){

                if ((i == 0 || i == numRows - 1
                    || j == 0 || j == numCols -1)
                    && board[i][j] == 'O'){

                    queue.offer(new int[]{i, j});
                    board[i][j] = '1';
                }
            }
        }
        while (!queue.isEmpty()){
            int[] curNode = queue.poll();
            int rowIdx = curNode[0];
            int colIdx = curNode[1];
            for (int i = 0; i < adjDelta.length; i++){
                int adjRow = rowIdx + adjDelta[i][0];
                int adjCol = colIdx + adjDelta[i][1];

                if (adjRow > 0 && adjRow < numRows
                && adjCol > 0 && adjCol < numCols
                && board[adjRow][adjCol] == 'O'){

                    queue.offer(new int[]{adjRow, adjCol});
                    board[adjRow][adjCol] = '1';
                }
            }
        }

        for (int i = 0; i < numRows; i++){
            for (int j = 0; j < numCols; j++){
                if (board[i][j] == 'O'){
                    board[i][j] = 'X';
                }
                else if (board[i][j] == '1'){
                    board[i][j] = 'O';
                }
            }
        }
    }
}

