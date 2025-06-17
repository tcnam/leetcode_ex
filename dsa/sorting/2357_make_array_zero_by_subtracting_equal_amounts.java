package sorting;

class Solution {
    public int minimumOperations(int[] nums) {
        int result = 0;
        int[] countVal = new int[101];
        int maxVal = 0;
        int culSub = 0;

        for (int i = 0; i < nums.length; i++ ){
            countVal[nums[i]] += 1;
            if (nums[i] > maxVal){
                maxVal = nums[i];
            }
        }
        while (maxVal > 0) {
            for (int i = 0; i < countVal.length; i++){
                if (countVal[i] > 0 && i > culSub){
                    int realSubVal = i - culSub;
                    maxVal = maxVal - realSubVal;
                    culSub += i - realSubVal;
                    countVal[i] -= 1;
                    result += 1;
                }
            }
        }
        return result;
    }
}
