class Node:

    def __init__(self, data):
        self.next = None
        self.data = data


class Stack:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)

        if not new_node:
            print("Stack overflow!")
            return
        new_node.next = self.head
        self.head = new_node

    def peek(self):
        if not self.isEmpty():
            return self.head.data

        else:
            print("stack is empty!")
            return

    def pop(self):

        if (self.isEmpty()):
            print("underflow condition!")
        else:
            temp = self.head

            self.head = self.head.next
            del temp

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.print()
