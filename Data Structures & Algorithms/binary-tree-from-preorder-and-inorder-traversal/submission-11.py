# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None 
        
        rootVal = preorder[0]

        indx = -1 

        for i in range(len(inorder)):
            if inorder[i] == rootVal:
                indx = i
                break
        
        newNode = TreeNode(rootVal)
        newNode.left = self.buildTree(preorder[1:i+1], inorder[:i])
        newNode.right = self.buildTree(preorder[i+1:], inorder[i+1:])

        return newNode
        


