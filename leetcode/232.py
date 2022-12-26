class MyQueue:
    def __init__(self):
        self.stack = []
        self.tmp_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.move()
        return self.tmp_stack.pop()

    def peek(self) -> int:
        self.move()
        return self.tmp_stack[-1]

    def empty(self) -> bool:
        return not(self.stack or self.tmp_stack)

    def move(self):
        if not self.tmp_stack:
            while self.stack:
                self.tmp_stack.append(self.stack.pop())
