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
    public boolean isBalanced(TreeNode root) {
        if (root == null){
            return true;
        }
        
        int leftMaxHeight = 1 + this.maxHeightCal(root.left);
        int rightMaxHeight = 1 + this.maxHeightCal(root.right);

        if (Math.abs(leftMaxHeight - rightMaxHeight) > 1){
            return false;
        }
        else {
            return true;
        }
    }

    public int maxHeightCal (TreeNode root){
        if (root == null){
            return 0;
        }

        int leftMaxHeight = 1 + this.maxHeightCal(root.left);
        int rightMaxHeight = 1 + this.maxHeightCal(root.right);
        return Math.max(leftMaxHeight, rightMaxHeight);
    }
}
