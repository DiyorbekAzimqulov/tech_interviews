from collections import deque
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        level order traversal is like Breadth First Search algorithm
                1
               / \
              3   5
             / \   \
            6   7   23
           / \
          10  12
        [[1], [3, 5], [6, 7, 23], [10, 12]] it is the result we are going to get
        use queue data structure to approach this problem
        queue -> first in first out
        at the beginnig root is in the queue
        get the queue item and put it to result array
        then add child of the root to the queue left child first and right child
        """
        if root is None:
            return []
        queue = deque([root])
        result = []
        while queue:
            
            level = len(queue)
            
            inner_level = []
            while level > 0:
                
                cur_element = queue.pop()  # popright
                inner_level.append(cur_element.val)
                if cur_element.left:
                    queue.appendleft(cur_element.left)
                if cur_element.right:
                    queue.appendleft(cur_element.right)
                level -= 1
            result.append(inner_level)
        return result