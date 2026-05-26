# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def checkBST(root,minVal, maxVal):
            if not root:
                return True
            
            if not(minVal < root.val < maxVal):
                return False
            
            return checkBST(root.left, minVal, root.val) and checkBST(root.right,root.val, maxVal)
        
        if not root:
            return True
        
        return checkBST(root, minVal = float('-inf'), maxVal = float('inf'))
        
        



        