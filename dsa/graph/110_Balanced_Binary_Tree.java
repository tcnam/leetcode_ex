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
        
        int result = this.heightCal(root);

        if (result == -1){
            return false;
        }
        else{
            return true;
        }
    }

    public int heightCal (TreeNode root){
        if (root == null){
            return 0;
        }

        int leftMaxHeight = this.heightCal(root.left);
        int rightMaxHeight = this.heightCal(root.right);

        if (leftMaxHeight == -1 || rightMaxHeight == -1 || Math.abs(leftMaxHeight - rightMaxHeight) > 1 == true){
            return -1;
        }
        else{
            return 1 + Math.max(leftMaxHeight, rightMaxHeight);
        }   
    }
}
