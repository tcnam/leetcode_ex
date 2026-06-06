import typing as t
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: t.Optional[ListNode], val: int) -> t.Optional[ListNode]:
        prev_node: ListNode = None
        pointer_node: ListNode = head
        while pointer_node:
            next_node = pointer_node.next
            if pointer_node.val == val:
                if prev_node:
                    prev_node.next = next_node
                else:
                    pointer_node.next = None
                    head = next_node
            else:
                prev_node = pointer_node
            pointer_node = next_node
        

        return head