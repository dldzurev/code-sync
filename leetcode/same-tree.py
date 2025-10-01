# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(p,q):
            if not p and not q:
                return True
            if(not p or not q):
                return False
            elif(p.val != q.val):
                return False
            elif(not p.right and not p.left and not q.right and not q.left ):
                return True
            return (bfs(p.left,q.left) and bfs(p.right,q.right))
        return bfs(p,q)