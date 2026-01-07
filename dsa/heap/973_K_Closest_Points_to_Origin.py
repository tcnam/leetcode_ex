from typing import List, Tuple

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result: List[List[int]] = []
        minHeap: MinHeap = MinHeap()
        for point in points:
            distance: int = pow(point[0], 2) + pow(point[1], 2)
            minHeap.addNode((distance, point[0], point[1]))
        
        for _ in range(0, k, 1):
            node: Tuple[int] = minHeap.popNode()
            result.append([node[1], node[2]])
        
        return result

class MinHeap:
    def __init__(self):
        self.nodes: List[Tuple[int]] = []
    
    def getLeftChildInd(self, ind:int) -> int:
        return ind*2 + 1
    
    def getRightChildInd(self, ind:int) -> int:
        return ind*2 + 2
    
    def getParInd(self, ind:int) -> int:
        return (ind-1)//2
    
    def isValidInd(self, ind:int) -> int:
        return ind >= 0 and ind < len(self.nodes)
    
    def swap(self, firstInd:int, secondInd:int):
        if self.isValidInd(firstInd) and self.isValidInd(secondInd):
            self.nodes[firstInd], self.nodes[secondInd] = self.nodes[secondInd], self.nodes[firstInd]
    
    def heapifyUp(self, ind:int):
        if not self.isValidInd(ind):
            return

        parInd: int = self.getParInd(ind)
        if not self.isValidInd(parInd):
            return

        if self.nodes[ind] < self.nodes[parInd]:
            self.swap(ind, parInd)
            self.heapifyUp(parInd)
    
    def heaptifyDown(self, ind:int):
        if not self.isValidInd(ind):
            return

        leftChildInd: int = self.getLeftChildInd(ind)
        rightChildInd: int = self.getRightChildInd(ind)

        if not self.isValidInd(leftChildInd):
            return
        
        smallerChildInd: int = leftChildInd

        if self.isValidInd(rightChildInd) and self.nodes[rightChildInd] <= self.nodes[leftChildInd]:
            smallerChildInd = rightChildInd
        
        if self.nodes[ind] > self.nodes[smallerChildInd]:
            self.swap(ind, smallerChildInd)
            self.heaptifyDown(smallerChildInd)
    
    def addNode(self, serInfo:Tuple[int]):
        self.nodes.append(serInfo)
        self.heapifyUp(len(self.nodes) - 1)
    
    def popNode(self) -> Tuple[int]:
        nodeInfo: Tuple[int] = None
        if self.nodes:
            self.swap(0, len(self.nodes) - 1)
            nodeInfo: Tuple[int] = self.nodes.pop()
            self.heaptifyDown(0)
        return nodeInfo