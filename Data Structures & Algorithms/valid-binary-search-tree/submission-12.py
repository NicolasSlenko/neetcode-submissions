# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValidBST(root,minVal,maxVal):
            if root is None:
                return True
            
            if minVal < root.val < maxVal:
                return isValidBST(root.left, minVal, root.val) and isValidBST(root.right, root.val, maxVal)
            else:
                return False 

        return isValidBST(root, float('-inf'), float('inf'))







