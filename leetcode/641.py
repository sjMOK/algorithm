class MyCircularDequeByArray:

    def __init__(self, k: int):
        self.deque = [None] * k
        self.maxlen = k
        self.n = 0
        self.front = 0
        self.rear = k - 1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.front = self._get_left_idx(self.front)
        self.deque[self.front] = value
        self.n += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.rear = self._get_right_idx(self.rear)
        self.deque[self.rear] = value
        self.n += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.deque[self.front] = None
        self.front = self._get_right_idx(self.front)
        self.n -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.deque[self.rear] = None
        self.rear = self._get_left_idx(self.rear)
        self.n -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.rear]

    def isEmpty(self) -> bool:
        return self.n == 0

    def isFull(self) -> bool:
        return self.n == self.maxlen

    def _get_left_idx(self, idx):
        return (idx - 1) % self.maxlen

    def _get_right_idx(self, idx):
        return (idx + 1) % self.maxlen


class DequeNode:
    def __init__(self, val=0):
        self.data = val
        self.left = None
        self.right = None


class MyCircularDequeByLinkedList:

    def __init__(self, k: int):
        self.max_len, self.cur_len = k, 0
        self.head, self.tail = DequeNode(val=None), DequeNode(val=None)
        self.head.right, self.tail.left = self.tail, self.head
    
    def _add(self, l_node, new):
        new.left, new.right = l_node, l_node.right
        l_node.right.left = l_node.right = new

    def _delete(self, node):
        node.right, node.right.left = node.right.right, node

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = DequeNode(val=value)
        self._add(self.head, new_node)
        self.cur_len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = DequeNode(val=value)
        self._add(self.tail.left, new_node)
        self.cur_len += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self._delete(self.head)
        self.cur_len -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self._delete(self.tail.left.left)
        self.cur_len -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.right.data

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.left.data

    def isEmpty(self) -> bool:
        return self.cur_len == 0

    def isFull(self) -> bool:
        return self.cur_len == self.max_len
