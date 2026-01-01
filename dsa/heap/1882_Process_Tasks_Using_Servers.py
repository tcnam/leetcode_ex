from typing import List, Tuple, Dict

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        result: List[int] = []
        serverPool: ServerPool = ServerPool()

        for ind, val in enumerate(servers):
            serverPool.availServers.addNode((val, ind))
        
        curTime: int = 0
        taskInd: int = 0

        while taskInd < len(tasks):
            serverPool.freeServers(curTime)
            serInfoWrapper:  Tuple[bool, Tuple[int]] = serverPool.popServer(tasks[taskInd], curTime)
            status: bool = serInfoWrapper[0]
            serInfo: Tuple[int] = serInfoWrapper[1]
            if status:
                result.append(serInfo[1])
                taskInd += 1
                curTime += 1
            else:
                curTime = max(curTime, serInfo[0])

        return result

class ServerPool:
    def __init__(self):
        self.availServers: MinHeap = MinHeap()
        self.ocpServers: MinHeap = MinHeap()
    
    def popServer(self, procTime:int, curTime:int) -> Tuple[bool, Tuple[int]]:
        serInfo: Tuple[int] = self.availServers.popNode()
        if serInfo:
            freeTime: int = curTime + procTime
            serWeight: int = serInfo[0]
            self.ocpServers.addNode((freeTime, serInfo[0], serInfo[1]))
            return (True, serInfo)
        else:
            minSerInfo: Tuple[int] = self.ocpServers.nodes[0]
            return (False, minSerInfo)
    
    def freeServers(self, curTime):
        while self.ocpServers.nodes and self.ocpServers.nodes[0][0] <= curTime:
            freeNode: Tuple[int] = self.ocpServers.popNode()
            weight: int = freeNode[1]
            ind: int = freeNode[2]
            self.availServers.addNode((weight, ind))

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
        nodeInfo: Tuple[int] = ()
        if self.nodes:
            self.swap(0, len(self.nodes) - 1)
            nodeInfo: Tuple[int] = self.nodes.pop()
            self.heaptifyDown(0)
        return nodeInfo