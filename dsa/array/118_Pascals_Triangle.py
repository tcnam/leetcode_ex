from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result: List[List[int]] = []
        for i in range (0, numRows, 1):
            result.append([])
            for j in range(0, i+1, 1):
                if j == 0 or j == i:
                    result[i].append(1)
                else:
                    if i > 1:
                        prevLeftVal: int = result[i-1][j-1] if j >= 0 else 0
                        prevRightVal: int = result[i-1][j]
                        result[i].append(prevLeftVal + prevRightVal)
        return result