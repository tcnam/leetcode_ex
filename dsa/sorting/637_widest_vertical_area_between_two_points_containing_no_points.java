package sorting;
import java.util.*;

class Solution {
    public int maxWidthOfVerticalArea(int[][] points) {
        int[] sortedArr = Arrays.stream(points).mapToInt(point -> point[0]).sorted().toArray();
        int maxWidth = 0;
        for (int i = 1; i < sortedArr.length; i ++){
            int tempWidth = sortedArr[i] - sortedArr[i-1];
            if (tempWidth > maxWidth){
                maxWidth = tempWidth;
            }
        }
        return maxWidth;
    }
}
