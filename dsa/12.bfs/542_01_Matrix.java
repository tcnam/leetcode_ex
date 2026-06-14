package bfs;

import java.util.*;

class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int row = mat.length;
        int col = mat[0].length;
        int[][] result = new int[row][col];
        Queue<int[]> queue = new LinkedList<int[]>();
        int[][] adjDelta = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

        for (int i = 0; i < mat.length; i++){
            for (int j = 0; j< mat[0].length; j++){
                if (mat[i][j] == 0){
                    queue.offer(new int[]{i, j});
                    result[i][j] = 0;
                }
                else {
                    result[i][j] = -1;
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

                if (adjRow >= 0 && adjRow < mat.length
                    && adjCol >= 0 && adjCol < mat[0].length){
                        if (result[adjRow][adjCol] == -1){
                            result[adjRow][adjCol] = result[rowIdx][colIdx] + 1;
                            queue.offer(new int[]{adjRow, adjCol});
                        }
                }
            } 
        }
        return result;
    }
}
