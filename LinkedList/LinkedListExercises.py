
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedListExercise: 
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self) -> str:
        result = '['
        current = self.head
        while(current):
            result += ('' if result == '[' else ", ") + str(current.data)
            current = current.next
        result += ']'
        return result

    def isEmpty(self):
        return self.size == 0

    def addLast(self, item):
        node = Node(item)

        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def InsertInSortedList(self, item):
        p1  = None
        curr = self.head
        node = Node(item)

        if item < self.head.data:
            node.next = self.head
            self.head = node
            return

        while curr and curr.data < item:
                p1 = curr
                curr = curr.next

        node.next = p1.next
        p1.next = node

    def isSorted(self):
        x = -32567
        current = self.head
        while current:
            if current.data < x: return False
            x = current.data
            current = current.next
        return True

    def removeDuplicates(self):
        prev = self.head
        curr = self.head.next

        while curr:
            if prev.data != curr.data:
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = prev.next

    def concat(self, list1, list2):
        pass

    def getKthFromTheEnd(self, k):
        if self.isEmpty():
            raise ValueError

        a = self.head       
        b = self.head

        for i in range(k-1):
            b = b.next
            if b == None: raise ValueError

        while b != self.tail:
            a = a.next
            b = b.next

        return a.data       

    def printMiddle(self):
        slow = self.head
        fast = self.head

        while fast != self.tail and fast.next != self.tail:
            slow = slow.next
            fast = fast.next.next
        if fast == self.tail:
            return slow.data
        else:
            return (slow.data, slow.next.data)
        


# Driver code======
list1 = LinkedListExercise()

list1.addLast(10)
list1.addLast(20)
list1.addLast(30)
list1.addLast(40)
list1.addLast(50)
list1.addLast(60)

print(list1.printMiddle())

        
