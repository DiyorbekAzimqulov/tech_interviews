"""
https://leetcode.com/problems/happy-number/
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        """
        happy number -> it is the number where sum of square of its digits equal to 1
        we use hash table here to keep track of visited sum of digits of square number
        if it is not happy number, then same value appears when sum square.
        
        """
        visited = set()
        while n not in visited:  # while n is not happy number
            # extract digits 
            visited.add(n)
            sum_ = 0
            while n != 0:
                digit = n % 10
                n //= 10
                sum_ += digit ** 2
            n = sum_
            if n == 1:
                return True
        
            # determine when it is in infinite loop
        return False