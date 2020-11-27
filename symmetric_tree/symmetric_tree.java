/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSymmetric(TreeNode root) {
        // 1. Initialize empty stack
        Stack<TreeNode> stack = new Stack<TreeNode>();
        // 2. Start from root
        TreeNode currentNode = root;
        // 3. Add root value to the stack. Root node will always be symmetric to itself. Hence, adding twice.
        stack.add(currentNode);
        stack.add(currentNode);

        // 4. Compare left and right nodes at any level using stack
        // Run until the stack is empty
        while(!stack.empty()) {
            // 4.1 Pop 2 nodes to check if they are same
            TreeNode node2 = stack.pop();
            TreeNode node1 = stack.pop();
            
            // 4.2 If both the nodes are null, then they are mirror and continue
            if((node1 == null) && (node2 == null)) {
                continue;
            }
            // 4.3 If either of the nodes is null, 2 nodes are not mirror
            if((node1 == null) || (node2 == null)) {
                return false;
            }
            // 4.4 If the value of 2 nodes do not match, they aren't mirror
            if(node1.val != node2.val) {
                return false;
            }
            // 4.5 Insert left and right nodes to the stack
            stack.add(node1.left);
            stack.add(node2.right);
            stack.add(node1.right);
            stack.add(node2.left);
        }
        // 5. Empty stack indicates all the nodes are traversed and the tree is symmetric
        return true;
    }
}