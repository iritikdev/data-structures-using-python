from Heap import Heap


class PriorityQueue:
    def __init__(self) -> None:
        self.heap = Heap()

    def __str__(self) -> str:
        return str(self.heap.items)

    def enqueue(self, item):
        self.heap.insert(item)

    def dequeue(self):
        return self.heap.remove()

    def isEmpty(self):
        return self.heap.isEmpty()


queue = PriorityQueue()
queue.enqueue(12)
queue.enqueue(5)
queue.enqueue(4)
queue.enqueue(80)
queue.enqueue(16)

print(queue)
print(queue.isEmpty())
