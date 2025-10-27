package island_matrix_traversal;

class Solution {
    public int countSubIslands(int[][] grid1, int[][] grid2) {
        int numRow = grid1.length;
        int numCol = grid1[0].length;
        boolean[][] visited = new boolean[numRow][numCol];
        int[][] adjDelta = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int result = 0;
        for (int i = 0; i < numRow; i++){
            for (int j = 0; j < numCol; j++){
                if (visited[i][j] == false && grid2[i][j] == 1){
                    int count = dfs(grid1, grid2, visited, adjDelta, i, j, numRow, numCol, 0);
                    if (count == 0){
                        result += 1;
                    }
                }
            }
        }
        return result;
    }

    private int dfs(int[][] grid1, int[][] grid2, boolean[][] visited, int[][] adjDelta
                        , int rowIdx, int colIdx, int numRow, int numCol, int count){
        visited[rowIdx][colIdx] = true;
        if (grid1[rowIdx][colIdx] == 0){
            count += 1;
        }
        for (int i = 0; i < adjDelta.length; i++){
            int adjRow = rowIdx + adjDelta[i][0];
            int adjCol = colIdx + adjDelta[i][1];
            if (isInside(adjRow, adjCol, numRow, numCol)
            && !visited[adjRow][adjCol]
            && grid2[adjRow][adjCol] == 1){
                count += dfs(grid1, grid2, visited, adjDelta, adjRow, adjCol, numRow, numCol, count);
            }
        }
        return count;
    }

    private boolean isInside(int rowIdx, int colIdx, int numRow, int numCol){
        return (
            rowIdx >= 0 && rowIdx < numRow
            && colIdx >=0 && colIdx < numCol
        );
    }
}
