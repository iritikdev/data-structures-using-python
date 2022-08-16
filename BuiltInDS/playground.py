from operator import contains


class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.leftchild = None
        self.rightchild = None
    def __str__(self) -> str:
        return f"Node{self.data}"
    def __repr__(self) -> str:
        return f"Node({self.data})"


class BinarySearchTree:
    
    root = Node()

    def insert(self, value):
        newNode = Node(value)
        # if tree is empty
        if self.root.data is None:
            self.root = newNode
            return
        current = self.root
        while current:
            if value == current.data:
                return
            if value < current.data:
                if current.leftchild == None:
                    current.leftchild = newNode
                    break
                current = current.leftchild
            else:
                if current.rightchild == None:
                    current.rightchild = newNode
                    break
                current = current.rightchild
    
    

tree = BinarySearchTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(1)
tree.insert(8)
tree.insert(12)
tree.insert(18)
tree.insert(17)
print("Done")