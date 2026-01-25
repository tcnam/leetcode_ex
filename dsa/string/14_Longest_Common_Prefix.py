from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result: str = ""
        refStr: str = strs[0]
        for ind in range (0, len(refStr), 1):
            count: int = 0
            for i in range(1, len(strs), 1):
                if ind >= len(strs[i]):
                    break
                if strs[i][ind] != refStr[ind]:
                    break
                count += 1
            if count < len(strs) - 1:
                break
            result += refStr[ind]
        return result

        