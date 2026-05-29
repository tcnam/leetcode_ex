package sorting;

class Solution {
    public int heightChecker(int[] heights) {
        int[] countHeight = new int[101];
        for (int i = 0; i < heights.length; i++){
            countHeight[heights[i]] += 1;
        }
        
        for (int i = 1; i < countHeight.length; i++){
            countHeight[i] += countHeight[i-1];
        }
        // countHeight[0] = -1;

        int result = 0;
        for (int i = 0; i < heights.length; i++){
            int lowerInd = countHeight[heights[i]-1];
            int upperInd = countHeight[heights[i]];
            if (i  < lowerInd || i >= upperInd){
                result += 1;
            }
        }
        return result;

    }
}


