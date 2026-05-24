class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        result: str = self.convertHelper(abs(num))
        if num > 0:
            return result
        else:
            return "-" + result
    
    def convertHelper(self, num: int) -> str:
        if num == 0:
            return ""
        
        remainder: int = num % 7
        return self.convertHelper(int(num / 7)) + str(remainder)