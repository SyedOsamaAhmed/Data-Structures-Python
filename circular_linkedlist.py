class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLL:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if (not self.head):
            self.head = new_node
            new_node.next = new_node

        else:
            curr_node = self.head
            while (curr_node.next != self.head):
                curr_node = curr_node.next

            curr_node.next = new_node
            new_node.next = self.head

    def insertAtStart(self, data):
        new_node = Node(data)

        if not self.head:
            new_node.next = new_node
            self.head = new_node

        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            self.head = new_node

    def insertAtIndex(self, index, data):
        new_node = Node(data)
        if (not self.head or index == 1):
            self.insertAtStart(data)

        elif index > self.length():
            print("position is greater than list length")
            return

        else:

            pos = 0
            temp = self.head.next

            while temp and pos < index - 1:
                pos = pos + 1
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

    def removeAtStart(self):
        if (not self.head):
            print("Circular linked list is empty")
            return

        elif self.head.next == self.head:
            self.head = None
            return
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next

    def removeAtIndex(self, index):
        if (not self.head):
            print("List is already empty!")
            return

        if index < 0:
            print("Invalid position")
            return

        elif index == 0:
            self.removeAtStart()

        else:
            temp = self.head
            pos = 0
            while (temp.next != self.head and pos != index):
                prev = temp
                temp = temp.next
                pos = pos + 1
            if index > pos:
                print("index out of range")
            prev.next = temp.next
            temp.next = None

    def length(self):
        if (not self.head):
            return 0
        else:
            curr = self.head
            count = 1
            while True:
                curr = curr.next
                if curr == self.head:
                    break

                count = count + 1

            return count

    def printCircularLL(self):
        if not self.head:
            print("circular linked list empty!")
            return
        curr_node = self.head

        while (True):
            print(curr_node.data)
            curr_node = curr_node.next
            if (curr_node == self.head):
                break


circularll = CircularLL()

circularll.append(1)
circularll.append(2)
circularll.append(3)
circularll.append(4)
circularll.append(5)
circularll.append(6)

circularll.insertAtIndex(4, 15)
circularll.printCircularLL()
