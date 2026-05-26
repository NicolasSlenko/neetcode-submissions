# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        traversal = []

        def dfs(root, taversal):
            if not root:
                traversal.append('N')
                return
            
            traversal.append(str(root.val))
            dfs(root.left, traversal)
            dfs(root.right, traversal)

        dfs(root, traversal)

        return ','.join(traversal)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        self.i = 0

        if data == 'N':
            return None

        def dfs():
            if vals[self.i] == 'N':
                self.i+=1
                return None
            root = TreeNode(int(vals[self.i]))
            self.i+=1
            root.left = dfs()
            root.right = dfs()
            return root 
      
        root = dfs()
        return root

            


        


      