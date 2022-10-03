class Stack:
    def __init__(self) -> None:
        self.items = []
        self.minStack = []

    def __len__(self):
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)

    def push(self,item):
        self.minStack.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def peek(self):
        return self.items[-1]

   
        
def main():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(5)
    stack.pop()
    print(stack.min())

if __name__ == "__main__":
    main()