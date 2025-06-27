package binary_search;

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int left = 0;
        int right = matrix.length * matrix[0].length - 1;

        while(left <= right){
            int mid = left + (right - left)/2;
            int rowInd = mid / matrix[0].length;
            int colInd = mid % matrix[0].length;

            if (matrix[rowInd][colInd] == target){
                return true;
            }else if (matrix[rowInd][colInd] > target){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return false;
    }
}
