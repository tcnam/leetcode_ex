class Solution:
    def isPalindrome(self, s: str) -> bool:
        normStr: str = self.normalizeStr(s)
        leftInd: int = 0
        rightInd: int = len(normStr) - 1
        while leftInd < rightInd:
            if normStr[leftInd] != normStr[rightInd]:
                return False
            leftInd += 1
            rightInd -= 1
        return True

    def normalizeStr(self, s: str) -> str:
        lowerStr: str = str.lower(s)
        result: str = ""
        for char in lowerStr:
            if (ord(char) >= ord("a") and ord(char) <= ord("z")
                or ord(char) >= ord("0") and ord(char) <= ord("9")):
                result += char
        return result
        