import typing as t

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        final_str: str = self.constructCurrStr(n)
        return final_str[k-1]
    
    def constructCurrStr(self, n: int) -> str:
        if n == 1:
            return "0"
        
        curr_str: str = self.constructNextStr(
            self.constructCurrStr(n - 1)
        )
        
        return curr_str
    
    def constructNextStr(self, s: str) -> str:
        reverse_str: str = ""
        for ind in range(len(s) - 1, -1, -1):
            if s[ind] == "0":
                reverse_str += "1"
            else:
                reverse_str += "0"
        return s + "1" + reverse_str
