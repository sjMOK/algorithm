class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def odd_even_list(head):
    odd_head = odd_tail = ListNode()
    even_head = even_tail = ListNode()

    is_odd = True
    while head:
        if is_odd:
            odd_tail.next = head
            odd_tail = head
            head = head.next
            odd_tail.next = None
        else:
            even_tail.next = head
            even_tail = head
            head = head.next
            even_tail.next = None

        is_odd = not is_odd

    odd_tail.next = even_head.next

    return odd_head.next
