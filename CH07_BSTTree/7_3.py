class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(int(val))
        else:
            current = self.root
            while True:
                if int(val) < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(int(val))
                        break
                elif int(val) > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(int(val))
                        break
                else:
                    break
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def father(r, data):
    target = int(data)
    if r.data == target:
        return f"None Because {target} is Root"
    
    parent = None
    current = r
    
    while current:
        if target < current.data:
            parent = current
            current = current.left
        elif target > current.data:
            parent = current
            current = current.right
        else:
            return parent.data if parent else f"None Because {target} is Root"
    
    return "Not Found Data"

tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)

printTree90(tree.root)
print(father(tree.root, data[1]))