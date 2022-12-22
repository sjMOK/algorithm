class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    cur, rev = head, None

    while cur:
        next = cur.next
        cur.next = rev
        rev = cur
        cur = next
