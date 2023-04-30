"""
Question: Given the root of a binary tree, return the preorder traversal of its nodes' values.
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/
"""
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        pre-order -> visit root first, then left and then right
        """
        result = []
        self.traverse(root, result)
        return result
    
    def traverse(self, root: Optional[TreeNode], result):
        if root is None:
            return
        result.append(root.val)
        self.traverse(root.left, result)
        self.traverse(root.right, result)
