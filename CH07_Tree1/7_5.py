class Queue:
    def __init__(self, q=None):
        # Use "is" for None comparison.
        if q is None:
            self.items = []
        else:
            self.items = q

    def enqueue(self, i):
        self.items.append(i)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return not self.items  # Simplify by checking if the list is empty.

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def add(self, data):
        self.root = BST._add(self.root, data)

    @staticmethod
    def _add(root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = BST._add(root.left, data)
        else:
            root.right = BST._add(root.right, data)
        return root

    def in_order(self):
        return BST._in_order(self.root)

    @staticmethod
    def _in_order(node, l=None, level=0):
        if l is None:
            l = []

        if node is None:
            return l
        l = BST._in_order(node.left, l, level + 1)
        l.append([node.data, level])
        l = BST._in_order(node.right, l, level + 1)
        return l

    def level_order(self):
        q = Queue()
        q.enqueue([self.root, 0, None])
        l = []
        while not q.is_empty():
            node, level, parent = q.dequeue()
            l.append([node.data, level, parent])
            if node.left is not None:
                q.enqueue([node.left, level + 1, node])
            if node.right is not None:
                q.enqueue([node.right, level + 1, node])
        return l


inp = [int(i) for i in input("Enter input: ").split()]

tree = BST()
for i in inp:
    tree.add(i)

in_order = tree.in_order()
level_order = tree.level_order()
q = Queue()
for node in level_order:
    q.enqueue(node)

level = 0
while not q.is_empty():
    prev_index = -1
    edge, line = "", ""
    edge_end = -1
    while q.peek()[1] == level:
        node = q.dequeue()
        search_node = node[:-1]
        index = in_order.index(search_node)
        parent_index = 0

        if node[2] is not None:
            parent_index = in_order.index([node[2].data, node[1] - 1])

        spaces = " " * len(" ".join([str(node[0]) for node in in_order[prev_index + 1: index]]))

        if index != 0:
            spaces += " "
        if prev_index != -1:
            spaces += " "

        if index < parent_index:
            edge_space = ""
            if prev_index == -1:
                edge_space = spaces + " " * len(str(in_order[index][0]))
            else:
                edge_space = " " * len(" ".join([str(node[0]) for node in in_order[edge_end + 1: index]])) + " " * len(
                    str(in_order[index][0]))
                edge_space += " " * 2
            edge += edge_space

            if parent_index - index > 1:
                edge += "_" * len(" ".join([str(node[0]) for node in in_order[index + 1: parent_index]]))
                edge += "_"
            edge += "/"
            edge += " " * len(str(in_order[parent_index][0]))
            edge_end = parent_index

        if index > parent_index:
            edge_space = ""
            if prev_index == -1:
                edge_space = " " * len(" ".join([str(node[0]) for node in in_order[:parent_index]]))
                if parent_index != 0:
                    edge_space += " "
                edge_space += " " * len(str(in_order[parent_index][0]))
            else:
                edge_space = " " * len(" ".join([str(node[0]) for node in in_order[edge_end + 1: parent_index]]))
                if parent_index - edge_end > 1:
                    edge_space += " " * 2
                    edge_space += " " * len(str(in_order[parent_index][0]))

            edge += edge_space
            edge += "\\"

            if index - parent_index > 1:
                edge += "_" * len(" ".join([str(node[0]) for node in in_order[parent_index + 1: index]]))
                edge += "_"

            edge += " " * len(str(in_order[index][0]))
            edge_end = index

        line += spaces
        line += str(node[0])
        prev_index = index

        if q.is_empty():
            break

    if node[2] is not None:
        print(edge)
    print(line)
    level += 1