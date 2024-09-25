class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Node insertion at beginning:

    def insertNodeAtBegin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node
# Node insertion at specific index:

    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertNodeAtBegin(data)

        position = 0
        current_node = self.head
        while (current_node != None and position + 1 != index):
            position = position + 1
            current_node = current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

# Node insertion at end:

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while (current_node.next):
            current_node = current_node.next

        current_node.next = new_node

# node removal at beginning:

    def removeAtBegin(self):
        if (self.head is None):
            return

        self.head = self.head.next

# node removal at end:

    def removeAtEnd(self):
        if (self.head is None):
            return
        curr_node = self.head
        while (curr_node and curr_node.next != None):
            curr_node = curr_node.next

        curr_node.next = None


#node removal at given index:

    def removeNodeAt(self, index):
        if (self.head is None):
            return
        pos = 0
        if (index == 0):
            self.removeAtBegin()
        else:
            curr_node = self.head
            while curr_node and pos != index:
                pos = pos + 1
                prev = curr_node
                curr_node = curr_node.next
                next = curr_node.next

            prev.next = next
            curr_node = None

    def printLL(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next

llist = LinkedList()
llist.insertNodeAtBegin(10)
llist.insertAtEnd(20)
llist.insertAtEnd(30)
llist.insertAtEnd(40)
llist.insertAtEnd(50)
# llist.insertAtIndex(90, 2)
# llist.removeAtBegin()
# llist.removeAtEnd()

llist.removeNodeAt(2)
llist.printLL()
