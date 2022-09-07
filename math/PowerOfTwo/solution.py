
"""
https://leetcode.com/problems/power-of-two/
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

complexity:
time -> O(1)
space -> O(1)
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        we simply use bit manipulation.
        so the given number is whether power of 2 or not, we simply apply bitwise             operation
        
        4 -> 0100
        8 -> 1000
        if 4 & 8 -> 0, 0, 0, 0
        7 -> 0111
        4 & 8 -> 0, 1, 0, 0
        """
        return n and not(n & (n-1))