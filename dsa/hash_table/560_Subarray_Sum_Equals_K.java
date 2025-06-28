package hash_table;
import java.util.*;

class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> mapVal = new HashMap<Integer, Integer>();
        int cumSum = 0;
        int result = 0;

        for (int i = 0; i < nums.length; i++){
            cumSum += nums[i];
            if (cumSum == k){
                System.out.println(cumSum);
                result += 1;
            }

            if (mapVal.containsKey(cumSum - k) == true){
                result += mapVal.get(cumSum - k);
            }

            if(mapVal.containsKey(cumSum) == true){
                mapVal.replace(cumSum, mapVal.get(cumSum) + 1);
            }
            else{
                mapVal.put(cumSum, 1);
            }


        }
        return result;
    }
}
