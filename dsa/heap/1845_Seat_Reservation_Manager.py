from typing import List, Optional
class SeatManager:

    def __init__(self, n: int):
        self.seats: List[int] = [
            i+1 for i in range(0, n, 1)
        ]
    
    def getLeftChildInd(self, parInd: int) -> int:
        return 2 * parInd + 1
    
    def getRightChildInd(self, parInd: int) -> int:
        return 2 * parInd + 2
    
    def getParInd(self, childInd: int) -> int:
        return (childInd - 1) // 2
    
    def checkValidInd(self, ind: int) -> bool:
        return ind >= 0 and ind < len(self.seats)

    def swap(self, firstInd: int, secondInd: int):
        tmpVal: int = self.seats[firstInd]
        self.seats[firstInd] = self.seats[secondInd]
        self.seats[secondInd] = tmpVal
    
    def heapfifyUp(self, childInd: Optional[int] = None):
        if not childInd:
            childInd: int = len(self.seats) - 1
        parInd: int = self.getParInd(childInd)
        if self.checkValidInd(parInd) and self.seats[childInd] < self.seats[parInd]:
            self.swap(childInd, parInd)
            self.heapfifyUp(parInd)
        
    def heaptifyDown(self, ind:Optional[int] = None):
        if not self.checkValidInd(ind):
            return
        
        leftChildInd: int = self.getLeftChildInd(ind)
        rightChildInd: int = self.getRightChildInd(ind)

        if not self.checkValidInd(leftChildInd):
            return
        
        smallerChildInd: int = leftChildInd
        
        if self.checkValidInd(rightChildInd) and self.seats[rightChildInd] < self.seats[leftChildInd]:
            smallerChildInd = rightChildInd
        
        if self.seats[ind] <= self.seats[smallerChildInd]:
            return
        else:
            self.swap(ind, smallerChildInd)
            self.heaptifyDown(smallerChildInd)        

    def reserve(self) -> int:
        if len(self.seats) != 0:
            self.swap(0, len(self.seats) - 1)
            minVal: int = self.seats.pop()
            self.heaptifyDown(0)
            return minVal

    def unreserve(self, seatNumber: int) -> None:
        self.seats.append(seatNumber)
        self.heapfifyUp()
    


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)