from typing import List, Set

class SmallestInfiniteSet:

    def __init__(self):
        self.nodes: List[int] = [i for i in range(1, 1001, 1)]
        self.existSet: Set[int] = set([i for i in range(1, 1001, 1)])
    
    def isValidInd(self, ind: int) -> bool:
        return ind >= 0 and ind < len(self.nodes)
    
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

        if not self.isValidInd(parInd):
            return
        
        if self.nodes[ind] < self.nodes[parInd]:
            self.swap(ind, parInd)
            self.heaptifyUp(parInd)
    
    def heaptifyDown(self, ind: int):
        if not self.isValidInd(ind):
            return
        
        leftChildInd: int = self.getLeftChildInd(ind)
        rightChildInd: int = self.getRightChildInd(ind)

        if not self.isValidInd(leftChildInd):
            return
        
        smallerChildInd: int = leftChildInd
        if self.isValidInd(rightChildInd) and self.nodes[smallerChildInd] > self.nodes[rightChildInd]:
            smallerChildInd = rightChildInd
        
        if self.nodes[ind] > self.nodes[smallerChildInd]:
            self.swap(ind, smallerChildInd)
            self.heaptifyDown(smallerChildInd)


    def popSmallest(self) -> int:
        node: int = None
        if self.nodes:
            self.swap(0, len(self.nodes) - 1)
            node = self.nodes.pop()
            self.existSet.remove(node)
            self.heaptifyDown(0)
        return node

    def addBack(self, num: int) -> None:
        if num not in self.existSet:
            self.existSet.add(num)
            self.nodes.append(num)
            self.heaptifyUp(len(self.nodes)-1)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)