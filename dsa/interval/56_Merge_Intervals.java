package interval;
import java.util.*;

class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> result = new ArrayList<>();
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        int tmpStart = intervals[0][0];
        int tmpEnd = intervals[0][1];
        for (int[] element : intervals) {
            if (isOverlap(tmpStart, tmpEnd, element[0], element[1])){
                tmpStart = Math.min(tmpStart, element[0]);
                tmpEnd = Math.max(tmpEnd, element[1]);
            }
            else{
                result.add(new int[]{tmpStart, tmpEnd});
                tmpStart = element[0];
                tmpEnd = element[1];
            }
        }
        result.add(new int[]{tmpStart, tmpEnd});

        return result.toArray(new int[result.size()][]);
    }

    private boolean isOverlap(int start1, int end1, int start2, int end2){
        return end1 >= start2 && start1 <= end2;
    }
}
