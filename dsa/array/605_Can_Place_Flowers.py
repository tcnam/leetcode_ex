from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count: int = 0
        for i in range(0, len(flowerbed), 1):
            leftInd: int = i - 1
            rightInd: int = i + 1
            emptyLeft: bool = True if leftInd < 0 or flowerbed[leftInd]==0 else False
            emptyRight: bool = True if rightInd >= len(flowerbed) or flowerbed[rightInd]==0 else False
            emptyCen: bool = True if flowerbed[i]==0 else False
            if emptyCen and emptyLeft and emptyRight:
                flowerbed[i] = 1
                count += 1
        return count >= n