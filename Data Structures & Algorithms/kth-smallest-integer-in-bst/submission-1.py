# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []

        def dfs(node):
            if not node:
                return None

            res = dfs(node.left)
            if res is not None:
                return res

            vals.append(node.val)
            if len(vals) == k:
                return vals[-1]

            return dfs(node.right)

        return dfs(root)