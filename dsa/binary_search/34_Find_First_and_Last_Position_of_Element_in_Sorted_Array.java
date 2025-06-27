package binary_search;

class Solution {
    public int[] searchRange(int[] nums, int target) {
        int leftLower = 0;
        int rightLower = nums.length - 1;

        int leftUpper = 0;
        int rightUpper = nums.length - 1;

        int leftResult = -1;
        int rightResult = -1;

        int[] result = new int[2];

        while (leftLower <= rightLower){
            int midLower = leftLower + (rightLower-leftLower)/2;
            if (nums[midLower] == target){
                if (midLower - 1 < 0){
                    leftResult = midLower;
                    break;
                }
                rightLower = midLower - 1;
            }
            else if (nums[midLower] < target){
                if (midLower + 1 < nums.length){
                    if (nums[midLower + 1] == target) {
                        leftResult = midLower + 1;
                        break;
                    }
                }
                leftLower = midLower + 1;
            }
            else{
                rightLower = midLower - 1;
            }
        }

        while (leftUpper <= rightUpper){
            int midUpper = leftUpper + (rightUpper-leftUpper)/2;
            if (nums[midUpper] == target){
                if (midUpper + 1 >= nums.length){
                    rightResult = midUpper;
                    break;
                }
                leftUpper = midUpper + 1;
            }
            else if(nums[midUpper] > target){
                if (midUpper - 1 >= 0){
                    if (nums[midUpper - 1] == target){
                        rightResult = midUpper - 1;
                        break;
                    }
                }
                rightUpper = midUpper - 1;
            }
            else {
                leftUpper = midUpper + 1;
            }
        }

        result[0] = leftResult;
        result[1] = rightResult;
        return result;
    }
}
