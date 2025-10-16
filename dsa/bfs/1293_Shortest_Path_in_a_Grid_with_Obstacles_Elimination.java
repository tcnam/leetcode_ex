package bfs;
import java.util.*;

class Solution {
    public int shortestPath(int[][] grid, int k) {
        int numRows = grid.length;
        int numCol = grid[0].length;
        int[][][] visited = new int[numRows][numCol][k+1];

        Queue<int[]> queue = new LinkedList<int[]>();
        queue.offer(new int[]{0, 0, k});
        visited[0][0][k] = 1;

        int[][] adjDelta = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
        int result = 0;

        while (!queue.isEmpty()){
            int queueSize = queue.size();
            for (int i = 0; i < queueSize; i++){
                int[] tmpNode = queue.poll();
                int rowIdx = tmpNode[0];
                int colIdx = tmpNode[1];
                int remainObs = tmpNode[2];
                if (rowIdx == numRows - 1
                && colIdx == numCol -1){
                    return result;
                }

                for (int j = 0; j < adjDelta.length; j++){
                    int adjRow = rowIdx + adjDelta[j][0];
                    int adjCol = colIdx + adjDelta[j][1];
                    if (adjRow >= 0 && adjRow < numRows
                    && adjCol >=0 && adjCol < numCol){
                        if (adjRow == numRows - 1
                        && adjCol == numCol -1){
                            return result + 1;
                        }
                        if (grid[adjRow][adjCol] == 1 
                        && remainObs > 0
                        && visited[adjRow][adjCol][remainObs-1] == 0){
                            visited[adjRow][adjCol][remainObs-1] = 1;
                            queue.offer(new int[]{adjRow, adjCol, remainObs-1});
                        }else if (grid[adjRow][adjCol] == 0
                        && visited[adjRow][adjCol][remainObs] == 0){
                            visited[adjRow][adjCol][remainObs] = 1;
                            queue.offer(new int[]{adjRow, adjCol, remainObs});
                        }
                    }
                }
            }
            result += 1;
        }
        // System.out.println(result);
        return -1;
    }
}