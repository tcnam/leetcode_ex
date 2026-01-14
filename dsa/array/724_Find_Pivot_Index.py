from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSumList: List[int] = [0]*len(nums)
        rightSumList: List[int] = [0]*len(nums)
        leftSumAcc: int = 0
        rightSumAcc: int = 0
        for ind in range(0, len(nums), 1):
            leftSumAcc += nums[ind]
            rightSumAcc += nums[len(nums)-1-ind]
            leftSumList[ind] = leftSumAcc
            rightSumList[len(nums)-1-ind] = rightSumAcc
        
        for ind in range(0, len(nums), 1):
            leftSum: int = leftSumList[ind-1] if ind-1>=0 and ind-1<len(nums) else 0
            rightSum: int = rightSumList[ind+1] if ind+1>=0 and ind+1<len(nums) else 0
            if leftSum == rightSum:
                return ind
        return -1