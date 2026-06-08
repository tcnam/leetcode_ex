import typing as t
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: t.Optional[TreeNode]) -> bool:
        return self.isSymmetricHelper(root.left, root.right)
    
    def isSymmetricHelper(self, left: t.Optional[TreeNode], right: t.Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        return (
            left.val == right.val
            and self.isSymmetricHelper(left.left, right.right)
            and self.isSymmetricHelper(left.right, right.left)
        )