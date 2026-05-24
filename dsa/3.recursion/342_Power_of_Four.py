class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        if n == 1 or n == 4:
            return True
        
        return (
            (n % 4 == 0)
            and (self.isPowerOfFour(int(n/4)))
        )
