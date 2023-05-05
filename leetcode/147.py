class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head):
        if not head.next:
            return head

        sorted_list = p = ListNode(0)
        
        while head:
            if head.val < p.val:
                p = sorted_list

            while p.next and head.val >= p.next.val:
                p = p.next

            p.next, head.next, head = head, p.next, head.next
            

        return sorted_list.next

            
        



from common import LinkedList
lst = LinkedList()
lst.add_by_list([-1,5,3,4,0])
result = Solution().insertionSortList(lst.head)

sorted_list = LinkedList()
sorted_list.add_by_linked_list(result)
print(sorted_list)