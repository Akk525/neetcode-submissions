class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        first = head
        second = dummy

        while first and n > 0:
            first = first.next
            n -= 1
        
        while first:
            second = second.next
            first = first.next
        
        second.next = second.next.next

        return dummy.next