N = int(input())
W = []
for i in range(N):
    line = [int(x) for x in input().split()]
    W.append(line)

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
        A = []
        if self.root is None:
            return
        if vertex is 'AAA':
            vertex = self.root
        if vertex is None:
            return
        self.print(vertex.left)
        A.append(vertex.data)
        self.print(vertex.right)
        return(A)


tree = Tree()
#
#
A = tree.print()
# проверка на A == sorted(A)

# 3
# 30 1 -1
# 17 -1 1
# 23 -1 -1