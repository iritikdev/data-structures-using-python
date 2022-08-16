
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def add(self, item):
        node  = Node(item)

        if self.isEmpty():
            self.head = self.tail = node
        
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1
    
    def remove(self):

        if self.head == None:
            print("Queue underflow")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        
        second = self.head.next
        self.head = None
        self.head = second

        self.size -= 1
  
    def toArray(self):
        array = []
        current = self.head
        while current:
            array.append(current.data)
            current = current.next
        return array

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty.")
            return
        return self.head.data

    def length(self):
        print(self.size)
queue = QueueLinkedList()

queue.add(10)
queue.add(20)
queue.add(30)

queue.remove()

queue.add(40)


print(queue.toArray())

queue.length()