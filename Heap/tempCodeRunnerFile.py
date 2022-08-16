
    for i in range(len(numbers)-1, -1, -1):
        numbers[i] = heap.remove()

    print(numbers)