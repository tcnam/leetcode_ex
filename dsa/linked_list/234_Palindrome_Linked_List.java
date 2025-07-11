package linked_list;

//  * Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode fastPointer = head;
        ListNode slowPointer = head;

        while (fastPointer != null && fastPointer.next != null){
            fastPointer = fastPointer.next.next;
            slowPointer = slowPointer.next;
        }

        ListNode prevNode = null;
        ListNode curNode = slowPointer;

        while (curNode != null){
            ListNode surNode = curNode.next;
            curNode.next = prevNode;
            prevNode = curNode;
            curNode = surNode;
        }

        ListNode rightNode = prevNode;
        ListNode leftNode = head;
        while (rightNode != null){
            if (rightNode.val != leftNode.val){
                return false;
            }
            rightNode = rightNode.next;
            leftNode = leftNode.next;
        }
        return true;
    }
}
