package island_matrix_traversal;

class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int maxArea = 0;
        int numRow = grid.length;
        int numCol = grid[0].length;
        int[][] adjDelta = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for (int i = 0; i < numRow; i++){
            for (int j = 0; j < numCol; j++){
                int calArea = 0;
                if (grid[i][j] == 1){
                    calArea = dfs(grid, i, j, adjDelta, numRow, numCol, calArea);
                }
                if (calArea > maxArea){
                    maxArea = calArea;
                }
            }
        }
        return maxArea;
    }

    private int dfs(int[][] grid, int rowIdx, int colIdx, int[][] adjDelta, int numRow, int numCol, int calArea){
        grid[rowIdx][colIdx] = 0;
        calArea += 1;
        for (int i = 0; i < adjDelta.length; i++){
            int adjRow = rowIdx + adjDelta[i][0];
            int adjCol = colIdx + adjDelta[i][1];
            if (isInside(adjRow, adjCol, numRow, numCol)
            && grid[adjRow][adjCol] == 1){
                calArea = dfs(grid, adjRow, adjCol, adjDelta, numRow, numCol, calArea);
            }
        }
        return calArea;
    }

    private boolean isInside(int rowIdx, int colIdx, int numRow, int numCol){
        if (rowIdx >= 0 && rowIdx < numRow
        && colIdx >= 0 && colIdx < numCol){
            return true;
        }else {
            return false;
        }
    }
}
