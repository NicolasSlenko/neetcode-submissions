class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def inorder(root, res):
            
            if not root:
                res.append(None)
                return 
            res.append(root.val)
            inorder(root.left, res)
            inorder(root.right, res)
        
            return res

        res1 = []
        res2 = []

        inorder(q, res1)
        inorder(p, res2)

        print(res1)
        print(res2)

        return True if res1 == res2 else False