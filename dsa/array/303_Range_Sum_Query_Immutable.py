from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums
        self.accSum: List[int] = self.calAccSum()
    
    def calAccSum(self):
        result: List[int] = []
        sum: int = 0
        for num in self.nums:
            sum += num
            result.append(sum)
        return result

    def sumRange(self, left: int, right: int) -> int:
        leftSum: int = self.accSum[left-1] if left > 0 else 0
        return self.accSum[right] - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)