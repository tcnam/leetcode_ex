package linked_list;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if (head == null){
            return null;
        }

        ListNode curNode = head;
        ListNode prevNode = null;

        while (curNode != null){
            ListNode surNode = curNode.next;
            if (curNode.val == val){
                if (prevNode != null){
                    prevNode.next = surNode;
                    curNode = prevNode;
                }
                else{
                    head = surNode;
                    curNode = null;
                }
            }
            prevNode = curNode;
            curNode = surNode;
        }
        return head;
    }
}
