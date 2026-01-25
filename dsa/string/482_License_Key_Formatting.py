class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result: str = ""
        count: int = 0
        upperS: str = str.upper(s)
        for i in range(len(upperS) - 1, -1, -1):
            if self.isValAlphanumeric(upperS[i]):
                if count == k:
                    result += "-"
                    count = 0
                result += upperS[i]
                count+=1
        return result[::-1]
    
    def isValAlphanumeric(self, char: str) -> bool:
        return (ord(char) >= ord("A") 
                    and ord(char) <= ord("Z")
                or ord(char) >= ord("0")
                    and ord(char) <= ord("9"))
