package graph;
import java.util.*;

//  * Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> paths = new ArrayList<String>();
        this.treePathHelper(root, paths, new StringBuilder());
        return paths;
    }

    public void treePathHelper(TreeNode root, List<String> paths, StringBuilder prefixPath){
        if (root == null){
            return;
        }

        int prefixLength = prefixPath.length();
        if (prefixLength != 0){
            prefixPath.append("->");
        }
        prefixPath.append(String.valueOf(root.val));
        if (root.left == null && root.right == null){
            paths.add(prefixPath.toString());
        }
        else{
            this.treePathHelper(root.left, paths, prefixPath);
            this.treePathHelper(root.right, paths, prefixPath);
        }

        prefixPath.setLength(prefixLength);
    }
}