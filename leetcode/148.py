class Solution:
    def merge_two_lists(self, l1, l2):
        if l1.val < l2.val:
            sorted_list = cur = l1
            l1 = l1.next
        else:
            sorted_list = cur = l2
            l2 = l2.next

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next

        cur.next = l1 or l2
        return sorted_list

    def sortList(self, head):
        if head is None:
            return head
        elif head.next is None:
            return head

        half = slow = fast = head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next

        l1, l2 = head, slow
        half.next = None

        l1 = self.sortList(l1)
        l2 = self.sortList(l2)

        return self.merge_two_lists(l1, l2)
