"""
https://leetcode.com/problems/reverse-integer/
"""

class Solution:
    def reverse(self, x: int) -> int:
        """
        range -> [-2147483648, 2147483647]
                            ^           ^
        """
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        reverse = 0
        negative = x < 0
        x = abs(x)
        while x != 0:
            digit = x % 10
            x //= 10
            if (MAX_INT // 10 < reverse) or (MAX_INT // 10 == reverse and MAX_INT % 10 <= digit):
                return 0
            if (MIN_INT // 10 > reverse) or (MIN_INT // 10 == reverse and MAX_INT % 10 >= digit):
                return 0
            reverse = reverse * 10 + digit
        if negative:
            reverse = -abs(reverse)
        return reverse
            
            
            