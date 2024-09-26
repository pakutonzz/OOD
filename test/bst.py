class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)
    
class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root,data)
        return self.root
    
    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left,data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right,data)

    def search(self, data):
        return self._search(self.root, data)
    
    def _search(self, node, data):
        if node is None:
            return False
        if node.data == data :
            return True
        if node.data > data :
            return self._search(node.right, data)
        else:
            return self._search(node.left, data)