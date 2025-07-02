package array;
class Solution {
    public int removeElement(int[] nums, int val) {
        int count = 0;
        int replaceInd = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] != val) {
                nums[replaceInd] = nums[i];
                replaceInd += 1;
                count += 1;
            }
        }
        return count;
    }
}
