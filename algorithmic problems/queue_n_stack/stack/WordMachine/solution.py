"""
https://binarysearch.com/problems/Word-Machine
"""

class Solution:
    def solve(self, ops):
        """
        if we are given number then we push it to the stack
        if we are given POP then we pop the element in the stack
        if we are given DUP then we duplicate top element in the stack
        if we are given + then pop two element and push their sum
        if we are given - then pop two element and push their difference
        if our stack empty and operations are given then return -1
        """
        stack = []
        for op in ops:
            if op.isnumeric():
                # push the element to the stack
                stack.append(int(op))
            elif op == "POP":
                if not stack:
                    return -1
                stack.pop()
            elif op == "DUP":
                if not stack:
                    return -1
                elem = stack.pop()
                stack.extend([elem, elem])
            elif op == "+":
                if len(stack) < 2:
                    return -1
                elem1 = stack.pop()
                elem2 = stack.pop()
                stack.append(elem1+elem2)
            elif op == "-":
                if len(stack) < 2:
                    return -1
                elem1 = stack.pop()
                elem2 = stack.pop()
                stack.append(elem1-elem2)
        return stack.pop()
