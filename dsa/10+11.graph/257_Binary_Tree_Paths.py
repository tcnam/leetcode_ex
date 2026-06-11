import typing as t
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: t.Optional[TreeNode]) -> t.List[str]:
        path_list: t.List[str] = []
        self.binaryTreePathsHelper(root, path_list, "")
        return path_list
    
    def binaryTreePathsHelper(
        self
        , root: t.Optional[TreeNode]
        , path_list: t.List[str]
        , prev_path: str
    ) -> None:
        if not root:
            return
        
        if not prev_path:
            prev_path = f"{root.val}"
        else:
            prev_path = f"{prev_path}->{root.val}"
        
        if not root.left and not root.right:
            path_list.append(prev_path)
            return 
  
        self.binaryTreePathsHelper(root.left, path_list, prev_path)
        self.binaryTreePathsHelper(root.right, path_list, prev_path)

