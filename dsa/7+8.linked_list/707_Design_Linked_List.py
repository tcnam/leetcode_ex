class Node:
    def __init__(self, val: int):
        self.val: int = val
        self.next: Node = None
        self.prev: Node = None
    
class MyLinkedList:

    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def get(self, index: int) -> int:
        pointer_node: Node = self.head
        for _ in range(0, index, 1):
            if not pointer_node:
                return -1
            pointer_node = pointer_node.next
        
        return pointer_node.val if pointer_node else -1


    def addAtHead(self, val: int) -> None:
        new_node: Node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node


    def addAtTail(self, val: int) -> None:
        new_node: Node = Node(val)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def addAtIndex(self, index: int, val: int) -> None:
        pointer_node: Node = self.head

        for ind in range(0, index, 1):
            if not pointer_node and ind < index:
                return
            pointer_node = pointer_node.next
        
        if not pointer_node:
            self.addAtTail(val)
            return
        
        prev_node: Node = pointer_node.prev
        if not prev_node:
            self.addAtHead(val)
            return
        
        new_node: Node = Node(val)
        prev_node.next = new_node
        new_node.prev = prev_node

        new_node.next = pointer_node
        pointer_node.prev = new_node


    def deleteAtIndex(self, index: int) -> None:
        pointer_node: Node = self.head

        for ind in range(0, index, 1):
            if not pointer_node and ind < index:
                return
            pointer_node = pointer_node.next
        
        if not pointer_node:
            return 
        
        if not pointer_node.prev:
            self.head = pointer_node.next
            if self.head: 
                self.head.prev = None
            pointer_node.next = None
            return
        
        if not pointer_node.next:
            self.tail = pointer_node.prev
            self.tail.next = None
            pointer_node.prev = None
            return
        
        next_node: Node = pointer_node.next
        prev_node: Node = pointer_node.prev

        prev_node.next = next_node
        next_node.prev = prev_node

        pointer_node.next = None
        pointer_node.prev = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)