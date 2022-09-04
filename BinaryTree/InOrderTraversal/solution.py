
"""
question: Given the root of a binary tree, return the inorder traversal of its nodes' values.
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/
"""

from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        in-order -> visit left,root then right
        """
        result = []
        self.traverse(root, result)
        return result
    
    def traverse(self, root: Optional[TreeNode], result):
        if root is None:
            return
        
        self.traverse(root.left, result)
        result.append(root.val)
        self.traverse(root.right, result)
