import typing as t

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: t.Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(
            1 + self.maxDepth(root.left)
            , 1 + self.maxDepth(root.right)
        )