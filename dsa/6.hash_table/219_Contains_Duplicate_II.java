package hash_table;
import java.util.*;

class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> mapVal = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++){
            if (mapVal.containsKey(nums[i]) == true 
                && Math.abs(i - mapVal.get(nums[i])) <= k){
                    return true;
                }
            else {
                mapVal.put(nums[i], i);
            }
        }
        return false;
    }
}
