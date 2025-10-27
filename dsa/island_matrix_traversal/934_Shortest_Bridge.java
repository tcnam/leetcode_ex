package island_matrix_traversal;
import java.util.*;

class Solution {
    int numRow;
    int numCol;
    int[][] adjDelta = new int[][]{{-1, 0}, {1,0}, {0,-1}, {0,1}};
    public int shortestBridge(int[][] grid) {
        numRow = grid.length;
        numCol = grid[1].length;
        int[][] distance = new int[numRow][numCol];
        Queue<int[]> queue = new LinkedList<int[]>();

        for (int i = 0; i < numRow; i++){
            for (int j = 0; j < numCol; j++){
                if (grid[i][j] == 1 && distance[i][j] == 0){
                    if (queue.isEmpty()){
                        dfs(grid, distance, i, j, queue);
                    }
                    else {
                        distance[i][j] = -1;
                    }
                }
            }
        }

        while (!queue.isEmpty()){
            int queueSize = queue.size();
            for (int i = 0; i < queueSize; i++){
                int[] cur = queue.poll();
                int rowIdx = cur[0];
                int colIdx = cur[1];
                for (int j = 0; j < 4; j++){
                    int adjRow = rowIdx + adjDelta[j][0];
                    int adjCol = colIdx + adjDelta[j][1];
                    if (isInside(adjRow, adjCol, numRow, numCol)){
                        if (distance[adjRow][adjCol] == 0) {
                            queue.offer(new int[]{adjRow, adjCol});
                            distance[adjRow][adjCol] = distance[rowIdx][colIdx] + 1;     
                        }
                        if (distance[adjRow][adjCol] == -1){
                            return distance[rowIdx][colIdx] - 1;
                        }
                    }
                }
            }
        }
        return -1;
    }

    private void dfs(int[][] grid, int[][] distance, int rowIdx, int colIdx, Queue<int[]> queue){
        distance[rowIdx][colIdx] = 1;
        queue.offer(new int[]{rowIdx, colIdx});
        for (int i = 0; i < 4; i++){
            int adjRow = rowIdx + adjDelta[i][0];
            int adjCol = colIdx + adjDelta[i][1];
            if (isInside(adjRow, adjCol, numRow, numCol) 
            && distance[adjRow][adjCol] == 0 
            && grid[adjRow][adjCol] == 1){
                dfs(grid, distance, adjRow, adjCol, queue);
            }
        }
    }

    private boolean isInside(int rowIdx, int colIdx, int numRow, int numCol){
        return (rowIdx >= 0 && rowIdx < numRow && colIdx >= 0 && colIdx < numCol);
    }
}
