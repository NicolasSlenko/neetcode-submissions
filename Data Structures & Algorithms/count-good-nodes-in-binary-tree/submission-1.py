# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = [0]

        if not root:
            return 0

        def dfs(root,maxVal):
            if root.val >= maxVal:
                res[0] += 1
                maxVal = root.val
            if root.left:
                dfs(root.left, maxVal)
            if root.right:
                dfs(root.right, maxVal)

        dfs(root, root.val)
        
        return res[0]

        