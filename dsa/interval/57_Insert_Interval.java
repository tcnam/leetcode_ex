package interval;
import java.util.*;

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<int[]>();
        int trackInd = -1;
        int tmpStart = newInterval[0];
        int tmpEnd = newInterval[1];
        for (int i = 0; i < intervals.length; i++){
            if (isOverlap(intervals[i][0], intervals[i][1], tmpStart, tmpEnd)){
                trackInd = i + 1;
                tmpStart = Math.min(intervals[i][0], tmpStart);
                tmpEnd = Math.max(intervals[i][1], tmpEnd);
                break;
            }
            else if (intervals[i][0] > tmpStart){
                trackInd = i;
                break;
            }
            else{
                result.add(new int[]{intervals[i][0], intervals[i][1]});
            }
        }

        if (trackInd >= 0){
            for (int i = trackInd; i < intervals.length; i++){
                if (isOverlap(intervals[i][0], intervals[i][1], tmpStart, tmpEnd)){
                    tmpStart = Math.min(intervals[i][0], tmpStart);
                    tmpEnd = Math.max(intervals[i][1], tmpEnd);
                }
                else{
                    result.add(new int[]{tmpStart, tmpEnd});
                    tmpStart = intervals[i][0];
                    tmpEnd = intervals[i][1];
                }
            }
        }

        result.add(new int[]{tmpStart, tmpEnd});
        return result.toArray(new int[result.size()][2]);
    }

    private boolean isOverlap(int startA, int endA, int startB, int endB){
        return (endA >= startB && startA <= endB);
    }
}
