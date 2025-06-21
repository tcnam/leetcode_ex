package binary_search;

class Solution {
    public int arrangeCoins(int n) {
        int left = 1;
        int right = n;

        while (left <= right){
            int mid = left + (right-left)/2;
            if ((long) (mid + 1)*mid/2 == (long)n){
                return mid;
            }
            else if (((long) (mid + 1)*mid/2 > (long)n) & ((long) (mid + 1)*mid/2 - mid <= (long)n)){
                return mid - 1;
            }
            else if((long) (mid + 1)*mid/2 > (long)n){
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
        return -1;
    }
}
