
#1. Rotate List
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head

        length = self.getlength(head)
        if k == 0 or k % length == 0:
            return head

        current = head
        # if k > length
        if k > length:
            k = k % length

        # find the new head of new list
        for i in range(length - k - 1):
            current = current.next

        newhead = current.next
        End = current

        while current.next:
            current = current.next

        current.next = head
        End.next = None

        return newhead

    def getlength(self, head):

        current = head
        n = 0
        while current:
            n += 1
            current = current.next
        return n



