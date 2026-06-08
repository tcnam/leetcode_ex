import typing as t
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> t.Optional[ListNode]:
        cur_node_a: ListNode = headA
        cur_node_b: ListNode = headB
        len_a: int = 0
        len_b: int = 0
        
        while cur_node_a:
            len_a += 1
            cur_node_a = cur_node_a.next
        
        while cur_node_b:
            len_b += 1
            cur_node_b = cur_node_b.next

        cur_node_a: ListNode = headA
        cur_node_b: ListNode = headB
        skip_ind: int = len_a - len_b

        if skip_ind >= 0:
            for ind in range(0, skip_ind, 1):
                cur_node_a = cur_node_a.next
        else:
            for ind in range(0, abs(skip_ind), 1):
                cur_node_b = cur_node_b.next
        
        while cur_node_a and cur_node_b:
            if cur_node_a == cur_node_b:
                return cur_node_a
            cur_node_a = cur_node_a.next
            cur_node_b = cur_node_b.next
        
        return None