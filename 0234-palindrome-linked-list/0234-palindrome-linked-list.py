class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        first = head
        second = prev

        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True