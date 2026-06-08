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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        return this.culSumPath(root, 0, targetSum);
    }

    public boolean culSumPath(TreeNode root, int culSum, int targetSum){
        if (root == null){
            return false;
        }

        if (root.left == null && root.right == null){
            if (culSum + root.val == targetSum){
                return true;
            }
            else {
                return false;
            }
        }
        int newCulSum = culSum + root.val;
        
        return this.culSumPath(root.left, newCulSum, targetSum) || this.culSumPath(root.right,newCulSum, targetSum);
    }
}
