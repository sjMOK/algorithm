class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    out = tail = ListNode(0)
    num1, num2 = 0, 0
    pos = 1

    while l1:
        num1 += l1.val * pos
        l1 = l1.next
        pos *= 10

    pos = 1
    while l2:
        num2 += l2.val * pos
        l2 = l2.next
        pos *= 10

    sum = num1 + num2

    if sum == 0:
        return out

    while sum > 0:
        digit = sum % 10
        node = ListNode(digit)
        tail.next = node
        tail = node
        sum //= 10


    return out.next
