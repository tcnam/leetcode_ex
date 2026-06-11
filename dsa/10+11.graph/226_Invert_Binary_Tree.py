import typing as t
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: t.Optional[TreeNode]) -> t.Optional[TreeNode]:
        self.invertTreeHelper(root)
        return root
    
    def invertTreeHelper(self, root: t.Optional[TreeNode]) -> None:
        if not root:
            return
        
        tempNode: TreeNode = root.left
        root.left = root.right
        root.right = tempNode
        
        self.invertTreeHelper(root.left)
        self.invertTreeHelper(root.right)
        