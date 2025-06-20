package binary_search;

class Solution {
    public int guessNumber(int n) {
        int left = 1;
        int right = n;
        while (left <= right){
            int mid = left + (right-left)/2;
            int guessResult = guess(mid);

            if (guessResult == 0){
                return mid;
            }
            else if (guessResult == 1) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        return -1;
    }

    public int guess(int mid){
        // jsut sample
        return 0;
    }    
}