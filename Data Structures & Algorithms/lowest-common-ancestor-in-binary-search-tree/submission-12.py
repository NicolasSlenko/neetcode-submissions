# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def CheckRoot(root, p, q):

            if root == p or root == q:
                return root

            if(root.val > p.val and root.val > q.val):
                return CheckRoot(root.left, p, q)
            
            elif(root.val < p.val and root.val < q.val):
                return CheckRoot(root.right, p, q)
            
            else:
                return root


        return CheckRoot(root,p,q)

       
        
        

        

