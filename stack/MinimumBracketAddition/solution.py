"""
https://binarysearch.com/problems/Minimum-Bracket-Addition
"""
class Solution:
    def solve(self, s):
        """
        if we encounter opening bracket we put it to the stack
        if we encounter closing bracket we check whether we have sufficient opening bracket, if we have then we pop that element, otherwise we need to insert bracket. 
        in the end if we have more opening brackets than closing ones
        then we add number of that brackets to the bracket insert count.
        ))(()())
        )))((
        time O(n)
        space O(1)
        """
        map_ = {
            ")": "("
        }
        stack = []
        add = 0
        for bracket in s:
            if bracket not in map_:
                # opening bracket
                stack.append(bracket)
            else:
                # closing bracket
                if stack:
                    stack.pop()
                else:
                    add += 1
        add += len(stack)
        return add
