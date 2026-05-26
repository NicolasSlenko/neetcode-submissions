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

            res[0] = max(res[0], root.val + leftSum + rightSum)

            return root.val + max(leftSum,rightSum)

        dfs(root)

        return res[0]






        
        



            


        