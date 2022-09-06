from typing import Optional
"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def is_leaf(self, node) -> bool:
        """
        it determines whether given node is a leaf node or not
        leaf node -> it does not have any child node
        """
        return node.left is None and node.right is None

        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        leaf node -> node that does not have any child nodes
        define cur_max = 1
        pass depth of the node to function call and if it is leaf node then we
        update the cur_max with depth of the leaf node.
        return the cur_max
                    3
                   / \
                  9   20
                     /  \
                    15   7
        time -> O(n)
        space -> O(n)
        """
        # edge case
        if root is None:
            return 0
        
        cur_max = 1
        cur_max = self.traverse(root, cur_max, depth=1)
        return cur_max

    def traverse(self, root, cur_max, depth):
        if root is None:
            return max(cur_max, depth)
        
        if self.is_leaf(root):
            # update cur_max 
            cur_max = max(cur_max, depth)
            return cur_max
        cur_max = self.traverse(root.left, cur_max, depth+1)
        cur_max = self.traverse(root.right, cur_max, depth+1)
        return cur_max
        
        