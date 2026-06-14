# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            tmp = []
            for i in range(level_size):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    tmp.append(node.val)
            if tmp:
                res.append(tmp)
        return res