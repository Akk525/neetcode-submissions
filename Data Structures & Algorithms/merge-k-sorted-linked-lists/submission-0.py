# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeLists(list1, list2):
            dummy = node = ListNode()

            while list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                node = node.next

            node.next = list1 or list2

            return dummy.next
        
        n = len(lists)

        if n == 0:
            return None

        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = mergeLists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]
