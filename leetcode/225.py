class MyStack:
    def __init__(self):
        self.queue = []
        self.tmp_queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        while len(self.queue) > 1:
            self.tmp_queue.append(self.queue.pop(0))
        
        ret = self.queue.pop()
        self.queue, self.tmp_queue = self.tmp_queue, self.queue

        return ret

    def top(self) -> int:
        while len(self.queue) > 1:
            self.tmp_queue.append(self.queue.pop(0))

        ret = self.queue.pop()
        self.tmp_queue.append(ret)
        self.queue, self.tmp_queue = self.tmp_queue, self.queue
        
        return ret

    def empty(self) -> bool:
        return not self.queue
