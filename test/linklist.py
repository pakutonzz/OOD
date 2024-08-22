class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList : 
    def __init__(self) -> None:
        self.head = Node(None) 

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next :
            cur = cur.next
        cur.next = new_node

    def insert(self, index, data):
        new_node = Node(data)
        cur = self.head
        for _ in range(index):
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node



    def isEmpty(self) :
        return self.head == None
    
