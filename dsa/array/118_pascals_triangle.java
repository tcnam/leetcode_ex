import java.util.*;

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>(numRows);

        for (int i = 0; i < numRows; i++){
            result.add(new ArrayList<>(i+1));
            for (int j = 0; j < i + 1; j ++) {
                if ( j == 0 || j == i || i == 0) {
                    result.get(i).add(1);
                }
                else{
                    result.get(i).add(result.get(i-1).get(j-1) + result.get(i-1).get(j));
                }
            }
        }
        return result;
    }
}