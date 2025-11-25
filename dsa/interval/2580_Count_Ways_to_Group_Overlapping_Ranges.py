from typing import List, Tuple
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        pairCount: int = 0
        ranges.sort(reverse=False, key=self.sortByStartAscEndDesc)
        curStart: int = ranges[0][0]
        curEnd: int = ranges[0][1]
        for ind, val in enumerate(ranges):
            if self.isOverlap(curStart, curEnd, val[0], val[1]):
                curStart = min(curStart, val[0])
                curEnd = max(curEnd, val[1])
            else:
                curStart = val[0]
                curEnd = val[1]
                pairCount += 1
        pairCount += 1
        result: int = pow(2, pairCount, 10**9 + 7)
        return pow(2, pairCount, 10**9 + 7)

    
    def isOverlap(self, startLeft:int, endLeft:int, startRight:int, endRight:int) -> bool:
        return endLeft >= startRight and startLeft <= endRight

    def sortByStartAscEndDesc(self, x:Tuple[int]) -> Tuple[int]:
        return (x[0], -x[1])