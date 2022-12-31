
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


# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         """
#         we know the power of 2's are in binary is like this:
#         2^0 = 1 -> 01 & 0 = 0
#         2^1 = 2 -> 10 & 01 = 0
#         2^2 = 4 -> 100 & 011 = 
#         2^3 = 8 -> 1000 & 0111 = 0
#         2^4 = 16 -> 10000 & 01111 = 
#         2^5 = 32 -> 100000 & 011111 = 0
#         so if we make bitwise AND operation with power of two and
#         one less than this number then we get 0
#         """
#         return n > 0 and n & (n-1) == 0