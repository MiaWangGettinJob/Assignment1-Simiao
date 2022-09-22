# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        current = head
        previous = None
        while current:
            if current.val == val:
                if current == head:
                    head = head.next
                    current = head
                else:
                    previous.next = current.next
                    current = previous.next
            else:
                previous = current
                current = current.next

        return head
