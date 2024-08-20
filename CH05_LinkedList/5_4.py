class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)
    
class LinkedList:
    def __init__(self):
        self.head = Node(None)  
        self.tail = self.head

    def __str__(self):
        values = []
        current = self.head.next
        while current:
            values.append(current.data)
            current = current.next
        return ' '.join(values)

    def is_empty(self):
        return self.head.next is None
        
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.prev = self.head
            self.head.next = new_node
            self.tail = new_node

        else:
            current = self.head.next
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
         

    def insert_before_cursor(self, data):

        new_node = Node(data)
        current = self.head.next
        while current.data != '|':
            current = current.next

        if current.data == '|':
            new_node.next = current
            new_node.prev = current.prev
            if current == self.head.next:
                self.head.next = new_node
                current.prev = new_node
            else:
                current.prev.next = new_node
                current.prev = new_node

        # current.prev.next = new_node
        # new_node.prev = current
        # new_node.next = current
        

    def move_left(self):
        current = self.head.next
        while current.data != '|':
            current = current.next

        
        if current.prev == self.head:
            return
        temp_next = current.prev.prev.next
        temp_prev = current.prev.prev
        if current.prev:
            if current.prev.prev:
                current.prev.prev.next = current
            current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
            current.prev.prev = current
            current.next = temp_next
            current.prev = temp_prev

        
    
    def move_right(self):
        current = self.head.next
        while current.data != '|':
            current = current.next
        if current.next == None:
            return
        temp_next = current.next.next
        temp_prev = current.next
        if current.next:
            if current.next.next:
                current.next.next.prev = current
            current.next.next = current
            current.prev.next = current.next
            current.next.prev = current.prev
            current.next = temp_next
            current.prev = temp_prev


    def backspace(self):
        current = self.head.next
        while current.data != '|':
            current = current.next
        if current.prev == self.head:
            return
        temp_prev = current.prev.prev
        if current.prev:
            if current.prev.prev:
                current.prev.prev.next = current
            current.prev = temp_prev
            if current.prev:
                current.prev.next = current
            else:
                self.head.next = current

    def delete(self):
        current = self.head.next
        while current.data != '|':
            current = current.next
        if current.next == None:
            return
        temp_next = current.next.next
        if current.next:
            if current.next.next:
                current.next.next.prev = current
            current.next = temp_next
            if current.next:
                current.next.prev = current
            else:
                self.tail = current

    def process_commands(self, commands):
        for command in commands.split(','):
            parts = command.split()
            if parts[0] == 'I':
                self.insert_before_cursor(parts[1])
            elif parts[0] == 'L':
                self.move_left()
            elif parts[0] == 'R':
                self.move_right()
            elif parts[0] == 'B':
                self.backspace()
            elif parts[0] == 'D':
                self.delete()


Vim = LinkedList()
Vim.append('|')
input_str = input("Enter Input : ")
Vim.process_commands(input_str)
print(Vim)