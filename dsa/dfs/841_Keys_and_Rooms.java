package dfs;
import java.util.*;

class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        // return nonRecursiveSolution(rooms);
        return recursiveSolution(rooms);
    }

    public boolean nonRecursiveSolution(List<List<Integer>> rooms){
        int roomsSize = rooms.size();
        boolean[] visited = new boolean[roomsSize];
        Stack<Integer> stack = new Stack<Integer>();
        
        for (int i = 0; i < rooms.get(0).size(); i++){
            stack.push(rooms.get(0).get(i));
            visited[0] = true;
        }

        while (!stack.isEmpty()){
            int curNode = stack.pop();
            if (!visited[curNode]){
                visited[curNode] = true;
                for (int i = 0; i < rooms.get(curNode).size(); i++){
                    stack.push(rooms.get(curNode).get(i));
                }
            }
        }

        for (int i = 0; i < roomsSize; i++){
            if (!visited[i]){
                return false;
            }
        }
        return true;
    }


    public boolean recursiveSolution(List<List<Integer>> rooms){
        int length = rooms.size();
        boolean[] visited = new boolean[length];
        dfs(0, rooms, visited);
        for (int i = 0; i < length; i++){
            if (!visited[i]){
                return false;
            }
        }
        return true;
    }

    public void dfs(int curIdx, List<List<Integer>> rooms, boolean[] visited){
        visited[curIdx] = true;
        for (int i = 0; i < rooms.get(curIdx).size(); i++){
            int adjIdx = rooms.get(curIdx).get(i);
            if (!visited[adjIdx]){
                dfs(adjIdx, rooms, visited);
            }
        }
    }
}
