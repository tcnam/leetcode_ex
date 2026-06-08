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
    public int maxDepth(TreeNode root) {
        if (root == null){
            return 0;
        }

        int leftMaxDepth = 1 + this.maxDepth(root.left);
        int rightMaxDepth = 1 + this.maxDepth(root.right);

        return Math.max(leftMaxDepth, rightMaxDepth);
    }
}
