package bfs;
import java.util.*;

class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int numRows = heights.length;
        int numCols = heights[0].length;
        int[][] adjDelta = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        Queue<int[]> queue = new LinkedList<int[]>();
        int[][][][] visited = new int[numRows][numCols][2][2];
        
        for (int i = 0; i < numRows; i++){
            for (int j = 0; j < numCols; j++){
                if ((i - 1 < 0 && i + 1 >= numRows)
                    || (j - 1 < 0 && j + 1 >= numCols)
                    || (i - 1 < 0 && j + 1 >= numCols
                    || (j - 1 < 0 && i + 1 >= numRows))){
                    queue.offer(new int[]{i, j, 1, 1});
                }
                else if (i - 1 < 0 || j - 1 < 0){
                    queue.offer(new int[]{i, j, 1, 0});
                }
                else if (i + 1 >= numRows || j + 1 >= numCols){
                    queue.offer(new int[]{i, j, 0, 1});
                }
            }
        }

        while (!queue.isEmpty()){
            int[] node = queue.poll();
            int rowIdx = node[0];
            int colIdx = node[1];
            int pacFlag = node[2];
            int atlFlag = node[3];
            visited[rowIdx][colIdx][pacFlag][atlFlag] = 1;

            for (int i = 0; i < adjDelta.length; i++){
                int adjRow = rowIdx + adjDelta[i][0];
                int adjCol = colIdx + adjDelta[i][1];
                if (adjRow >= 0 && adjRow < numRows
                    && adjCol >=0 && adjCol < numCols
                    && heights[adjRow][adjCol] >= heights[rowIdx][colIdx]
                    && visited[adjRow][adjCol][pacFlag][atlFlag] == 0){

                    queue.offer(new int[]{adjRow, adjCol, pacFlag, atlFlag});
                    visited[adjRow][adjCol][pacFlag][atlFlag] = 1;
                }
            }
        }

        for (int i = 0; i < visited.length; i++){
            for (int j = 0; j < visited[0].length; j++){
                if (visited[i][j][1][1] == 1
                    || (visited[i][j][1][0] == 1 && visited[i][j][0][1] == 1)){
                    result.add(new ArrayList<>(Arrays.asList(i, j)));
                }
            }
        }
        return result;
    }
}