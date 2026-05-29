package sorting;
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int nums1Ind = m - 1;
        int nums2Ind = n - 1;
        int numsInd = m + n - 1;

        while (nums1Ind >= 0 && nums2Ind >= 0){
            if (nums2[nums2Ind] > nums1[nums1Ind]) {
                nums1[numsInd] = nums2[nums2Ind];
                nums2Ind -= 1;
            }
            else{
                nums1[numsInd] = nums1[nums1Ind];
                nums1Ind -= 1;
            }
            numsInd -= 1;
        }

        while (nums1Ind >= 0){
            nums1[numsInd] = nums1[nums1Ind];
            nums1Ind -= 1;  
            numsInd -= 1;         
        }

        while (nums2Ind >= 0){
            nums1[numsInd] = nums2[nums2Ind];
            nums2Ind -= 1; 
            numsInd -= 1;
        }
    }
}
