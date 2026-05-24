class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        remainder: int = n % k
        return remainder + self.sumBase(int(n/k), k) 
    

