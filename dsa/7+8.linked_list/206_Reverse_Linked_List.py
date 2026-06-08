import typing as t
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: t.Optional[ListNode]) -> t.Optional[ListNode]:
        prev_node: ListNode = None
        pointer_node: ListNode = head

        while pointer_node:
            next_node: ListNode = pointer_node.next
            pointer_node.next = prev_node
            prev_node = pointer_node
            pointer_node = next_node
            
        return prev_node
        