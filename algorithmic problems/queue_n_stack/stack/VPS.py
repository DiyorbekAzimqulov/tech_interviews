"""
https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
"""


class Solution:

    def maxDepth(self, s: str) -> int:
        """
        we loop through the string
        if we see ( then we put it to the stack
        if we see ) then we pop from the stack
            then we update our max_depth variable so that it always keeps track of max depth.
        """
        max_depth = 0
        stack = []
        for char in s:
            if char == '(':
                stack.append(0)
            elif char == ')':
                depth = len(stack)
                max_depth = max(depth, max_depth)
                stack.pop()
        return max_depth