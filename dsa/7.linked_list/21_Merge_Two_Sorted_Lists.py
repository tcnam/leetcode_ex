import typing as t
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: t.Optional[ListNode], list2: t.Optional[ListNode]) -> t.Optional[ListNode]:
        pointer1: ListNode = list1
        pointer2: ListNode = list2

        pointer: ListNode = ListNode()
        result: ListNode = pointer

        while pointer1 and pointer2:
            if pointer1.val < pointer2.val:
                pointer.next = pointer1
                pointer1 = pointer1.next
            else:
                pointer.next = pointer2
                pointer2 = pointer2.next

            pointer = pointer.next
        
        while pointer1:
            pointer.next = pointer1
            pointer1 = pointer1.next
            pointer = pointer.next
        
        while pointer2:
            pointer.next = pointer2
            pointer2 = pointer2.next
            pointer = pointer.next
        
        return result.next
