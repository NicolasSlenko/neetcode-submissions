# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inOrder(root, res):
            if not root:
                return
            
            if root.left:
                inOrder(root.left, res)
            
            res.append(root.val)

            if root.right:
                inOrder(root.right, res)
            
        
        res = []
        inOrder(root, res)

        return res[k-1]