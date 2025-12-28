from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sortedTasks: List[int] = sorted(tasks, key = Solution.sortByFirstVal, reverse = False)
        curTime: int = 0
        result: List[int] = []
        minHeap: MinHeap = MinHeap()

        for ind, val in enumerate(sortedTasks):
            curQueueTime = val[0]
            task: Task = Task(ind, val[0], val[1])
            minHeap.addTask(task)
            if not lock and len(minHeap.nodes) > 0:
                lock = True
        
        while len(minHeap.nodes) > 0:
            result.append(minHeap.popTask().ind)
        
        return result

    def sortByFirstVal(x:List[int]) -> int:
        return x[0]

class Task:
    def __init__(self, ind: int, queueTime: int, procTime: int):
        self.ind: int = ind
        self.queueTime: int = queueTime
        self.procTime: int = procTime

class MinHeap:
    def __init__(self):
        self.nodes: List[Task] = []
    
    def getLeftChildInd(self, ind: int) -> int:
        return ind * 2 + 1
    
    def getRightChildInd(self, ind: int) -> int:
        return ind * 2 + 2
    
    def getParInd(self, ind: int) -> int:
        return (ind-1)//2
    
    def isValidInd(self, ind:int) -> bool:
        return ind >= 0 and ind < len(self.nodes)
    
    def swap(self, firstInd: int, secondInd):
        tmpVal: int = self.nodes[firstInd]
        self.nodes[firstInd] = self.nodes[secondInd]
        self.nodes[secondInd] = tmpVal
    
    def heaptifyUp(self, ind: int):
        parInd: int = self.getParInd(ind)
        if not self.isValidInd(parInd):
            return
        if self.nodes[parInd].procTime > self.nodes[ind].procTime:
            self.swap(parInd, ind)
            self.heaptifyUp(parInd)
    
    def heaptifyDown(self, ind:int):
        if not self.isValidInd(ind):
            return
        
        leftChildInd: int = self.getLeftChildInd(ind)
        rightChildInd: int = self.getRightChildInd(ind)

        if not self.isValidInd(leftChildInd):
            return
        
        smallerChildInd: int = leftChildInd

        if self.isValidInd(rightChildInd) and self.nodes[rightChildInd].procTime < self.nodes[leftChildInd].procTime:
            smallerChildInd = rightChildInd
        
        if self.nodes[ind].procTime > self.nodes[smallerChildInd].procTime:
            self.swap(ind, smallerChildInd)
            self.heaptifyDown(smallerChildInd)
    
    def addTask(self, task: Task):
        self.nodes.append(task)
        self.heaptifyUp(len(self.nodes) - 1)
    
    def popTask(self) -> int:
        self.swap(0, len(self.nodes) - 1)
        task: Task = self.nodes.pop(len(self.nodes) - 1)
        self.heaptifyDown(0)
        return task
