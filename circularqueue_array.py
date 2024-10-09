class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.queue = [None for i in range(size)]

    def enqueue(self, data):

        if (self.rear + 1) % self.size == self.front:
            print("Queue is full!")

        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data

        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):

        if self.front == -1:
            print("Queue is empty!")
            return

        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp

        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def display(self):
        if self.front == -1:
            print("Queue is empty!")
            return

        elif self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])


circle = CircularQueue(5)
circle.enqueue(1)
circle.enqueue(11)
circle.enqueue(14)
circle.enqueue(15)
circle.enqueue(30)

circle.dequeue()
circle.dequeue()
circle.dequeue()
circle.dequeue()
circle.dequeue()
circle.display()
