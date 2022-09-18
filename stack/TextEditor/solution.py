"""
https://binarysearch.com/problems/Text-Editor
"""
class Solution:
    def solve(self, s):
        """
        we use stack data structure here, and we put characters to the stack
        and if we see backspace sign then we pop the stack
        """
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "<" and i+1 < len(s):
                if s[i+1] == '-':
                    if stack:
                        stack.pop()
                    i += 1
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
            i += 1
        return "".join(stack)
        
        
