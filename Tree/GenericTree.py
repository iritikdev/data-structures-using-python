class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.children = []

def main():
    items = [10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80, 110, -1, 120, -1, -1, 90, -1, -1, 40, 100, -1, -1, -1]
    root = None

    st = list()
    for item in items:
        if len(st) > 0 and item == -1:
            st.pop()
        else:
            node = Node(item)
            if len(st) > 0:
                st[-1].children.append(node)
                st.append(node)
            else: root = node



if __name__ == '__main__':
    main()
    print("Done")