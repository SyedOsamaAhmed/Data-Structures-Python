class Queue:

    def __init__(self, capacity):
        self.front = 0
        self.rear = -1
        self.capacity = capacity
        self.queue = [None] * capacity

    def enqueue(self, data):
        if self.rear == self.capacity - 1:
            print("Queue is full")
            return

        self.rear += 1
        self.queue[self.rear] = data

    def dequeue(self):
        if self.front > self.rear:
            print("Queue is empty")
            return

        for i in range(self.rear):
            self.queue[i] = self.queue[i + 1]

        self.rear -= 1

    def frontElement(self):
        if self.rear == -1:
            print("Queue is empty")
            return

        print(f"{self.queue[self.front]}")

    def print(self):
        if self.front > self.rear:
            print("Queue is empty")

        for i in range(self.front, self.rear + 1):
            print(f"{self.queue[i]}")


myQueue = Queue(6)

myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(21)
myQueue.enqueue(81)
myQueue.enqueue(101)
myQueue.enqueue(181)

myQueue.dequeue()
myQueue.dequeue()

myQueue.print()

myQueue.frontElement()
