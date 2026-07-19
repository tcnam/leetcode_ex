package island_matrix_traversal;

class Solution {
    public int numIslands(char[][] grid) {
        int[][] adjDelta = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int numRow = grid.length;
        int numCol = grid[0].length;
        int result = 0;

        for (int i = 0; i < numRow; i++){
            for (int j = 0; j < numCol; j++){
                if (grid[i][j] == '1'){
                    dfs(grid, i, j, adjDelta, numRow, numCol);
                    result += 1;
                }
            }
        }
        return result;
    }

    private void dfs(char[][] grid, int rowIdx, int colIdx, int[][] adjDelta, int numRow, int numCol){
        grid[rowIdx][colIdx] = '0';
        for (int i = 0; i < adjDelta.length; i++){
            int adjRow = rowIdx + adjDelta[i][0];
            int adjCol = colIdx + adjDelta[i][1];
            if (isInside(adjRow, adjCol, numRow, numCol)
            && grid[adjRow][adjCol] == '1'){
                dfs(grid, adjRow, adjCol, adjDelta, numRow, numCol);
            }
        }
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
