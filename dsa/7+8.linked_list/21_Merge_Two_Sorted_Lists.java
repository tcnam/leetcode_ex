package linked_list;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode ind1 = list1;
        ListNode ind2 = list2;

        ListNode list = new ListNode(0);
        ListNode ind = list;

        while (ind1 != null & ind2 != null){
            if (ind1.val > ind2.val){
                ind.next = new ListNode(ind2.val);
                ind2 = ind2.next;
            }
            else {
                ind.next = new ListNode(ind1.val);
                ind1 = ind1.next;
            }
            ind = ind.next;
        }

        while (ind1 != null){
            ind.next = new ListNode(ind1.val);
            ind1 = ind1.next;
            ind = ind.next;
        }

        while (ind2 != null){
            ind.next = new ListNode(ind2.val);
            ind2 = ind2.next;
            ind = ind.next;
        }
        return list.next;
    }
}
