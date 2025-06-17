package sorting;
import java.util.*;
class Solution {
    public int[][] sortTheStudents(int[][] score, int k) {
        Map<Integer, Integer> originInd = new HashMap<Integer, Integer>();
        Integer[] cloneArr = new Integer[score.length];
        int[][] result = new int[score.length][score[0].length];
        for (int i = 0; i < score.length; i++){
            originInd.put(score[i][k], i);
            cloneArr[i] = score[i][k];
            // System.out.println(cloneArr[i]);
        }
        // Solution.sort(cloneArr, 0, cloneArr.length - 1);
        // for (int i = 0; i < cloneArr.length; i ++){
        //     System.out.println(cloneArr[i]);
        // }
        
        Arrays.sort(cloneArr, Collections.reverseOrder());
        
        for (int i = 0; i < result.length; i ++){
            result[i] = score[originInd.get(cloneArr[i])];
        }
        return result;
    }
    public static void sort(Integer[] arr, int leftInd, int rightInd){
        if (leftInd < rightInd){
            int midInd = (int) (rightInd - leftInd)/2;
            Solution.sort(arr, leftInd, midInd);
            Solution.sort(arr, midInd + 1, rightInd);
            Solution.merge(arr, leftInd, midInd, rightInd);
        }
    }

    public static void merge(Integer[] arr, int leftInd, int midInd, int rightInd){
        int leftArrSize = midInd - leftInd;
        int rightArrSize = rightInd - midInd + 1;

        int[] leftArr = new int[leftArrSize];
        int[] rightArr = new int[rightArrSize];

        for (int i = 0; i < leftArrSize; i++){
            leftArr[i] = arr[i];
        }

        for (int j = 0; j < rightArrSize; j++){
            rightArr[j] = arr[j + midInd];
        }

        int i = 0;
        int j = 0;
        int arrInd = 0;

        while (i < leftArrSize && j < rightArrSize){
            if (leftArr[i] > rightArr[j]){
                arr[arrInd] = leftArr[i];
                i += 1;
            }
            else{
                arr[arrInd] = rightArr[j];
                j += 1;
            }
            arrInd+=1;
        }

        while (i < leftArrSize){
            arr[arrInd] = leftArr[i];
            i += 1;
            arrInd+=1;
        }

        while (j < rightArrSize){
            arr[arrInd] = rightArr[j];
            j += 1;     
            arrInd += 1;      
        }
    }
}
