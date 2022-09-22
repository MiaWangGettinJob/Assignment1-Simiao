#4. Split Linked List in Parts
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """

        length = self.getlength(head)
        normalSize = length // k
        longpartNum = length % k
        result = [normalSize + 1] * longpartNum + [normalSize] * (k - longpartNum)
        current, previous = head, None
        for index, size in enumerate(result):
            newhead = current
            for i in range(size):
                previous = current
                current = current.next
            if previous:
                previous.next = None
            result[index] = newhead


        return result