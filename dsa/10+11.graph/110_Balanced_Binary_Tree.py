import typing as t
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: t.Optional[TreeNode]) -> bool:
        height_dict: t.Dict[TreeNode, int] = {}
        return self.isBalancedHelper(root, height_dict)
    
    def isBalancedHelper(self, root: t.Optional[TreeNode], height_dict: t.Dict[TreeNode, int]) -> bool:
        if not root:
            return True
        
        heightLeft: int = self.heightCal(root.left, height_dict)
        heightRight: int = self.heightCal(root.right, height_dict)

        return (
            abs(heightLeft - heightRight) <= 1
            and self.isBalancedHelper(root.left, height_dict)
            and self.isBalancedHelper(root.right, height_dict)
        )
    
    def heightCal(self, root: t.Optional[TreeNode], height_dict: t.Dict[TreeNode, int]) -> int:
        if not root:
            return 0
        
        if root in height_dict:
            return height_dict.get(root)
        
        root_height: int = max(
            1 + self.heightCal(root.left, height_dict)
            , 1 + self.heightCal(root.right, height_dict)
        )
        height_dict[root] = root_height

        return root_height