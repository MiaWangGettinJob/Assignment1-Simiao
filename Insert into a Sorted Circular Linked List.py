#5. Insert into a Sorted Circular Linked List
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        node = Node(insertVal, None)
        if not head:
            node.next = node
            return node

        previous, current = head, head.next

        while True:
            if previous.val <= insertVal <= current.val:
                previous.next = node
                node.next = current
                return head
            elif current.val < previous.val and (previous.val <= insertVal or insertVal <= current.val):
                previous.next = node
                node.next = current
                return head


            previous, current = current, current.next

            if previous == head:
                break

        previous.next = node
        node.next = current
        return head









