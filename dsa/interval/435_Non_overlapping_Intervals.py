from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result: int = 0
        intervals.sort(reverse=False, key=lambda x: x[0])
        startCur: int = intervals[0][0]
        endCur: int = intervals[0][1]
        for i in range(1, len(intervals), 1):
            if self.isOverlap(startCur, endCur, intervals[i][0], intervals[i][1]):
                result += 1
                if (endCur < intervals[i][1]):
                    continue
            startCur = intervals[i][0]
            endCur = intervals[i][1]
        return result
    
    def isOverlap(self, startLeft: int, endLeft: int, startRight: int, endRight: int) -> bool:
        return endLeft > startRight and startLeft < endRight