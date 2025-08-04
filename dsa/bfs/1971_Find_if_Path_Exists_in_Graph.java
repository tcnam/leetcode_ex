package bfs;
import java.util.*;

class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {

        Map<Integer, List<Integer>> nodeMap = new HashMap<Integer, List<Integer>>();
        Queue<Integer> queue = new LinkedList<Integer>();

        for (int i = 0; i < edges.length; i++){
            if (nodeMap.containsKey(edges[i][0]) == true){
                nodeMap.get(edges[i][0]).add(edges[i][1]);
            }
            else{
                nodeMap.put(edges[i][0], new ArrayList<Integer>(Arrays.asList(edges[i][1])));
            }

            if (nodeMap.containsKey(edges[i][1]) == true){
                nodeMap.get(edges[i][1]).add(edges[i][0]);
            }
            else{
                nodeMap.put(edges[i][1], new ArrayList<Integer>(Arrays.asList(edges[i][0])));
            }
        }

        queue.add(source);
        while (queue.peek() != null){

            int curNode = queue.remove();

            if (curNode == destination){
                return true;
            }

            if (nodeMap.containsKey(curNode) == true){
                for (int i = 0; i < nodeMap.get(curNode).size(); i++){
                    queue.add(nodeMap.get(curNode).get(i));
                }
            }
            nodeMap.remove(curNode);
        }
        return false;
    }
}
