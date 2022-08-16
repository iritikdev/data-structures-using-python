from Heap import Heap


class MaxHeap:
    @staticmethod
    def heapify(array):
        lastParentIndex = len(array) // 2 - 1
        for i in range(lastParentIndex, -1, -1):
            MaxHeap._heapify(array, i)

    @staticmethod
    def _heapify(array, index):
        largerIndex = index

        leftIndex = index * 2 + 1
        if leftIndex < len(array) and array[leftIndex] > array[largerIndex]:
            largerIndex = leftIndex

        rightIndex = index * 2 + 2
        if rightIndex < len(array) and array[rightIndex] > array[largerIndex]:
            largerIndex = rightIndex

        if index == largerIndex:
            return

        MaxHeap._swap(array, index, largerIndex)
        MaxHeap._heapify(array, largerIndex)

    def _swap(array, first, second):
        array[first], array[second] = array[second], array[first]

    @staticmethod
    def getKthLargest(array, k):
        if k < 1 or k > len(array):
            return
        heap = Heap()

        for item in array:
            heap.insert(item)

        for i in range(k-1):
            heap.remove()

        return heap.max()

    @staticmethod
    def isMaxHeap(array):
        pass


def main():
    numbers = [5, 3, 8, 4, 1, 2]
    print(MaxHeap.getKthLargest(numbers, 10))


if __name__ == "__main__":
    main()
