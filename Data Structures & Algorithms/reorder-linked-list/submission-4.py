# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find the center (Fast and slow pointer)
        # 2. Split the list into two halves (second half is slow.next)
        # 3. Reverse second half (two pointer approch)
        # 4. merge alternatively (merge with two pointer)

        if not head or not head.next:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        first = head
        tmp_node = slow.next
        slow.next = None


        prev = None
        while tmp_node:
            next_node = tmp_node.next
            tmp_node.next = prev
            prev = tmp_node
            tmp_node = next_node
        
        second = prev
        while second and first:
            next_node1 = first.next
            next_node2 = second.next
            first.next = second
            second.next = next_node1
            first = next_node1
            second = next_node2