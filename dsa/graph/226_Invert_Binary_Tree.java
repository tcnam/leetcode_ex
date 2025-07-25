package graph;


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
    public TreeNode invertTree(TreeNode root) {
        this.invertTreeHelper(root);
        return root;
    }

    public void invertTreeHelper(TreeNode root){
        if (root == null){
            return;
        }
        TreeNode tempNode = root.left;
        root.left = root.right;
        root.right = tempNode;
        this.invertTreeHelper(root.left);
        this.invertTreeHelper(root.right);
    }
}
