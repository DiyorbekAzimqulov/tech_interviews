
"""
question: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/
Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""

from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traverse(root, result)
        return result
        
        
    def traverse(self, root, result):
        if root is None:
            return None
        self.traverse(root.left, result)
        self.traverse(root.right, result)
        result.append(root.val)
    