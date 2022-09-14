"""
https://leetcode.com/problems/search-in-a-binary-search-tree/
"""

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        """
         if root value is equal to the search val return that root
         if root value is less than search value search right child of root
         if root value is greater than search value, search left child of root
         
         Complexity analysis:
         time -> O(logn)
         space -> O(1)
        """
        
        # base case
        if root is None:
            return None
        if root.val == val:
            return root
        # recursive case
        if root.val > val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)