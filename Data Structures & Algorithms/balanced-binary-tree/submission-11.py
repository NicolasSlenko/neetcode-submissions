# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def checkHeight(node):
            if not node:
                return 0 
            
            return max(1+ checkHeight(node.left), 1+ checkHeight(node.right))

        def dfs(node):
            if not node:
                return True 
            
            if abs(checkHeight(node.left) - checkHeight(node.right)) > 1:
                return False 
        
            return dfs(node.left) and dfs(node.right)  
        
        return dfs(root)

        