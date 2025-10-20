package dfs;
import java.util.*;

class Solution {
    public int findCircleNum(int[][] isConnected) {
        int result = 0;
        Stack<Integer> stack = new Stack<Integer>();
        boolean[] visited = new boolean[isConnected.length];

        for (int i = 0; i < visited.length; i++){
            if (!visited[i]){
                visited[i] = true;
                for (int j = 0; j < visited.length; j++){
                    if (isConnected[i][j] == 1 && !visited[j]){
                        stack.push(j);
                    }
                }
                while (!stack.isEmpty()){
                    int curNode = stack.pop();
                    visited[curNode] = true;
                    for (int k = 0; k < visited.length; k++){
                        if (isConnected[curNode][k] == 1 && !visited[k]){
                            stack.push(k);
                        }
                    }
                }
                result += 1;
            }
        }
        return result;
    }
}
