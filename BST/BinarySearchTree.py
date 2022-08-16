from os import remove


class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return f"Node({str(self.data)})"
    def __repr__(self):
        return "Node(" + str(self.data) + ")"

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    def __repr__(self):
        return str("")

    def insert(self, value):
        node = Node(value)
        # if tree is empty
        if self.root is None:
            self.root = node
            return
        current = self.root
        while current:
            if value == current.data:
                return
            if value < current.data:
                if current.left == None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right == None:
                    current.right = node
                    break
                current = current.right

    def find(self, value):
        current = self.root
        while current is not None:
            if value < current.data:
                current = current.left
            elif value > current.data:
                current = current.right
            else:
                return True
        return False

    def preorder(self, root):
        if root is None:
            return
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    
    def inorder(self, root):
        if root is None: 
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)

    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")

    def isLeaf(self, root):
        return root.left is None and root.right is None

    def height(self,root):
        if root is None:
            return -1
        if self.isLeaf(root):
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def equals(self, first, second):
        if first is None and second is None:
            return True
        if first is not None and second is not None:
            return first.data == second.data and self.equals(first.left, second.left) and self.equals(first.right, second.right)
        return False

    def getNodesAtDistance(self, root, distance, items):
        if root is None:
            return
        if distance == 0:
            items.append(root.data)
            return
        self.getNodesAtDistance(root.left, distance-1, items)
        self.getNodesAtDistance(root.right, distance-1, items)
    
    def getNodesAtDistanceCall(self, i, root):
        items = []
        self.getNodesAtDistance(root, i, items)
        return items

    def traverseLevelOrder(self, root):
        for i in range(self.height(root)+1):
            for item in self.getNodesAtDistanceCall(i,root):
                print(item, end=" ")
            
    def leftView(self,root):
        for i in range(self.height(root)+1):
            items = self.getNodesAtDistanceCall(i,root)
            print(items[0])
   
    def rightView(self,root):
        for i in range(self.height(root)+1):
            items = self.getNodesAtDistanceCall(i,root)
            print(items[-1])

    def countLeaves(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left = self.countLeaves(root.left)
        right = self.countLeaves(root.right)
        
        return left + right

    def sumOfLeaves(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.data
        return self.sumOfLeaves(root.left) + self.sumOfLeaves(root.right)

    def sumRootToLeaf(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.data
        left  = self.sumOfLeaves(root.left)
        right  = self.sumOfLeaves(root.right)

        return left + right
        
    def size(self,root):
        if root is None:
            return 0
        left = self.size(root.left)
        right = self.size(root.right)

        return left + right + 1

    def insertNode(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node
            return
        current = self.root
        while True:
            if val < current.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            elif val > current.data:
                if current.right is None:
                    current.right = node
                    break
                current = current.right
            elif val == current.data:
                return

    def remove(self, data):
        current = self.root
        if current is None:
            return None
        if data < current.data:
            current.left = remove(current.left, data)
        elif data > current.data:
            current.right = remove(current.right, data)
        else:
            if current.left is not None and current is not None:
                lmax = self.maximum(current.left)
                current.data = lmax
            elif current.left is not None:
                return current.left
            elif current.right is not None:
                return current.right
            else:
                return None 
    
    def iterativePreorder(self):
        preoder = []
        if self.root is None:
            return preoder

        stack = list()
        stack.append(self.root)

        while len(stack) != 0:
            node = stack.pop()
            preoder.append(node.data)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return preoder

    def iterativeInorder(self):
        current = self.root
        items = []
        stack = []
        
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                if len(stack) == 0: break
                current = stack.pop()
                items.append(current.data)
                current = current.right

        return items

    def ceil(self,value):
        current = self.root
        ceil = -1
        while current is not None:
            if value == current.data:
                ceil = value
                return ceil
            if value > current.data:
                current = current.right
            else:
                ceil = current.data
                current = current.left
        return ceil

    def leftMostElement(self,root):

        if root.left is None and root.right is None:
            return root.data

        left = self.leftMostElement(root.left)

        print(left)

        items = []
        items.e




# Driver Code
def main():
    

    tree = BinarySearchTree()

    tree.insertNode(7)
    tree.insertNode(4)
    tree.insertNode(9)
    tree.insertNode(5)
    tree.insertNode(10)
    tree.insertNode(11)
    

    print(tree.leftMostElement(tree.root))

if __name__ == '__main__':
    main()
    print("\nDone")