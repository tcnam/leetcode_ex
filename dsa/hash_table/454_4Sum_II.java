package hash_table;
import java.util.*;

class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        Map<Integer, Integer> mapVal = new HashMap<Integer, Integer>();
        int result = 0;

        for (int i = 0; i < nums1.length; i++){
            for (int j = 0; j < nums2.length; j++){
                int tempSum = nums1[i] + nums2[j];
                if (mapVal.containsKey(tempSum) == true){
                    mapVal.replace(tempSum, mapVal.get(tempSum) + 1);
                }
                else{
                    mapVal.put(tempSum, 1);
                }
            }
        }

        for (int k = 0; k < nums3.length; k++){
            for (int l = 0; l < nums4.length; l++){
                int tempSum = -(nums3[k] + nums4[l]);
                if (mapVal.containsKey(tempSum) == true){
                    result += mapVal.get(tempSum);
                }
            }
        }
        return result;
    }
}
