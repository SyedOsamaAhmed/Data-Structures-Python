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

circularll.insertAtStart(20)
circularll.insertAtStart(30)
circularll.insertAtStart(50)

circularll.printCircularLL()
