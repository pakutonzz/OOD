class Node :
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = Node(None)
        self.size = 0
    
    def __str__(self):
        current = self.head.next
        if not current:
            return ""
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return "->".join(result)

    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.size += 1

    def insert(self, index, data):
        if index < 0 or index > self.size:
            print("Data cannot be added")
            return
        
        new_node = Node(data)
        current = self.head
        for _ in range(index):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1

        return 1

inp = input('Enter Input : ')
il, *o = inp.split(",")

n = il.split()

ll = LinkedList()

for element in n:
    ll.append(int(element))

if ll.isEmpty() :
    print("List is empty")
else :
    print(f"link list : {ll}")
    
for operation in o:
    index, data = map(int, operation.split(":"))
    if ll.insert(index, data) :
        print(f"index = {index} and data = {data}")
    if ll.isEmpty() :
        print("List is empty")
    else :
        print(f"link list : {ll}")