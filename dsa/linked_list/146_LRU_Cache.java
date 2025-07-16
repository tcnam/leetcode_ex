package linked_list;

import java.util.*;

class Node {
    int key;
    int value;
    Node prev;
    Node next;

    public Node (int key, int value){
        this.key = key;
        this.value = value;
        this.prev = null;
        this.next = null;
    }

    public Node (int key, int value, Node prev, Node next){
        this.key = key;
        this.value = value;
        this.prev = prev;
        this.next = next;
    }
}

class DoubleLinkedList {
    Node head;
    Node tail;

    public DoubleLinkedList (){
        this.head = null;
        this.tail = null;
    }

    public DoubleLinkedList (Node newNode){
        this.head = newNode;
        this.tail = newNode;
    }
}

class LRUCache {

    DoubleLinkedList ll;
    Map<Integer, Node> map;
    int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.ll = new DoubleLinkedList();
        this.map = new HashMap<Integer, Node>();
    }

    private void llInterate(){
        Node indNode = this.ll.head;
        System.out.printf("LinkedList value: \n");
        while (indNode != null){
            System.out.printf("(%d, %d) ->", indNode.key, indNode.value);
            indNode = indNode.next;
        }
        System.out.printf("\n");
    }
    
    public int get(int key) {
        // System.out.printf("hashmap when geting key: %d\n", key);
        // for (Integer k : this.map.keySet()) {
        //     System.out.printf("Key: %d, value: %d\n", k, this.map.get(k).value);
        // }

        if (this.map.containsKey(key) == true){
            Node tempNode = this.map.get(key);
            Node nextNode = tempNode.next;
            Node prevNode = tempNode.prev;

            if (prevNode != null && nextNode != null){
                prevNode.next = nextNode;
                nextNode.prev = prevNode;
            }
            // else if (prevNode != null && nextNode == null) {
                
            // }
            else if (prevNode == null && nextNode != null){
                nextNode.prev = null;
                this.ll.head = nextNode;
            }
            else{
                // System.out.printf("hashmap value: %d\n", tempNode.value);
                return tempNode.value;
            }
            this.ll.tail.next = tempNode;
            tempNode.prev = this.ll.tail;
            tempNode.next = null;
            this.ll.tail = tempNode;
            // System.out.printf("hashmap value: %d\n", tempNode.value);
            return tempNode.value;

        }else{
            // System.out.printf("hashmap value: %d\n", -1);
            return -1;
        }
    }
    
    public void put(int key, int value) {
        // System.out.printf("hashmap after inserting key: %d, value: %d \n", key, value);

        if (this.map.containsKey(key) == true){
            Node tempNode = this.map.get(key);
            tempNode.value = value;

            Node nextNode = tempNode.next;
            Node prevNode = tempNode.prev;
            // for (Integer k : this.map.keySet()) {
            //     System.out.printf("Key: %d, value: %d\n", k, this.map.get(k).value);
            // }
            
            
            if (prevNode != null && nextNode != null){
                prevNode.next = nextNode;
                nextNode.prev = prevNode;
            }
            // else if (prevNode != null && nextNode == null) {
                
            // }
            else if (prevNode == null && nextNode != null){
                nextNode.prev = null;
                this.ll.head = nextNode;
            }
            else{
                return;
            }
            this.ll.tail.next = tempNode;
            tempNode.prev = this.ll.tail;
            tempNode.next = null;
            this.ll.tail = tempNode;
            // this.llInterate();
            
        }
        else{
            Node newNode = new Node(key, value);
            if (this.map.size() == this.capacity){
                this.map.remove(this.ll.head.key); 
                this.ll.head = this.ll.head.next;
                if (this.ll.head != null){
                    this.ll.head.prev = null;
                }
                               
            }
            this.map.put(key, newNode);

            if (this.map.size() == 1 ){
                this.ll.head = newNode;
                this.ll.tail = newNode;
            }
            else{
                this.ll.tail.next = newNode;
                newNode.prev = this.ll.tail;
                newNode.next = null;
                this.ll.tail = newNode;
            }
            // this.llInterate();
            // for (Integer k : this.map.keySet()) {
            //     System.out.printf("Key: %d, value: %d\n", k, this.map.get(k).value);
            // }

        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
