import sys

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node({str(self.value)})"

class LinkedList:
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.size = 0

    def isEmpty(self):
        return self.first == None

    def addLast(self, item):
        """ Add item at last index """
        node = Node(item)

        if self.isEmpty():
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node 
        
        self.size += 1      

    def addFirst(self, item):
        """ Add item at first index """
        node = Node(item)
        
        if self.isEmpty():
            self.first = self.last = node
        else:
            node.next = self.first
            self.first = node

        self.size += 1

    def indexOf(self, item) -> int:
        index = 0
        current  = self.first
        while(current):
            if current.value == item:
                return index
            index += 1
            current = current.next
        return -1

    def contains(self, item) -> bool:
        """ Return True if LinkedList object contains item """
        current = self.first
        while current:
            if current.value == item:
                return True
            current = current.next
        return False

    def size(self):
        " Return lenght of linkedList "
        return self.size

    def __str__(self) -> str:
        result = '['
        current = self.first
        while(current):
            result += ('' if result == '[' else ", ") + str(current.value)
            current = current.next
        result += ']'
        return result
    
    def removeLast(self):
        # LinkedList is empty
        if self.isEmpty():
            raise ValueError
        
        # Have one element
        if self.first == self.last:
            self.first = self.last = None
            return

        current = self.first
        while current:
            if current.next == self.last:
                break
            current = current.next
        current.next = None
        self.last = current

        # decrement the size
        self.size -= 1

    def removeFirst(self):
        if self.isEmpty():
            raise ValueError

        if self.first == self.last:
            self.first = self.last = None
            return

        second = self.first.next
        self.first.next = None
        self.first = second

        self.size -= 1
        
    def toList(self):
        result = []
        current = self.first

        while current:
            result.append(current.value)
            current = current.next
        
        return result

    def reverse(self):
        self.last = self.first
        c1 = None
        c2 = None
        current = self.first

        while current != None:
            c1 = c2
            c2 = current
            current = current.next

            c2.next = c1
        self.first = c2
    
    def getFirst(self):
        if self.size == 0: return "empty"
        return self.first.value
    
    def getLast(self):
        if self.size == 0: return "empty"
        return self.last.value

    def getAt(self, index):
        counter = 0
        current = self.first
        if index < 0 or index >= self.size: return "Invalid index"
        while current:
            if counter == index: return current.value
            counter += 1
            current = current.next

    def sum(self):
        sum = 0
        current = self.first
        while current:
            sum += current.value
            current = current.next
        return sum

    def max(self):
        if self.isEmpty():
            return "List is empty"
        
        max = self.first.value
        current = self.first

        while current:
            if current.value > max:
                max = current.value
            current = current.next 
        
        return max

    def moveToHead(self, key):
        prev = None
        curr = self.first

        while curr:
            if key == curr.value:
                prev.next = curr.next
                curr.next = self.first
                self.first = curr
            prev = curr
            curr = curr.next

    def insert(self, index, item):
        node = Node(item)
        # O(1)
        if index == 0:
            node.next = self.first
            self.first = node
            return
        
        current = self.first

        for i in range(index-1):
            current = current.next

        node.next = current.next
        current.next = node




# Driver code
list = LinkedList()

list.addLast(10)
list.addLast(20)
list.addLast(30)

list.insert(1, 5)
print(list)