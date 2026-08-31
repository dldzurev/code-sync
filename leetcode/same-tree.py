# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def is_same(a,b):
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False
            return (is_same(a.left,b.left) and is_same(a.right,b.right))
        return is_same(p,q)