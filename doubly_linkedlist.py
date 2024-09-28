class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLL:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if (self.head is None):
            self.head = new_node

        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next

            curr.next = new_node
            new_node.prev = curr

    def insertAtBegin(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node

        else:
            curr = self.head
            new_node.next = curr
            curr.prev = new_node
            self.head = new_node

    def insertAtPos(self, data, pos):
        new_node = Node(data)
        if not self.head or pos == 1:
            self.insertAtBegin(data)
            return

        index = 0
        temp = self.head.next
        while temp.next and index < pos - 1:
            index = index + 1
            temp = temp.next

        if pos > index:
            print("position out of range")

        new_node.next = temp.next
        temp.next = new_node
        new_node.prev = temp

    def print(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


doublyll = DoublyLL()
doublyll.append(1)
doublyll.append(2)
doublyll.append(3)
doublyll.insertAtPos(12, 2)
doublyll.insertAtPos(14, 1)
doublyll.insertAtPos(15, 6)
doublyll.print()
