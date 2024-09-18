class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.data)
    
class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
        return self.root
    
    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def find_below(self, node, value, result):
        if node is not None:
            self.find_below(node.left, value, result)
            if node.data < value:
                result.append(node.data)
            self.find_below(node.right, value, result)

    def get_below(self, value):
        result = []
        self.find_below(self.root, value, result)
        return result

inp = input("Enter Input : ")
v, t = inp.split('|')
v = list(map(int, v.split()))
t = int(t)

bst = BST()
for value in v:
    bst.insert(value)

bst.printTree(bst.root)

below = bst.get_below(t)
print("--------------------------------------------------")
if below:
    print(f"Below {t} : {' '.join(map(str, below))}")
else:
    print(f"Below {t} : Not have")
    