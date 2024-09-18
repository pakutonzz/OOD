class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def append(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._append(self.root, data)

    def _append(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._append(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._append(node.right, data)

    def cut(self, data):
        self.root, removed = self._cut(self.root, data)
        if not removed:
            print("Not thing change")
        
    def _cut(self, node, data):
        if node is None:
            return node, False

        if node.data == data:
            if node.right:
                node.right = None
                return node, True
            elif node.left:
                node.left = None
                return node, True
            else:
                return node, False

        elif data < node.data:
            node.left, removed = self._cut(node.left, data)
        else:
            node.right, removed = self._cut(node.right, data)

        return node, removed

    def preorder(self, node, stop):
        if node:
            if node.data > stop:
                print(node.data, end=' ')
            else:
                print("".join(str(ord(char)) for char in node.data), end=' ')
            self.preorder(node.left, stop)
            self.preorder(node.right, stop)

    def inorder(self, node, stop):
        if node:
            self.inorder(node.left, stop)
            if node.data > stop:
                print(node.data, end=' ')
            else:
                print("".join(str(ord(char)) for char in node.data), end=' ')
            self.inorder(node.right, stop)

    def postorder(self, node, stop):
        if node:
            self.postorder(node.left, stop)
            self.postorder(node.right, stop)
            if node.data > stop:
                print(node.data, end=' ')
            else:
                print("".join(str(ord(char)) for char in node.data), end=' ')

    def printMirrorTree(self, node, level=0):
        if node is not None:
            self.printMirrorTree(node.left, level + 1)
            print('     ' * level, node)
            self.printMirrorTree(node.right, level + 1)

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
print("What is this a plum tree")
first, inp = input('Enter Input : ').split('/')

print("FIrst look of this plum tree")

first = first.split()
for i in first:
    T.append(i)
T.printTree(T.root)
print("********************************************")
inp = inp.split(',')
for i in inp:
    print(i)
    if i[:2] == "AP":
        T.append(i[3:])
        T.printTree(T.root)
    elif i[:2] == "CU":
        T.cut(i[3:])
        T.printTree(T.root)
    elif i[:2] == "CH":
        print('preorder  :', end=' ')
        T.preorder(T.root, i[3:])
        print('\ninorder   :', end=' ')
        T.inorder(T.root, i[3:])
        print('\npostorder :', end=' ')
        T.postorder(T.root, i[3:])
        print()
    elif i[:2] == "MI":
        T.printMirrorTree(T.root)
    print("********************************************")
print("the last result")
T.printTree(T.root)