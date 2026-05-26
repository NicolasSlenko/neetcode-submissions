# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        q = collections.deque()
        q.append(root)

        while q:
            rightMost = q[-1]
            res.append(rightMost.val)
            for i in range(len(q)):
                nextNode = q.popleft()
                if nextNode:
                    if nextNode.left:
                        q.append(nextNode.left)
                    if nextNode.right:
                        q.append(nextNode.right)
        return res



            
        

        return res

        