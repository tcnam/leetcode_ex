from typing import List, Tuple
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap: MinHeap = MinHeap()
        result: int = -1
        for row in matrix:
            for item in row:
                minHeap.addNode(item)
        for _ in range(0, k, 1):
            result = minHeap.popNode()
        return result
           
class MinHeap:
    def __init__(self):
        self.nodes: List[Tuple[int]] = []
    
    def isValidInd(self, ind: int) -> bool:
        return ind >= 0 and ind < len(self.nodes)
    
    def getParInd(self, ind: int) -> int:
        return (ind-1)//2
    
    def getLeftChildInd(self, ind: int) -> int:
        return ind*2+1
    
    def getRightChildInd(self, ind: int) -> int:
        return ind*2+2
    
    def swap(self, firstInd: int, secondInd: int) -> None:
        if self.isValidInd(firstInd) and self.isValidInd(secondInd):
            self.nodes[firstInd], self.nodes[secondInd] = self.nodes[secondInd], self.nodes[firstInd]
    
    def heaptifyUp(self, ind: int) -> None:
        if not self.isValidInd(ind):
            return
        parInd: int = self.getParInd(ind)
        if not self.isValidInd(parInd):
            return
        if self.nodes[ind] < self.nodes[parInd]:
            self.swap(ind, parInd)
            self.heaptifyUp(parInd)
    
    def heaptifyDown(self, ind: int) -> None:
        if not self.isValidInd(ind):
            return
        
        leftChildInd: int = self.getLeftChildInd(ind)
        rightChildInd: int = self.getRightChildInd(ind)

        if not self.isValidInd(leftChildInd):
            return
        
        smallerChildInd: int = leftChildInd

        if self.isValidInd(rightChildInd) and self.nodes[rightChildInd] < self.nodes[leftChildInd]:
            smallerChildInd = rightChildInd
        
        if self.nodes[smallerChildInd] < self.nodes[ind]:
            self.swap(smallerChildInd, ind)
            self.heaptifyDown(smallerChildInd)

    def addNode(self, node:int) -> None:
        self.nodes.append(node)
        self.heaptifyUp(len(self.nodes) - 1)

    def popNode(self) -> int:
        self.swap(0, len(self.nodes) - 1)
        node: int = self.nodes.pop()
        self.heaptifyDown(0)
        return node
    