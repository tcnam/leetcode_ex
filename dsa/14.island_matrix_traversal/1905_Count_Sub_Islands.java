package island_matrix_traversal;

class Solution {
    int numRow;
    int numCol;
    int[][] adjDelta = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public int countSubIslands(int[][] grid1, int[][] grid2) {
        numRow = grid1.length;
        numCol = grid1[0].length;
        boolean[][] visited = new boolean[numRow][numCol];
        int result = 0;
        for (int i = 0; i < numRow; i++){
            for (int j = 0; j < numCol; j++){
                if (visited[i][j] == false && grid2[i][j] == 1){
                    if (dfs(grid1, grid2, visited, i, j)){
                        result+=1;
                    }
                }
            }
        }
        return result;
    }

    private boolean dfs(int[][] grid1, int[][] grid2, boolean[][] visited, int rowIdx, int colIdx){
        visited[rowIdx][colIdx] = true;
        boolean ok = grid1[rowIdx][colIdx] == 1;
        for (int i = 0; i < adjDelta.length; i++){
            int adjRow = rowIdx + adjDelta[i][0];
            int adjCol = colIdx + adjDelta[i][1];
            if (isInside(adjRow, adjCol, numRow, numCol)
            && !visited[adjRow][adjCol]
            && grid2[adjRow][adjCol] == 1){
                ok &= dfs(grid1, grid2, visited, adjRow, adjCol);
            }
        }
        return ok;
    }

    private boolean isInside(int rowIdx, int colIdx, int numRow, int numCol){
        return (
            rowIdx >= 0 && rowIdx < numRow
            && colIdx >=0 && colIdx < numCol
        );
    }
}
