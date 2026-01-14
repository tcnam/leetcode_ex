class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind: int = 0
        for num in nums:
            if num != val:
                nums[ind] = num
                ind += 1
        return ind