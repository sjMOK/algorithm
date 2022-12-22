class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    head = tail = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            tail = list1
            list1 = list1.next
        else:
            tail.next = list2
            tail = list2
            list2 = list2.next

    if list1:
        tail.next = list1
    else:
        tail.next = list2

    return head.next
