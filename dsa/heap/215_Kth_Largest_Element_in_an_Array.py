from typing import List, Set
class MaxHeap:
    def __init__(self):
        self.nodes: List[int] = []
    
    def getLeftChildInd(self, ind: int) -> int:
        return ind * 2 + 1
    
    def getRightChildInd(self, ind:int) -> int:
        return ind * 2 + 2
    
    def getParInd(self, ind:int) -> int:
        return (ind-1)//2
    
    def isValidInd(self, ind:int) -> bool:
        return ind >= 0 and ind < len(self.nodes)
    
    def swap(self, firstInd: int, secondInd: int):
        tmpVal: int = self.nodes[firstInd]
        self.nodes[firstInd] = self.nodes[secondInd]
        self.nodes[secondInd] = tmpVal
    
    def heaptifyUp(self, ind):
        parInd: int = self.getParInd(ind)
        if not self.isValidInd(parInd):
            return
        if self.nodes[parInd] < self.nodes[ind]:
            self.swap(parInd, ind)
            self.heaptifyUp(parInd)
    
    def heaptifyDown(self, ind: int):
        if not self.isValidInd(ind):
            return 
        
        leftChildInd: int = self.getLeftChildInd(ind)
        rightChildInd: int = self.getRightChildInd(ind)

        if not self.isValidInd(leftChildInd):
            return 
        
        biggerChildInd: int = leftChildInd
        
        if self.isValidInd(rightChildInd) and self.nodes[rightChildInd] > self.nodes[leftChildInd]:
            biggerChildInd = rightChildInd
        
        if self.nodes[ind] > self.nodes[biggerChildInd]:
            return
        else:
            self.swap(ind, biggerChildInd)
            self.heaptifyDown(biggerChildInd)
    
    def addVal(self, val: int):
        self.nodes.append(val)
        self.heaptifyUp(len(self.nodes)-1)
    
    def popMaxVal(self) -> int:
        if len(self.nodes) != 0:
            self.swap(0, len(self.nodes) - 1)
            maxVal: int = self.nodes.pop()
            self.heaptifyDown(0)
            return maxVal

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap: MaxHeap = MaxHeap()
        maxVal: int = 0
        for num in nums:
            maxHeap.addVal(num)
        
        for i in range(0, k, 1):
            maxVal = maxHeap.popMaxVal()

        return maxVal
        