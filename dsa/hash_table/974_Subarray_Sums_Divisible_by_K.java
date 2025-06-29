package hash_table;
import java.util.*;

class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        Map<Integer, Integer> mapVal = new HashMap<Integer, Integer>();
        int result = 0;
        int sumRemainder = 0;

        for (int i = 0; i < nums.length; i++){
            // to calculate correctly remainder with negative number
            sumRemainder = ((sumRemainder + nums[i]) % k + k) %k;

            if(sumRemainder % k == 0){
                result += 1;
            }

            if (mapVal.containsKey(sumRemainder) == true){
                result += mapVal.get(sumRemainder);
                mapVal.replace(sumRemainder, mapVal.get(sumRemainder) + 1);
            }
            else{
                mapVal.put(sumRemainder, 1);
            }
        }
        return result;
    }
}
