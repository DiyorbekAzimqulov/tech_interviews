"""
https://leetcode.com/problems/insert-into-a-binary-search-tree/
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        we can perform insertion to BST in different ways. we may add a new node as a leaf node to BST
        or make a new node not as leaf node but among other nodes in BST
        these two approaches are valid as long as we keep the properties of BST
        """
        # solving iteratively
        
        if root is None:
            return TreeNode(val)
        cur = root
        while cur:
            if val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    node = TreeNode(val)
                    cur.left = node
                    return root
            else:
                if cur.right:
                    cur = cur.right
                else:
                    node = TreeNode(val)
                    cur.right = node
                    return root
        return root
        