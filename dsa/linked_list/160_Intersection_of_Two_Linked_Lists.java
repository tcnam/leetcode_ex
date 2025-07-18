package linked_list;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int lengthA = 0;
        int lengthB = 0;

        ListNode nodeA = headA;
        ListNode nodeB = headB;

        while (nodeA != null){
            lengthA += 1;
            nodeA = nodeA.next;
        }

        while (nodeB != null){
            lengthB += 1;
            nodeB = nodeB.next;
        }

        ListNode slowNode = null;
        ListNode fastNode = null;

        if (lengthA > lengthB){
            fastNode = headA;
            slowNode = headB;
        }else{
            fastNode = headB;
            slowNode = headA;
        }

        int count = 0;
        while (count < Math.abs(lengthA - lengthB)){
            fastNode = fastNode.next;
            count += 1;
        }

        while (fastNode != null && slowNode != null){
            if (fastNode == slowNode){
                return fastNode;
            }
            fastNode = fastNode.next;
            slowNode = slowNode.next;
        }
        return null;
    }
}
