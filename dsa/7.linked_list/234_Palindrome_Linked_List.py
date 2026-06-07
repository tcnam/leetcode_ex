import typing as t
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: t.Optional[ListNode]) -> bool:
        fast_pointer: ListNode = head
        slow_pointer: ListNode = head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        prev_pointer: ListNode = None
        while slow_pointer:
            next_pointer: ListNode = slow_pointer.next
            slow_pointer.next = prev_pointer
            prev_pointer = slow_pointer
            slow_pointer = next_pointer
        
        cur_pointer: ListNode = head
        
        while prev_pointer and cur_pointer:
            if prev_pointer.val != cur_pointer.val:
                return False
            prev_pointer = prev_pointer.next
            cur_pointer = cur_pointer.next
        
        return True
        
