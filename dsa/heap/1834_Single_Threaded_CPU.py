from typing import List, Tuple

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(0, len(tasks), 1):
            tasks[i].append(i)

        sortedTasks: List[int] = sorted(tasks, key = Solution.sortByFirstVal, reverse = False)

        curTime: int = 0
        taskInd: int = 0

        result: List[int] = []
        minHeap: MinHeap = MinHeap()
        
        while taskInd < len(tasks) or minHeap.nodes:
            if not minHeap.nodes:
                curTime = max(curTime, sortedTasks[taskInd][0])
            
            while taskInd < len(tasks) and sortedTasks[taskInd][0] <= curTime:
                minHeap.addTask((sortedTasks[taskInd][1], sortedTasks[taskInd][2]))
                taskInd += 1
            
            procTime, ind = minHeap.popTask()
            result.append(ind)
            curTime += procTime
        
        return result

    def sortByFirstVal(x:List[int]) -> int:
        return x[0], x[2]


class MinHeap:
    def __init__(self):
        self.nodes: List[Tuple[int]] = []
    
    def getLeftChildInd(self, ind: int) -> int:
        return ind * 2 + 1
    
    def getRightChildInd(self, ind: int) -> int:
        return ind * 2 + 2
    
    def getParInd(self, ind: int) -> int:
        return (ind-1)//2
    
    def isValidInd(self, ind:int) -> bool:
        return ind >= 0 and ind < len(self.nodes)
    
    def swap(self, firstInd: int, secondInd):
        tmpVal: Tuple[int] = self.nodes[firstInd]
        self.nodes[firstInd] = self.nodes[secondInd]
        self.nodes[secondInd] = tmpVal
    
    def heaptifyUp(self, ind: int):
        parInd: int = self.getParInd(ind)
        if not self.isValidInd(parInd):
            return
        if self.nodes[parInd] > self.nodes[ind]:
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

        if self.isValidInd(rightChildInd) and self.nodes[rightChildInd] < self.nodes[leftChildInd]:
            smallerChildInd = rightChildInd
        
        if self.nodes[ind] > self.nodes[smallerChildInd]:
            self.swap(ind, smallerChildInd)
            self.heaptifyDown(smallerChildInd)
    
    def addTask(self, task: Tuple[int]):
        self.nodes.append(task)
        self.heaptifyUp(len(self.nodes) - 1)
    
    def popTask(self) -> int:
        self.swap(0, len(self.nodes) - 1)
        task: Task = self.nodes.pop(len(self.nodes) - 1)
        self.heaptifyDown(0)
        return task
