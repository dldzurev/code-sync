# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_valid(root,min_,max_):
            if not root: return True
            if (root.val >= max_) or (root.val <= min_):return False
            return (check_valid(root.right,root.val,max_) and check_valid(root.left,min_,root.val))
        return check_valid(root,-math.inf,math.inf)