#3. Swapping Nodes in a Linked List
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = self.getlength(head)
        if not head:
            return None

        back, current, front = None, head, None
        n = 1
        if k > length - k + 1:
            k  = length - k + 1

        while current:
            if n == k:
                swap1 = current

            if n == length - k + 1:
                current.val, swap1.val = swap1.val, current.val
                break

            n += 1
            current = current.next

        return head

    def getlength(self, head):
        current = head
        n = 0
        while current:
            n += 1
            current = current.next
        return n
