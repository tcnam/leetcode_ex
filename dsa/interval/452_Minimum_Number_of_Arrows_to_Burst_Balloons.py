from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        result: int = 0
        points.sort(reverse=False, key=lambda x: x[0])
        startCur: int = points[0][0]
        endCur: int = points[0][1]
        for i in range(1, len(points), 1):
            if self.isOverlap(startCur, endCur, points[i][0], points[i][1]):
                startCur = max(startCur, points[i][0])
                endCur = min(endCur, points[i][1])
                continue
            result += 1
            startCur = points[i][0]
            endCur = points[i][1]
        return result + 1


    def isOverlap(self, startLeft:int, endLeft:int, startRight:int, endRight:int) -> bool:
        return endLeft >= startRight and startLeft <= endRight
        