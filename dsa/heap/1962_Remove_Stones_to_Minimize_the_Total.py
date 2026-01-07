from typing import List
import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        return self.minStoneSumLib(piles, k)
    
    def minStoneSumLib(self, piles: List[int], k: int) -> int:
        result: int = 0
        negPiles: List[int] = [-val for val in piles]
        heapq.heapify(negPiles)

        for _ in range(0, k, 1):
            node: int = -heapq.heappop(negPiles)
            newNode: int = node - node//2
            heapq.heappush(negPiles, -newNode)
        
        for item in negPiles:
            result += -(item)

        return result
    
    def minStoneSumScratch(self, piles: List[int], k: int) -> int:
        result: int = 0
        maxHeap: MaxHeap = MaxHeap()

        for pile in piles:
            maxHeap.addNode(pile)

        for _ in range(0, k, 1):
            node: int = maxHeap.popNode()
            newNode: int = node - node//2
            maxHeap.addNode(newNode)

        for item in maxHeap.nodes:
            result += item

        return result
    

class MaxHeap:
    def __init__(self):
        self.nodes: List[int] = []
    
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
        
        if self.nodes[ind] > self.nodes[parInd]:
            self.swap(ind, parInd)
            self.heaptifyUp(parInd)
        
    def heaptifyDown(self, ind: int) -> None:
        if not self.isValidInd(ind):
            return

        leftChildInd: int = self.getLeftChildInd(ind)
        rightChildInd: int = self.getRightChildInd(ind)

        if not self.isValidInd(leftChildInd):
            return
        
        biggerChildInd: int = leftChildInd
        
        if self.isValidInd(rightChildInd) and self.nodes[rightChildInd] > self.nodes[biggerChildInd]:
            biggerChildInd = rightChildInd
        
        if self.nodes[biggerChildInd] > self.nodes[ind]:
            self.swap(ind, biggerChildInd)
            self.heaptifyDown(biggerChildInd)
    
    def popNode(self) -> int:
        node: int = None
        if self.nodes:
            self.swap(0, len(self.nodes)-1)
            node = self.nodes.pop()
            self.heaptifyDown(0)
        return node
    
    def addNode(self, node: int) -> None:
        self.nodes.append(node)
        self.heaptifyUp(len(self.nodes)-1)