
from typing import List


class Heap:
    def __init__(self) -> None:
        self.items = []
        self.size = 0

    def __str__(self) -> str:
        return str(self.items)

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, first, second):
        self.items[first], self.items[second] = self.items[second], self.items[first]

    def _bubbleUp(self):
        i = self.size - 1
        while i > 0 and self.items[i] > self.items[self._parent(i)]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def insert(self, item):
        self.items.append(item)
        self.size += 1
        self._bubbleUp()

    def create(self, items: List):
        for item in items:
            self.insert(item)

    def _leftChildIndex(self, i):
        return (i * 2) + 1

    def _rightChildIndex(self, i):
        return (i * 2) + 2

    def _leftChild(self, index):
        return self.items[self._leftChildIndex(index)]

    def _rightChild(self, index):
        return self.items[self._rightChildIndex(index)]

    def _isValidParent(self, i):
        if not (self._hasLeftChild(i)):
            return True
        if not (self._hasRightChild(i)):
            return self.items[i] >= self._leftChild(i)
        return self.items[i] >= self._leftChild(i) and self.items[i] >= self._rightChild(i)

    def _hasLeftChild(self, index):
        return self._leftChildIndex(index) <= self.size

    def _hasRightChild(self, index):
        return self._rightChildIndex(index) <= self.size

    def _largerChildIndex(self, i):
        if not (self._hasLeftChild(i)):
            return i
        if not (self._hasRightChild(i)):
            return self._leftChildIndex(i)
        return self._leftChildIndex(i) if self._leftChild(i) > self._rightChild(i) else self._rightChildIndex(i)

    def remove(self):
        if self.size == 0:
            print("Empty Heap")
            return
        root = self.items[0]
        self.items[0] = self.items[self.size-1]
        self.size -= 1

        self._bubbleDown()
        return root

    def _bubbleDown(self):
        i = 0
        while (i <= self.size and not self._isValidParent(i)):
            largerChildIndex = self._largerChildIndex(i)
            self._swap(i, largerChildIndex)

    def max(self):
        if self.size == 0:
            return
        return self.items[0]

    def isEmpty(self):
        return self.size == 0


def main():
    heap = Heap()

    numbers = [10, 2, 5, 17, 4, 8, 9]
    heap.create(numbers)
    print(heap)

    for i in range(len(numbers)-1, -1, -1):
        numbers[i] = heap.remove()

    print(numbers)


if __name__ == "__main__":
    main()
