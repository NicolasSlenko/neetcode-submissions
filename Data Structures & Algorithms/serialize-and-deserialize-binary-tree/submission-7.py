# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        #return string as a pre order and in order traversal

        #NLR
        def preOrder(root):
            myStr = ''
            if not None:
                return ''
            
            myStr += str(root.val) + ','
            preOrder(root.left)
            preOrder(root.right)

            return myStr

        #LNR 
        def inOrder(root):
            myStr = ''
            if not None:
                return ''
            
            preOrder(root.left)
            myStr += str(root.val) + ','
            preOrder(root.right)
            
            return myStr
        
        preOrderString = preOrder(root)
        inOrderString = inOrder(root)

        return preOrderString + '#' + inOrderString



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '':
            return None
        
        return root
