package dfs;
import java.util.*;

class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] visited = new boolean[rooms.size()];
        Stack<Integer> stack = new Stack<Integer>();
              
        for (int i = 0; i < rooms.get(0).size(); i++){
            stack.push(rooms.get(0).get(i));
            visited[0] = true;
        }
        int countVisited = 1;

        while (!stack.isEmpty()){
            int curNode = stack.pop();
            if (!visited[curNode]){
                visited[curNode] = true;
                countVisited += 1;
                for (int i = 0; i < rooms.get(curNode).size(); i++){
                    stack.push(rooms.get(curNode).get(i));
                }
            }
        }

        if (countVisited == rooms.size()){
            return true;
        }
        else {
            return false;
        }
    }
}
