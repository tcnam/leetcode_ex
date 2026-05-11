class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse_x: int = 0
        tmp: int = x
        while tmp > 0:
            remainder: int = tmp % 10
            reverse_x = reverse_x * 10 + remainder
            tmp = int(tmp/10)
        
        if x == reverse_x:
            return True
        else:
            return False
            
