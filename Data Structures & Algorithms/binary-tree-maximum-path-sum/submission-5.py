# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #global variable
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            leftPath = dfs(root.left)
            rightPath = dfs(root.right)

            leftPath = max(leftPath, 0)
            rightPath = max(rightPath, 0)

            #check without split
            currentPath = root.val + max(leftPath,rightPath)

            if currentPath > res[0]:
                res[0] = currentPath
            

            #check WITH split
            splitPath = root.val + leftPath + rightPath

            if splitPath > res[0]:
                res[0] = splitPath
            
            return currentPath
            
        dfs(root)   
        return res[0]



            


        