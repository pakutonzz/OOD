class AVLTree:

    class AVLNode:

        def __init__(self, data, left=None, right=None):
            self.data = int(data)
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()

        def __str__(self):
            return str(self.data)

        def setHeight(self):
            a = self.getHeight(self.left)
            b = self.getHeight(self.right)
            self.height = 1 + max(a, b)
            return self.height

        def getHeight(self, node):
            return -1 if node is None else node.height

        def balanceValue(self):
            return self.getHeight(self.right) - self.getHeight(self.left)

    def __init__(self, root=None):
        self.root = None if root is None else root

    def add(self, data):
        self.root = self._add(self.root, data)

    def _add(self, root, data):
        if root is None:
            return AVLTree.AVLNode(data)
        if int(data) < root.data:
            root.left = self._add(root.left, data)
        else:
            root.right = self._add(root.right, data)

        root.setHeight()

        balance = root.balanceValue()

        if balance < -1:  
            if root.left.balanceValue() <= 0:
                return self.rotateRightChild(root)  
            else:
                root.left = self.rotateLeftChild(root.left)
                return self.rotateRightChild(root)  

        if balance > 1:  
            if root.right.balanceValue() >= 0:
                return self.rotateLeftChild(root)  
            else:
                root.right = self.rotateRightChild(root.right)
                return self.rotateLeftChild(root)

        return root

    def rotateLeftChild(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        root.setHeight()
        new_root.setHeight()
        return new_root

    def rotateRightChild(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        root.setHeight()
        new_root.setHeight()
        return new_root

    def postOrder(self):
        print('AVLTree post-order : ',end = '')
        self._postOrder(self.root)
        print()

    def _postOrder(self, root):
        if root is not None:
            self._postOrder(root.left)
            self._postOrder(root.right)
            print(root.data, end=' ')

    def printTree(self):
        self._printTree(self.root)
        print()

    def _printTree(self, node, level=0):
        if node is not None:
            self._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self._printTree(node.left, level + 1)


avl1 = AVLTree()
inp = input('Enter Input : ').split(',')

for i in inp:
    if i[:2] == "AD":
        avl1.add(i[3:])
    elif i[:2] == "PR":
        avl1.printTree()
    elif i[:2] == "PO":
        avl1.postOrder()
