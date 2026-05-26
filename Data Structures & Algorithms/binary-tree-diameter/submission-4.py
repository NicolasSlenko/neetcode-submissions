# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        def dfs(root):
            nonlocal best 
            if not root:
                return 0
            
            mpL = dfs(root.left)
            mpR = dfs(root.right)

            best = max(best, mpL+mpR)

            return 1 + max(mpL,mpR)
        
        dfs(root)
        return best

        