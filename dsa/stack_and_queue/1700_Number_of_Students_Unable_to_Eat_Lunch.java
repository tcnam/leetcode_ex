package stack_and_queue;
import java.util.*;

class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        Queue<Integer> studentsQueue = new LinkedList<Integer>();

        for (int i = 0 ; i < students.length; i ++){
            studentsQueue.add(students[i]);
        }

        int curNmStudent = students.length;
        int count = 0;

        int indSandwiches = 0;

        while (indSandwiches < sandwiches.length){
            if (count >= curNmStudent){
                return curNmStudent;
            }

            if (sandwiches[indSandwiches] == studentsQueue.peek()){
                studentsQueue.remove();
                indSandwiches += 1;
                count = 0;
                curNmStudent -= 1;
            }
            else{
                count += 1;
                studentsQueue.add(studentsQueue.remove());
            }
        }
        return 0;
    }
}
