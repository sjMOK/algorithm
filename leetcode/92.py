class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_between(head, left, right):
    root = prev = ListNode(None)
    root.next = head

    for _ in range(left - 1):
        prev = prev.next

    cur = prev.next
    for _ in  range(left, right):
        next = cur.next
        cur.next, next.next, prev.next = next.next, prev.next, next

    return root.next
