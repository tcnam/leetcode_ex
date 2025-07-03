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
    public ListNode reverseList(ListNode head) {
        if (head == null){
            return null;
        }

        if (head.next == null){
            return head;
        }
        ListNode prevNode = null;
        ListNode indNode = head;
        while (indNode != null){
            ListNode nextNode = indNode.next;
            indNode.next = prevNode;
            prevNode = indNode;
            indNode = nextNode;
        }
        return prevNode;
    }
}
