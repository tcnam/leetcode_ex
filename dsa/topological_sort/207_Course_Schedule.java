package topological_sort;
import java.util.*;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        return bfsSolution(numCourses, prerequisites);
    }

    private boolean bfsSolution(int numCourses, int[][] prerequisites){
        int[] inDrege = new int[numCourses];
        List<List<Integer>> adjMatrix = new ArrayList<List<Integer>>(numCourses);
        for (int i = 0; i < numCourses; i++){
            adjMatrix.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < prerequisites.length; i++){
            int course = prerequisites[i][0];
            int preCourse = prerequisites[i][1];
            inDrege[course] += 1;
            adjMatrix.get(preCourse).add(course);
        }

        Queue<Integer> queue = new LinkedList<Integer>();
        List<Integer> result = new ArrayList<Integer>(numCourses);
        for (int i = 0; i < numCourses; i++){
            if(inDrege[i]==0){
                queue.add(i);
            }
        }
        while (!queue.isEmpty()){
            int cur = queue.poll();
            result.add(cur);
            for (int i = 0; i < adjMatrix.get(cur).size(); i++){
                inDrege[adjMatrix.get(cur).get(i)] -= 1;
                if (inDrege[adjMatrix.get(cur).get(i)]==0){
                    queue.add(adjMatrix.get(cur).get(i));
                }
            }
        }
        return result.size() == numCourses;
        
    }
}
