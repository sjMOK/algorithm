class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.front = 0
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.rear = self.next(self.rear)
        self.queue[self.rear] = value

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.queue[self.front] = None
        self.front = self.next(self.front)

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return (self.front == self.next(self.rear)) and self.queue[self.rear] is None

    def isFull(self) -> bool:
        return (self.front == self.next(self.rear)) and self.queue[self.rear] is not None

    def next(self, idx):
        return (idx + 1) % len(self.queue)
