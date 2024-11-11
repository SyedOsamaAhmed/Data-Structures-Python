class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def PreOrder(node: Node):
    if node is None:
        return

    print(node.data, end=" ")

    PreOrder(node.left)
    PreOrder(node.right)


def PostOrder(node: Node):
    if node is None:
        return

    PostOrder(node.left)
    PostOrder(node.right)

    print(node.data, end=" ")


def InOrder(node: Node):
    if node is None:
        return

    InOrder(node.left)
    print(node.data, end=' ')
    InOrder(node.right)


root = Node(4)
n1 = Node(1)
n2 = Node(6)
n3 = Node(5)
n4 = Node(2)

root.left = n1
root.right = n2
n1.left = n3
n1.right = n4

# PreOrder(root)
# PostOrder(root)
InOrder(root)
