from typing import List
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        result: int = len(intervals)
        intervals.sort(reverse=False, key = lambda x: (x[0], -x[1]))
        startCur: int = intervals[0][0]
        endCur: int = intervals[0][1]
        for i in range(1, len(intervals), 1):
            if self.isContain(startCur, endCur, intervals[i][0], intervals[i][1]):
                result -= 1
                continue
            startCur = intervals[i][0]
            endCur = intervals[i][1]
        return result
            
    
    def isContain(self, startLeft: int, endLeft: int, startRight: int, endRight: int) -> bool:
        return startLeft <= startRight and endLeft >= endRight