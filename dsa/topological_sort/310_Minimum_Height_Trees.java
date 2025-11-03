package topological_sort;
import java.util.*;

class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        List<List<Integer>> adjMatrix = new ArrayList<List<Integer>>();
        int[] inDegree = new int[n];
        List<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < n; i++){
            adjMatrix.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < edges.length; i++){
            int nodea = edges[i][0];
            int nodeb = edges[i][1];
            adjMatrix.get(nodea).add(nodeb);
            adjMatrix.get(nodeb).add(nodea);
            inDegree[nodea] += 1;
            inDegree[nodeb] += 1;
        }

        Queue<Integer> queue = new LinkedList<Integer>();
        for (int i = 0; i < n; i++){
            if (inDegree[i] == 1){
                queue.offer(i);
            } else if (inDegree[i] == 0){
                result.add(i);
            }
        }
        while (!queue.isEmpty()){
            int queueSize = queue.size();
            result.clear();
            for (int j = 0; j < queueSize; j++){
                int cur = queue.poll();
                result.add(cur);
                for (int k = 0; k < adjMatrix.get(cur).size(); k++){
                    inDegree[adjMatrix.get(cur).get(k)] -= 1;
                    if (inDegree[adjMatrix.get(cur).get(k)] == 1){
                        queue.offer(adjMatrix.get(cur).get(k));
                    }
                }
            }
        }

        return result;
    }
}