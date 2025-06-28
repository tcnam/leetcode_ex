package hash_table;
import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> valMap = new HashMap<Integer, Integer>();
        int[] result = new int[2];
        result[0] = -1;
        result[1] = -1;
        for (int i = 0; i < nums.length; i++){
            if (valMap.containsKey(target-nums[i]) == true){
                result[0] = valMap.get(target-nums[i]);
                result[1] = i;
                return result;
            }
            valMap.put(nums[i], i);
        }
        return result;
    }
}
