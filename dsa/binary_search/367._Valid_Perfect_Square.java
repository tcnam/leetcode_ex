package binary_search;

class Solution {
    public boolean isPerfectSquare(int num) {
        int left = 1;
        int right = num;

        while (left <= right){
            int mid = left + (right-left)/2;
            if ((long) mid * mid == (long)num){
                return true;
            }
            else if ((long)mid * mid > (long)num){
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
        return false;
    }
}