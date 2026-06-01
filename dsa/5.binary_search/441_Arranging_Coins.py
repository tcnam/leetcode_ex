class Solution:
    def arrangeCoins(self, n: int) -> int:
        left: int = 0
        right: int = n
        while left <= right:
            mid: int = int((right - left) / 2) + left
            cur_sum_val: int = self.sum(mid)
            next_sum_val: int = self.sum(mid + 1)
            if n >= cur_sum_val and n < next_sum_val:
                return mid
            elif n < cur_sum_val:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1 
    
    def sum(self, n: int) -> int:
        return (n + 1) * n / 2