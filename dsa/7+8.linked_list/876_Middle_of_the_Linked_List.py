import typing as t
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def middleNode(self, head: t.Optional[ListNode]) -> t.Optional[ListNode]:
        slow_pointer: ListNode = head
        fast_pointer: ListNode = head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        return slow_pointer