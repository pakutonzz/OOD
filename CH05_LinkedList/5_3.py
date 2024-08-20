class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class LinkedList :
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
    def __str__(self) -> str:
        s = []
        cur = self.head
        while cur:
            if not cur.data :
                break
            s.append(cur.data)
            cur = cur.next
        return " -> ".join(s)
    def data(self):
        s = []
        cur = self.head.next
        while cur :
            if cur is self.tail :
                break
            s.append(cur.data)
            cur = cur.next
        return s
    
def merge_list():
    temp_listLinkedList = list_linkedlist[:]
    for linkedlist1 in temp_listLinkedList :
        for linkedlist2 in temp_listLinkedList:
            if linkedlist1 in list_linkedlist and linkedlist2 in list_linkedlist :
                if linkedlist1 is not linkedlist2 :
                    if linkedlist1.tail.data in linkedlist2.data() or linkedlist2.tail.data in linkedlist1.data() :
                        break
                    if linkedlist1.head.data == linkedlist2.tail.data : 
                        linkedlist2.tail.next = linkedlist1.head.next
                        linkedlist2.tail = linkedlist1.tail
                        if linkedlist1 in list_linkedlist :
                            list_linkedlist.remove(linkedlist1)
                    elif linkedlist2.head.data == linkedlist1.tail.data :
                        linkedlist1.tail.next = linkedlist2.head.next
                        linkedlist1.tail = linkedlist2.tail
                        if linkedlist2 in list_linkedlist :
                            list_linkedlist.remove(linkedlist2)

l1 = LinkedList()
list_linkedlist = [l1]
found = False
inp = input("Enter edges: ").split(",")

for section in inp :
    data_n1,data_n2 = section.split(">")
    n1 = Node(data_n1)
    n2 = Node(data_n2)
    n1.next = n2
    for linkedlist in  list_linkedlist :
        if not linkedlist.head :
            linkedlist.head = n1
            linkedlist.tail = n2
            break
        else :
            if n2.data in linkedlist.data() :
                continue
            if linkedlist.head.data == n2.data :
                n2.next = linkedlist.head.next
                linkedlist.head = n1
                break
            elif linkedlist.tail.data == n1.data :
                linkedlist.tail.next = n2
                linkedlist.tail = n2
                break
    else :
        l2 =LinkedList()
        l2.head = n1
        l2.tail = n2
        list_linkedlist.append(l2)
    merge_list()

dict_intersection_head = {}
dict_intersection_tail = {}
dict_intersection_size = {}
for linkedlist1 in list_linkedlist :
    for linkedlist2 in list_linkedlist[list_linkedlist.index(linkedlist1):]:
        if linkedlist1 is not linkedlist2 :
            cur_node = linkedlist1.head
            while cur_node :
                if cur_node.data == linkedlist2.tail.data :
                    dict_intersection_head.update({linkedlist2.head.data : linkedlist2})
                    dict_intersection_tail.update({cur_node.data : linkedlist2.tail})
                cur_node = cur_node.next


list_node_pass = []
found = False
for intersection_tail_name , intersection_tail_node in dict_intersection_tail.items() :
    for linkedlist in list_linkedlist :
        node_loop = linkedlist.head
        while node_loop :
            if node_loop.data == intersection_tail_name and node_loop is not intersection_tail_node:
                cur = node_loop
                list_node_pass = []
                found = False
                while cur :
                    list_node_pass.append(cur)
                    cur = cur.next
                for linkedlist2 in list_linkedlist :
                    if found and list_node_pass[-1].data != linkedlist2.head.data :
                        found = False
                    node_loop2 = linkedlist2.head
                    while node_loop2 :
                        if node_loop2.data == list_node_pass[-1].data and node_loop2 not in list_node_pass:
                            found =True
                        if node_loop2 in list_node_pass :
                            found = False
                            break
                        if found and node_loop2.data not in [i.data for i in list_node_pass]:
                            list_node_pass.append(node_loop2)
                        node_loop2 =  node_loop2.next
            node_loop = node_loop.next
    dict_intersection_size.update({intersection_tail_name : len(list_node_pass)})



for key, value in sorted(dict_intersection_size.items()) :
    print(f"Node({key}, size={value})")

found = False
temp_listLinkedlist = list_linkedlist[:]
for linked in temp_listLinkedlist :
    cur = linked.head
    while cur :
        for name, node in dict_intersection_tail.items():
            if cur is node:
                node.data = None
                found = True
            elif cur.data == name :
                cur.data = None
                l3 = LinkedList()
                l3.head = cur.next
                list_linkedlist.append(l3)
                found = True
        cur = cur.next
    if not found :
        list_linkedlist.remove(linked)

s = ",".join(list(map(str,list_linkedlist)))
s = s.replace(' -> ', " ")
s = s.split(",")
temp = []
data = []
max_length = 0
# print(s)
for result in s :
    if result :
        list_number = list(map(int,result.split(" ")))
        length = len(list_number)
        temp.append(list_number)
        if length > max_length :
            max_length = length
        

temp.sort()

for i in range(max_length):
    for list_number in temp :
        try :
            if list_number[i] not in data :
                data.append(list_number[i])
        except :
            continue
if len(data) > 0 :
    print("Delete intersection then swap merge:")
    print(" -> ".join(list(map(str,data))))
else :
    print("No intersection")