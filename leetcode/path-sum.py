# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(curr,sum_):
            if not curr: return False
            sum_ += curr.val
            if(curr.left == None and curr.right == None):
                return sum_ == targetSum
            return(dfs(curr.left,sum_) or dfs(curr.right,sum_))
        return dfs(root,0)