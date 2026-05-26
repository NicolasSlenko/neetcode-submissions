# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def inOrder(root, res):
            if not root:
                res.append(None)
                return 
            
            res.append(root.val)
            inOrder(root.left, res)
            inOrder(root.right, res)

        def searchInTree(root, subroot):
            if not root:
                return False
            
            if(root.val == subroot.val):
                res1 = []
                res2 = []
                inOrder(root,res1)
                inOrder(subroot,res2)

                if res1 == res2:
                    return True
            
            return searchInTree(root.left, subroot) or searchInTree(root.right, subroot)
            
            
        

        return searchInTree(root, subRoot)
            

            




            