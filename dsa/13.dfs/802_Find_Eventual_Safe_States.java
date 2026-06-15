package dfs;
import java.util.*;

class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int graphSize = graph.length;
        boolean[] visited = new boolean[graphSize];
        boolean[] path = new boolean[graphSize];
        List<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < graphSize; i++){
            if (!visited[i]){
                dfs(graph, i, visited, path);
            }
        }
        
        for (int i = 0; i < graphSize; i++){
            if (!path[i]){
                result.add(i);
            }
        }
        return result;
    }

    public boolean dfs(int[][] graph, int curIdx, boolean[] visited, boolean[] path){
        visited[curIdx] = true;
        path[curIdx] = true;
        for (int i = 0; i < graph[curIdx].length; i++){
            if (!visited[graph[curIdx][i]]){
                if (!dfs(graph, graph[curIdx][i], visited, path)){
                    return false;
                }
            }
            
            if (path[graph[curIdx][i]]){
                return false;
            }
        }
        path[curIdx] = false;
        return true;
    }
}
