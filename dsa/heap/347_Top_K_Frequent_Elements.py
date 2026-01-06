from typing import Dict, Tuple, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsFreq: Dict[int, int] = {}
        result: List[int] = []
        maxHeap: MaxHeap = MaxHeap()

        for num in nums:
            numsFreq[num] = numsFreq.get(num, 0) + 1

        for key in numsFreq.keys():
            maxHeap.addNode((numsFreq.get(key), key))
        
        for _ in range(k):
            result.append(maxHeap.popNode()[1])

        return result


class MaxHeap:
    def __init__(self):
        self.nodes: List[int] = []
    
    def isValidInd(self, ind: int) -> bool:
        return 0 <= ind and ind < len(self.nodes)
    
    def getParInd(self, ind: int) -> int:
        return (ind-1)//2
    
    def getLeftChildInd(self, ind: int) -> int:
        return ind*2+1
    
    def getRightChildInd(self, ind: int) -> int:
        return ind*2+2
    
    def swap(self, firstInd: int, secondInd: int):
        if self.isValidInd(firstInd) and self.isValidInd(secondInd):
            self.nodes[firstInd], self.nodes[secondInd] = self.nodes[secondInd], self.nodes[firstInd]
        
    def heaptifyUp(self, ind: int):
        if not self.isValidInd(ind):
            return
        
        parInd: int = self.getParInd(ind)

        if self.isValidInd(parInd) and self.nodes[ind] > self.nodes[parInd]:
            self.swap(ind, parInd)
            self.heaptifyUp(parInd)
        
    def heaptifyDown(self, ind: int):
        if not self.isValidInd(ind):
            return
        
        leftChildInd: int = self.getLeftChildInd(ind)
        rightChildInd: int = self.getRightChildInd(ind)

        if not self.isValidInd(leftChildInd):
            return
        
        biggerChildInd: int = leftChildInd

        if self.isValidInd(rightChildInd) and self.nodes[biggerChildInd] < self.nodes[rightChildInd]:
            biggerChildInd = rightChildInd
        
        if self.nodes[ind] < self.nodes[biggerChildInd]:
            self.swap(ind, biggerChildInd)
            self.heaptifyDown(biggerChildInd)
    
    def popNode(self) -> Tuple[int]:
        node: Tuple[int] = None
        if self.nodes:
            self.swap(0, len(self.nodes)-1)
            node = self.nodes.pop()
            self.heaptifyDown(0)
        return node
    
    def addNode(self, node: Tuple[int]):
        self.nodes.append(node)
        self.heaptifyUp(len(self.nodes)-1)

