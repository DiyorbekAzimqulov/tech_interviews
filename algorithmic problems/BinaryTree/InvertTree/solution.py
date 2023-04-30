"""
https://leetcode.com/problems/invert-binary-tree/
"""

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        inverting binary tree means swaping left and right child nodes
        """
        if root is None:
            return root
        # swap two child nodes
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        # recursively call other nodes in tree
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        