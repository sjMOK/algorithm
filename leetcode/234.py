def is_palindrome(head):
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    while slow.val == rev.val:
        slow, rev = slow.next, rev.next
    
    return not rev
