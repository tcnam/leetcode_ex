package dfs;

class Solution {
    public boolean isBipartite(int[][] graph) {
        int grpSize = graph.length;
        int[] colors = new int[grpSize]; //0: unvisited, 1: partion 1, 2: partiion 2
        for (int i = 0; i < grpSize; i++){
            if (colors[i] == 0){
                if (!dfs(graph, i, colors, 1)){
                    return false;
                }
            }
        }
        return true;
    }

    public boolean dfs(int[][] graph, int curIdx, int[] colors, int colorVal){
        if (colors[curIdx] != 0){
            return colorVal == colors[curIdx];
        }
        colors[curIdx] = colorVal;
        int nextColorVal = (colorVal == 1) ? 2 : 1;
        for (int i = 0; i < graph[curIdx].length; i++){
            if (!dfs(graph, graph[curIdx][i], colors, nextColorVal)){
                return false;
            }
        }
        return true;
    }
}
