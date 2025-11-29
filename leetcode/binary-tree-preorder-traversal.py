# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #root left right
        lsit = []
        
        def preord(root):
            if(root == None):
                return []
            lsit.append(root.val)
            preord(root.left)
            preord(root.right)
            return
        preord(root)
        return lsit