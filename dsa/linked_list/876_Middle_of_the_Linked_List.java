package linked_list;
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
class Solution {
    public ListNode middleNode(ListNode head) {
        // 2 first condition to check if listnode is null or listnode just contain 1 node
        // 2 pointer, one fast, one slow
        if (head == null){
            return null;
        }

        ListNode slowPointer = head;
        ListNode fastPointer = head;

        while (fastPointer.next != null){
            fastPointer = fastPointer.next.next;
            slowPointer = slowPointer.next;
            if (fastPointer == null){
                break;
            }
        }
        return slowPointer;
    }
}