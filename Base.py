class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, data, vertex=None):
        if self.root is None:
            self.root = Node(data)
            return
        if vertex is None:
            vertex = self.root
        if vertex.data >= data:
            if vertex.left is None:
                vertex.left = Node(data)
                return
            else:
                self.add(data, vertex.left)
        if vertex.data < data:
            if vertex.right is None:
                vertex.right = Node(data)
                return
            else:
                self.add(data, vertex.right)

    def print(self, vertex= 'AAA'):
        if self.root is None:
            return
        if vertex is 'AAA':
            vertex = self.root
        if vertex is None:
            return
        self.print(vertex.left)
        print(vertex.data, end=' ')
        self.print(vertex.right)

tree = Tree()
Read = list(map(int, input().split()))
for x in Read:
    tree.add(x)
tree.print()