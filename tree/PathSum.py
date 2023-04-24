from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        apply DFS
        """
        if root is None:
            return []
        result = []
        stack = [root]
        value_stack = [root.val]
        cur = root
        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)

            # first in last out
            # if right node is added to stack first then it is out lastly
            if not node.left and not node.right:
                if sum(value_stack) == targetSum:
                    return True
                else:
                    value_stack.pop()
            if node.right:
                stack.append(node.right)
                value_stack.append(node.right.val)
            if node.left:
                stack.append(node.left)
                value_stack.append(node.left.val)
        return False
