from typing import Dict, List, Tuple
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        result: List[int] = [-1]*len(intervals)
        sortedStart: List[int] = sorted(
                [(ind, val[0]) for ind, val in enumerate(intervals)]
                , reverse=False
                , key=self.sortByVal)

        for i in range (0, len(intervals), 1):
            endVal: int = intervals[i][1]
            ind: int = self.binarySearchStartPoint(sortedStart=sortedStart, endVal=endVal)
            if ind >= 0 and ind < len(intervals):
                result[i] =  sortedStart[ind][0]

        return result
    
    def binarySearchStartPoint(self, sortedStart: List[int], endVal: int) -> int:
        leftInd: int = 0
        rightInd: int = len(sortedStart)
        while (leftInd < rightInd):
            midInd: int = leftInd + int((rightInd - leftInd)/2)
            if (sortedStart[midInd][1] >= endVal):
                rightInd = midInd
            else:
                leftInd = midInd + 1
        return leftInd
    
    def sortByVal(self, x:Tuple[int]) -> int:
        return x[1]