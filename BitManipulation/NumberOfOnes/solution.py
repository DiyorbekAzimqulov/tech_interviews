"""
https://leetcode.com/problems/number-of-1-bits/
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        1001
        dividing it by 2 returns whether that bit ends with 1 or 0
        we count 1's
        """
        result = 0
        while n:
            result += n % 2
            n = n >> 1
        return result