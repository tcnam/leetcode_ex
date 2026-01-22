from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result: List[int] = []
        length: int = len(nums)
        leftProdNums: List[int] = [0]*length
        rightProdNums: List[int] = [0]*length
        leftProd: int = 1
        rightProd: int = 1
        for i in range(0, length, 1):
            leftProd = leftProd * nums[i]
            rightProd = rightProd * nums[length-1-i]
            leftProdNums[i] = leftProd
            rightProdNums[length-1-i] = rightProd
        
        for i in range(0, length, 1):
            leftVal: int = leftProdNums[i-1] if i - 1 >= 0 else 1
            rightVal: int = rightProdNums[i+1] if i + 1< length else 1
            result.append(leftVal*rightVal)
        
        return result
