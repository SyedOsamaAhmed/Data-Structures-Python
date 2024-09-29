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

    def removeAtBegin(self):
        if not self.head:
            print("List is empty!")
            return

        else:

            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None

    def removeAtEnd(self):
        if not self.head:
            print("List is empty!")

        curr_node = self.head
        previous = curr_node.prev

        while curr_node.next:
            previous = curr_node
            curr_node = curr_node.next

        previous.next = None
        curr_node.prev = None
        curr_node = None

    def calculateLength(self):
        if not self.head:
            return 0

        else:
            curr = self.head
            count = 1
            while curr.next:
                curr = curr.next
                count += 1
            return count

    def deleteAtIndex(self, index):
        if self.head is None:
            print("List is empty!")
            return

        elif (index == 1):
            self.removeAtBegin()

        elif index > self.calculateLength():
            print("index invalid!")
            return
        else:
            pos = 1
            curr = self.head
            previous_node = None
            next_node = None
            while curr and pos != index:
                pos = pos + 1
                previous_node = curr
                curr = curr.next
                next_node = curr.next

            previous_node.next = next_node
            if next_node:
                next_node.prev = previous_node
            curr.next = None
            curr.prev = None
            curr = None

    def print(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


doublyll = DoublyLL()
doublyll.append(1)
doublyll.append(2)
doublyll.append(3)
doublyll.append(4)
doublyll.append(5)
doublyll.deleteAtIndex(2)

doublyll.print()
