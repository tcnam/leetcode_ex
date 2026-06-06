class Node {
    public int val;
    public Node next;

    public Node(int val){
        this.val = val;
        this.next = null;
    }
}
class MyLinkedList {
    Node head;
    int len;

    public MyLinkedList() {
        this.head = null;
        this.len = 0;
    }
    
    public int get(int index) {
        if (index >= this.len){
            return -1;
        }

        Node indNode = this.head;
        for (int i = 0; i < index; i++){
            indNode = indNode.next;
        }
        return indNode.val;
    }
    
    public void addAtHead(int val) {
        Node newNode = new Node(val);
        newNode.next = this.head;
        this.head = newNode;
        this.len += 1;
    }
    
    public void addAtTail(int val) {
        if (this.head == null){
            this.addAtHead(val);
        }
        else{
            Node newNode = new Node(val);
            Node indNode = this.head;
            while (indNode.next != null){
                indNode = indNode.next;
            }
            indNode.next = newNode;
            this.len += 1;
        }
        
    }
    
    public void addAtIndex(int index, int val) {
        if (index == 0){
            this.addAtHead(val);
            return;
        }

        if (index == this.len){
            this.addAtTail(val);
            return;
        }

        if (index > this.len){
            return;
        }

        Node newNode = new Node(val);
        Node indNode = this.head;

        for (int i = 0; i < index - 1; i++){
            indNode = indNode.next;
        }

        Node nextNode = indNode.next;
        indNode.next = newNode;
        newNode.next = nextNode;
        this.len += 1;
    }
    
    public void deleteAtIndex(int index) {
        if (index >= this.len){
            return;
        }

        if (index == 0){
            this.head = this.head.next;
            this.len -= 1;
            return;
        }

        Node indNode = this.head;
        for (int i = 0; i < index - 1; i++){
            indNode = indNode.next;
        }
        if (index == this.len - 1){
            indNode.next = null;
        }
        else {
            Node newNextNode = indNode.next.next;
            indNode.next = newNextNode;
        }
        this.len -= 1;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */