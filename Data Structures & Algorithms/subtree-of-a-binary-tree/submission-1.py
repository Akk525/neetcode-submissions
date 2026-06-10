class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return "#"
            
            return f",{node.val},{serialize(node.left)},{serialize(node.right)}"
        
        return serialize(subRoot) in serialize(root)