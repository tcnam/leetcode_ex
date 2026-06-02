package hash_table;
import java.util.*;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> setVal = new HashSet<Integer>();
        for (int i = 0; i<nums.length; i++){
            if(setVal.contains(nums[i])==true){
                return true;
            }
            else{
                setVal.add(nums[i]);
            }
        }
        return false;
    }
}
