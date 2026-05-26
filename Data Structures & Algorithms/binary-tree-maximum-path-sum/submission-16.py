# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        res = [root.val]

        def dfs(root, split = False): 
            if not root:
                return 0

            leftSum = max(0, dfs(root.left))
            rightSum = max(0, dfs(root.right))

            currentSum = root.val + max(leftSum, rightSum)
            res[0] = max(currentSum, res[0])

            if not split and root.left and root.right:
                sumIncludingSplit = root.val + max(0, dfs(root.left, split = True)) + max(0,dfs(root.right, split = True) )
                res[0] = max(res[0], sumIncludingSplit)

            return currentSum 

        dfs(root)

        return res[0]






        
        



            


        