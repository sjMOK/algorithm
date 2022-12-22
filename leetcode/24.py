class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head

    next = head.next
    head.next = next.next
    next.next = head

    head.next = swap_pairs(head.next)
    return next
