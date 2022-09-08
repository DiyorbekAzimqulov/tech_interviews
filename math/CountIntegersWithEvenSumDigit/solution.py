"""
https://leetcode.com/problems/count-integers-with-even-digit-sum/
"""

class Solution:
    def digit_sum(self, num: int) -> int:
        result = 0
        while num != 0:
            digit = num % 10
            result += digit
            num //= 10
        return result

    def countEven(self, num: int) -> int:
        count = 0
        for i in range(2, num+1):
            if self.digit_sum(i) % 2 == 0:
                count += 1
        return count