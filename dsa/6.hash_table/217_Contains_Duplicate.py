import typing as t

class Solution:
    def containsDuplicate(self, nums: t.List[int]) -> bool:
        return self.method1(nums)
        # return self.method2(nums)
    
    def method1(self, nums: t.List[int]) -> bool:
        unique_set: t.Set[int] = set(nums)
        return len(unique_set) != len(nums)
    
    def method2(self, nums: t.List[int]) -> bool:
        unique_set: t.Set[int] = set()
        for ind in range(0, len(nums), 1):
            if nums[ind] in unique_set:
                return True
            else:
                unique_set.add(nums[ind])
        
        return False