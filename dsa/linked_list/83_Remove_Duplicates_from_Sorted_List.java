package linked_list;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null){
            return null;
        }

        if (head.next == null){
            return head;
        }

        ListNode curNode = head.next;
        ListNode prevNode = head;
        while (curNode != null){
            ListNode surNode = curNode.next;
            if (curNode.val == prevNode.val){
                prevNode.next = surNode;
            }
            else{
                prevNode = curNode;
            }
            curNode = surNode;
        }
        return head;
    }
}
