from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = self.tail = ListNode(None)

    def append(self, node):
        self.tail.next = node
        self.tail = node


def merge_k_lists(lists):
    heap = []
    linked_list = LinkedList()
    for lst in lists:
        while lst:
            heappush(heap, lst.val)
            lst = lst.next

    while heap:
        linked_list.append(ListNode(heappop(heap)))

    return linked_list.head.next
