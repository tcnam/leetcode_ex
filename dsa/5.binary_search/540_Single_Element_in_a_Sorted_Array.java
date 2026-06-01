package binary_search;

class Solution {
    public int singleNonDuplicate(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right){
            int mid = left + (right-left)/2;
            // System.out.printf("mid: %d, left: %d, right:%d\n", mid, left, right);
            int rightVal = -1;
            int leftVal = -1;
            
            if (mid + 1 < nums.length){
                rightVal = nums[mid+1];
            }

            if (mid - 1 >= 0){
                leftVal = nums[mid-1];
            }

            if (nums[mid] != leftVal & nums[mid] != rightVal){
                return nums[mid];
            }
            else {
                if ((mid % 2 == 0 & nums[mid] == rightVal & nums[mid] != leftVal) 
                    || (mid % 2 == 1 & nums[mid] == leftVal & nums[mid] != rightVal)){
                        left = mid + 1;
                    }
                else {
                    right = mid - 1;
                }
            }

        }
        return -1;
    }
}

