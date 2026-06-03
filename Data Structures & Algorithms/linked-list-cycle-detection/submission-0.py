# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        links = {}

        cur_node = head

        while cur_node:
            if cur_node not in links:
                links[cur_node] = cur_node.next
            else:
                return True
            cur_node = cur_node.next
        return False