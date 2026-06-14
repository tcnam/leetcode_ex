package bfs;
import java.util.*;

class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        Queue<int[]> queue = new LinkedList<int[]>();
        int result = 0;

        if (grid[0][0] == 1){
            return -1;
        }
        queue.offer(new int[]{0, 0});
        grid[0][0] = 1;
        
        while (queue.isEmpty() == false){
            int queueLen = queue.size();
            for (int queueIdx = 0; queueIdx < queueLen; queueIdx++){
                int[] tempList = queue.poll();
                int rowIdx = tempList[0];
                int colIdx = tempList[1];
                
                if (rowIdx == grid.length - 1 && colIdx == grid[0].length - 1){
                    return result + 1;
                }

                for (int i = -1; i <= 1; i++){
                    for (int j = -1; j <= 1; j++){
                        int adjRowIdx = rowIdx + i;
                        int adjColIdx = colIdx + j;
                        if (adjRowIdx >= 0 && adjRowIdx < grid.length
                            && adjColIdx >= 0 && adjColIdx < grid[0].length
                            && grid[adjRowIdx][adjColIdx] == 0){
                            // need to masked adj as visited also to eliminate duplicate processing
                            grid[adjRowIdx][adjColIdx] = 1;
                            queue.offer(new int[]{adjRowIdx, adjColIdx});
                        }
                    }
                }
                
                
            }
            result += 1;
        }
        return -1;
    }
}
