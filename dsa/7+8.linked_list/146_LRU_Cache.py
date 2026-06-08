import typing as t

class Node:
    def __init__(self, key: int, val: int):
        self.key: int = key
        self.val: int = val
        self.next: Node = None
        self.prev: Node = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cur_capacity: int = 0
        self.key_dict: t.Dict[int, Node] = {}
        self.head: Node = None
        self.tail: Node = None

    def get(self, key: int) -> int:
        node: Node = self.key_dict.get(key)
        if node:
            prev_node: Node = node.prev
            next_node: Node = node.next
            
            if not next_node and prev_node:
                self.tail = self.tail.prev
                self.tail.next = None
                node.prev = None
                
                node.next = self.head
                self.head.prev = node
                self.head = node
            
            if prev_node and next_node:
                prev_node.next = next_node
                next_node.prev = prev_node

                node.next = self.head
                node.prev = None
                self.head.prev = node
                self.head = node
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node: Node = self.key_dict.get(key)
        if node:
            node.val = value
            prev_node: Node = node.prev
            next_node: Node = node.next
            
            if not next_node and prev_node:
                self.tail = self.tail.prev
                self.tail.next = None
                node.prev = None
                
                node.next = self.head
                self.head.prev = node
                self.head = node
            
            if prev_node and next_node:
                prev_node.next = next_node
                next_node.prev = prev_node

                node.next = self.head
                node.prev = None
                self.head.prev = node
                self.head = node
        else:
            new_node: Node = Node(key, value)

            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

            if self.cur_capacity == self.capacity:
                self.key_dict.pop(self.tail.key)
                new_tail: Node = self.tail.prev
                new_tail.next = None
                self.tail.prev = None
                self.tail = new_tail
            else:
                self.cur_capacity += 1
            
            self.key_dict[key] = new_node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# [6,11] -> [3,17] -> (10: 13) 