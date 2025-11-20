from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result: List[List[int]] = []
        firstInd: int = 0
        secondInd: int = 0
        firstListLen: int = len(firstList)
        secondListLen: int = len(secondList)
        while (firstInd < firstListLen and secondInd < secondListLen):
            startLeft: int = firstList[firstInd][0]
            endLeft: int = firstList[firstInd][1]
            startRight: int = secondList[secondInd][0]
            endRight: int = secondList[secondInd][1]
            if self.isOverlap(startLeft, endLeft, startRight, endRight):
                result.append([max(startLeft, startRight), min(endLeft, endRight)])
                
            if (endRight > endLeft):
                firstInd += 1
            else:
                secondInd += 1
        return result

    def isOverlap(self, startLeft: int, endLeft: int, startRight: int, endRight: int) -> bool:
        return endLeft >= startRight and startLeft <= endRight        