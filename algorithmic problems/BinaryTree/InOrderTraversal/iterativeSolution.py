# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        pre-order traversal using iterative method
        solution: pre-order itself means visiting root node first then left and then right
        stack: first in last out data structure
        """
        if root is None:
            return []
        result = []
        stack = [root]
        cur = root
        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            
            # first in last out
            # if right node is added to stack first then it is out lastly
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
            
                
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         """
#         pre-order -> visit root first, then left and then right
#         """
#         result = []
#         self.traverse(root, result)
#         return result
    
#     def traverse(self, root: Optional[TreeNode], result):
#         if root is None:
#             return
#         result.append(root.val)
#         self.traverse(root.left, result)
#         self.traverse(root.right, result)
